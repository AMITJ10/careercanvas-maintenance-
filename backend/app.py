import io
import os
import tempfile
from pathlib import Path
from datetime import datetime

import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv

# ---- Load .env early
load_dotenv()

# ---- Auth helpers (kept as-is)
from auth import (
    init_auth,
    get_user_info,
    logout_user,
    start_google_oauth,
    start_linkedin_oauth,
    handle_oauth_callback,
    start_guest_session,
    email_sign_in,
    email_sign_up,
)

# ---- App modules
from resume_templates import TEMPLATES, get_template_by_id, get_template_preview
from resume_builder import create_resume_builder_interface
from career_advisor import CareerAdvisor
from resume_parser import parse_resume


# ==================== Page & Styles ====================
st.set_page_config(
    page_title="CareerCanvas AI - Career Assistant",
    layout="wide",
    page_icon="🎨",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root{
  /* Enhanced Color Palette */
  --primary: #4f46e5;
  --primary-light: #6366f1;
  --primary-dark: #3730a3;
  --primary-glow: #8b5cf6;
  
  --secondary: #06b6d4;
  --secondary-light: #22d3ee;
  --secondary-dark: #0891b2;
  
  --accent: #f59e0b;
  --accent-light: #fbbf24;
  --success: #10b981;
  --warning: #f59e0b;
  --error: #ef4444;
  
  /* Modern Background System */
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --bg-tertiary: #334155;
  --bg-card: rgba(30, 41, 59, 0.8);
  --bg-glass: rgba(51, 65, 85, 0.15);
  --bg-glass-strong: rgba(51, 65, 85, 0.25);
  
  /* Text Colors */
  --text-primary: #f8fafc;
  --text-secondary: #cbd5e1;
  --text-muted: #94a3b8;
  --text-accent: #e2e8f0;
  
  /* Interactive Elements */
  --border-primary: rgba(148, 163, 184, 0.2);
  --border-secondary: rgba(148, 163, 184, 0.1);
  --border-accent: rgba(79, 70, 229, 0.3);
  
  /* Shadows & Effects */
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.12);
  --shadow-md: 0 8px 25px rgba(0, 0, 0, 0.15);
  --shadow-lg: 0 15px 35px rgba(0, 0, 0, 0.2);
  --shadow-glow: 0 0 30px rgba(79, 70, 229, 0.15);
  
  /* Gradients */
  --gradient-primary: linear-gradient(135deg, var(--primary) 0%, var(--primary-glow) 100%);
  --gradient-secondary: linear-gradient(135deg, var(--secondary) 0%, var(--secondary-light) 100%);
  --gradient-bg: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 50%, var(--bg-primary) 100%);
  --gradient-card: linear-gradient(145deg, rgba(30, 41, 59, 0.9) 0%, rgba(51, 65, 85, 0.8) 100%);
  
  /* Transitions */
  --transition-smooth: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-fast: all 0.15s ease-out;
}

html, body, [data-testid="stAppViewContainer"]{
  background: var(--gradient-bg) !important;
  color: var(--text-primary) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif !important;
  font-weight: 400;
  line-height: 1.6;
}

/* Remove Streamlit branding */
#MainMenu, header, footer, .stDeployButton { display: none !important; }
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a { display: none !important; }

.block-container{ 
  padding-top: 1rem; 
  padding-bottom: 1rem; 
  max-width: 1400px;
}

/* Enhanced Site Header */
.site-title{
  display: flex; 
  align-items: center; 
  justify-content: center; 
  gap: 16px;
  margin: 0 0 24px 0; 
  padding: 20px 0;
  background: var(--gradient-card);
  border-radius: 16px;
  border: 1px solid var(--border-primary);
  box-shadow: var(--shadow-md);
  backdrop-filter: blur(10px);
}

.site-title h1{
  margin: 0; 
  font-size: 48px; 
  font-weight: 800; 
  letter-spacing: -0.02em;
  font-family: 'Space Grotesk', sans-serif;
  background: linear-gradient(135deg, #a5b4fc 0%, #c7d2fe 25%, #e0e7ff  50%, #c7d2fe 75%, #a5b4fc 100%);
  -webkit-background-clip: text; 
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
  0%, 100% { background-position: -200% center; }
  50% { background-position: 200% center; }
}

.site-title small{ 
  color: var(--text-secondary); 
  letter-spacing: 2px; 
  text-transform: uppercase; 
  font-weight: 500;
  font-size: 14px;
}

/* Typography Enhancements */
h1, h2, h3, h4, h5, h6 { 
  color: var(--text-primary) !important; 
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  line-height: 1.2;
}
p, li, span, label { color: var(--text-primary) !important; }
small, .muted { color: var(--text-muted) !important; }

/* Enhanced Links */
a { 
  color: var(--secondary-light) !important; 
  text-decoration: none;
  transition: var(--transition-fast);
  position: relative;
}
a:hover { 
  color: var(--secondary) !important; 
  text-decoration: none;
}
a::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: -2px;
  left: 0;
  background: var(--gradient-secondary);
  transition: var(--transition-smooth);
}
a:hover::after {
  width: 100%;
}

