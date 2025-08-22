import os
import json
import logging
from typing import List, Dict, Any, Optional

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def _get_env(*names: str, default: str = "") -> str:
    """Return the first present/nonnull env var from names, else default."""
    for n in names:
        v = os.getenv(n)
        if v is not None and str(v).strip():
            return str(v).strip()
    return default


def _safe_text(resp: requests.Response) -> str:
    try:
        return resp.text
    except Exception:
        try:
            return str(resp.content[:500])
        except Exception:
            return "<unreadable>"


def _messages_to_prompt(messages: List[Dict[str, str]]) -> str:
    parts: List[str] = []
    system_blocks: List[str] = []
    for m in messages:
        role = m.get("role", "user")
        content = (m.get("content") or "").strip()
        if not content:
            continue
        if role == "system":
            system_blocks.append(content)
        elif role == "user":
            parts.append(f"User: {content}")
        elif role == "assistant":
            parts.append(f"Assistant: {content}")
        else:
            parts.append(f"{role.capitalize()}: {content}")
    sys_text = ""
    if system_blocks:
        sys_text = "System instructions:\n" + "\n".join(system_blocks) + "\n\n"
    return sys_text + "\n".join(parts) + "\nAssistant:"


class LLMClient:
    """
    Unified client for hosted LLMs:
      - OpenRouter (preferred)
      - Hugging Face Inference API (fallback)

    Strict: no local/hardcoded fallbacks.
    Includes smart OpenRouter model fallback when a slug has no endpoints.
    """

    def __init__(self):
        # ---------- OpenRouter ----------
        self.or_api_key = _get_env("OPENROUTER_API_KEY")

        # Accept either OPENROUTER_MODEL or LLM_MODEL (your .env may use LLM_MODEL)
        self.or_model = _get_env("OPENROUTER_MODEL", "LLM_MODEL")

        # Allow overriding; default to official base
        self.or_base = _get_env("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1").rstrip("/")

        # Optional attribution headers (support both naming styles)
        self.or_http_referer = _get_env("OPENROUTER_HTTP_REFERER", "OPENROUTER_SITE_URL")
        self.or_title = _get_env("OPENROUTER_APP_TITLE", "OPENROUTER_APP_NAME", default="CVCompass AI")

        # Optional fallback list (comma-separated)
        self.or_fallbacks_env = _get_env("OPENROUTER_FALLBACK_MODELS", "LLM_FALLBACK_MODELS")

        # ---------- Hugging Face ----------
        self.hf_token = _get_env("HF_TOKEN")
        self.hf_model = _get_env("HF_MODEL")

        # Request defaults
        self.timeout = 60

        # Diagnostics
        self._last_model_used: Optional[str] = None
        self._last_provider: Optional[str] = None

    # --------------- Public API ---------------
    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 1024,
        require_hosted: bool = True,
    ) -> str:
        """
        Route to OpenRouter first; if not configured, use Hugging Face.
        """
        # Prefer OpenRouter
        if self._has_openrouter():
            out = self._chat_openrouter_with_fallbacks(messages, temperature, max_tokens)
            self._last_provider = "openrouter"
            return out

        # Otherwise Hugging Face
        if self._has_hf():
            out = self._chat_huggingface(messages, self.hf_model, temperature, max_tokens)
            self._last_provider = "huggingface"
            self._last_model_used = self.hf_model
            return out

        if require_hosted:
            raise RuntimeError(
                "No hosted LLM configured. Set either:\n"
                "- OPENROUTER_API_KEY + (OPENROUTER_MODEL or LLM_MODEL)\n"
                "  (Optional: OPENROUTER_HTTP_REFERER/OPENROUTER_SITE_URL, "
                "OPENROUTER_APP_TITLE/OPENROUTER_APP_NAME, OPENROUTER_BASE_URL, "
                "OPENROUTER_FALLBACK_MODELS/LLM_FALLBACK_MODELS)\n"
                "OR\n"
                "- HF_TOKEN + HF_MODEL"
            )
        raise RuntimeError("Hosted LLM unavailable and strict mode is enabled.")

    def get_last_model_used(self) -> Optional[str]:
        return self._last_model_used

    def get_last_provider(self) -> Optional[str]:
        return self._last_provider

    # --------------- Provider checks ---------------
    def _has_openrouter(self) -> bool:
        return bool(self.or_api_key and self.or_model)

    def _has_hf(self) -> bool:
        return bool(self.hf_token and self.hf_model)

    # --------------- OpenRouter (with smart fallbacks) ---------------
    def _chat_openrouter_with_fallbacks(
        self,
        messages: List[Dict[str, str]],
        temperature: float,
        max_tokens: int,
    ) -> str:
        """
        Try the configured model. If 404 "No endpoints found", attempt:
          - same model without ':free' suffix
          - models from OPENROUTER_FALLBACK_MODELS / LLM_FALLBACK_MODELS
          - 'openrouter/auto'
        """
        tried: List[str] = []
        primary = self.or_model

        candidates: List[str] = [primary]

        # If primary ends with ':free', add a version without it right after
        if primary.endswith(":free"):
            candidates.append(primary.rsplit(":free", 1)[0])

        # Add env-provided fallbacks
        if self.or_fallbacks_env:
            env_models = [m.strip() for m in self.or_fallbacks_env.split(",") if m.strip()]
            candidates.extend(env_models)

        # Always add openrouter/auto as last resort
        if "openrouter/auto" not in candidates:
            candidates.append("openrouter/auto")

        last_error: Optional[Exception] = None
        for model in candidates:
            try:
                content = self._chat_openrouter(messages, temperature, max_tokens, model_override=model)
                self._last_model_used = model
                return content
            except RuntimeError as e:
                tried.append(model)
                # Only swallow and continue on 404 "No endpoints found", otherwise re-raise
                msg = str(e)
                if "OpenRouter error 404" in msg and "No endpoints found" in msg:
                    last_error = e
                    continue
                # Other errors (401/429/500 etc.) → stop and bubble up
                raise

        # If we exhausted candidates
        if last_error:
            raise last_error
        raise RuntimeError(f"OpenRouter could not complete request. Tried models: {tried}")

    def _chat_openrouter(
        self,
        messages: List[Dict[str, str]],
        temperature: float,
        max_tokens: int,
        model_override: Optional[str] = None,
    ) -> str:
        url = f"{self.or_base}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.or_api_key}",
            "Content-Type": "application/json",
        }
        # Optional attribution headers recommended by OpenRouter
        if self.or_http_referer:
            headers["HTTP-Referer"] = self.or_http_referer
        if self.or_title:
            headers["X-Title"] = self.or_title

        payload: Dict[str, Any] = {
            "model": model_override or self.or_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=self.timeout)
        except requests.RequestException as e:
            raise RuntimeError(f"OpenRouter request failed: {e}") from e

        if resp.status_code >= 400:
            detail = _safe_text(resp)
            raise RuntimeError(
                f"OpenRouter error {resp.status_code} at {url}. "
                f"Model='{payload['model']}'. Response:\n{detail}"
            )

        try:
            data = resp.json()
        except Exception as e:
            raise RuntimeError(f"OpenRouter returned non-JSON response: {resp.text[:500]}") from e

        try:
            content = data["choices"][0]["message"]["content"]
            if not isinstance(content, str) or not content.strip():
                raise KeyError("Empty content")
            return content
        except Exception:
            raise RuntimeError(
                f"Unexpected OpenRouter payload format:\n{json.dumps(data, indent=2)[:1500]}"
            )

    # --------------- Hugging Face ---------------
    def _chat_huggingface(
        self,
        messages: List[Dict[str, str]],
        model: str,
        temperature: float,
        max_tokens: int,
    ) -> str:
        url = f"https://api-inference.huggingface.co/models/{model}"
        headers = {
            "Authorization": f"Bearer {self.hf_token}",
            "Content-Type": "application/json",
        }

        prompt = _messages_to_prompt(messages)
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": max_tokens,
                "temperature": temperature,
                "return_full_text": False,
            }
        }

        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=self.timeout)
        except requests.RequestException as e:
            raise RuntimeError(f"Hugging Face request failed: {e}") from e

        if resp.status_code == 403:
            raise RuntimeError(
                "Hugging Face returned 403 (forbidden). "
                "Your token lacks permission to call this model/provider. "
                "Ensure your HF account has access and the token has the correct scope."
            )
        if resp.status_code >= 400:
            detail = _safe_text(resp)
            raise RuntimeError(
                f"Hugging Face error {resp.status_code} for model='{model}'. Response:\n{detail}"
            )

        try:
            data = resp.json()
        except Exception as e:
            raise RuntimeError(f"Hugging Face returned non-JSON response: {resp.text[:500]}") from e

        # Common formats
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and "generated_text" in item and str(item["generated_text"]).strip():
                    return item["generated_text"]
            if data and isinstance(data[0], dict):
                txt = data[0].get("generated_text") or data[0].get("text")
                if isinstance(txt, str) and txt.strip():
                    return txt

        if isinstance(data, dict):
            cand = data.get("generated_text") or data.get("text")
            if isinstance(cand, str) and cand.strip():
                return cand

        raise RuntimeError(f"Unexpected Hugging Face payload:\n{json.dumps(data, indent=2)[:1500]}")
