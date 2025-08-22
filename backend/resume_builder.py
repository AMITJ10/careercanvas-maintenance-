# resume_builder.py
# Builder with LHS form + RHS live preview (properly scaled and fitted). No Download/Reset here (handled in app.py).

import streamlit as st
from resume_templates import get_template_preview, get_template_with_content  # ⬅️ added

def _assemble_html_from_state(template_id: str) -> str:
    """Create a properly formatted resume HTML using session state fields with better template fitting."""
    # Gather fields with defaults
    name = st.session_state.get("contact_name", "Your Name")
    title = st.session_state.get("contact_title", "Your Professional Title")
    email = st.session_state.get("contact_email", "your.email@example.com")
    phone = st.session_state.get("contact_phone", "+91 99999 99999")
    summary = st.session_state.get("summary_text", "Write a compelling professional summary highlighting your key achievements and expertise.")
    skills = st.session_state.get("skill_list", "List your key skills, technologies, and tools")

    # Experience fields
    exp_company = st.session_state.get("work_company", "Company Name")
    exp_role = st.session_state.get("work_role", "Your Job Title")
    exp_duration = st.session_state.get("work_duration", "Jan 2020 – Present")
    exp_desc = st.session_state.get("work_desc", "• Describe your key achievements and responsibilities\n• Use bullet points with metrics and impact\n• Focus on results and outcomes")

    # Education fields
    edu_school = st.session_state.get("edu_school", "University/Institution Name")
    edu_degree = st.session_state.get("edu_degree", "Degree Program")
    edu_duration = st.session_state.get("edu_duration", "2016 – 2020")

    # Format experience description as bullet points
    exp_bullets = ""
    if exp_desc:
        lines = [line.strip() for line in exp_desc.split('\n') if line.strip()]
        for line in lines:
            if not line.startswith('•') and not line.startswith('-'):
                line = '• ' + line
            exp_bullets += f"<li>{line[2:] if line.startswith(('• ', '- ')) else line}</li>"

    # A compact, ATS-safe generic layout (kept from your previous file)
    filled = f"""
<div style="font-family:Inter,Arial,sans-serif; line-height:1.6; color:#333; padding:40px 50px;">
  <div style="text-align:center; margin-bottom:30px; border-bottom:2px solid #2563eb; padding-bottom:20px;">
    <h1 style="margin:0; font-size:32px; font-weight:800; color:#1e40af;">{name.upper()}</h1>
    <div style="font-size:18px; color:#555; margin:8px 0;">{title}</div>
    <div style="font-size:14px; color:#666;">{email} • {phone}</div>
  </div>

  <div style="margin-bottom:25px;">
    <h2 style="color:#1e40af; border-bottom:1px solid #e5e7eb; padding-bottom:5px; font-size:18px;">PROFESSIONAL SUMMARY</h2>
    <p style="color:#4a5568; margin:10px 0;">{summary}</p>
  </div>

  <div style="margin-bottom:25px;">
    <h2 style="color:#1e40af; border-bottom:1px solid #e5e7eb; padding-bottom:5px; font-size:18px;">PROFESSIONAL EXPERIENCE</h2>
    <div style="margin-bottom:20px;">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <h3 style="margin:0; font-size:16px; color:#2d3748;">{exp_role}</h3>
        <span style="color:#666; font-size:14px;">{exp_duration}</span>
      </div>
      <div style="font-weight:600; color:#555; margin:2px 0 10px 0;">{exp_company}</div>
      <ul style="margin:5px 0; padding-left:20px;">{exp_bullets}</ul>
    </div>
  </div>

  <div style="margin-bottom:25px;">
    <h2 style="color:#1e40af; border-bottom:1px solid #e5e7eb; padding-bottom:5px; font-size:18px;">SKILLS</h2>
    <p style="color:#4a5568; margin:10px 0;">{skills}</p>
  </div>

  <div style="margin-bottom:20px;">
    <h2 style="color:#1e40af; border-bottom:1px solid #e5e7eb; padding-bottom:5px; font-size:18px;">EDUCATION</h2>
    <div style="display:flex; justify-content:space-between;">
      <div>
        <div style="font-weight:600; color:#2d3748;">{edu_degree}</div>
        <div style="color:#666;">{edu_school}</div>
      </div>
      <div style="color:#666;">{edu_duration}</div>
    </div>
  </div>
</div>
"""
    return filled