/* Modern Card System */
.card{
  background: var(--gradient-card);
  border: 1px solid var(--border-primary);
  border-radius: 16px;
  padding: 20px;
  box-shadow: var(--shadow-md);
  backdrop-filter: blur(12px);
  transition: var(--transition-smooth);
  position: relative;
  overflow: hidden;
}

.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.3), transparent);
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
  border-color: var(--border-accent);
}

/* Enhanced Input System */
.stTextInput > div > div > input,
.stTextArea textarea,
.stSelectbox > div > div > select{
  background: rgba(15, 23, 42, 0.8) !important;
  color: var(--text-primary) !important;
  border: 2px solid var(--border-primary) !important;
  border-radius: 12px !important;
  padding: 12px 16px !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  transition: var(--transition-smooth) !important;
}

.stTextInput > div > div > input:focus,
.stTextArea textarea:focus {
  border-color: var(--primary) !important;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
  outline: none !important;
}

.stTextInput > div > div > input::placeholder,
.stTextArea textarea::placeholder { 
  color: var(--text-muted) !important; 
  font-weight: 400 !important;
}

/* Enhanced Selectbox */
.stSelectbox div[data-baseweb="select"] {
  background: rgba(15, 23, 42, 0.8) !important;
  color: var(--text-primary) !important;
  border: 2px solid var(--border-primary) !important;
  border-radius: 12px !important;
  transition: var(--transition-smooth) !important;
}

.stSelectbox div[data-baseweb="select"]:hover {
  border-color: var(--primary-light) !important;
}

.stSelectbox div[data-baseweb="select"] input { 
  color: var(--text-primary) !important; 
  font-weight: 500 !important;
}

/* Enhanced & Corrected Dropdown Menu */

/* Main dropdown container */
div[data-testid="stSelectbox"] [data-baseweb="menu"],
.stSelectbox [data-baseweb="menu"] {
background: rgba(15, 23, 42, 1) !important; /* Dark, semi-transparent background */
border: 1px solid #4A5568 !important; /* A subtle border color */
border-radius: 12px !important;
box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4) !important;
backdrop-filter: blur(16px) !important; /* Corrected syntax for a "frosted glass" effect */
z-index: 9999 !important;
margin-top: 4px !important;
}

/* Individual dropdown options */
div[data-testid="stSelectbox"] [data-baseweb="menu"] div[role="option"],
.stSelectbox [data-baseweb="menu"] div[role="option"] {
background: transparent !important;
color: #2D3748 !important; /* Changed to a light gray for high contrast */
font-weight: 500 !important;
padding: 12px 16px !important;
border-radius: 8px !important;
margin: 4px 8px !important;
transition: all 0.2s ease-in-out !important;
}

/* Hover state for options */
div[data-testid="stSelectbox"] [data-baseweb="menu"] div[role="option"]:hover,
.stSelectbox [data-baseweb="menu"] div[role="option"]:hover {
background: rgba(79, 70, 229, 0.2) !important;
color: #FFFFFF !important; /* Becomes bright white on hover */
}

/* Style for the currently selected option */
div[data-testid="stSelectbox"] [data-baseweb="menu"] div[aria-selected="true"],
.stSelectbox [data-baseweb="menu"] div[aria-selected="true"] {
  background: #4F46E5 !important; /* Using a solid color from your hover effect */
  color: white !important;
  font-weight: 600 !important;
}

/* Modern Button System */
.stButton > button {
  color: white !important;
  background: var(--gradient-primary) !important;
  border: none !important;
  border-radius: 12px !important;
  padding: 12px 24px !important;
  font-weight: 600 !important;
  font-size: 14px !important;
  transition: var(--transition-smooth) !important;
  box-shadow: var(--shadow-sm) !important;
  position: relative !important;
  overflow: hidden !important;
}

.stButton > button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: var(--transition-smooth);
}

.stButton > button:hover { 
  transform: translateY(-1px) !important;
  box-shadow: var(--shadow-md) !important;
  filter: brightness(1.1) !important;
}

.stButton > button:hover::before {
  left: 100%;
}

.stButton > button:active { 
  transform: translateY(0) !important;
}

.stButton > button:focus { 
  outline: none !important;
  box-shadow: var(--shadow-md), 0 0 0 3px rgba(79, 70, 229, 0.3) !important;
}

/* Secondary Button Variant */
.stButton > button[data-baseweb="button"][kind="secondary"],
.stButton > button[kind="secondary"] {
  background: rgba(51, 65, 85, 0.8) !important;
  border: 2px solid var(--border-primary) !important;
  color: var(--text-primary) !important;
}

.stButton > button[kind="secondary"]:hover {
  background: rgba(79, 70, 229, 0.2) !important;
  border-color: var(--primary) !important;
}

/* Enhanced Sidebar */
[data-testid="stSidebar"]{
  background: var(--gradient-card) !important;
  border-right: 1px solid var(--border-primary) !important;
  backdrop-filter: blur(12px) !important;
}

