# auth.py — file-backed email auth, Google/LinkedIn OAuth, and Guest sessions

import os
import json
import uuid
import hashlib
from datetime import datetime
from typing import Optional, Dict, Any

import requests
import base64
from urllib.parse import urlencode
import streamlit as st

DATA_DIR = "data"
USERS_PATH = os.path.join(DATA_DIR, "users.json")
SESSIONS_PATH = os.path.join(DATA_DIR, "sessions.json")

# ---- OAuth config from environment ----
GOOGLE_CLIENT_ID       = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET   = os.getenv("GOOGLE_CLIENT_SECRET", "")
LINKEDIN_CLIENT_ID     = os.getenv("LINKEDIN_CLIENT_ID", "")
LINKEDIN_CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET", "")
OAUTH_REDIRECT_URI     = os.getenv("OAUTH_REDIRECT_URI", "http://localhost:8501/")

# ---------------- File helpers ----------------
def _ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(USERS_PATH):
        with open(USERS_PATH, "w", encoding="utf-8") as f:
            json.dump({"users": {}}, f)
    if not os.path.exists(SESSIONS_PATH):
        with open(SESSIONS_PATH, "w", encoding="utf-8") as f:
            json.dump({"sessions": {}}, f)

def _load_json(path: str) -> Dict[str, Any]:
    _ensure_dirs()
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_json(path: str, data: Dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def _hash_password(password: str, salt: Optional[str] = None) -> str:
    """Simple salted SHA256 (demo only)."""
    if not salt:
        salt = uuid.uuid4().hex
    h = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return f"{salt}${h}"

def _check_password(password: str, salted_hash: str) -> bool:
    try:
        salt, _ = salted_hash.split("$", 1)
        return _hash_password(password, salt) == salted_hash
    except Exception:
        return False


# ---------------- Core manager ----------------
class AuthManager:
    def __init__(self):
        _ensure_dirs()

    # Users
    def register_user(self, email: str, full_name: str, provider: str = "email", password: Optional[str] = None, role: str = "user") -> bool:
        email = (email or "").strip().lower()
        full_name = (full_name or "").strip()
        if not email or not full_name:
            return False
        users_db = _load_json(USERS_PATH)
        if email in users_db["users"]:
            return False
        entry = {
            "email": email,
            "name": full_name,
            "provider": provider,
            "role": role,
            "created_at": datetime.utcnow().isoformat() + "Z",
        }
        if provider == "email":
            if not password:
                return False
            entry["password"] = _hash_password(password)
        users_db["users"][email] = entry
        _save_json(USERS_PATH, users_db)
        return True

    def authenticate_user(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        email = (email or "").strip().lower()
        users_db = _load_json(USERS_PATH)["users"]
        user = users_db.get(email)
        if not user or user.get("provider") != "email":
            return None
        if not _check_password(password, user.get("password","")):
            return None
        return user

    def get_user(self, email: str) -> Optional[Dict[str, Any]]:
        return _load_json(USERS_PATH)["users"].get((email or "").strip().lower())

    # Sessions
    def create_session(self, email: str) -> str:
        sessions = _load_json(SESSIONS_PATH)
        sid = uuid.uuid4().hex
        sessions["sessions"][sid] = {"email": (email or "").strip().lower(), "created_at": datetime.utcnow().isoformat() + "Z"}
        _save_json(SESSIONS_PATH, sessions)
        return sid

    def get_user_by_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        sessions = _load_json(SESSIONS_PATH)
        info = sessions["sessions"].get(session_id)
        if not info:
            return None
        return self.get_user(info["email"])

    def logout(self, session_id: str) -> None:
        sessions = _load_json(SESSIONS_PATH)
        if session_id in sessions["sessions"]:
            sessions["sessions"].pop(session_id)
            _save_json(SESSIONS_PATH, sessions)


# ---------------- Streamlit helpers (used in app.py) ----------------
def init_auth() -> AuthManager:
    if "auth_manager" not in st.session_state:
        st.session_state.auth_manager = AuthManager()
    return st.session_state.auth_manager

def check_authentication() -> bool:
    return bool(st.session_state.get("authenticated", False))

def get_user_info() -> Optional[Dict[str, Any]]:
    return st.session_state.get("user_info")

def _finalize_login(user: Dict[str, Any]):
    st.session_state.user_info = user
    st.session_state.authenticated = True

def logout_user():
    """Clear current session and state."""
    am: AuthManager = st.session_state.get("auth_manager") or AuthManager()
    sid = st.session_state.get("session_id")
    if sid:
        try:
            am.logout(sid)
        except Exception:
            pass
    for key in ["authenticated", "user_info", "session_id"]:
        if key in st.session_state:
            del st.session_state[key]


# ---------------- Email Sign in / Sign up ----------------
def email_sign_in(email: str, password: str):
    try:
        am = init_auth()
        user = am.authenticate_user(email, password)
        if not user:
            return False, "Invalid email or password."
        _finalize_login(user)
        st.session_state.session_id = am.create_session(user["email"])
        return True, "Signed in."
    except Exception as e:
        return False, f"Sign in error: {e}"

def email_sign_up(name: str, email: str, password: str):
    try:
        am = init_auth()
        if not name or not email or not password:
            return False, "All fields are required."
        created = am.register_user(email=email, full_name=name, provider="email", password=password, role="user")
        if not created:
            return False, "Account already exists or invalid data."
        user = am.get_user(email)
        _finalize_login(user)
        st.session_state.session_id = am.create_session(user["email"])
        return True, "Account created."
    except Exception as e:
        return False, f"Sign up error: {e}"


# ---------------- Guest Session ----------------
def start_guest_session():
    """Create a limited-access guest user session."""
    guest = {
        "email": "guest@cvcompass.local",
        "name": "Guest User",
        "provider": "guest",
        "role": "guest",
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    st.session_state.user_info = guest
    st.session_state.authenticated = True
    st.session_state.session_id = "guest"  # not persisted


# ---------------- OAuth Helpers ----------------
def _save_oauth_state(state: str, provider: str):
    st.session_state[f"oauth_state_{provider}"] = state

def _pop_oauth_state(provider: str) -> str:
    return st.session_state.pop(f"oauth_state_{provider}", "")

def start_google_oauth():
    """Render a Google OAuth link (Authorization Code flow)."""
    if not (GOOGLE_CLIENT_ID and OAUTH_REDIRECT_URI):
        st.error("Google OAuth not configured.")
        return
    state = uuid.uuid4().hex
    _save_oauth_state(state, "google")
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": OAUTH_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "state": state,
        "access_type": "offline",
        "prompt": "consent",
    }
    auth_url = "https://accounts.google.com/o/oauth2/v2/auth?" + urlencode(params)
    st.markdown(f"[Click to continue with Google]({auth_url})")

def start_linkedin_oauth():
    """Render a LinkedIn OAuth link (Authorization Code flow)."""
    if not (LINKEDIN_CLIENT_ID and OAUTH_REDIRECT_URI):
        st.error("LinkedIn OAuth not configured.")
        return
    state = uuid.uuid4().hex
    _save_oauth_state(state, "linkedin")
    params = {
        "response_type": "code",
        "client_id": LINKEDIN_CLIENT_ID,
        "redirect_uri": OAUTH_REDIRECT_URI,
        "scope": "r_liteprofile r_emailaddress",
        "state": state,
    }
    auth_url = "https://www.linkedin.com/oauth/v2/authorization?" + urlencode(params)
    st.markdown(f"[Click to continue with LinkedIn]({auth_url})")

def handle_oauth_callback() -> bool:
    """
    Complete OAuth if ?code=…&state=… present in the URL.
    Safe to call every run; returns True if a login was completed.
    """
    qs = st.query_params
    code = qs.get("code")
    state = qs.get("state")
    if not code or not state:
        return False

    # Guess provider: Google adds 'scope' in the callback; LinkedIn does not.
    provider = "google" if qs.get("scope") else "linkedin"
    expected = _pop_oauth_state(provider)
    if not expected or expected != state:
        st.error("OAuth state mismatch.")
        return False

    am = init_auth()
    try:
        if provider == "google":
            token = requests.post("https://oauth2.googleapis.com/token", data={
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
                "code": code,
                "grant_type": "authorization_code",
                "redirect_uri": OAUTH_REDIRECT_URI,
            }).json()
            id_token = token.get("id_token", "")
            if not id_token:
                raise RuntimeError("No id_token in Google response")
            body = id_token.split(".")[1] + "=="
            payload = json.loads(base64.urlsafe_b64decode(body).decode())
            email = payload.get("email")
            name = payload.get("name", "Google User")
            role = "user"

        else:
            token = requests.post("https://www.linkedin.com/oauth/v2/accessToken", data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": OAUTH_REDIRECT_URI,
                "client_id": LINKEDIN_CLIENT_ID,
                "client_secret": LINKEDIN_CLIENT_SECRET,
            }, headers={"Content-Type":"application/x-www-form-urlencoded"}).json()
            access = token.get("access_token")
            if not access:
                raise RuntimeError("No access_token from LinkedIn")
            prof = requests.get(
                "https://api.linkedin.com/v2/me",
                headers={"Authorization": f"Bearer {access}"}
            ).json()
            mail = requests.get(
                "https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))",
                headers={"Authorization": f"Bearer {access}"}
            ).json()
            name = (prof.get("localizedFirstName","") + " " + prof.get("localizedLastName","")).strip() or "LinkedIn User"
            email = mail.get("elements",[{}])[0].get("handle~",{}).get("emailAddress")
            role = "user"

        if not email:
            st.error("Provider did not return an email.")
            return False

        if not am.get_user(email):
            am.register_user(email=email, full_name=name, provider=provider, role=role)
        user = am.get_user(email)

        _finalize_login(user)
        st.session_state.session_id = am.create_session(user["email"])
        st.success(f"Signed in as {name}")
        return True

    except Exception as e:
        st.error(f"OAuth error: {e}")
        return False
