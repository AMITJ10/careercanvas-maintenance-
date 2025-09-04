# resume_builder.py
# Builder with LHS form + RHS live preview (properly scaled and fitted). No Download/Reset here (handled in app.py).

import streamlit as st
import streamlit.components.v1 as components
from resume_templates import get_template_preview, get_template_with_content, get_template_by_id
import base64
import io
from PIL import Image

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

    # A compact, ATS-safe generic layout
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
    <h2 style="color:#1e40af; border-bottom:1px solid #e5e7eb; padding-bottom:5px; font-size:18px;">EXPERIENCE</h2>
    <div>
      <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
        <div style="font-weight:600; color:#2d3748;">{exp_role} — {exp_company}</div>
        <div style="color:#666;">{exp_duration}</div>
      </div>
      <ul style="margin:6px 0 0 18px; color:#4a5568;">{exp_bullets}</ul>
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

    # Use the exact template HTML passed from Templates page
    if "builder_template_html" in st.session_state and st.session_state["builder_template_html"]:
        current_html = st.session_state["builder_template_html"]
    else:
        # Fallback to template preview if no HTML was passed
        current_html = get_template_preview(template_id)
        st.session_state["builder_template_html"] = current_html

    # Check if template has image slot
    template = get_template_by_id(template_id)
    has_image_slot = template and template.get("has_image_slot", False)

    col_form, col_prev = st.columns([0.8, 0.7], gap="large")

    with col_form:
        st.markdown("### ✏️ Fill Your Details")
        
        # Photo upload for templates with image slots
        if has_image_slot:
            st.markdown("#### 📷 Profile Photo")
            uploaded_photo = st.file_uploader("Upload profile photo", type=["png", "jpg", "jpeg", "webp"], key="photo_upload")
            if uploaded_photo:
                try:
                    img = Image.open(uploaded_photo).convert("RGB")
                    bio = io.BytesIO()
                    img.save(bio, format="PNG")
                    data_uri = "data:image/png;base64," + base64.b64encode(bio.getvalue()).decode()
                    
                    # Replace photo placeholder in HTML
                    updated_html = st.session_state["builder_template_html"].replace("{{PHOTO_URL}}", data_uri)
                    st.session_state["builder_template_html"] = updated_html
                    st.success("Photo uploaded successfully!")
                except Exception as e:
                    st.error(f"Error uploading photo: {e}")

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

        # Initialize builder HTML if needed
        if "builder_template_html" not in st.session_state or not st.session_state["builder_template_html"]:
            st.session_state["builder_template_html"] = _assemble_html_from_state(template_id)

    with col_prev:
        st.markdown("### 👀 Live Preview")

        html_doc = st.session_state.get("builder_template_html") or _assemble_html_from_state(template_id)

        # Render the resume correctly (not as raw HTML text) and fit inside preview container
        # Use components.html so full HTML documents render properly
        components.html(html_doc, height=980, scrolling=True)

        template_info = st.session_state.get('selected_template', 'Unknown')
        st.caption(f"📋 Template: {template_info}")
        st.caption("💡 Fill the form on the left to see live updates")