def create_resume_builder_interface():
    template_id = st.session_state.get("selected_template")

    if not template_id:
        st.info("Select a template from the Templates page to start building your resume.")
        return

    # Initialize once with the EXACT template HTML chosen on Templates page
    if not st.session_state.get("initialized_from_template_html"):
        try:
            st.session_state["resume_html"] = get_template_with_content(template_id)
        except Exception:
            st.session_state["resume_html"] = get_template_preview(template_id)
        st.session_state["initialized_from_template_html"] = True  # ⬅️ one-time init

    col_form, col_prev = st.columns([0.8,0.7 ], gap="large")

    with col_form:
        st.markdown("### ✏️ Fill Your Details")

        # Contact Information
        st.markdown("#### 📞 Contact Information")
        st.text_input("Full Name", key="contact_name", placeholder="e.g., John Smith")
        st.text_input("Professional Title", key="contact_title", placeholder="e.g., Senior Software Engineer")
        st.text_input("Email", key="contact_email", placeholder="e.g., john.smith@email.com")
        st.text_input("Phone", key="contact_phone", placeholder="e.g., +91 99999 99999")

        # Professional Summary
        st.markdown("#### 📝 Professional Summary")
        st.text_area(
            "Professional Summary",
            key="summary_text",
            height=120,
            placeholder=(
                "Write a compelling 2-4 sentence summary highlighting your key achievements, "
                "years of experience, and expertise areas..."
            ),
        )

        # Experience Section
        st.markdown("#### 💼 Experience")
        st.text_input("Company", key="work_company", placeholder="e.g., Google India")
        st.text_input("Job Title", key="work_role", placeholder="e.g., Senior Software Engineer")
        st.text_input("Duration", key="work_duration", placeholder="e.g., Jan 2022 – Present")
        st.text_area(
            "Key Achievements",
            key="work_desc",
            height=140,
            placeholder=(
                "• Describe your key achievements with metrics\n"
                "• Use bullet points for better readability\n"
                "• Focus on impact and results\n"
                "• Include numbers and percentages where possible"
            ),
        )

        # Education Section
        st.markdown("#### 🎓 Education")
        st.text_input("Institution", key="edu_school", placeholder="e.g., IIT Delhi")
        st.text_input("Degree", key="edu_degree", placeholder="e.g., B.Tech in Computer Science")
        st.text_input("Duration", key="edu_duration", placeholder="e.g., 2018 – 2022")

        # Skills Section
        st.markdown("#### 🛠️ Skills")
        st.text_area(
            "Technical Skills",
            key="skill_list",
            height=100,
            placeholder=(
                "List your key skills, technologies, programming languages, frameworks, tools, etc.\n"
                "e.g., Python, JavaScript, React, AWS, Docker, Kubernetes"
            ),
        )

        # As user types, assemble a fresh HTML (keeps your existing behavior)
        st.session_state["resume_html"] = _assemble_html_from_state(template_id)

    with col_prev:
        st.markdown("### 👀 Live Preview")

        html_fragment = st.session_state.get("resume_html") or _assemble_html_from_state(template_id)

        st.markdown(
    f"""
<div class="preview-viewport" style="max-width: 100%; margin: 0 auto;">
  <div class="preview-scale" style="transform: scale(0.75); transform-origin: left center; width: 740px; margin: 0 auto;">
    <div class="pdf" style="width: 650px; height: 923px; background: #000; color: #111; border: 1px solid #e5e7eb; border-radius: 10px; box-shadow: 0 10px 24px rgba(0,0,0,0.35); overflow: hidden;">
      {html_fragment}
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

        template_info = st.session_state.get('selected_template', 'Unknown')
        st.caption(f"📋 Template: {template_info}")
        st.caption("💡 Fill the form on the left to see live updates")