.sidebar-logo{ 
  text-align: center; 
  padding: 16px 0 20px 0; 
  border-bottom: 1px solid var(--border-secondary); 
  margin-bottom: 16px;
}

.sidebar-logo h2{ 
  margin: 0; 
  color: var(--text-accent); 
  font-weight: 800; 
  font-size: 20px;
  font-family: 'Space Grotesk', sans-serif;
}

/* Enhanced Grids */
.dashboard-grid{ 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
  gap: 16px; 
  margin: 20px 0;
}

.feature-grid{ 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
  gap: 16px;
}

/* KPI Cards Enhancement */
.kpi-card {
  background: var(--gradient-card);
  border: 1px solid var(--border-primary);
  border-radius: 16px;
  padding: 20px;
  text-align: center;
  transition: var(--transition-smooth);
  position: relative;
  overflow: hidden;
}

.kpi-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--gradient-primary);
}

.kpi-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}

.kpi-value {
  font-size: 32px;
  font-weight: 800;
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 8px 0;
}

.kpi-label {
  color: var(--text-secondary);
  font-size: 13px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Preview Viewport Enhancement */
.preview-viewport{ 
  background: rgba(15, 23, 42, 0.8);
  border-radius: 16px;
  padding: 16px;
  border: 1px solid var(--border-primary);
  backdrop-filter: blur(12px);
  box-shadow: var(--shadow-md);
  margin: 0 auto;
  max-width: 900px;
}

.preview-scale{ 
  width: 794px; 
  height: 1123px; 
  transform-origin: top center;
}

.pdf{ 
  width: 794px; 
  min-height: 1123px; 
  background: #ffffff; 
  color: #111111; 
  border-radius: 12px; 
  box-shadow: var(--shadow-lg); 
  padding: 28px 36px; 
  overflow: auto;
}

/* Enhanced Expander */
[data-testid="stExpander"] {
  background: var(--gradient-card) !important;
  border: 1px solid var(--border-primary) !important;
  border-radius: 12px !important;
  backdrop-filter: blur(12px) !important;
}

/* Enhanced Footer */
.site-info{ 
  margin-top: 32px; 
  color: var(--text-muted); 
  text-align: center; 
  font-size: 13px; 
  border-top: 1px solid var(--border-secondary); 
  padding-top: 20px;
  font-weight: 500;
}

/* Loading States */
.stSpinner {
  color: var(--primary) !important;
}

/* Success/Warning/Error Messages */
.stSuccess, .stWarning, .stError, .stInfo {
  border-radius: 12px !important;
  border: none !important;
  backdrop-filter: blur(12px) !important;
}

.stSuccess {
  background: rgba(16, 185, 129, 0.15) !important;
  color: #10b981 !important;
}

.stWarning {
  background: rgba(245, 158, 11, 0.15) !important;
  color: #f59e0b !important;
}

.stError {
  background: rgba(239, 68, 68, 0.15) !important;
  color: #ef4444 !important;
}

.stInfo {
  background: rgba(6, 182, 212, 0.15) !important;
  color: #06b6d4 !important;
}

/* Feature Button Enhancement */
.feature-button {
  background: var(--gradient-card) !important;
  border: 2px solid var(--border-primary) !important;
  border-radius: 16px !important;
  padding: 20px !important;
  transition: var(--transition-smooth) !important;
  text-align: left !important;
  min-height: 120px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
}

.feature-button:hover {
  border-color: var(--primary) !important;
  background: rgba(79, 70, 229, 0.1) !important;
  transform: translateY(-2px) !important;
  box-shadow: var(--shadow-lg) !important;
}

/* Responsive Design */
@media (max-width: 768px) {
  .site-title h1 {
    font-size: 36px;
  }
  
  .dashboard-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .feature-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
  
  .site-title {
    padding: 16px 0;
  }
  
  .site-title h1 {
    font-size: 28px;
  }
}

/* Dark theme consistency */
.css-1d391kg, .css-1y4p8pa {
  background-color: transparent !important;
}
</style>
""",
    unsafe_allow_html=True,
)


# ==================== Session State ====================
def init_state():
    if "auth_manager" not in st.session_state:
        st.session_state.auth_manager = init_auth()
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "user_info" not in st.session_state:
        st.session_state.user_info = None
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Dashboard"
    if "selected_template" not in st.session_state:
        st.session_state.selected_template = None
    if "career_query" not in st.session_state:
        st.session_state.career_query = ""
    if "open_template_modal_tid" not in st.session_state:
        st.session_state.open_template_modal_tid = None
    if "auth_tab" not in st.session_state:
        st.session_state.auth_tab = "signin"  # 'signin' | 'signup'

init_state()
handle_oauth_callback()  # OAuth redirects


def refresh_auth_snapshot():
    ui = get_user_info()
    if ui:
        st.session_state.user_info = ui
        st.session_state.authenticated = True

refresh_auth_snapshot()


# ==================== Role Gate ====================
def current_role() -> str:
    ui = st.session_state.get("user_info") or {}
    return ui.get("role", "guest" if not st.session_state.get("authenticated") else "user")

def gate(feature_name: str) -> bool:
    # Guest can access Dashboard, Templates, Builder.
    role = current_role()
    if role == "guest":
        return feature_name in {"Dashboard", "Templates", "Builder"}
    return True


# ==================== Logos ====================
def _find_logo():
    from pathlib import Path as _Path
    candidates = [
        _Path("CareerCanvasAI-removebg-preview.png"),
        _Path("assets/CareerCanvasAI-removebg-preview.png"),
        _Path("static/CareerCanvasAI-removebg-preview.png"),
        _Path("images/CareerCanvasAI-removebg-preview.png"),
        _Path(__file__).with_name("CareerCanvasAI-removebg-preview.png"),
        _Path(__file__).parent / "assets/CareerCanvasAI-removebg-preview.png",
        _Path(__file__).parent / "static/CareerCanvasAI-removebg-preview.png",
    ]
    for p in candidates:
        try:
            if p.exists():
                return str(p)
        except Exception:
            continue
    return None

def show_logo(width: int = 46):
    try:
        p = _find_logo()
        if p:
            st.image(p, width=width)
        else:
            st.markdown(
                '<div style="display:inline-flex;align-items:center;justify-content:center;width:46px;height:46px;border-radius:10px;background:#4f46e5;color:#fff;font-weight:800;">CC</div>',
                unsafe_allow_html=True,
            )
    except Exception:
        st.markdown(
            '<div style="display:inline-flex;align-items:center;justify-content:center;width:46px;height:46px;border-radius:10px;background:#4f46e5;color:#fff;font-weight:800;">CC</div>',
            unsafe_allow_html=True,
        )
GOOGLE_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 48 48" aria-hidden="true" focusable="false">
  <path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.6 32.4 29.3 36 24 36 16.8 36 11 30.2 11 23S16.8 10 24 10c3.6 0 6.9 1.4 9.4 3.6l5.7-5.7C35.4 3.3 29.9 1 24 1 11.8 1 2 10.8 2 23s9.8 22 22 22c11 0 21-8 21-22 0-1.4-.1-2.8-.4-4.5z"/>
  <path fill="#FF3D00" d="M6.3 14.7l6.6 4.8C14.7 16.9 18.9 14 24 14c3.6 0 6.9 1.4 9.4 3.6l5.7-5.7C35.4 7.3 29.9 5 24 5 16 5 9.2 9.2 6.3 14.7z"/>
  <path fill="#4CAF50" d="M24 41c5.2 0 10-2 13.5-5.3l-6.2-5.1C29.5 32.3 26.9 33.4 24 33.4 18.8 33.4 14.4 29.9 13.1 25h-6.9v5.4C8.8 36.7 15.9 41 24 41z"/>
  <path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-1 3.1-3.4 5.6-6.3 6.9l.1.1 6.2 5.1c-.4.3 6.7-3.9 6.7-12.7 0-1.4-.1-2.8-.4-4.5z"/>
</svg>
"""

LINKEDIN_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="#0A66C2" aria-hidden="true" focusable="false">
  <path d="M20.447 20.452H17.21V14.86c0-1.332-.024-3.047-1.858-3.047-1.861 0-2.146 1.45-2.146 2.949v5.69H9.77V9h3.104v1.561h.045c.433-.82 1.492-1.683 3.069-1.683 3.282 0 3.886 2.159 3.886 4.972v6.602zM5.337 7.433c-.998 0-1.806-.81-1.806-1.807 0-.997.808-1.806 1.806-1.806s1.807.809 1.807 1.806c0 .997-.81 1.807-1.807 1.807zM6.556 20.452H4.117V9h2.439v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/>
</svg>
"""


# ==================== PDF helpers ====================
def html_to_pdf_bytes(html: str) -> bytes | None:
    # Try pdfkit (wkhtmltopdf)
    try:
        import pdfkit  # type: ignore
        return pdfkit.from_string(html, False)
    except Exception:
        pass
    # Try WeasyPrint
    try:
        from weasyprint import HTML
        return HTML(string=html).write_pdf()
    except Exception:
        pass
    # Try xhtml2pdf
    try:
        from xhtml2pdf import pisa
        buf = io.BytesIO()
        pisa.CreatePDF(src=html, dest=buf)
        return buf.getvalue()
    except Exception:
        pass
    return None

def text_to_pdf_bytes(title: str, text: str) -> bytes:
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.units import mm

        buf = io.BytesIO()
        doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm)
        styles = getSampleStyleSheet()
        story = [Paragraph(f"<b>{title}</b>", styles["Title"]), Spacer(1, 8)]
        for para in text.split("\n\n"):
            story.append(Paragraph(para.replace("\n", "<br/>"), styles["BodyText"]))
            story.append(Spacer(1, 6))
        doc.build(story)
        return buf.getvalue()
    except Exception:
        return text.encode("utf-8")


# ==================== Auth Landing ====================
def _ensure_state():
    st.session_state.setdefault("auth_tab", "signin")
    st.session_state.setdefault("current_page", "Dashboard")
    st.session_state.setdefault("authenticated", False)
    st.session_state.setdefault("user_info", {})

def render_auth_landing():
    _ensure_state()

    st.markdown('<div class="card" style="max-width:760px;margin:0 auto;">', unsafe_allow_html=True)
    top = st.columns([1, 8])
    with top[0]:
        show_logo(46)
    with top[1]:
        st.markdown("## CVCompass AI")
        st.caption("Career Assistant")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Sign In", use_container_width=True, key="tab_signin",
                     type="primary" if st.session_state.auth_tab == "signin" else "secondary"):
            st.session_state.auth_tab = "signin"
    with c2:
        if st.button("Sign Up", use_container_width=True, key="tab_signup",
                     type="primary" if st.session_state.auth_tab == "signup" else "secondary"):
            st.session_state.auth_tab = "signup"

    if st.session_state.auth_tab == "signin":
        with st.form("signin_form", clear_on_submit=False):
            email = st.text_input("Email", placeholder="Enter your email")
            pwd = st.text_input("Password", type="password", placeholder="Enter your password")

            row = st.columns([2, 1])
            with row[0]:
                submitted = st.form_submit_button("Sign In")
            with row[1]:
                guest = st.form_submit_button("Continue as Guest")

            if submitted:
                if not email or not pwd:
                    st.warning("Please enter both email and password.")
                else:
                    ok, msg = email_sign_in(email, pwd)
                    if ok:
                        refresh_auth_snapshot()
                        st.rerun()
                    else:
                        st.error(msg or "Invalid credentials.")
            if guest:
                start_guest_session()
                refresh_auth_snapshot()
                st.rerun()

        colg, coll = st.columns(2)
        with colg:
            cols = st.columns([1, 6])
            with cols[0]:
                st.markdown(GOOGLE_SVG, unsafe_allow_html=True)
            with cols[1]:
                if st.button("Continue with Google", use_container_width=True, key="google_oauth_btn"):
                    start_google_oauth()
        with coll:
            cols = st.columns([1, 6])
            with cols[0]:
                st.markdown(LINKEDIN_SVG, unsafe_allow_html=True)
            with cols[1]:
                if st.button("Continue with LinkedIn", use_container_width=True, key="linkedin_oauth_btn"):
                    start_linkedin_oauth()

    else:
        with st.form("signup_form", clear_on_submit=False):
            name = st.text_input("Full Name", placeholder="Enter your full name")
            email2 = st.text_input("Email", placeholder="Enter your email")
            pwd2 = st.text_input("Password", type="password", placeholder="Create a strong password")
            submitted2 = st.form_submit_button("Create Account")
            if submitted2:
                if not (name and email2 and pwd2):
                    st.warning("Please fill in all fields.")
                else:
                    ok, msg = email_sign_up(name, email2, pwd2)
                    if ok:
                        st.success("Account created. You are signed in.")
                        refresh_auth_snapshot()
                        st.rerun()
                    else:
                        st.error(msg or "Could not create account.")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
<div class="site-info">
  © {datetime.now().year} CVCompass AI — Build ATS-friendly resumes, analyze your CV, and prepare for interviews with AI.
</div>
""",
        unsafe_allow_html=True,
    )


