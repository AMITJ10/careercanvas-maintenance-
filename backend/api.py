from __future__ import annotations

import os
from typing import Any, Dict, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse, StreamingResponse
from pydantic import BaseModel, Field

# Templates & previews
from resume_templates import get_all_templates, get_template_preview

# Optional: reuse your Streamlit builder's exact assembler if present
try:
    from resume_builder import _assemble_html_from_state as assemble_from_state  # type: ignore
except Exception:
    assemble_from_state = None

# LLM status & roadmap
from career_advisor import CareerAdvisor
from pdf_generator import generate_resume_pdf
try:
    from llm_client import check_llm_status
except Exception:
    check_llm_status = None

app = FastAPI(title="CVCompass API", version="1.3.0")

# ---------- CORS ----------
frontend_origin = os.getenv("FRONTEND_ORIGIN")
allow_origins = (
    [frontend_origin]
    if frontend_origin
    else [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "*"  # dev fallback; tighten for production
    ]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Models ----------
class RenderPayload(BaseModel):
    # Accept template_id in body (for /api/render route)
    template_id: Optional[str] = Field(default=None)

    contact_name: Optional[str] = None
    contact_title: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    summary_text: Optional[str] = None
    work_company: Optional[str] = None
    work_role: Optional[str] = None
    work_duration: Optional[str] = None
    work_desc: Optional[str] = None
    edu_school: Optional[str] = None
    edu_degree: Optional[str] = None
    edu_duration: Optional[str] = None
    skill_list: Optional[str] = None

class PrepPayload(BaseModel):
    role: str
    seniority: str
    company_type: str

# ---------- Helpers ----------
def _bullets(text: Optional[str]) -> str:
    if not text:
        return "<li>Describe achievements with measurable impact</li>"
    out = []
    for raw in (l.strip() for l in text.split("\n")):
        if not raw:
            continue
        if raw.startswith("• "):
            raw = raw[2:]
        elif raw.startswith("- "):
            raw = raw[2:]
        out.append(f"<li>{raw}</li>")
    return "".join(out)

def _assemble_html_internal(template_id: str, p: Dict[str, Any]) -> str:
    name = (p.get("contact_name") or "Your Name").upper()
    title = p.get("contact_title") or "Your Professional Title"
    email = p.get("contact_email") or "your.email@example.com"
    phone = p.get("contact_phone") or "+91 99999 99999"
    summary = p.get("summary_text") or "Write a strong professional summary…"

    company = p.get("work_company") or "Company Name"
    role = p.get("work_role") or "Your Job Title"
    duration = p.get("work_duration") or "Jan 2020 – Present"
    exp_ul = _bullets(p.get("work_desc"))

    school = p.get("edu_school") or "University/Institution Name"
    degree = p.get("edu_degree") or "Degree Program"
    edu_dur = p.get("edu_duration") or "2016 – 2020"
    skills = p.get("skill_list") or "Python, React, SQL, AWS, Docker"

    if template_id == "se_modern":
        accent, border = "#1e40af", "2px solid #2563eb"
    elif template_id == "ds_elegant":
        accent, border = "#047857", "3px solid #059669"
    elif template_id == "pm_clarity":
        accent, border = "#6b21a8", "3px solid #7c3aed"
    else:
        accent, border = "#1e40af", "2px solid #2563eb"

    return f"""
<div style="font-family:Inter,Arial,sans-serif; line-height:1.6; color:#333; padding:40px 50px;">
  <div style="text-align:center; margin-bottom:30px; border-bottom:{border}; padding-bottom:20px;">
    <h1 style="margin:0; font-size:32px; font-weight:800; color:{accent};">{name}</h1>
    <div style="font-size:18px; color:#555; margin:8px 0;">{title}</div>
    <div style="font-size:14px; color:#666;">{email} • {phone}</div>
  </div>

  <div style="margin-bottom:25px;">
    <h2 style="color:{accent}; border-bottom:1px solid #e5e7eb; padding-bottom:5px; font-size:18px;">PROFESSIONAL SUMMARY</h2>
    <p style="color:#4a5568; margin:10px 0;">{summary}</p>
  </div>

  <div style="margin-bottom:25px;">
    <h2 style="color:{accent}; border-bottom:1px solid #e5e7eb; padding-bottom:5px; font-size:18px;">PROFESSIONAL EXPERIENCE</h2>
    <div style="margin-bottom:20px;">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <h3 style="margin:0; font-size:16px; color:#2d3748;">{role}</h3>
        <span style="color:#666; font-size:14px;">{duration}</span>
      </div>
      <div style="font-weight:600; color:#555; margin:2px 0 10px 0;">{company}</div>
      <ul style="margin:5px 0; padding-left:20px;">{exp_ul}</ul>
    </div>
  </div>

  <div style="margin-bottom:25px;">
    <h2 style="color:{accent}; border-bottom:1px solid #e5e7eb; padding-bottom:5px; font-size:18px;">TECHNICAL SKILLS</h2>
    <p style="color:#4a5568; margin:10px 0;">{skills}</p>
  </div>

  <div style="margin-bottom:20px;">
    <h2 style="color:{accent}; border-bottom:1px solid #e5e7eb; padding-bottom:5px; font-size:18px;">EDUCATION</h2>
    <div style="display:flex; justify-content:space-between;">
      <div>
        <div style="font-weight:600; color:#2d3748;">{degree}</div>
        <div style="color:#666;">{school}</div>
      </div>
      <div style="color:#666;">{edu_dur}</div>
    </div>
  </div>
</div>
"""

# ---------- Routes ----------

# Root → redirect to docs (only one root route!)
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs", status_code=307)

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return RedirectResponse(url="/docs")

@app.get("/api/templates")
def api_list_templates():
    return {
        "templates": [
            {
                "id": t["id"],
                "name": t["name"],
                "role": t["role"],
                "icon": t.get("icon", "📄"),
                "description": t.get("description", ""),
            }
            for t in get_all_templates()
        ]
    }

@app.get("/api/templates/{template_id}/preview", response_class=HTMLResponse)
def api_template_preview(template_id: str):
    html = get_template_preview(template_id)
    if not html:
        raise HTTPException(404, f"Template not found: {template_id}")
    return HTMLResponse(content=html)

# Path-style endpoint (preferred by the frontend)
@app.post("/api/render/{template_id}", response_class=HTMLResponse)
def api_render_template(template_id: str, payload: RenderPayload):
    p = payload.model_dump()
    if assemble_from_state:
        try:
            html = assemble_from_state(template_id)  # type: ignore
        except Exception:
            html = _assemble_html_internal(template_id, p)
    else:
        html = _assemble_html_internal(template_id, p)
    return HTMLResponse(content=html)

# Body-style endpoint (also allowed)
@app.post("/api/render", response_class=HTMLResponse)
def api_render_template_body(payload: RenderPayload):
    if not payload.template_id:
        raise HTTPException(status_code=422, detail="For this route, 'template_id' must be provided in the JSON body.")
    p = payload.model_dump()
    template_id = p.pop("template_id")
    if assemble_from_state:
        try:
            html = assemble_from_state(template_id)  # type: ignore
        except Exception:
            html = _assemble_html_internal(template_id, p)
    else:
        html = _assemble_html_internal(template_id, p)
    return HTMLResponse(content=html)

# ---------- PDF Rendering ----------
def _payload_to_pdf_data(payload: RenderPayload) -> Dict[str, Any]:
    # Map the simpler RenderPayload fields into the reportlab-based PDF schema
    name = (payload.contact_name or "").strip()
    first_name = name.split(" ")[0] if name else ""
    last_name = " ".join(name.split(" ")[1:]) if name and len(name.split(" ")) > 1 else ""

    experiences = []
    if any([payload.work_company, payload.work_role, payload.work_desc, payload.work_duration]):
        experiences.append({
            "title": payload.work_role or "Role",
            "company": payload.work_company or "Company",
            "location": "",
            "start_date": (payload.work_duration or "").split("–")[0].strip() if payload.work_duration else "",
            "end_date": (payload.work_duration or "").split("–")[-1].strip() if payload.work_duration else "",
            "current": False,
            "description": payload.work_desc or "",
        })

    education = []
    if any([payload.edu_school, payload.edu_degree, payload.edu_duration]):
        education.append({
            "degree": payload.edu_degree or "",
            "institution": payload.edu_school or "",
            "location": "",
            "graduation_date": payload.edu_duration or "",
            "gpa": "",
        })

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": payload.contact_email or "",
        "phone": payload.contact_phone or "",
        "city": "",
        "linkedin": "",
        "professional_summary": payload.summary_text or "",
        "experiences": experiences,
        "education": education,
        "technical_skills": payload.skill_list or "",
        "soft_skills": "",
    }

@app.post("/api/pdf/{template_id}")
def api_render_pdf(template_id: str, payload: RenderPayload):
    data = _payload_to_pdf_data(payload)
    pdf_buf = generate_resume_pdf(template_id, data)
    return StreamingResponse(pdf_buf, media_type="application/pdf", headers={
        "Content-Disposition": "attachment; filename=resume.pdf"
    })

@app.get("/api/llm/status")
def api_llm_status():
    if check_llm_status:
        return check_llm_status()
    return {
        "openrouter_available": bool(os.getenv("OPENROUTER_API_KEY")),
        "huggingface_available": bool(os.getenv("HF_TOKEN")),
        "demo_mode": not (os.getenv("OPENROUTER_API_KEY") or os.getenv("HF_TOKEN")),
    }

advisor = CareerAdvisor()

@app.post("/api/interview/roadmap")
def api_interview_roadmap(p: PrepPayload):
    out = advisor.interview_prep_dsa(p.role, p.seniority, p.company_type)
    if not out:
        raise HTTPException(503, "Roadmap generation failed")
    return out

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=int(os.getenv("PORT", "8000")), reload=True)
