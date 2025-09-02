from typing import Dict, List, Any
import re
# ---------------------------
# Templates registry
# ---------------------------
_TEMPLATES: Dict[str, Dict[str, Any]] = {
    # 1) Sample 1 (A4 Clean)
    "sample1_a4_clean": {
        "name": "A4 Clean (Sample 1)",
        "role": "All",
        "icon": "🧾",
        "description": "Single-column A4, subtle dividers, ATS-safe.",
        "preview_html": "<div style='padding:12px;font-family:Inter,Arial,sans-serif'><strong>Sample 1</strong> • A4 clean layout</div>",
        "filled_content": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Your Name</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#000000;color:#1f2937;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Inter,Arial,sans-serif;line-height:1.55;">
<!-- Page -->
<main style="max-width:210mm;margin:28px auto;padding:0;background:#000000;box-shadow:0 6px 24px rgba(0,0,0,.08);">
<!-- Content area sized like A4 with printable padding -->
<div style="padding:22mm 18mm 20mm 18mm;">
<!-- Title / Header -->
<header style="text-align:center;margin-bottom:16px;">
<h1 style="margin:0 0 8px 0;font-size:32px;letter-spacing:.2px;font-weight:800;">Your Name</h1>
<div style="font-size:14px;color:#0a4a8a;">
<a href="https://github.com/username" style="color:#0a4a8a;text-decoration:none;">GitHub: username</a>
<span style="color:#6b7280;margin:0 8px;">|</span>
<a href="https://linkedin.com/in/username" style="color:#0a4a8a;text-decoration:none;">LinkedIn: username</a>
<span style="color:#6b7280;margin:0 8px;">|</span>
<a href="https://mysite.com" style="color:#0a4a8a;text-decoration:none;">mysite.com</a>
<span style="color:#6b7280;margin:0 8px;">|</span>
<a href="mailto:email@mysite.com" style="color:#0a4a8a;text-decoration:none;">email@mysite.com</a>
<span style="color:#6b7280;margin:0 8px;">|</span>
<a href="tel:+000000000000" style="color:#0a4a8a;text-decoration:none;">+00.00.000.000</a>
</div>
</header>
<!-- Divider -->
<div style="height:1px;background:#e5e7eb;margin:8px 0 18px 0;"></div>
<!-- Summary -->
<section style="margin-bottom:16px;">
<h2 style="margin:0 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:700;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Summary</h2>
<p style="margin:0;">
This CV can also be automatically compiled and published using GitHub Actions. For details, <a href="https://github.com/jitinnair1/autoCV" style="color:#0a4a8a;text-decoration:none;border-bottom:1px dashed #0a4a8a;">click here</a>.
</p>
</section>
<!-- Work Experience -->
<section style="margin-bottom:16px;">
<h2 style="margin:0 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:700;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Work Experience</h2>
<!-- jobshort -->
<div style="margin:8px 0 10px 0;">
<div style="display:flex;align-items:flex-start;gap:8px;">
<div style="font-weight:700;">Designation</div>
<div style="flex:1 1 auto;"></div>
<div style="white-space:nowrap;color:#374151;">Jan 2021 – present</div>
</div>
<p style="margin:6px 0 0 0;">
Replace with concise, impact-focused bullets describing scope, scale, and measurable outcomes.
</p>
</div>
<!-- joblong -->
<div style="margin:10px 0 0 0;">
<div style="display:flex;align-items:flex-start;gap:8px;">
<div style="font-weight:700;">Designation</div>
<div style="flex:1 1 auto;"></div>
<div style="white-space:nowrap;color:#374151;">Mar 2019 – Jan 2021</div>
</div>
<ul style="margin:6px 0 0 16px;padding:0;list-style-type:'– ';">
<li style="margin:4px 0;">Summarize the work in crisp bullet points.</li>
<li style="margin:4px 0;">Use metrics (%, ₹, time) to show impact.</li>
</ul>
</div>
</section>
<!-- Projects -->
<section style="margin-bottom:16px;">
<h2 style="margin:0 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:700;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Projects</h2>
<div style="display:flex;align-items:flex-start;gap:8px;">
<div style="font-weight:700;">Some Project</div>
<div style="flex:1 1 auto;"></div>
<div><a href="https://example.com" style="color:#0a4a8a;text-decoration:none;">Demo</a></div>
</div>
<p style="margin:6px 0 0 0;">One-liner with problem → approach → outcome.</p>
</section>
<!-- Education -->
<section style="margin-bottom:16px;">
<h2 style="margin:0 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:700;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Education</h2>
<div style="display:grid;grid-template-columns:120px 1fr;gap:8px 14px;">
<div style="color:#374151;">2030 – present</div>
<div>PhD (Subject) at <strong>University</strong> <span style="float:right;color:#374151;">(GPA: 4.0/4.0)</span></div>
<div style="color:#374151;">2023 – 2027</div>
<div>Bachelor's Degree at <strong>College</strong> <span style="float:right;color:#374151;">(GPA: 4.0/4.0)</span></div>
<div style="color:#374151;">2022</div>
<div>Class 12th Some Board <span style="float:right;color:#374151;">(Grades)</span></div>
<div style="color:#374151;">2021</div>
<div>Class 10th Some Board <span style="float:right;color:#374151;">(Grades)</span></div>
</div>
</section>
<!-- Publications -->
<section style="margin-bottom:16px;">
<h2 style="margin:0 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:700;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Publications</h2>
<p style="margin:0;">
(Bibliography entries would be rendered here from <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)
</p>
</section>
<!-- Skills -->
<section>
<h2 style="margin:0 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:700;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Skills</h2>
<div style="display:grid;grid-template-columns:160px 1fr;gap:8px 14px;">
<div style="font-weight:600;">Category</div>
<div style="color:#111827;">List, Of, Relevant, Skills</div>
<div style="font-weight:600;">Category</div>
<div style="color:#111827;">More, Relevant, Skills</div>
</div>
</section>
<!-- Footer -->
<div style="text-align:center;margin-top:22mm;font-size:12px;color:#6b7280;">
Last updated: 19 Aug 2025
</div>
</div>
</main>
</body>
</html>"""
    },

    # 2) Sample 2 (LuxSleek) — light sidebar, dark text
    "sample2_luxsleek": {
        "name": "LuxSleek (Sample 2)",
        "role": "All",
        "icon": "🎛️",
        "description": "Left light sidebar, two-column LuxSleek aesthetic.",
        "preview_html": "<div style='padding:12px;font-family:Inter,Arial,sans-serif'><strong>LuxSleek</strong> • Two-column with sidebar</div>",
        "filled_content": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>LuxSleek CV – John Miller</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#eceff4;color:#111827;font-family: 'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;">
<div style="max-width:210mm; margin:0 auto; background:#ffffff; box-shadow:0 6px 24px rgba(0,0,0,.08);">
<!-- Top band -->
<div style="height:5mm; background:#304263;"></div>
<!-- Two-column layout -->
<div style="display:flex; align-items:flex-start;">
<!-- LEFT COLUMN (light) -->
<aside style="width:33%; background:#e7eef8; color:#111827; padding:18px 0 24px 0;">
<div style="padding-left:9%; padding-right:9%;">
<div style="margin-top:12px; font-size:26px; letter-spacing:0.03em; font-variant:all-small-caps;">
John <span style="font-weight:700;">Miller</span>
</div>
<div style="display:flex; justify-content:center; margin:10px 0 8px 0;">
<img src="https://via.placeholder.com/300x300.png?text=Photo" alt="Profile photo" style="width:65%; height:auto; border-radius:6px; display:block;" />
</div>
<div style="margin-top:10px;">
<div style="text-transform:lowercase; font-variant:small-caps; font-weight:700; margin:20px 0 6px 0;">profile summary</div>
<div style="height:1px; background:#cbd5e1; margin-top:-2px; margin-bottom:10px;"></div>
<p style="margin:0; line-height:1.5;">
Experienced <em>Data Analyst</em> with 5+ years across SQL, Python, Power BI, and reporting. Comfortable translating complex data into actionable insights.
</p>
</div>
<div style="margin-top:16px;">
<div style="text-transform:lowercase; font-variant:small-caps; font-weight:700; margin:20px 0 6px 0;">contact</div>
<div style="height:1px; background:#cbd5e1; margin-top:-2px; margin-bottom:10px;"></div>
<div style="font-size:14px; line-height:1.7;">
<div>✉ <a href="mailto:XXXXXXX@gmail.com" style="color:#0a4a8a; text-decoration:none;">XXXXXXX@gmail.com</a></div>
<div>☎ <a href="tel:+910000000000" style="color:#0a4a8a; text-decoration:none;">+91 00 00 00 00 00</a></div>
<div>✎ <span>XXXXXXXXXXXXX</span></div>
</div>
</div>
<div style="margin-top:16px;">
<div style="text-transform:lowercase; font-variant:small-caps; font-weight:700; margin:20px 0 6px 0;">skills</div>
<div style="height:1px; background:#cbd5e1; margin-top:-2px; margin-bottom:10px;"></div>
<ul style="margin:0; padding-left:18px; line-height:1.55; font-size:14px;">
<li>SQL, Power BI, DAX, Python</li>
<li>Pandas, NumPy, Databricks</li>
<li>Excel, Word, PowerPoint</li>
<li>Reporting, ETL, Data Quality</li>
</ul>
</div>
</div>
</aside>
<!-- RIGHT COLUMN -->
<section style="width:67%; padding:22px 24px 28px 24px;">
<div style="text-transform:lowercase; font-variant:small-caps; letter-spacing:.03em; color:#1f2937; font-size:26px; font-weight:700; margin:0 0 6px 0;">Experience</div>
<div style="height:2px; background:#304263; opacity:.35; margin-top:-6px; margin-bottom:10px;"></div>
<div style="margin-bottom:6px; display:flex; align-items:flex-start;">
<div style="flex:1 1 auto;">
<span style="text-transform:lowercase; font-variant:small-caps;">Data analyst</span> at <em>XXXX (Hyderabad)</em>
</div>
<div style="white-space:nowrap; font-weight:700;">2018.08–2024.05</div>
</div>
<ul style="margin:4px 0 0 0; padding-left:18px; list-style-type:'• '; line-height:1.55;">
<li>Collected, cleaned, and processed large datasets; improved data integrity.</li>
<li>Built interactive dashboards in Power BI; communicated KPIs to stakeholders.</li>
<li>Authored performant SQL (joins, window functions, CTEs) and automated ETL.</li>
</ul>
<div style="margin:18px 0 8px 0; text-transform:lowercase; font-variant:small-caps; letter-spacing:.03em; color:#1f2937; font-size:26px; font-weight:700;">Education</div>
<div style="height:2px; background:#304263; opacity:.35; margin-top:-6px; margin-bottom:10px;"></div>
<div style="display:flex; align-items:flex-start; margin-bottom:6px;">
<div style="flex:1 1 auto;"><span style="text-transform:lowercase; font-variant:small-caps;">MCA</span>, JNTU Kakinada University</div>
<div style="white-space:nowrap; font-weight:700;">2012–2015</div>
</div>
<div style="display:flex; align-items:flex-start;">
<div style="flex:1 1 auto;">B.Sc. (MPC), Acharya Nagarjuna University</div>
<div style="white-space:nowrap; font-weight:700;">2007–2010</div>
</div>
<div style="margin:18px 0 8px 0; text-transform:lowercase; font-variant:small-caps; letter-spacing:.03em; color:#1f2937; font-size:26px; font-weight:700;">Certifications</div>
<div style="height:2px; background:#304263; opacity:.35; margin-top:-6px; margin-bottom:10px;"></div>
<ul style="margin:0; padding-left:18px; list-style-type:'• '; line-height:1.55;">
<li>Intro to Data Analysis using Excel — Coursera</li>
<li>Data Analysis with Python (IBM) — Jul 3, 2024</li>
<li>SQL — HackerRank</li>
</ul>
<div style="margin:18px 0 8px 0; text-transform:lowercase; font-variant:small-caps; letter-spacing:.03em; color:#1f2937; font-size:26px; font-weight:700;">Hobbies</div>
<div style="height:2px; background:#304263; opacity:.35; margin-top:-6px; margin-bottom:10px;"></div>
<p style="margin:0;">Listening to music, playing cricket.</p>
<div style="text-align:center;margin-top:18px;font-size:12px;color:#6b7280;">Last updated: 19 Aug 2025</div>
</section>
</div>
<div style="height:5mm; background:#ffffff;"></div>
</div>
<style>
@media print {
body { background:#ffffff; }
div[style*="max-width:210mm"] { box-shadow:none !important; margin:0 !important; width:210mm !important; }
a { color:#1f2937 !important; text-decoration: none !important; }
}
</style>
</body>
</html>"""
    },

    # 3) Two-Column Blue Sidebar (Operations Manager) — light colors
    "ops_two_col_blue": {
        "name": "Two-Column Blue",
        "role": "Operations Manager",
        "icon": "🧩",
        "description": "Light sidebar with photo, clean right content.",
        "preview_html": "<div style='padding:12px'><b>Ops Two-Column</b> • Sidebar + photo</div>",
        "filled_content": """<div style="display:flex;font-family:Inter,Arial,sans-serif;background:#f5f7fb;">
<aside style="width:30%;background:#e8f0f8;color:#111827;padding:22px 18px;">
<div style="text-align:center;font-size:26px;font-weight:800;margin-bottom:8px;">Ananya <span style="font-weight:300;">Singh</span></div>
<div style="text-align:center;margin:10px 0;"><img src="https://via.placeholder.com/240x240.png?text=Your+Photo" style="width:80%;border-radius:8px;" alt="Photo"/></div>
<div style="font-size:13px;line-height:1.6">
<div><a href="https://github.com/ananya" style="color:#0a4a8a;text-decoration:none">GitHub: ananya</a></div>
<div><a href="https://linkedin.com/in/ananyasingh" style="color:#0a4a8a;text-decoration:none">LinkedIn: /in/ananyasingh</a></div>
<div><a href="https://ananya.co" style="color:#0a4a8a;text-decoration:none">ananya.co</a></div>
<div><a href="mailto:ananya@co.com" style="color:#0a4a8a;text-decoration:none">ananya@co.com</a></div>
<div><a href="tel:+919999999999" style="color:#0a4a8a;text-decoration:none">+91 99999 99999</a></div>
</div>
<hr style="border:0;border-top:1px solid #cbd5e1;margin:14px 0"/>
<div style="text-transform:uppercase;font-weight:700;margin:8px 0">Skills</div>
<ul style="padding-left:18px;margin:0;line-height:1.5">
<li>Process Excellence, Lean, Six Sigma</li>
<li>Vendor Mgmt, Forecasting, S&OP</li>
<li>Stakeholder Communication</li>
</ul>
</aside>
<main style="width:70%;background:#ffffff;padding:24px 28px;">
<h2 style="margin:0 0 10px 0;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Summary</h2>
<p>Operations leader with 8+ years owning S&OP, vendor management and cost optimisation. Reduced logistics spend 18% YoY and improved OTIF from 86%→96%.</p>
<h2 style="margin:18px 0 8px 0;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Work Experience</h2>
<div style="display:flex;gap:8px"><b>Ops Manager</b><div style="flex:1"></div><div style="color:#374151">2021–Present</div></div>
<ul style="margin:6px 0 0 18px">
<li>Implemented S&OP cadence, cutting stockouts by 32%.</li>
<li>Negotiated 11% cost reduction across top 5 vendors.</li>
</ul>
<div style="display:flex;gap:8px;margin-top:8px"><b>Senior Analyst</b><div style="flex:1"></div><div style="color:#374151">2018–2021</div></div>
<ul style="margin:6px 0 0 18px">
<li>Designed allocation model; +7pp OTIF.</li>
<li>Built KPI dashboards with Power BI.</li>
</ul>
<h2 style="margin:18px 0 8px 0;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Projects</h2>
<div style="display:flex"><b>Distribution Network Optimiser</b><div style="flex:1"></div><a href="https://example.com" style="color:#0a4a8a">Link</a></div>
<p>Optimised hub-spoke routes for 14 cities using linear programming; -12% linehaul cost.</p>
<h2 style="margin:18px 极 8px 0;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Education</h2>
<div style="display:grid;grid-template-columns:120px 1fr;gap:8px 14px;">
<div style="color:#374151;">2013–2015</div><div>MBA, <b>IIM Lucknow</b> <span style="float:right;color:#374151">(GPA: 8.8/10)</span></div>
<div style="color:#374151;">2009–2013</div><div>B.E., <b>VTU</b> <span style="float:right;color:#374151">(GPA: 8.2/10)</span></div>
</div>
<h2 style="margin:18px 0 8px 0;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Publications</h2>
<p>(Entries would be rendered from <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)</p>
<div style="text-align:center;margin-top:18px;font-size:12px;color:#6b7280;">Last updated: 19 Aug 2025</div>
</main>
</div>"""
    },

    # 4) Timeline Accent (Teacher)
    "teacher_timeline": {
        "name": "Timeline Accent",
        "role": "Teacher",
        "icon": "📚",
        "description": "Horizontal header with photo + clean sections.",
        "preview_html": "<div style='padding:12px'><b>Teacher</b> • Timeline layout</div>",
        "filled_content": """<div style="font-family:Inter,Arial,sans-serif;background:#f6f7fb;padding:20px;">
<header style="display:flex;gap:16px;align-items:center;background:#ffffff;border-radius:10px;padding:12px 16px;box-shadow:0 极 8px rgba(0,0,0,.05);">
<img src="https://via.placeholder.com/140x140.png?text=Photo" style="border-radius:8px;" alt="Photo"/>
<div>
<h1 style="margin:0">Priya Sharma</h1>
<div><a href="https://github.com/priya" style="color:#0a4a8a;text-decoration:none">GitHub: priya</a> • <a href="极://linkedin.com/in/priyasharma" style="color:#0a4a8a">LinkedIn</a> • <a href="https://priya.edu" style="color:#0a4a8a">priya.edu</a> • <a href="mailto:priya@school.edu" style="color:#0a4a8a">priya@school.edu</a> • <a href="tel:+911234567890" style="color:#极a4a8a">+91 12345 67890</a></div>
</div>
</header>
<section style="margin-top:16px;background:#ffffff;border-radius:10px;padding:16px;">
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin:0 0 8px 0;">Summary</h2>
<p>Student-focused educator with 7+ years in STEM curriculum, project-based learning and Olympiad mentoring; 92% pass rate.</p>
<h2 style="极-bottom:1px solid #e5e7eb;padding-bottom:6px;margin:14px 0 8px 0;">Work Experience</h2>
<div><b>Senior Teacher</b> <span style="float:right;color:#374151">2021–Present</span></div>
<ul style="margin:6极 0 0 18px">
<li>Designed inquiry-based physics labs; +24% concept retention.</li>
<li>Mentored 3 national-level olympiad finalists.</li>
</ul>
<div style="margin-top:8px"><b>Teacher</b> <span style="float:right;color:#374151">2017–2021</span></div>
<ul style="margin:6px 0 0 18px">
<li>Led grade-wide flipped classroom program.</li>
<li>Co-created digital assessments in LMS.</li>
</ul>
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin:14px 0 8px 0;">Projects</h2>
<div style="display:flex"><b>STEM Fair</b><div style="flex:1"></div><a href="https://example.com" style="color:#0a4a8a">Link</a></div>
<p>Organised district STEM fair; 500+ participants; sponsorship ₹3L.</p>
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin:14px 0 8px 0;">Education</h2>
<div style="display:grid;grid-template-columns:120px 1极;gap:8px 14px;">
<div style="color:#374151;">2015–2017</div><div>M.Ed., <b>DU</b> <span style="float:right;color:#374151">(GPA: 9.2/10)</span></div>
<div style="color:#374151;">2011–2015</div><div>B.Sc. Physics, <b>PU</b> <span style="float:right;color:#374151">(GPA: 8.9/极)</span></div>
</div>
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin:14px 0 8px 0;">Publications</极>
<p>(Entries from <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)</p>
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin:14px 0 8px 0;">Skills</h2>
<div style="display:grid;grid-template-columns:160px 1fr;gap:8px 14px;">
<div style="font-weight:600;">Pedagogy</div><div>Curriculum Design, Assessment, PBL</div>
<div style="font-weight:600;">Tools</div><div>Google Classroom, LMS, Excel</div>
</div>
<div style="text-align:center;margin-top:18px;font-size:12px;color:#6b7280;">Last updated: 19 Aug 2025</div>
</section>
</div>"""
    },

    # 5) Minimal Serif (Content Writer)
    "writer_minimal_serif": {
        "name": "Minimal Serif",
        "role": "Content Writer",
        "icon": "🖋️",
        "description": "Serif headings, airy spacing, photo.",
        "preview_html": "<div style='padding:12px'><b>Writer</b> • Minimal serif</div>",
        "filled_content": """<div style="font-family:Georgia, 'Times New Roman', serif; color:#1f2937; line-height:1.7; padding:24px 28px;">
<div style="display:flex; gap:16px; align-items:center; border-bottom:1px solid #e5e7eb; padding-bottom:10px;">
<img src="https://via.placeholder.com/120x120.png?极=Photo" style="border-radius:8px" alt="Photo"/>
<div>
<h1 style="margin:0;">Rhea Kapoor</h1>
<div><a href="https://github.com/rhea" style="color:#0a4a8a;text-decoration:none;">GitHub: rhea</a> • <a href="https://linkedin.com/in/rheakapoor" style="color:#0a4a8a">LinkedIn</a> • <a href="https://rhea.blog" style="color:#0a4a8a">rhea.blog</a> • <a href="mailto:rhea@blog.com" style="color:#0a4a8a">rhea@blog.com</a> • <a href="tel:+919876543210" style="color:#0a4a8a">+91 98765 43210</a></div>
</div>
</div>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:16px;">Summary</h2>
<p>Content strategist and writer delivering long-form and SEO content; grew organic traffic 3.2× in 12 months.</p>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:16px;">Work Experience</h2>
<div style="display:flex"><b>Lead Writer</b><div style="flex:1"></div><div style极color:#374151">2022–Present</div></div>
<ul style="margin:6px 0 极 18px"><li>Editorial calendar; +65% CTR from SERP.</li><li>Managed 5 freelancers; copy QA.</li></ul>
<div style="display:flex;margin-top:8px"><b>Writer</b><div style="flex:1"></div><div style="color:#374151">2019–2022</div></div>
<ul style="margin:6px 0 0 18px"><li>Published 120+ articles; avg 4.8/5 reader score.</li></ul>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:16px;">Projects</h2>
<div style="display:flex"><b>Knowledge Hub</b><div style="flex:1"></div><a href="https://example.com" style="color:#0a4a8a">Link</a></div>
<p>Built internal style guide; reduced edit cycles 40%.</极>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:16px;">Education</h2>
<div style="display:grid;grid-template-columns:120px 1fr;gap:8px 14px;">
<div style="color:#374151;">2015–2018</div><div>BA English, <b>DU</b> <span style="float:right;color:#374151">(GPA: 8.7/10)</span></div>
<div style="color:#374151;">2013–2015</div><div>Class 12 CBSE <span style="float:right;color:#374151">(92%)</span></div>
</div>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:极0; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:16px;">Publications</h2>
<p>(Entries from <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)</p>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:16px;">Skills</h2>
<div style="display:grid;grid-template-columns:160px 1fr;gap:8px 14px;">
<div style="font-weight:600;">Writing</div><div>Long-form, SEO, Research, Editing</div>
<div style="font-weight:600;">Tools</div><div>Docs, Notion, Ahrefs</div>
</div>
<div style="text-align:center;margin-top:18px;font-size:12px;color:#6b7280;">Last updated: 19 Aug 2025</div>
</div>"""
    },

    # 6) Left Accent Bar (Sales Manager)
    "sales_left_bar": {
        "name": "Left Accent Bar",
        "role": "Sales Manager",
        "icon": "💼",
        "description": "Accent bar + metrics focus.",
        "preview_html": "<div style='极adding:12px'><b>Sales</b> • Accent bar</div>",
        "filled_content": """<div style="display:flex;font-family:Inter,Arial,sans-serif;">
<div style="width:8px;background:#b91c1c;"></div>
<div style="flex:1;padding:22px 24px;">
<div style="display:flex;gap:12px;align-items:center">
<img src="https://via.placeholder.com/96.png" style="border-radius:8px" alt="Photo"/>
<div>
<h1 style="margin:0">Arjun Rao</h1>
<div><a href="https://github.com/arjun" style="color:#0a4a8a">GitHub</a> • <a href="https://linkedin.com/in/arjunrao" style="color:#0a4a8a">LinkedIn</a> • <a href="https://arjun.io" style="color:#0a4a8a">arjun.io</a> • <a href="mailto:arjun@sales.com" style="color:#0a4a8a">arjun@sales.com</a> • <a href="tel:+919000000000" style="color:#0a4a8a">+91 90000 00000</a></div>
</极>
</div>
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin-top:12px">Summary</h2>
<p>Sales leader with 9+ years in B2B SaaS; $8.4M quota; 126% average attainment.</p>
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin-top:12px">Work Experience</h2>
<div style="display:flex"><b>Regional Sales Manager</b><div style="flex:1"></div><div style="color:#374151">2021–Present</div></div>
<ul style="margin:6px 0 0 18px"><li>Built 8-rep team; +42% pipeline velocity.</li><li>Won 3 enterprise logos; $3.1M ARR.</li></ul>
<div style="display:flex;margin-top:8px"><b>Account Executive</b><div style="flex:1"></div><div style="color:#374151">2016–2021</div></div>
<ul style="margin:6px 0 0 18px"><li>Beat quota 12/12 quarters; $5.3M total.</li></ul>
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin-top:12px">Projects</h2>
<div style="display:flex"><b极Playbook 2.0</b><div style="flex:1"></div><a href="https://example.com" style="color:#0a4a8a">Link</a></div>
<p>Rebuilt MEDDICC process; 14-day shorter cycle.</p>
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin-top:12px">Education</h2>
<div style="display:grid;grid-template-columns:120px 1fr;gap:8px 14px;">
<div style="color:#374151;">2012–2014</div><div>MBA, <b>ISB</b> <span style="float:right;color:#374151">(GPA: 8.6/10)</span></div>
<div style="color:#374151;">2008–2012</div><div>BBA, <b>MU</b> <span style="float:right;color:#374151">(GPA: 8.4/10)</span></div>
</div>
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin-top:12px">Publications</h2>
<p>(From <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)</p>
<h2 style="border-bottom:1px solid #e5e7eb;padding-bottom:6px;margin-top:12px">Skills</h2>
<div style="display:grid;grid-template-columns:160px 1fr;gap:8px 14px;">
<div style="font-weight:600;">Sales</div><div>MEDDICC, Forecasting, Negotiation</div>
<div style="font-weight:600;">Tools</div><div>Salesforce, HubSpot, Excel</极>
</div>
<div style="text-align:center;margin-top:18px;font-size:12px;color:#6b7280;">Last updated: 19 Aug 2025</div>
</div>
</div>"""
    },

    # 7) Photo Top (Graphic Designer) — light header
    "designer_photo_top": {
        "name": "Photo Top",
        "role": "Graphic Designer",
        "icon": "🎨",
        "description": "Wide photo header, airy sections.",
        "preview_html": "<div style='padding:12px'><b>Designer</b> • Photo header</div>",
        "filled_content": """<div style="极ont-family:Inter,Arial,sans-serif;">
<header style="text-align:center;padding:16px 0;background:#f3f4f6;color:#1极2937">
<img src="https://via.placeholder.com/180x180.png?text=Photo" style="border-radius:50%;border:4px solid #ffffff" alt="Photo"/>
<h1 style="margin:8px 0 0 0">Mehul Verma</h1>
<div style="font-size:14px"><a href="https://github.com/mehul" style="color:#0a4a8a">GitHub</a> • <a href="https://linkedin.com/in/mehulv" style="color:#0a4a8a">LinkedIn</a> • <a href="https://mehul.design" style="color:#0a4a8a">mehul.design</a> • <a href="mail极:mehul@design.com" style="color:#0a4a8a">mehul@design.com</a> • <a href="tel:+919111111111" style="color:#0a4a8a">+91 91111 11111</a></div>
</header>
<main style="max-width:210mm;margin:0 auto;background:#ffffff;padding:20px 24px">
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px;">Summary</h2>
<p>Brand & UI designer with 6+ years shipping multi-device systems; portfolio across fintech, SaaS, retail.</p>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Work Experience</h2>
<div style="display:flex"><b>Lead Designer</b><div style="flex:1"></div><div style="color:#374151">2021–Present</div></div>
<ul style="margin:6px 0 0 18px"><li>Scaled design system; -30% design-dev rework.</li></ul>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Projects</h2>
<div style="display:flex"><b>Design System</b><div style="flex:1"></div><a href="https://example.com" style="color:#0a4a8a">Link</a></div>
<p>Tokens + components; cross-platform kit.</p>
<h2 style="font-size:18极; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Education</h2>
<div style极display:grid;grid-template-columns:120px 1fr;gap:8px 14px;">
<div style="color:#374151;">2013–2017</div><div>B.Des, <b>NID</b> <span style="float:right;color:#374151">(GPA: 8.5/10)</span></div>
<div style="color:#374151;">2011–2013</div><div>Class 12 CBSE <span style="float:right;color:#374151">(91%)</span></div>
</div>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Publications</h2>
<p>(From <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)</p>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Skills</h2>
<div style="display:grid;grid-template-columns:160px 1fr;gap:8px 14px;">
<div style="font-weight:600;">Design</div><div>Brand, UI, Motion</div>
<div style="font-weight:600;">Tools</div><div>Figma, After Effects, Illustrator</div>
</div>
<div style="text-align:center;margin-top:18px;font-size:12px;color:#6b7280;">Last updated: 19 Aug 2025</div>
</main>
</div>"""
    },

    # 8) Classic Grid (HR Generalist)
    "hr_classic_grid": {
        "name": "Classic Grid",
        "role": "HR Generalist",
        "icon": "👥",
        "description": "Grid details with photo badge.",
        "preview_html": "<div style='padding:12px'><b>HR</b> • Classic grid</div>",
        "filled_content": """<div style="font-family:Inter,Arial,sans-serif;max-width:210mm;margin:0 auto;background:#ffffff;padding:22mm 18mm;">
<div style="display:flex;gap:16px;align-items:center">
<img src="https://via.placeholder.com/110.png" style="border-radius:8px" alt="Photo"/>
<div>
<h极 style="margin:0">Simran Kaur</h1>
<div><a href="https://github.com/simran" style="color:#0a4a8a">GitHub</a> • <a href="https://linkedin.com/in/simrank" style="color:#0a4a8a">LinkedIn</a> • <a href="https://simran.hr" style="color:#0a4a8a">simran.h极</a> • <a href="mailto:simran@hr.com" style="color:#0a4a8a">simran@hr.com</极> • <a href="tel:+919222222222" style="color:#0a4a8a">+91 92222 22222</a></div>
</div>
</div>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Summary</h2>
<p>HR generalist with hiring, onboarding and policy programs; hired 120+ roles in 18 months.</p>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Work Experience</h2>
<div style="display:flex"><b>HR Generalist</b><div style="flex:1"></div><div style="color:#374151">2022–Present</div></div>
<ul style="margin:6px 0 0 18px"><li>Scaled TA pipeline; 20 days faster TTF.</li></ul>
<div style="display:flex;margin-top:8px"><b>HR Associate</b><div style="flex:1"></div><div style="color:#374151">2020–2022</div></div>
<ul style="margin:6px 0 0 18px"><li>Rolled onboarding program; CSAT 4.7/5.</li></ul>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Projects</h2>
<div style="display:flex"><b>Policy Hub</b><div style="flex:1"></div><a href="https://example.com" style="color:#0a4a8a">Link</a></div>
<p>Consolidated HR policies; reduced queries 35%.</p>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Education</h2>
<div style="display:grid;grid-template-columns:120px 1fr;gap:8px 极4px;">
<div style="color:#374151;">2018–2020</div><div>MHRM, <b>XLRI</b> <span style="float:right;color:#374151">(GPA: 8.9/10)</span></div>
<div style="极olor:#374151;">2015–2018</div><div>B.Com, <b>DU</b> <span style="float:right;color:#374151">(GPA: 8.4/10)</span></div>
</div>
<h2 style="font-size:18px; letter-spacing:.6px;极ext-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Publications</h2>
<p>(From <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)</p>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Skills</h2>
<div style="display:grid;grid-template-columns:160px 1fr;gap:8px 14px;">
<div style="font-weight:600;">HR</div><div>Recruiting, Onboarding, Policy</div>
<div style="font-weight:600;">Tools</div><div>ATS, Excel, Docs</div>
</div>
<div style="text-align:center;margin-top:18px;font-size:12px;color:#6b7280;">Last updated: 19 Aug 2025</div>
</div>"""
    },

    # 9) Elegant Symmetry (Marketing Manager)
    "mkt_elegant_symmetry": {
        "name": "Elegant Symmetry",
        "role": "Marketing Manager",
        "icon": "📣",
        "description": "Symmetric header, soft lines, photo.",
        "preview_html": "<div style='padding:12px'><b>Marketing</b> • Elegant</div>",
        "filled_content": """<div style="font-family:Inter,Arial,sans-serif;">
<header style="text-align:center;padding:16px 0;border-bottom:1px solid #e5e7eb">
<img src="https://via.placeholder.com/120.png" style="border-radius:50%" alt="Photo"/>
<h1 style="margin:8px 0 0 0">Neha Gupta</h1>
<div><a href="https://github.com/neha" style="color:#0a4a8a">GitHub</a> • <a href="https://linkedin.com/in/nehagupta" style="color:#0a4a8a">LinkedIn</a> • <a href="https://neha.dev" style="color:#0a4a8a">neha.dev</a> • <a href="mailto:neha@marketing.com" style="color:#0a4a8a">neha@marketing.com</a> • <a href="tel:+919333333333" style="color:#0a4a8a">+91 93333 33333</a></div>
</header>
<main style="极ax-width:210mm;margin:0 auto;padding:20px 24px">
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:极px;">Summary</h2>
<p>B2B marketing across lifecycle; +38% SQLs, +22% retention.</p>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Work Experience</h2>
<div style="display:flex"><b>Marketing Manager</b><div style="flex:1"></div><div style="color:#374151">2021–Present</div></div>
<ul style="margin:6px 0 0 18px"><li>Scaled PLG motion; +31% PQL→SQL.</li></ul>
<div style="display:flex;margin-top:8px"><b>Growth Marketer</b><div style="flex:1"></div><div style="color:#374151">极8–2021</div></div>
<ul style="margin:6px 0 0 18px"><li>Ran 50+ experiments; CAC -18%.</li></ul>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Projects</h2>
<div style="display:flex"><b>Docs Revamp</b><div style="flex:1"></div><a href="https://example.com" style="color:#0a4a8a">Link</a></div>
<p>Improved activation; +12% Day-7.</p>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Education</h2>
<div style="display:grid;grid-template-columns:120px 1fr;gap:8px 14px;">
<div style="color:#374151;">2014–2016</div><div>MBA, <b>IIFT</b> <span style="float:right;color:#374151">(GPA: 8.8/10)</span></div>
<div style="color:#374151;">2010–2014</div><div>BBA <span style="float:right;color:#374151">(GPA: 8.1/10)</span></div>
</div>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Publications</h2>
<p>(From <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)</p>
<h2 style="font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px; margin-top:12px;">Skills</h2>
<div style="display:极rid;grid-template-columns:160px 1fr;gap:8px 14px;">
<div style="font-weight:600;">Marketing</div><div>Lifecycle, PLG, SEO/SEM</div>
<div style="font-weight:600;">Tools</div><div>GA4, Looker, HubSpot</div>
</div>
<div style="text-align:center;margin-top:18px;font-size:12px;color:#6b7280;">Last updated: 19 Aug 2025</div>
</main>
</div>"""
    },

    # 10) Bordered Cards (Project Manager)
    "pm_bordered_cards": {
        "name": "Bordered Cards",
        "role": "Project Manager",
        "icon": "🗂️",
        "description": "Carded sections with subtle borders.",
        "preview_html": "<div style='padding:12px'><极>PM</b> • Bordered cards</div>",
        "filled_content": """<div style="font-family:Inter,Arial,sans-serif;max-width:210mm;margin:0 auto;padding:18mm;background:#ffffff;">
<div style="text-align:center">
<h1 style="margin:0">Rohit Nair</h1>
<div><a href="https://github.com/rohit" style="color:#0a4a8a">GitHub</a> • <a href="https://linkedin.com/in/rohitnair" style="color:#0a4a8a">LinkedIn</a> • <a href="https://rohit.pm" style="color:#0a4a8a">rohit.pm</a> • <a href="mailto:rohit@pm.com" style="color:#0a4a8a">rohit@pm.com</a> • <a href="tel:+919444444444" style="color:#0a4a8a">+91 94444 44444</a></div>
</div>
<section style="border:1px solid #e5e7eb;border-radius:8px;padding:12px 14px;margin-top:12px">
<h2 style="margin:0 极 6px 0">Summary</h2>
<p>PM delivering cross-functional programs; on-time delivery 97% across 12 releases.</p>
</section>
<section style="border:1px solid #e5e7eb;border-radius:8px;padding:12px 14px;margin-top:12px">
<h2 style="margin:0 0 6px 0">Work Experience</h2>
<div style="display:flex"><b>Project Manager</b><div style="flex:1"></div><div style="color:#374151">2021–Present</div></div>
<ul style="margin:6px 0 0 18px"><li>Roadmap cadence; burn-down predictability ↑.</li></ul>
<div style="display:flex;margin-top:8px"><b>Associate PM</b><div style="flex:极"></div><div style="color:#374151">2018–2021</div></div>
<ul style="margin:6px 0 0 18px"><li>Release governance; reduced rollbacks.</li></ul>
</section>
<section style="border:1px solid #e5e7eb;border-radius:8px;padding:12px 14px;margin-top:12px">
<h2 style="margin:0 0 6px 0">Projects</h2>
<div style="display:flex"><b>PMO Toolkit</b><div style="flex:1"></div><a href="https://example.com" style="color:#0a4a8a">Link</a></div>
<p>Templates for RAID, RACI, governance.</p>
</section>
<section style="border:1px solid #e5e7eb;border-radius:8px;padding:12px 14px;margin-top:12px">
<h2 style="margin:0 0 6px 0">Education</h2>
<div style="display:grid;grid-template-columns:120px 1fr;gap:8px 14px;">
<div style="color:#374151;">2015–2017</div><div>MBA, <b>SPJIMR</极> <span style="float:right;color:#374151">(GPA: 8.7/10)</span></div>
<div style="color:#374151;">2011–2015</div><div>B.E. <span style="float:right;color:#374151">(GPA: 8.3/10)</span></div>
</div>
</section>
<section style="border:1px solid #e5e7eb;border-radius:8px;padding:12px 14px;margin-top:12px">
<h2 style="margin:0 0 6px 0">Publications</h2>
<p>(From <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)</p>
</section>
<section style="border:1px solid #e5e7eb;border-radius:8px;padding:12px 14px;margin-top:12px">
<h2 style="margin:0 0 6px 0">Skills</h2>
<div style="display:grid;grid-template-columns:160px 1fr;gap:8px 14px;">
<div style="font-weight:600;">Delivery</div><div>Ag极e, RAID, Stakeholder</div>
<div style="font-weight:600;">Tools</div><div>Jira, Confluence, Sheets</div>
</div>
</section>
<div style="text-align:center;margin-top:12px;font-size:12px;color:#6b7280;">Last updated: 19 Aug 2025</div>
</div>"""
    },

    # 11) Mono Typography (Data Analyst)
    "da_mono_typography": {
        "name": "Mono Typography",
        "role": "Data Analyst",
        "icon": "📊",
        "description": "Monospace accents, clean dividers.",
        "preview_html": "<div style='padding:12px'><b>Data Analyst</b> • Mono</div>",
        "filled_content": """<div style="font-family:Inter,Arial,sans-serif;max-width:210mm;margin:0 auto;background:#000000;padding:20mm 18mm;">
<header style="border-bottom:1px solid #ffffff;padding-bottom:6px;margin-bottom:8px">
<h1 style="margin:极">Ishaan Mehta</h1>
<div style="font-family:ui-monospace, SFMono-Regular, Men极o, monospace;font-size:12px;">
<a href="https://github.com/ishaan" style="color:#022345">GitHub</a> • <a href="https://linkedin.com/in/ishaan" style="color:#0a4a8a">LinkedIn</a> • <a href="https://ishaan.dev" style="color:#051f38">ishaan.dev</a> • <a href="mailto:ishaan@data.com" style="color:#0a4a8a">ishaan@data.com</a> • <a href="tel:+919555555555" style="color:#0a4a8a">+91 95555 55555</a>
</div>
</header>
<h2 style="margin:0 0 6px 0; font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px;">Summary</h2>
<p style="margin-top:6px">Analytics specialist; ETL, BI, experimentation; +18% activation.</p>
<h2 style="margin:16px 0 6px 0; font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px;">Work Experience</h2>
<div style="display:flex;align-items:flex-start"><b>Senior Analyst</b><div style="flex:1"></div><div style="color:#374151">2021–Present</div></div>
<ul style="margin:6px 0 0 18px">
<li>Built attribution models; LTV uplift 14%.</li>
<li>Designed metrics layer; single source of truth across 9 domains.</li>
</ul>
<h2 style="margin:16px 0 6px 0; font-size:18px; letter-spacing:.6极; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px;">Projects</h2>
<div style="display:flex;align-items:flex-start"><b>Experiment Hub</b><div style="flex:1"></div><a href="https://example.com" style="color:#0a4a8a">Link</a></div>
<p style="margin-top:6px">Unified A/B test registry with GA4 + BigQuery; automated CUPED and sequential testing.</p>
<h2 style="margin:16px 0 6px 0; font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #e5e7eb; padding-bottom:6px;">Education</h2>
<div style="display:grid;grid-template-columns:120px 1fr;gap:8px 14px;">
<div style="color:#374151;">2014–2018</div>
<div>B.Tech, <b>VJTI</b> <span style="float:right;color:#374151">(GPA: 8.5/10)</span></div>
</div>
<h2 style="margin:16px 0 6px 0; font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #010712; padding-bottom:6px;">Publications</h2>
<p style="margin-top:6px">(Entries sourced from <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)</p>
<h2 style="margin:16px 0 6px 0; font-size:18px; letter-spacing:.6px; text-transform:uppercase; font-weight:700; border-bottom:1px solid #0a0101; padding-bottom:6px;">Skills</h2>
<div style="display:grid;grid-template-columns:160px 1fr;gap:8px 14px;">
<div style="font-weight:600;">Analytics</div><div>Experimentation, Attribution, Cohorts</div>
<div style="font-weight:600;">Data</div><div>SQL, Python, dbt, GA4, BigQuery</div>
<div style="font-weight:600;">Viz</div><div>Looker, Power BI</div>
</div>
<div style="text-align:center;margin-top:18px;font-size:12px;color:#040a14;">Last updated: 19 Aug 2025</div>
</div>"""
    },

    # 12) ATS Split (Machine Learning Engineer) — light rail, ATS-friendly
    "ml_ats_split": {
        "name": "ATS Split",
        "role": "Machine Learning Engineer",
        "icon": "🤖",
        "description": "ATS-safe two-column with left rail skills & tech; no images.",
        "preview_html": "<div style='padding:12px;font-family:Inter,Arial,sans-serif'><b>ML Engineer</b> • ATS two-column</div>",
        "filled_content": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>ML Engineer – Alex Sharma</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#000000;color:#111827;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Inter,Arial,sans-serif;line-height:1.6;">
  <main style="max-width:210mm;margin:24px auto;background:#ffffff;box-shadow:0 6px 24px rgba(0,0,0,.08);">
    <div style="display:flex;align-items:flex-start;">
      <!-- LEFT RAIL -->
      <aside style="width:32%;background:#eef2f7;color:#111827;padding:18px 16px;">
        <div style="font-size:26px;font-weight:800;letter-spacing:.2px;">Alex <span style="font-weight:300;">Sharma</span></div>
        <div style="font-size:13极;margin-top:6px;line-height:1.7;">
          <div><a href="mailto:alex@ml.ai" style="color:#0a4a8a;text-decoration:none;">alex@ml.ai</a></div>
          <div><a href="https://github.com/alexsh" style="color:#0a4a8a;text-decoration:none;">github.com/alexsh</a></div>
          <div><a href="https://linkedin.com/in/alexsharma" style="color:#0a4a8a;text-decoration:none;">linkedin.com/in/alexsharma</a></div>
          <div><a href="https://alex.ai" style="极olor:#0a4a8a;text-decoration:none;">alex.ai</a></div>
          <div><a href="tel:+919888888888" style="color:#0a4a8a;text-decoration:none;">+91 98888 88888</a></div>
        </div>

        <div style="height:1px;background:#cbd5e1;margin:12px 0;"></div>

        <div style="text-transform:uppercase;font-weight:700;margin:10px 0 6px 0;">Skills</div>
        <ul style="margin:0;padding-left:18px;line-height:1.5;">
          <li>PyTorch, TensorFlow, JAX</li>
          <li>Transformers, LLMs, RAG</li>
          <li>Vector DBs (FAISS, pgvector)</li>
          <li>Docker, Kubernetes, Triton</li>
          <li>GCP, AWS (S3, EMR, SageMaker)</li>
          <li>Experimentation, A/B, DPO</li>
        </ul>

        <div style="text-transform:uppercase;font-weight:700;margin:12px 0 6px 0;">Languages</div>
        <div>Python, C++, SQL</div>

        <div style="text-transform:uppercase;font-weight:700;margin:12px 0 6px 0;">Education</div>
        <div style="font-size:14px;">
          <div><b>M.Tech (AI)</b>, IIT Bombay <span style="float:right;color:#374151;">2017–2019</span></div>
          <div><b>B.Tech (CS)</b>, COEP <span style="float:right;color:#374151;">2013–2017</span></div>
        </div>
      </aside>

      <!-- RIGHT CONTENT -->
      <section style="width:68%;padding:20px 22px;">
        <h2 style="margin:0 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:800;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Summary</h2>
        <p style="margin:6px 0 0 0;">
          ML engineer focused on LLMs and applied ML in production. Led training/evaluation of models up to 13B params; designed retrieval pipelines and safe rollout strategies. Shipped features that cut inference cost 27% and improved win-rate +5.8pp.
        </p>

        <h2 style="margin:16px 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:800;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Work Experience</h2>
        <div style="display:flex;gap:8px;align-items:flex-start;margin-top:2px;">
          <div style="font-weight:700;">Senior ML Engineer — AcmeAI</div>
          <div style="flex:1 1 auto;"></div>
          <div style="white-space:nowrap;color:#374151;">2021–Present</div>
        </div>
        <ul style="margin:6px 0 0 18px;">
          <li>Built RAG service with vector DB (FAISS/pgvector); 250ms p95 on 48k corp docs.</li>
          <li>Fine-tuned instruction models with LoRA + DPO; <span style="font-family:ui-monospace">+5.8pp</span> eval win-rate vs baseline.</li>
          <li>Deployed Triton + A100 autoscaling; inference cost -27% via batching + KV caching.</li>
        </ul>

        <div style="display:flex;gap:8px;align-items:flex-start;margin-top:10px;">
          <div style="font-weight:极00;">ML Engineer — DataWorks</div>
          <div style="flex:1 1 auto;"></div>
          <div style="white-space:nowrap;color:#374151;">2019–2021</div>
        </div>
        <ul style="margin:6px 0 0 18px;">
          <li>Productionized NLP pipelines (spaCy + Transformers) for support triage; -19% handle time.</li>
          <li>Implemented feature store + model registry; reduced deploy regressions 30%.</li>
          <li>Introduced offline/online eval parity; cut post-deploy rollback rate by 60%.</li>
        </ul>

        <h2 style="margin:16px 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:800;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Projects</h2>
        <div style="display:flex;align-items:flex-start;">
          <div style="font-weight:700;">LLM Guardrails & Eval Harness</div>
          <div style="flex:1 1 auto;"></div>
          <div><a href="https://example.com" style="color:#0a4a8a;text-decoration:none;">Link</a></div>
        </div>
        <p style="margin:6px 0 0 0;">Policy-based router (toxicity, PII, jailbreak) + eval suite with prompt sets and paired comparison.</p>

        <h2 style="margin:16px 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:800;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Publications</h2>
        <p style="margin:6px 0 0 0;">(Entries sourced from <code style="font-size:12px;background:#f1f5f9;padding:2px 4px;border-radius:4px;">citations.bib</code>.)</p>

        <h2 style="margin:16px 0 8px 0;font-size:18px;letter-spacing:.极px;text-transform:uppercase;font-weight:800;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Skills</h2>
        <div style="display:grid;grid-template-columns:160px 1fr;gap:8px 14px;">
          <div style="font-weight:600;">Modeling</div><极>Transformers, RLHF/DPO, distillation</div>
          <div style="font-weight:600;">Data</div><div>Feature stores, ETL, streaming (Kafka)</div>
          <div style="font-weight:600;">Systems</div><div>CUDA basics, serving, observability</div>
          <div style="font-weight:600;">MLOps</div><div>CI/CD, registry, evals, canary</div>
        </div>

        <div style="text-align:center;margin-top:18px;font-size:12px;color:#6b7280;">Last updated: 19 Aug 2025</div>
      </section>
    </div>

    <div style="height:6mm;background:#000000;"></div>
  </main>

  <style>
    @media print {
      body { background:#ffffff; }
      main { box-shadow:none !important; margin:0 !important; width:210mm !important; }
      a { color:#1f2937 !important; text-decoration:none !important; }
    }
  </style>
</body>
</html>"""
    }
}

_DARK_TEXT = "#0b0f14"  # very dark, readable on white/light backgrounds
# map common neutral grays used in the templates → darker text
_COLOR_MAP = {
    "#1f2937": _DARK_TEXT,
    "#111827": _DARK_TEXT,
    "#374151": _DARK_TEXT,
    "#4b5563": _DARK_TEXT,
    "#6b7280": "#1a2430",   # secondary text -> darker neutral
    "#666":    "#1a2430",
    "#555":    "#15202b",
    "#0a4a8a": "#0a3a6a",   # links slightly darker blue for contrast
}

_COLOR_RE = re.compile("|".join(map(re.escape, _COLOR_MAP.keys())), re.I)

def _normalize_darker_text(html: str) -> str:
    """Force darker, readable text across any template HTML (inline-safe)."""
    if not isinstance(html, str) or not html.strip():
        return html
    html = _COLOR_RE.sub(lambda m: _COLOR_MAP.get(m.group(0).lower(), m.group(0)), html)

    # If body exists but no explicit color on body, enforce one
    if "<body" in html:
        # Extract tag attrs and see if 'color:' present
        try:
            after = html.split("<body", 1)[1].split(">", 1)[0]
        except Exception:
            after = ""
        if "color:" not in after:
            html = html.replace("<body", f"<body style=\"color:{_DARK_TEXT};\"", 1)
    else:
        # Fragment root: inject color into the first style-bearing root container
        if "style='" in html[:400]:
            html = html.replace("style='", f"style='color:{_DARK_TEXT}; ", 1)
        elif 'style="' in html[:400]:
            html = html.replace('style="', f'style="color:{_DARK_TEXT}; ', 1)
    return html
# ---------------------------
# Helper API (used by app.py)
# ---------------------------


TEMPLATES = _TEMPLATES  # public alias expected by app.py

# ADD this helper (near other helpers)
def get_template_by_id(template_id: str) -> Dict[str, Any]:
    return _TEMPLATES[template_id]

# REPLACE your existing __all__ with this
__all__ = [
    "TEMPLATES",
    "get_template_by_id",
    "get_template_preview",
    "get_template_with_content",
    "get_roles",
    "filter_templates_by_role",
]

def get_template_preview(template_id: str) -> str:
    """Return darker-text preview HTML for a template (fallback to content)."""
    t = _TEMPLATES.get(template_id) or {}
    raw = t.get("preview_html") or t.get("filled_content") or "<div>Preview unavailable</div>"
    return _normalize_darker_text(raw)

def get_template_with_content(template_id: str) -> str:
    """Return darker-text full template HTML (fallback to preview)."""
    t = _TEMPLATES.get(template_id) or {}
    raw = t.get("filled_content") or t.get("preview_html") or "<div>No content</div>"
    return _normalize_darker_text(raw)

def get_roles() -> List[str]:
    roles = {"All"}
    for t in _TEMPLATES.values():
        r = (t.get("role") or "").strip() or "All"
        roles.add(r)
    return ["All"] + sorted([r for r in roles if r != "All"])

def filter_templates_by_role(role: str) -> Dict[str, Dict[str, Any]]:
    role = (role or "All").strip()
    if role == "All":
        return dict(_TEMPLATES)
    return {k: v for k, v in _TEMPLATES.items() if (v.get("role") or "").strip() == role}