# ==================== Sidebar & Navigation ====================
def render_app_sidebar():
    with st.sidebar:
        st.markdown('<div class="sidebar-logo">', unsafe_allow_html=True)
        show_logo(46)
        st.markdown('<h2 style="margin-top:8px;">CVCompass AI</h2></div>', unsafe_allow_html=True)

        ui = st.session_state.get("user_info") or {}
        if ui:
            st.markdown(
                f'<div class="card"><div style="font-weight:700">{ui.get("name","User")}</div>'
                f'<div style="color:var(--text-secondary); font-size:12px">{ui.get("email","")}</div>'
                f'<div style="color:var(--text-secondary); font-size:12px">Role: {ui.get("role","user")}</div></div>',
                unsafe_allow_html=True,
            )
            if st.button("Logout", use_container_width=True, key="logout_btn", type="secondary"):
                logout_user()
                st.session_state.authenticated = False
                st.session_state.user_info = None
                st.rerun()

        st.markdown("### Navigation")
        items = ["Dashboard", "Templates", "Builder", "Analyzer", "Career Guide", "Interview Prep"]
        for item in items:
            disabled = not gate(item)
            if st.button(
                f"{'🏠' if item=='Dashboard' else '📄' if item=='Templates' else '🛠️' if item=='Builder' else '📊' if item=='Analyzer' else '💡' if item=='Career Guide' else '💬'}  {item}",
                key=f"nav_{item}", use_container_width=True, disabled=disabled
            ):
                if not disabled:
                    st.session_state.current_page = item
                    st.rerun()
            if disabled:
                st.caption(f"🔒 {item} (sign in required)")


