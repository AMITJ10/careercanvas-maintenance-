from __future__ import annotations

from io import BytesIO
from typing import Any, Dict, List

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

# ------------------------------------------------------------------------------------
# generate_resume_pdf(template_id, data) -> BytesIO
#   - template_id: "modern" | "classic" | "minimal" | your custom ids
#   - data: dict with keys: first_name,last_name,email,phone,city,linkedin,professional_summary,
#            experiences: List[{title, company, location, start_date, end_date/current, description}],
#            education:   List[{degree, institution, location, graduation_date, gpa}],
#            technical_skills: str, soft_skills: str
# ------------------------------------------------------------------------------------

def _full_name(data: Dict[str, Any]) -> str:
    fn = data.get("first_name", "").strip()
    ln = data.get("last_name", "").strip()
    return (fn + " " + ln).strip() or (data.get("name") or "Your Name")

def _value(v, default=""):
    v = v or default
    return str(v)

def _hline(width=1, color=colors.black):
    return HRFlowable(width="100%", thickness=width, color=color, spaceBefore=6, spaceAfter=6)

def _styles(template_id: str):
    ss = getSampleStyleSheet()
    base = ParagraphStyle(
        "Base",
        parent=ss["Normal"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#0b0f14"),
    )
    h1 = ParagraphStyle(
        "H1", parent=base, fontSize=22, leading=26, spaceAfter=4, textColor=colors.HexColor("#0b0f14"), alignment=1
    )
    h2 = ParagraphStyle(
        "H2", parent=base, fontSize=12.5, leading=16, spaceBefore=10, spaceAfter=4, textColor=colors.HexColor("#0b0f14"),
    )
    small = ParagraphStyle("Small", parent=base, fontSize=9.5, leading=13, textColor=colors.HexColor("#1a2430"))
    bullet = ParagraphStyle("Bullet", parent=base, leftIndent=10, bulletIndent=0, spaceBefore=2, spaceAfter=2)
    accent = colors.HexColor("#1388ff") if template_id == "modern" else colors.HexColor("#111111")
    return base, h1, h2, small, bullet, accent

def generate_resume_pdf(template_id: str, data: Dict[str, Any]) -> BytesIO:
    template_id = (template_id or "modern").lower()
    buf = BytesIO()
    doc = SimpleDocTemplate(
        buf,
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=18 * mm,
        bottomMargin=16 * mm,
        title="Resume",
    )

    base, h1, h2, small, bullet, accent = _styles(template_id)
    flow = []

    # Header
    flow.append(Paragraph(_full_name(data), h1))
    contact_line = " • ".join(
        [p for p in [
            _value(data.get("email")),
            _value(data.get("phone")),
            _value(data.get("city")),
            _value(data.get("linkedin")),
        ] if p]
    )
    if contact_line.strip():
        flow.append(Paragraph(contact_line, small))
    flow.append(Spacer(1, 6))

    # Horizontal rule / accent
    if template_id in ("modern", "classic"):
        flow.append(_hline(1.2, accent))
    else:
        flow.append(_hline(0.8, colors.HexColor("#1b2533")))

    # Summary
    summary = data.get("professional_summary", "").strip()
    if summary:
        flow.append(Paragraph("Summary", h2))
        flow.append(Paragraph(summary.replace("\n", "<br/>"), base))

    # Experience
    exps: List[Dict[str, Any]] = data.get("experiences", []) or []
    if exps:
        flow.append(Paragraph("Experience", h2))
        for e in exps:
            title = _value(e.get("title", "Role"))
            company = _value(e.get("company", "Company"))
            location = _value(e.get("location", ""))
            date = _value(f"{e.get('start_date','')} - {e.get('end_date','Present')}".strip(" -"))
            header = f"<b>{title}</b> at {company}"
            meta = " • ".join([p for p in [location, date] if p])
            flow.append(Paragraph(header, base))
            if meta:
                flow.append(Paragraph(meta, small))
            desc = (e.get("description") or "").strip()
            if desc:
                # simple bullet support with leading •
                for line in desc.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith("•") or line.startswith("- "):
                        flow.append(Paragraph(line.replace("- ", "• ", 1), bullet, bulletText="•"))
                    else:
                        flow.append(Paragraph(line, base))
            flow.append(Spacer(1, 4))

    # Education
    edus: List[Dict[str, Any]] = data.get("education", []) or []
    if edus:
        flow.append(Paragraph("Education", h2))
        tbl = []
        for ed in edus:
            left = f"<b>{_value(ed.get('degree',''))}</b><br/>{_value(ed.get('institution',''))}"
            right = "<br/>".join(
                [p for p in [_value(ed.get("location","")), _value(ed.get("graduation_date","")), _value(ed.get("gpa",""))] if p]
            )
            tbl.append([Paragraph(left, base), Paragraph(right, small)])
        t = Table(tbl, colWidths=[110*mm, 60*mm])
        t.setStyle(TableStyle([
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("INNERGRID", (0,0), (-1,-1), 0.25, colors.whitesmoke),
            ("BOX", (0,0), (-1,-1), 0.25, colors.whitesmoke),
        ]))
        flow.append(t)

    # Skills
    tech = (data.get("technical_skills") or "").strip()
    soft = (data.get("soft_skills") or "").strip()
    if tech or soft:
        flow.append(Paragraph("Skills", h2))
        if tech:
            flow.append(Paragraph(f"<b>Technical:</b> {tech}", base))
        if soft:
            flow.append(Paragraph(f"<b>Soft:</b> {soft}", base))

    # Minimal layout variation per template
    if template_id == "modern":
        # subtle accent line at end
        flow.append(Spacer(1, 8))
        flow.append(_hline(1.0, accent))
    elif template_id == "classic":
        flow.append(Spacer(1, 6))
        flow.append(_hline(0.8, colors.HexColor("#060404")))

    doc.build(flow)
    buf.seek(0)
    return buf


# -------------------- Preview Support --------------------
def _sample_data_for_template(template_id: str) -> Dict[str, Any]:
    return {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@email.com",
        "phone": "(123) 456-7890",
        "city": "Pune, IN",
        "linkedin": "linkedin.com/in/janedoe",
        "professional_summary": "Results-oriented engineer with measurable impact. Passionate about ML and product quality.",
        "experiences": [{
            "title": "Software Engineer",
            "company": "Acme Corp",
            "location": "Remote",
            "start_date": "01/2022",
            "end_date": "Present",
            "current": True,
            "description": "• Built features improving conversion by 12%\n• Reduced API latency by 35% via caching\n• Led testing & CI adoption",
        }],
        "education": [{
            "degree": "B.E. in AI & DS",
            "institution": "Savitribai Phule Pune University",
            "location": "Pune",
            "graduation_date": "06/2023",
            "gpa": "8.7/10",
        }],
        "technical_skills": "Python, C++, SQL, ML, Streamlit, LangChain, FAISS",
        "soft_skills": "Leadership, Communication, Problem Solving",
    }

def create_template_preview_pdf(template_id: str) -> BytesIO:
    data = _sample_data_for_template(template_id)
    return generate_resume_pdf(template_id, data)