# ==================== Template Preview (modal) ====================
def _render_pdf_scaled_in_modal(html_fragment: str, title: str = "Template Preview", scale: float = 0.55):
    try:
        modal = st.modal(title, key=f"modal_{st.session_state.open_template_modal_tid}")
        with modal:
            st.markdown(
                f"""
<div class="preview-viewport">
  <div class="preview-scale" style="transform: scale({scale});">
    <div style="width:794px;height:1123px;background:#fff;color:#111;border-radius:10px;border:1px solid #e5e7eb;box-shadow:0 8px 22px rgba(0,0,0,.35);padding:28px 36px;overflow:hidden;">
      {html_fragment}
    </div>
  </div>
</div>
""",
                unsafe_allow_html=True,
            )
            st.button("Close", key="close_preview_btn_in_modal", on_click=_close_template_modal)
    except Exception:
        components.html(
            f"""
<div style="display:flex;justify-content:center;align-items:flex-start;">
  <div class="preview-viewport">
    <div class="preview-scale" style="transform: scale({scale});">
      <div style="width:794px;height:1123px;background:#fff;color:#111;border-radius:10px;border:1px solid #e5e7eb;box-shadow:0 8px 22px rgba(0,0,0,.35);padding:28px 36px;overflow:hidden;">
        {html_fragment}
      </div>
    </div>
  </div>
</div>
""",
            height=int(1123 * scale) + 60,
            scrolling=False,
        )
        st.button("Close Preview", key="close_preview_btn_fallback", on_click=_close_template_modal)

def _close_template_modal():
    st.session_state.open_template_modal_tid = None


# ==================== Pages ====================
def page_dashboard():
    st.markdown(
        '<div class="card">Welcome to CVCompass AI. Use the sidebar to explore Templates, Builder, and Analyzer.</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="dashboard-grid">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4, gap="small")
    _kpi(c1, "12", "Resumes Created", "📄")
    _kpi(c2, "12", "Templates", "🎨")
    _kpi(c3, "98%", "ATS Compatible", "✅")
    _kpi(c4, "Cloud", "Processing", "☁️")
    st.markdown('</div>', unsafe_allow_html=True)

    st.subheader("Features we offer")
    f1, f2, f3 = st.columns(3, gap="small")
    with f1:
        if st.button("🎨  Choose Template\nPick from ATS-optimized templates.", use_container_width=True, key="feat_templates"):
            st.session_state.current_page = "Templates"; st.rerun()
    with f2:
        if st.button("🛠️  Build Your Resume\nAI suggestions and live preview.", use_container_width=True, key="feat_builder"):
            st.session_state.current_page = "Builder"; st.rerun()
    with f3:
        if st.button("📊  Analyze & Improve\nUpload a resume for instant insights.", use_container_width=True, key="feat_analyzer"):
            st.session_state.current_page = "Analyzer"; st.rerun()

def _kpi(col, v, label, icon):
    with col:
        st.markdown(
            f'<div class="kpi-card">'
            f'<div style="font-size:24px;margin-bottom:8px">{icon}</div>'
            f'<div class="kpi-value">{v}</div>'
            f'<div class="kpi-label">{label}</div>'
            f'</div>',
            unsafe_allow_html=True
        )


# ==================== Pages ====================
def page_templates():
    st.header("📄 Professional Templates")

    # role filter (clear preview when role changes)
    roles = ["technical", "non-technical"]
    sel = st.selectbox("Filter by role", roles, index=0)
    if st.session_state.get("templates_role") != sel:
        st.session_state.templates_role = sel
        st.session_state.preview_template_id = None

    templates = [t for t in TEMPLATES if t["role_category"] == sel]
    if not templates:
        st.info("No templates for this role.")
        return

    cols = st.columns(3)
    for i, template in enumerate(templates):
        with cols[i % 3]:
            st.markdown(
                f'<div class="card"><div style="display:flex;gap:12px;align-items:center;margin-bottom:12px;">'
                f'<div style="font-size:24px">📄</div>'
                f'<div><div style="font-weight:700;font-size:16px">{template["name"]}</div>'
                f'<div style="font-size:12px;color:var(--text-secondary)">{template["role_category"]}</div></div></div>'
                f'<div style="font-size:13px;color:var(--text-secondary);line-height:1.5">{"Photo slot included" if template["has_image_slot"] else "Text-based layout"}</div></div>',
                unsafe_allow_html=True,
            )
            cprev, cuse = st.columns(2)
            with cprev:
                if st.button("👁 Preview", key=f"prev_{template['id']}", use_container_width=True):
                    st.session_state.preview_template_id = template["id"]
                    st.session_state["scroll_to_preview"] = True
            with cuse:
                disabled = not gate("Builder")
                if st.button("Use", key=f"use_{template['id']}", use_container_width=True, disabled=disabled):
                    if disabled:
                        st.warning("Sign in to use the builder.")
                    else:
                        st.session_state.selected_template = template["id"]
                        st.session_state.builder_template_html = template["html"]
                        st.session_state.current_page = "Builder"
                        st.rerun()

    # Anchor just above preview block for smooth scrolling
    components.html('<div id="preview_block"></div>', height=0)

    # single inline preview block below the role subcontainer
    preview_tid = st.session_state.get("preview_template_id")
    if preview_tid:
        template = get_template_by_id(preview_tid)
        if template:
            st.markdown("### Preview")
            # Smooth scroll into view if just clicked Preview
            if st.session_state.get("scroll_to_preview"):
                components.html(
                    """
<script>
  document.getElementById("preview_block")?.scrollIntoView({behavior:"smooth", block:"start"});
</script>
""",
                    height=0,
                )
                st.session_state["scroll_to_preview"] = False
            # Render template HTML at a sensible height
            components.html(template["html"], height=900, scrolling=True)



def page_builder():
    if not gate("Builder"):
        st.error("🔒 Builder is not available.")
        return
    if not st.session_state.get("selected_template"):
        st.info("Pick a template on the Templates page.")
        return

    # Render the entire builder UI first
    try:
        create_resume_builder_interface()
    except Exception as e:
        st.error(f"Builder error: {e}")

    st.markdown("---")
    st.markdown("#### Actions")

    # Actions row at the bottom
    ctrl = st.columns([1, 1, 1, 4])
    with ctrl[0]:
        if st.button("⬇️ Download PDF", use_container_width=True, key="download_pdf_btn"):
            html = None
            for candidate in ("rendered_resume_html", "resume_html", "final_html"):
                if candidate in st.session_state and isinstance(st.session_state[candidate], str) and st.session_state[candidate].strip():
                    html = st.session_state[candidate]; break
            if html is None:
                try:
                    html = get_template_preview(st.session_state.selected_template)
                except Exception:
                    html = None
            pdf_bytes = html_to_pdf_bytes(html) if html else None
            if not pdf_bytes:
                text_resume = "Resume\n\n"
                for k, v in st.session_state.items():
                    if any(k.startswith(p) for p in ("contact_", "work_", "edu_", "skill_", "summary_", "builder_")) and isinstance(v, str):
                        text_resume += f"{k}: {v}\n"
                pdf_bytes = text_to_pdf_bytes("CVCompass Resume", text_resume)
            st.download_button(
                "Download Resume (PDF)",
                data=pdf_bytes,
                file_name=f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

    with ctrl[1]:
        if st.button("🔄 Reset builder", use_container_width=True, key="reset_builder_btn"):
            for k in list(st.session_state.keys()):
                if k.startswith(("builder_", "resume_", "work_", "edu_", "skill_", "contact_", "section_", "form_")):
                    del st.session_state[k]
            st.success("Builder reset.")
            st.rerun()

    # NEW: quick switch back to templates
    with ctrl[2]:
        if st.button("🎨 Choose another template", use_container_width=True, key="choose_other_template_btn"):
            st.session_state.preview_template_id = None
            st.session_state.current_page = "Templates"
            st.rerun()



def page_analyzer():
    if not gate("Analyzer"):
        st.error("🔒 Analyzer is available after sign-in.")
        return
    st.header("📊 Resume Analyzer")
    up = st.file_uploader("Upload your resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
    if up is not None:
        suffix = Path(up.name).suffix or ".pdf"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(up.getbuffer())
            tmp_path = tmp.name
        try:
            with st.spinner("Reading your file…"):
                text = parse_resume(tmp_path)
            st.success("Resume parsed.")
            st.markdown("### 🔍 Content Preview")
            preview_text = text[:1000] + ("…" if len(text) > 1000 else "")
            st.text_area("First 1000 characters", preview_text, height=280, disabled=True)
            with st.spinner("Analyzing with AI…"):
                advisor = CareerAdvisor()
                feedback_md = advisor.analyze_resume_text(text)
            st.markdown("### ✨ Suggestions")
            st.markdown(feedback_md, unsafe_allow_html=False)
        except Exception as e:
            st.error(f"❌ Unable to analyze resume: {e}")
        finally:
            try: os.unlink(tmp_path)
            except Exception: pass


def page_career_guide():
    if not gate("Career Guide"):
        st.error("🔒 Career Guide is available after sign-in.")
        return
    st.header("💡 Career Guide")
    topics = [
        "How to transition into AI/ML from software engineering?",
        "Best way to tailor my resume for data science roles?",
        "How to negotiate a salary for an ML Engineer role?",
        "Portfolio ideas to stand out for LLM roles?",
    ]
    c1, c2 = st.columns(2)
    for i, t in enumerate(topics):
        with (c1 if i % 2 == 0 else c2):
            if st.button(t, use_container_width=True, key=f"topic_{i}", type="secondary"):
                st.session_state["career_query"] = t
    st.text_area("Ask your question", key="career_query", placeholder="Type a specific career question…", height=140)
    if st.button("🤖 Get AI advice", use_container_width=True):
        q = (st.session_state.get("career_query", "") or "").strip()
        if not q:
            st.warning("Enter a question to get advice.")
        else:
            with st.spinner("Thinking…"):
                advisor = CareerAdvisor()
                try:
                    answer_md = advisor.ask(q)   # STRICT — live LLM only
                    st.markdown("### 💬 AI Advice")
                    st.markdown(answer_md, unsafe_allow_html=False)
                except Exception as e:
                    st.error(
                        "LLM call failed. Verify OpenRouter/HF credentials and model names in your environment. "
                        "See detailed error below."
                    )
                    st.exception(e)


# ==================== Interview Prep ====================

def page_interview_prep():
    if not gate("Interview Prep"):
        st.error("🔒 Interview Prep is available after sign-in.")
        return

    st.header("💬 Interview Preparation")

    c1, c2, c3 = st.columns(3)
    with c1: role = st.text_input("🎯 Target Role", value="Data Scientist")
    with c2: seniority = st.selectbox("📈 Seniority Level", ["Entry Level","Junior","Mid-Level","Senior","Lead/Principal","Executive"], index=2)
    with c3: company_type = st.selectbox("🏢 Company Type", ["Startup","Tech Company","Enterprise","Consulting","Finance","Healthcare"], index=1)

    if st.button("🎯 Generate AI Interview Pack", use_container_width=True):
        with st.spinner("Generating your personalized interview guide…"):
            advisor = CareerAdvisor()
            try:
                # 1) Generate guide
                if _is_technical_role(role):
                    guide_md = advisor.interview_prep_dsa(role, seniority, company_type)
                else:
                    guide_md = advisor.interview_prep_general(role, seniority, company_type)

                # Normalize underline headings to # style to avoid literal ===== lines
                guide_md = _normalize_markdown_headings(guide_md)
                st.markdown("### 📋 Your Interview Guide (AI-generated)")
                st.markdown(guide_md, unsafe_allow_html=False)

                # 2) Stage-wise roadmap
                roadmap_md = advisor.stage_roadmap(role, seniority, company_type)
                roadmap_md = _normalize_markdown_headings(roadmap_md)
                st.markdown("### 🛣️ Role Roadmap (AI-generated)")
                st.markdown(roadmap_md, unsafe_allow_html=False)

                # (Optional) Keep download flow only for the interview guide to avoid UI drift
                pdf_bytes = text_to_pdf_bytes(f"{role} Interview Guide", _strip_md(guide_md))
                st.download_button(
                    "⬇️ Download Guide (PDF)",
                    data=pdf_bytes,
                    file_name=f"interview_guide_{role.replace(' ','_').lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
            except Exception as e:
                st.error(
                    "LLM call failed. Verify OpenRouter/HF credentials and model names in your environment. "
                    "See detailed error below."
                )
                st.exception(e)

def _is_technical_role(role: str) -> bool:
    r = (role or "").lower()
    tech_keywords = [
        "engineer","developer","scientist","ml","ai","data","backend","frontend","full stack",
        "ios","android","mobile","security","cloud","devops","sre","platform","systems","embedded","analytics","analyst"
    ]
    return any(k in r for k in tech_keywords)

def _strip_md(md: str) -> str:
    lines = []
    for line in (md or "").splitlines():
        line = line.replace("**", "")
        if line.startswith("#"):
            line = line.lstrip("# ").upper()
        line = line.replace("•", "- ")
        lines.append(line)
    return "\n".join(lines)

def _normalize_markdown_headings(md: str) -> str:
    # Convert patterns like "Title\n=====..." into "### Title"
    lines = (md or "").splitlines()
    output = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if i + 1 < len(lines):
            underline = lines[i + 1].strip()
            if set(underline) <= set("=") and len(underline) >= 3:
                output.append(f"### {line.strip('* ').strip()}")
                i += 2
                continue
            if set(underline) <= set("-") and len(underline) >= 3:
                output.append(f"### {line.strip('* ').strip()}")
                i += 2
                continue
        # Convert bold heading style like **Title** to ## style
        if line.startswith("**") and line.endswith("**") and len(line) > 4:
            output.append(f"### {line.strip('* ')}")
        else:
            output.append(line)
        i += 1
    return "\n".join(output)



# ==================== Router ====================
def run():
    _ensure_state()
    if not st.session_state.get("authenticated"):
        render_auth_landing()
        return

    # Header with logo
    cols = st.columns([1, 8])
    with cols[0]:
        show_logo(46)
    with cols[1]:
        st.markdown("# CVCompass AI")
        st.caption("Career Assistant")

    render_app_sidebar()

    page = st.session_state.get("current_page", "Dashboard")
    if page == "Dashboard":
        page_dashboard()
    elif page == "Templates":
        page_templates()
    elif page == "Builder":
        page_builder()
    elif page == "Analyzer":
        page_analyzer()
    elif page == "Career Guide":
        page_career_guide()
    elif page == "Interview Prep":
        page_interview_prep()
    else:
        page_dashboard()

    st.markdown(
        f"""
<div class="site-info">
  © {datetime.now().year} CVCompass AI — Build ATS-friendly resumes, analyze your CV, and prepare for interviews with AI.
</div>
""",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    run()