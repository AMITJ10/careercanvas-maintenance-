# resume_templates.py - CareerCanvas AI Resume Templates

TEMPLATES = [
    {
        "id": "t01-classic-a4",
        "name": "Classic A4 (Clean)",
        "role_category": "technical",
        "has_image_slot": False,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Your Name</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#f5f6f8;color:#1f2937;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Inter,Arial,sans-serif;line-height:1.55;">
  <!-- Page -->
  <main style="max-width:210mm;margin:28px auto;padding:0;background:#fff;box-shadow:0 6px 24px rgba(0,0,0,.08);">
    <!-- Content area sized like A4 with printable padding -->
    <div style="padding:22mm 18mm 20mm 18mm;">

      <!-- Title / Header -->
      <header style="text-align:center;margin-bottom:16px;">
        <h1 style="margin:0 0 8px 0;font-size:32px;letter-spacing:.2px;font-weight:800;">Your Name</h1>
        <div style="font-size:14px;color:#0a4a8a;">
          <a href="https://github.com/username" style="color:#0a4a8a;text-decoration:none;">GitHub: username</a>
          <span style="color:#94a3b8;margin:0 8px;">|</span>
          <a href="https://linkedin.com/in/username" style="color:#0a4a8a;text-decoration:none;">LinkedIn: username</a>
          <span style="color:#94a3b8;margin:0 8px;">|</span>
          <a href="https://mysite.com" style="color:#0a4a8a;text-decoration:none;">mysite.com</a>
          <span style="color:#94a3b8;margin:0 8px;">|</span>
          <a href="mailto:email@mysite.com" style="color:#0a4a8a;text-decoration:none;">email@mysite.com</a>
          <span style="color:#94a3b8;margin:0 8px;">|</span>
          <a href="tel:+000000000000" style="color:#0a4a8a;text-decoration:none;">+00.00.000.000</a>
        </div>
      </header>

      <!-- Divider -->
      <div style="height:1px;background:#e5e7eb;margin:8px 0 18px 0;"></div>

      <!-- Summary -->
      <section style="margin-bottom:16px;">
        <h2 style="margin:0 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:700;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Summary</h2>
        <p style="margin:0;">
          This CV can also be automatically compiled and published using GitHub Actions.
          For details, <a href="https://github.com/jitinnair1/autoCV" style="color:#0a4a8a;text-decoration:none;border-bottom:1px dashed #0a4a8a;">click here</a>.
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
            <div style="white-space:nowrap;color:#475569;">Jan 2021 – present</div>
          </div>
          <p style="margin:6px 0 0 0;">
            long long line of blah blah that will wrap when the table fills the column width long long line of blah blah that will wrap when the table fills the column width long long line of blah blah that will wrap when the table fills the column width long long line of blah blah that will wrap when the table fills the column width
          </p>
        </div>

        <!-- joblong -->
        <div style="margin:10px 0 0 0;">
          <div style="display:flex;align-items:flex-start;gap:8px;">
            <div style="font-weight:700;">Designation</div>
            <div style="flex:1 1 auto;"></div>
            <div style="white-space:nowrap;color:#475569;">Mar 2019 – Jan 2021</div>
          </div>
          <ul style="margin:6px 0 0 16px;padding:0;list-style-type:'– ';">
            <li style="margin:4px 0;">long long line of blah blah that will wrap when the table fills the column width</li>
            <li style="margin:4px 0;">again, long long line of blah blah that will wrap when the table fills the column width but this time even more long long line of blah blah. again, long long line of blah blah that will wrap when the table fills the column width but this time even more long long line of blah blah</li>
          </ul>
        </div>
      </section>

      <!-- Projects -->
      <section style="margin-bottom:16px;">
        <h2 style="margin:0 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:700;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Projects</h2>
        <div style="display:flex;align-items:flex-start;gap:8px;">
          <div style="font-weight:700;">Some Project</div>
          <div style="flex:1 1 auto;"></div>
          <div><a href="https://some-link.com" style="color:#0a4a8a;text-decoration:none;">Link to Demo</a></div>
        </div>
        <p style="margin:6px 0 0 0;">
          long long line of blah blah that will wrap when the table fills the column width long long line of blah blah that will wrap when the table fills the column width long long line of blah blah that will wrap when the table fills the column width long long line of blah blah that will wrap when the table fills the column width
        </p>
      </section>

      <!-- Education -->
      <section style="margin-bottom:16px;">
        <h2 style="margin:0 0 8px 0;font-size:18px;letter-spacing:.6px;text-transform:uppercase;font-weight:700;border-bottom:1px solid #e5e7eb;padding-bottom:6px;">Education</h2>

        <div style="display:grid;grid-template-columns:120px 1fr;gap:8px 14px;">
          <div style="color:#475569;">2030 – present</div>
          <div>PhD (Subject) at <strong>University</strong> <span style="float:right;color:#475569;">(GPA: 4.0/4.0)</span></div>

          <div style="color:#475569;">2023 – 2027</div>
          <div>Bachelor's Degree at <strong>College</strong> <span style="float:right;color:#475569;">(GPA: 4.0/4.0)</span></div>

          <div style="color:#475569;">2022</div>
          <div>Class 12th Some Board <span style="float:right;color:#475569;">(Grades)</span></div>

          <div style="color:#475569;">2021</div>
          <div>Class 10th Some Board <span style="float:right;color:#475569;">(Grades)</span></div>
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
          <div style="font-weight:600;">Some Skills</div>
          <div style="color:#111827;">This, That, Some of this and that etc.</div>
          <div style="font-weight:600;">Some More Skills</div>
          <div style="color:#111827;">Also some more of this, Some more that, And some of this and that etc.</div>
        </div>
      </section>

      <!-- Footer -->
      <div style="text-align:center;margin-top:22px;font-size:12px;color:#64748b;">
        Last updated: 19 Aug 2025
      </div>

    </div>
  </main>

  <!-- Print helpers -->
  <div style="display:none;">
    <!-- Intentionally left minimal; using inline styles for all layout/typography -->
  </div>
</body>
</html>"""
    },
    {
        "id": "t02-luxsleek",
        "name": "LuxSleek Professional",
        "role_category": "non-technical",
        "has_image_slot": True,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>LuxSleek CV – John Miller</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#eceff4;color:#111827;font-family: 'Fira Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;">

  <!-- A4 canvas -->
  <div style="max-width:210mm; margin:0 auto; background:#ffffff; box-shadow:0 6px 24px rgba(0,0,0,.08);">

    <!-- Full-bleed top band -->
    <div style="height:5mm; background:#304263;"></div>

    <!-- Two-column layout -->
    <div style="display:flex; align-items:flex-start;">

      <!-- LEFT COLUMN -->
      <aside style="width:33%; background:#304263; color:#ffffff; padding:18px 0 24px 0;">
        <!-- inner padding: emulate explicit left/right margins used in TeX -->
        <div style="padding-left:9%; padding-right:9%;">

          <!-- Name -->
          <div style="margin-top:12px; font-size:26px; letter-spacing:0.03em; font-variant:all-small-caps;">
            John <span style="font-weight:700;">Miller</span>
          </div>

          <!-- Portrait -->
          <div style="display:flex; justify-content:center; margin:10px 0 8px 0;">
            <img src="{{PHOTO_URL}}" alt="Profile photo" style="width:65%; height:auto; border-radius:6px; display:block;" />
          </div>

          <!-- Section: Profile Summary -->
          <div style="margin-top:10px;">
            <div style="text-transform:lowercase; font-variant:small-caps; font-weight:700; margin:20px 0 6px 0;">
              profile summary
            </div>
            <div style="height:1px; background:#e5e7eb; opacity:.7; margin-top:-2px; margin-bottom:10px;"></div>
            <p style="margin:0; line-height:1.5;">
              Experienced <em>Data Analyst</em> with over 5+ years of expertise in SQL, Python, Excel, Power BI, Power BI Service, T-SQL, BIRT reporting tool, and Kibana. Proficient in data manipulation, statistical analysis, and data visualization. Skilled in data collection, cleansing, analysis, and creating insightful visual reports to support data-driven decision-making. Strong communicator with a track record of translating complex data into actionable business insights.
            </p>
          </div>

          <!-- Section: Contact details -->
          <div style="margin-top:16px;">
            <div style="text-transform:lowercase; font-variant:small-caps; font-weight:700; margin:20px 0 6px 0;">
              contact details
            </div>
            <div style="height:1px; background:#e5e7eb; opacity:.7; margin-top:-2px; margin-bottom:10px;"></div>
            <div style="font-size:14px; line-height:1.7;">
              <div style="display:flex; align-items:center; gap:8px;"><span style="opacity:.9;">✉</span> <a href="mailto:XXXXXXX@gmail.com" style="color:#ffffff; text-decoration:none;">XXXXXXX@gmail.com</a></div>
              <div style="display:flex; align-items:center; gap:8px;"><span style="opacity:.9;">☎</span> <a href="tel:+910000000000" style="color:#ffffff; text-decoration:none;">+91&nbsp;00&nbsp;00&nbsp;00&nbsp;00&nbsp;00</a></div>
              <div style="display:flex; align-items:center; gap:8px;"><span style="opacity:.9;">✎</span> <span>XXXXXXXXXXXXX</span></div>
            </div>
          </div>

          <!-- Section: Personal information -->
          <div style="margin-top:16px;">
            <div style="text-transform:lowercase; font-variant:small-caps; font-weight:700; margin:20px 0 6px 0;">
              personal information
            </div>
            <div style="height:1px; background:#e5e7eb; opacity:.7; margin-top:-2px; margin-bottom:10px;"></div>
            <div style="font-size:14px; line-height:1.7;">
              <div>Citizenship: <strong>Indian</strong></div>
              <div>Family: <strong>Married with children</strong></div>
              <div>Languages: <strong>English</strong>, <strong>Hindi</strong>, <strong>Telugu</strong></div>
            </div>
          </div>

          <!-- Section: Skills -->
          <div style="margin-top:16px;">
            <div style="text-transform:lowercase; font-variant:small-caps; font-weight:700; margin:20px 0 6px 0;">
              skills
            </div>
            <div style="height:1px; background:#e5e7eb; opacity:.7; margin-top:-2px; margin-bottom:10px;"></div>
            <ul style="margin:0; padding-left:18px; line-height:1.55; font-size:14px;">
              <li>SQL, SSMS, Power BI, Power BI Service, DAX Functions, Tableau, Python, PySpark</li>
              <li>Pandas, NumPy, Warehouse, Azure Databricks</li>
              <li>Microsoft Excel, MS Word, MS PowerPoint</li>
              <li>SQL Server, T-SQL, Kibana, Eclipse BIRT, ETL</li>
              <li>JavaScript, HTML, GitHub</li>
              <li>Communication and team collaboration</li>
            </ul>
          </div>

        </div>
      </aside>

      <!-- RIGHT COLUMN -->
      <section style="width:67%; padding:22px 24px 28px 24px;">

        <!-- Section: Experience -->
        <div style="margin-bottom:18px;">
          <div style="text-transform:lowercase; font-variant:small-caps; letter-spacing:.03em; color:#304263; font-size:26px; font-weight:700; margin:0 0 6px 0;">
            Experience
          </div>
          <div style="height:2px; background:#304263; opacity:.9; margin-top:-6px; margin-bottom:10px;"></div>

          <!-- Job entry -->
          <div style="margin-bottom:6px; display:flex; align-items:flex-start;">
            <div style="flex:1 1 auto;">
              <span style="text-transform:lowercase; font-variant:small-caps;">Data analyst</span> at
              <em>XXXX (Hyderabad).</em>
            </div>
            <div style="white-space:nowrap; font-weight:700;">2018.08–2024.05</div>
          </div>

          <ul style="margin:4px 0 0 0; padding-left:18px; list-style-type:'♦  '; line-height:1.55;">
            <li>Collected, cleaned, and processed large datasets from multiple sources to ensure data accuracy and integrity.</li>
            <li>Conducted exploratory data analysis to identify patterns, trends, and insights using statistical methods and data visualization techniques to support business decisions.</li>
            <li>Maintained automated data pipelines for efficient ETL processes using SQL and Python.</li>
            <li>Created interactive dashboards and reports using Power BI, DAX, and Power BI Service to visualize KPIs and communicate findings to stakeholders.</li>
            <li>Collaborated with cross-functional teams to define requirements, analyze business problems, and develop data-driven solutions; delivered ad-hoc analyses to support strategic initiatives.</li>
            <li>Performed data quality assessments and implemented governance policies to ensure accuracy, consistency, and compliance.</li>
            <li>Authored complex SQL using <code style="background:#f1f5f9; padding:1px 4px; border-radius:3px;">UNION</code>/<code style="background:#f1f5f9; padding:1px 4px; border-radius:3px;">UNION ALL</code>, joins, grouping, filters, and windowing; optimized via stored procedures, views, functions, indexes; used temp tables, CTEs, and variables.</li>
            <li>Hands-on with T-SQL and Microsoft SQL Server Management Studio; solid grasp of DBMS and warehousing concepts.</li>
            <li>Modeled relationships (1-1, 1-many, many-1, many-many); monitored and validated key metric insights from daily reports.</li>
          </ul>
        </div>

        <!-- Section: Education -->
        <div style="margin-bottom:18px;">
          <div style="text-transform:lowercase; font-variant:small-caps; letter-spacing:.03em; color:#304263; font-size:26px; font-weight:700; margin:0 0 6px 0;">
            Education
          </div>
          <div style="height:2px; background:#304263; opacity:.9; margin-top:-6px; margin-bottom:10px;"></div>

          <div style="display:flex; align-items:flex-start; margin-bottom:6px;">
            <div style="flex:1 1 auto;">
              <span style="text-transform:lowercase; font-variant:small-caps;">Master of Computer Application (MCA).</span>
              <em> from JNTU Kakinada University</em>.
            </div>
            <div style="white-space:nowrap; font-weight:700;">2012–2015</div>
          </div>

          <div style="display:flex; align-items:flex-start;">
            <div style="flex:1 1 auto;">
              <span style="text-transform:lowercase; font-variant:small-caps;">Bachelor of Science in Mathematics, Physics, and Computer Science.</span>
              <em> Acharya Nagarjuna University</em>.
            </div>
            <div style="white-space:nowrap; font-weight:700;">2007–2010</div>
          </div>
        </div>

        <!-- Section: Certifications -->
        <div style="margin-bottom:18px;">
          <div style="text-transform:lowercase; font-variant:small-caps; letter-spacing:.03em; color:#304263; font-size:26px; font-weight:700; margin:0 0 6px 0;">
            Certifications
          </div>
          <div style="height:2px; background:#304263; opacity:.9; margin-top:-6px; margin-bottom:10px;"></div>

          <ul style="margin:0; padding-left:18px; list-style-type:'♦  '; line-height:1.55;">
            <li><span style="text-transform:lowercase; font-variant:small-caps;">Introduction to Data Analysis using Microsoft Excel</span>, <em>Coursera.</em></li>
            <li><span style="text-transform:lowercase; font-variant:small-caps;">Data Analysis With Python, Cognitive Class DA0101EN</span>, <em>provided by IBM.</em> <strong>July-3-2024</strong></li>
            <li><span style="text-transform:lowercase; font-variant:small-caps;">SQL</span>, <em>HackerRank</em></li>
          </ul>
        </div>

        <!-- Section: Hobbies -->
        <div>
          <div style="text-transform:lowercase; font-variant:small-caps; letter-spacing:.03em; color:#304263; font-size:26px; font-weight:700; margin:0 0 6px 0;">
            Hobbies
          </div>
          <div style="height:2px; background:#304263; opacity:.9; margin-top:-6px; margin-bottom:10px;"></div>
          <p style="margin:0;">Listening to music, playing cricket</p>
        </div>

      </section>
    </div>

    <!-- Bottom whitespace strip to emulate full-bleed -->
    <div style="height:5mm; background:#ffffff;"></div>
  </div>

  <!-- Print adjustments -->
  <style>
    @media print {
      body { background:#ffffff; }
      /* Remove shadows and fit to page */
      div[style*="max-width:210mm"] { box-shadow:none !important; margin:0 !important; width:210mm !important; }
      a { color: #304263 !important; text-decoration: none !important; }
    }
  </style>
</body>
</html>"""
    },
    {
        "id": "t03-elegant-two-col",
        "name": "Elegant Two Column",
        "role_category": "non-technical",
        "has_image_slot": True,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Sarah Johnson</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#f8f9fa;color:#2c3e50;font-family:'Georgia',serif;line-height:1.6;">
  <main style="max-width:210mm;margin:20px auto;background:#ffffff;box-shadow:0 4px 20px rgba(0,0,0,.1);">
    <div style="display:flex;">
      <!-- Left Column -->
      <aside style="width:35%;background:#34495e;color:#ecf0f1;padding:30px 25px;">
        <div style="text-align:center;margin-bottom:25px;">
          <img src="{{PHOTO_URL}}" alt="Profile" style="width:120px;height:120px;border-radius:50%;border:4px solid #ecf0f1;margin-bottom:15px;" />
          <h1 style="margin:0;font-size:24px;font-weight:300;letter-spacing:1px;">SARAH JOHNSON</h1>
          <p style="margin:5px 0 0 0;font-size:14px;opacity:0.9;">Marketing Director</p>
        </div>
        
        <section style="margin-bottom:25px;">
          <h2 style="margin:0 0 15px 0;font-size:16px;font-weight:600;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #e74c3c;padding-bottom:5px;">Contact</h2>
          <div style="font-size:13px;line-height:1.8;">
            <p style="margin:0;"><strong>Email:</strong> <a href="mailto:sarah.johnson@email.com" style="color:#ecf0f1;">sarah.johnson@email.com</a></p>
            <p style="margin:0;"><strong>Phone:</strong> <a href="tel:+15551234567" style="color:#ecf0f1;">+1 (555) 123-4567</a></p>
            <p style="margin:0;"><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/sarahjohnson" style="color:#ecf0f1;">linkedin.com/in/sarahjohnson</a></p>
            <p style="margin:0;"><strong>Location:</strong> New York, NY</p>
          </div>
        </section>

        <section style="margin-bottom:25px;">
          <h2 style="margin:0 0 15px 0;font-size:16px;font-weight:600;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #e74c3c;padding-bottom:5px;">Skills</h2>
          <div style="font-size:13px;">
            <div style="margin-bottom:12px;">
              <p style="margin:0 0 5px 0;font-weight:600;">Digital Marketing</p>
              <div style="background:#2c3e50;height:6px;border-radius:3px;"><div style="background:#e74c3c;height:6px;width:95%;border-radius:3px;"></div></div>
            </div>
            <div style="margin-bottom:12px;">
              <p style="margin:0 0 5px 0;font-weight:600;">Brand Strategy</p>
              <div style="background:#2c3e50;height:6px;border-radius:3px;"><div style="background:#e74c3c;height:6px;width:90%;border-radius:3px;"></div></div>
            </div>
            <div style="margin-bottom:12px;">
              <p style="margin:0 0 5px 0;font-weight:600;">Team Leadership</p>
              <div style="background:#2c3e50;height:6px;border-radius:3px;"><div style="background:#e74c3c;height:6px;width:88%;border-radius:3px;"></div></div>
            </div>
            <div style="margin-bottom:12px;">
              <p style="margin:0 0 5px 0;font-weight:600;">Analytics & ROI</p>
              <div style="background:#2c3e50;height:6px;border-radius:3px;"><div style="background:#e74c3c;height:6px;width:85%;border-radius:3px;"></div></div>
            </div>
          </div>
        </section>

        <section>
          <h2 style="margin:0 0 15px 0;font-size:16px;font-weight:600;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #e74c3c;padding-bottom:5px;">Languages</h2>
          <div style="font-size:13px;line-height:1.8;">
            <p style="margin:0;"><strong>English:</strong> Native</p>
            <p style="margin:0;"><strong>Spanish:</strong> Fluent</p>
            <p style="margin:0;"><strong>French:</strong> Conversational</p>
          </div>
        </section>
      </aside>

      <!-- Right Column -->
      <section style="width:65%;padding:30px 35px;">
        <section style="margin-bottom:25px;">
          <h2 style="margin:0 0 15px 0;font-size:20px;color:#34495e;font-weight:600;text-transform:uppercase;letter-spacing:1px;border-bottom:3px solid #e74c3c;padding-bottom:8px;">Summary</h2>
          <p style="margin:0;font-size:14px;text-align:justify;">
            Results-driven Marketing Director with over 8 years of experience developing and executing comprehensive marketing strategies that drive brand awareness and revenue growth. Proven track record of leading cross-functional teams, managing multi-million dollar budgets, and delivering measurable ROI through innovative digital campaigns and strategic partnerships.
          </p>
        </section>

        <section style="margin-bottom:25px;">
          <h2 style="margin:0 0 15px 0;font-size:20px;color:#34495e;font-weight:600;text-transform:uppercase;letter-spacing:1px;border-bottom:3px solid #e74c3c;padding-bottom:8px;">Work Experience</h2>
          
          <div style="margin-bottom:20px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
              <h3 style="margin:0;font-size:16px;font-weight:600;color:#2c3e50;">Marketing Director</h3>
              <span style="font-size:13px;color:#7f8c8d;font-weight:500;">2020 – Present</span>
            </div>
            <p style="margin:0 0 8px 0;font-size:14px;color:#e74c3c;font-weight:500;">TechCorp Solutions, New York</p>
            <ul style="margin:0;padding-left:20px;font-size:13px;">
              <li>Led a team of 12 marketing professionals across digital, content, and brand marketing divisions</li>
              <li>Increased brand awareness by 150% through integrated marketing campaigns and strategic partnerships</li>
              <li>Managed annual marketing budget of $2.5M, consistently delivering 25% ROI improvement year-over-year</li>
              <li>Launched successful product campaigns resulting in 40% increase in qualified leads</li>
            </ul>
          </div>

          <div style="margin-bottom:20px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
              <h3 style="margin:0;font-size:16px;font-weight:600;color:#2c3e50;">Senior Marketing Manager</h3>
              <span style="font-size:13px;color:#7f8c8d;font-weight:500;">2017 – 2020</span>
            </div>
            <p style="margin:0 0 8px 0;font-size:14px;color:#e74c3c;font-weight:500;">Digital Innovations Inc., Boston</p>
            <ul style="margin:0;padding-left:20px;font-size:13px;">
              <li>Developed and executed digital marketing strategies across multiple channels including social media, email, and PPC</li>
              <li>Collaborated with sales team to create lead nurturing campaigns that improved conversion rates by 35%</li>
              <li>Managed relationships with external agencies and vendors to optimize campaign performance</li>
            </ul>
          </div>
        </section>

        <section style="margin-bottom:25px;">
          <h2 style="margin:0 0 15px 0;font-size:20px;color:#34495e;font-weight:600;text-transform:uppercase;letter-spacing:1px;border-bottom:3px solid #e74c3c;padding-bottom:8px;">Projects</h2>
          <div style="margin-bottom:15px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px;">
              <h3 style="margin:0;font-size:15px;font-weight:600;color:#2c3e50;">Global Brand Relaunch Campaign</h3>
              <a href="https://campaign-demo.com" style="color:#e74c3c;text-decoration:none;font-size:13px;">View Campaign</a>
            </div>
            <p style="margin:0;font-size:13px;">
              Orchestrated complete brand identity overhaul including logo redesign, messaging framework, and multi-channel launch strategy. Campaign reached 2M+ impressions and generated 15,000 new leads within first quarter.
            </p>
          </div>
        </section>

        <section style="margin-bottom:25px;">
          <h2 style="margin:0 0 15px 0;font-size:20px;color:#34495e;font-weight:600;text-transform:uppercase;letter-spacing:1px;border-bottom:3px solid #e74c3c;padding-bottom:8px;">Education</h2>
          <div style="display:grid;grid-template-columns:120px 1fr;gap:10px;font-size:13px;">
            <div style="color:#7f8c8d;font-weight:500;">2013 – 2017</div>
            <div>MBA in Marketing at <strong>Harvard Business School</strong> <span style="float:right;color:#7f8c8d;">(GPA: 3.8/4.0)</span></div>
            <div style="color:#7f8c8d;font-weight:500;">2009 – 2013</div>
            <div>Bachelor of Arts in Communications at <strong>Columbia University</strong> <span style="float:right;color:#7f8c8d;">(GPA: 3.7/4.0)</span></div>
          </div>
        </section>

        <section style="margin-bottom:25px;">
          <h2 style="margin:0 0 15px 0;font-size:20px;color:#34495e;font-weight:600;text-transform:uppercase;letter-spacing:1px;border-bottom:3px solid #e74c3c;padding-bottom:8px;">Publications</h2>
          <p style="margin:0;font-size:13px;">
            "The Future of Digital Marketing: Trends and Strategies for 2024" - <em>Marketing Today Magazine</em>, March 2024<br/>
            "Building Brand Loyalty in the Digital Age" - <em>Harvard Business Review</em>, September 2023
          </p>
        </section>

        <section>
          <h2 style="margin:0 0 15px 0;font-size:20px;color:#34495e;font-weight:600;text-transform:uppercase;letter-spacing:1px;border-bottom:3px solid #e74c3c;padding-bottom:8px;">Skills</h2>
          <div style="display:grid;grid-template-columns:140px 1fr;gap:8px;font-size:13px;">
            <div style="font-weight:600;">Marketing Tools</div>
            <div>HubSpot, Salesforce, Google Analytics, Adobe Creative Suite, Mailchimp</div>
            <div style="font-weight:600;">Specializations</div>
            <div>Brand Strategy, Digital Marketing, Content Marketing, Lead Generation, Marketing Automation</div>
          </div>
        </section>

        <div style="text-align:center;margin-top:30px;font-size:11px;color:#95a5a6;">
          Last updated: 19 Aug 2025
        </div>
      </section>
    </div>
  </main>
</body>
</html>"""
    },
    {
        "id": "t04-modern-grid",
        "name": "Modern Grid Layout",
        "role_category": "technical",
        "has_image_slot": False,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Alex Chen</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#f0f2f5;color:#1a202c;font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.6;">
  <main style="max-width:210mm;margin:20px auto;background:#ffffff;box-shadow:0 10px 40px rgba(0,0,0,.1);">
    <div style="padding:40px;">
      <!-- Header Grid -->
      <header style="display:grid;grid-template-columns:1fr auto;gap:30px;margin-bottom:40px;padding-bottom:25px;border-bottom:3px solid #4299e1;">
        <div>
          <h1 style="margin:0 0 8px 0;font-size:36px;font-weight:800;color:#2d3748;letter-spacing:-0.5px;">Alex Chen</h1>
          <p style="margin:0 0 15px 0;font-size:18px;color:#4299e1;font-weight:600;">Full Stack Developer</p>
          <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:8px;font-size:14px;">
            <div><strong>Email:</strong> <a href="mailto:alex.chen@email.com" style="color:#4299e1;text-decoration:none;">alex.chen@email.com</a></div>
            <div><strong>Phone:</strong> <a href="tel:+15551234567" style="color:#4299e1;text-decoration:none;">+1 (555) 123-4567</a></div>
            <div><strong>GitHub:</strong> <a href="https://github.com/alexchen" style="color:#4299e1;text-decoration:none;">github.com/alexchen</a></div>
            <div><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/alexchen" style="color:#4299e1;text-decoration:none;">linkedin.com/in/alexchen</a></div>
          </div>
        </div>
        <div style="text-align:right;">
          <div style="background:#4299e1;color:#ffffff;padding:15px 20px;border-radius:8px;font-size:14px;font-weight:600;">
            <div>5+ Years</div>
            <div style="font-size:12px;opacity:0.9;">Experience</div>
          </div>
        </div>
      </header>

      <!-- Main Grid Layout -->
      <div style="display:grid;grid-template-columns:2fr 1fr;gap:40px;">
        <!-- Left Column -->
        <div>
          <section style="margin-bottom:35px;">
            <h2 style="margin:0 0 20px 0;font-size:22px;font-weight:700;color:#2d3748;text-transform:uppercase;letter-spacing:1px;border-left:4px solid #4299e1;padding-left:15px;">Summary</h2>
            <p style="margin:0;font-size:15px;text-align:justify;color:#4a5568;">
              Passionate Full Stack Developer with 5+ years of experience building scalable web applications using modern technologies. Expertise in React, Node.js, Python, and cloud platforms. Strong background in agile development, system architecture, and leading technical teams to deliver high-quality software solutions.
            </p>
          </section>

          <section style="margin-bottom:35px;">
            <h2 style="margin:0 0 20px 0;font-size:22px;font-weight:700;color:#2d3748;text-transform:uppercase;letter-spacing:1px;border-left:4px solid #4299e1;padding-left:15px;">Work Experience</h2>
            
            <div style="margin-bottom:25px;padding:20px;background:#f7fafc;border-radius:8px;border-left:4px solid #4299e1;">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
                <h3 style="margin:0;font-size:18px;font-weight:600;color:#2d3748;">Senior Full Stack Developer</h3>
                <span style="background:#4299e1;color:#ffffff;padding:4px 12px;border-radius:20px;font-size:12px;font-weight:600;">2021 – Present</span>
              </div>
              <p style="margin:0 0 12px 0;font-size:15px;color:#4299e1;font-weight:500;">TechFlow Solutions, San Francisco</p>
              <ul style="margin:0;padding-left:20px;font-size:14px;color:#4a5568;">
                <li>Led development of microservices architecture serving 100K+ daily active users</li>
                <li>Implemented CI/CD pipelines reducing deployment time by 70% using Docker and Kubernetes</li>
                <li>Mentored team of 6 junior developers and conducted technical interviews</li>
                <li>Optimized database queries resulting in 40% improvement in application performance</li>
              </ul>
            </div>

            <div style="margin-bottom:25px;padding:20px;background:#f7fafc;border-radius:8px;border-left:4px solid #68d391;">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
                <h3 style="margin:0;font-size:18px;font-weight:600;color:#2d3748;">Full Stack Developer</h3>
                <span style="background:#68d391;color:#ffffff;padding:4px 12px;border-radius:20px;font-size:12px;font-weight:600;">2019 – 2021</span>
              </div>
              <p style="margin:0 0 12px 0;font-size:15px;color:#68d391;font-weight:500;">StartupXYZ, Austin</p>
              <ul style="margin:0;padding-left:20px;font-size:14px;color:#4a5568;">
                <li>Built responsive web applications using React, Redux, and Node.js</li>
                <li>Integrated third-party APIs and payment systems (Stripe, PayPal)</li>
                <li>Collaborated with UX/UI designers to implement pixel-perfect interfaces</li>
              </ul>
            </div>
          </section>

          <section style="margin-bottom:35px;">
            <h2 style="margin:0 0 20px 0;font-size:22px;font-weight:700;color:#2d3748;text-transform:uppercase;letter-spacing:1px;border-left:4px solid #4299e1;padding-left:15px;">Projects</h2>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
              <div style="padding:20px;background:#f7fafc;border-radius:8px;border-top:3px solid #9f7aea;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
                  <h3 style="margin:0;font-size:16px;font-weight:600;color:#2d3748;">E-Commerce Platform</h3>
                  <a href="https://demo-ecommerce.com" style="color:#9f7aea;text-decoration:none;font-size:12px;">Live Demo</a>
                </div>
                <p style="margin:0;font-size:13px;color:#4a5568;">
                  Full-featured e-commerce platform with React frontend, Node.js backend, and MongoDB database. Includes payment processing, inventory management, and admin dashboard.
                </p>
              </div>
              <div style="padding:20px;background:#f7fafc;border-radius:8px;border-top:3px solid #ed8936;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
                  <h3 style="margin:0;font-size:16px;font-weight:600;color:#2d3748;">Task Management App</h3>
                  <a href="https://github.com/alexchen/taskapp" style="color:#ed8936;text-decoration:none;font-size:12px;">GitHub</a>
                </div>
                <p style="margin:0;font-size:13px;color:#4a5568;">
                  Real-time collaborative task management application built with React, Socket.io, and Express. Features include drag-and-drop interface and team collaboration tools.
                </p>
              </div>
            </div>
          </section>
        </div>

        <!-- Right Column -->
        <div>
          <section style="margin-bottom:30px;">
            <h2 style="margin:0 0 15px 0;font-size:18px;font-weight:700;color:#2d3748;text-transform:uppercase;letter-spacing:1px;">Technical Skills</h2>
            <div style="background:#f7fafc;padding:20px;border-radius:8px;">
              <div style="margin-bottom:15px;">
                <h4 style="margin:0 0 8px 0;font-size:14px;font-weight:600;color:#4299e1;">Frontend</h4>
                <div style="display:flex;flex-wrap:wrap;gap:6px;">
                  <span style="background:#4299e1;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">React</span>
                  <span style="background:#4299e1;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">Vue.js</span>
                  <span style="background:#4299e1;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">TypeScript</span>
                  <span style="background:#4299e1;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">Tailwind CSS</span>
                </div>
              </div>
              <div style="margin-bottom:15px;">
                <h4 style="margin:0 0 8px 0;font-size:14px;font-weight:600;color:#68d391;">Backend</h4>
                <div style="display:flex;flex-wrap:wrap;gap:6px;">
                  <span style="background:#68d391;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">Node.js</span>
                  <span style="background:#68d391;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">Python</span>
                  <span style="background:#68d391;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">Express</span>
                  <span style="background:#68d391;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">Django</span>
                </div>
              </div>
              <div style="margin-bottom:15px;">
                <h4 style="margin:0 0 8px 0;font-size:14px;font-weight:600;color:#9f7aea;">Database</h4>
                <div style="display:flex;flex-wrap:wrap;gap:6px;">
                  <span style="background:#9f7aea;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">MongoDB</span>
                  <span style="background:#9f7aea;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">PostgreSQL</span>
                  <span style="background:#9f7aea;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">Redis</span>
                </div>
              </div>
              <div>
                <h4 style="margin:0 0 8px 0;font-size:14px;font-weight:600;color:#ed8936;">DevOps</h4>
                <div style="display:flex;flex-wrap:wrap;gap:6px;">
                  <span style="background:#ed8936;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">Docker</span>
                  <span style="background:#ed8936;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">AWS</span>
                  <span style="background:#ed8936;color:#ffffff;padding:4px 8px;border-radius:12px;font-size:11px;">Kubernetes</span>
                </div>
              </div>
            </div>
          </section>

          <section style="margin-bottom:30px;">
            <h2 style="margin:0 0 15px 0;font-size:18px;font-weight:700;color:#2d3748;text-transform:uppercase;letter-spacing:1px;">Education</h2>
            <div style="background:#f7fafc;padding:20px;border-radius:8px;">
              <div style="margin-bottom:15px;">
                <h4 style="margin:0;font-size:15px;font-weight:600;color:#2d3748;">Master of Science in Computer Science</h4>
                <p style="margin:2px 0;font-size:13px;color:#4299e1;">Stanford University</p>
                <p style="margin:2px 0;font-size:12px;color:#718096;">2017 – 2019 | GPA: 3.9/4.0</p>
              </div>
              <div>
                <h4 style="margin:0;font-size:15px;font-weight:600;color:#2d3748;">Bachelor of Science in Software Engineering</h4>
                <p style="margin:2px 0;font-size:13px;color:#4299e1;">UC Berkeley</p>
                <p style="margin:2px 0;font-size:12px;color:#718096;">2013 – 2017 | GPA: 3.8/4.0</p>
              </div>
            </div>
          </section>

          <section style="margin-bottom:30px;">
            <h2 style="margin:0 0 15px 0;font-size:18px;font-weight:700;color:#2d3748;text-transform:uppercase;letter-spacing:1px;">Publications</h2>
            <div style="background:#f7fafc;padding:20px;border-radius:8px;font-size:13px;color:#4a5568;">
              <p style="margin:0 0 10px 0;">"Microservices Architecture Patterns" - <em>IEEE Software</em>, 2024</p>
              <p style="margin:0;">"Optimizing React Performance at Scale" - <em>ACM Computing Surveys</em>, 2023</p>
            </div>
          </section>

          <section>
            <h2 style="margin:0 0 15px 0;font-size:18px;font-weight:700;color:#2d3748;text-transform:uppercase;letter-spacing:1px;">Skills</h2>
            <div style="background:#f7fafc;padding:20px;border-radius:8px;font-size:13px;">
              <div style="display:grid;grid-template-columns:auto 1fr;gap:8px;">
                <div style="font-weight:600;color:#2d3748;">Languages</div>
                <div style="color:#4a5568;">JavaScript, TypeScript, Python, Java, Go</div>
                <div style="font-weight:600;color:#2d3748;">Methodologies</div>
                <div style="color:#4a5568;">Agile, Scrum, TDD, CI/CD, Microservices</div>
              </div>
            </div>
          </section>
        </div>
      </div>

      <div style="text-align:center;margin-top:40px;font-size:12px;color:#a0aec0;border-top:1px solid #e2e8f0;padding-top:20px;">
        Last updated: 19 Aug 2025
      </div>
    </div>
  </main>
</body>
</html>"""
    },
    {
        "id": "t05-sideband",
        "name": "Professional Sideband",
        "role_category": "non-technical",
        "has_image_slot": True,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Maria Rodriguez</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#fafafa;color:#333333;font-family:'Roboto',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.5;">
  <main style="max-width:210mm;margin:15px auto;background:#ffffff;box-shadow:0 0 30px rgba(0,0,0,.15);">
    <!-- Top accent band -->
    <div style="height:8px;background:linear-gradient(90deg,#667eea 0%,#764ba2 100%);"></div>
    
    <div style="display:flex;">
      <!-- Left sidebar -->
      <aside style="width:30%;background:#f8f9fa;padding:30px 25px;border-right:1px solid #e9ecef;">
        <div style="text-align:center;margin-bottom:30px;">
          <img src="{{PHOTO_URL}}" alt="Profile" style="width:140px;height:140px;border-radius:50%;border:5px solid #667eea;margin-bottom:20px;" />
          <h1 style="margin:0 0 5px 0;font-size:22px;font-weight:700;color:#2c3e50;">Maria Rodriguez</h1>
          <p style="margin:0;font-size:14px;color:#667eea;font-weight:500;text-transform:uppercase;letter-spacing:1px;">HR Director</p>
        </div>

        <section style="margin-bottom:25px;">
          <h3 style="margin:0 0 15px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #667eea;padding-bottom:5px;">Contact Info</h3>
          <div style="font-size:13px;line-height:1.8;">
            <div style="margin-bottom:8px;display:flex;align-items:center;">
              <span style="width:20px;color:#667eea;">📧</span>
              <a href="mailto:maria.rodriguez@email.com" style="color:#333333;text-decoration:none;">maria.rodriguez@email.com</a>
            </div>
            <div style="margin-bottom:8px;display:flex;align-items:center;">
              <span style="width:20px;color:#667eea;">📱</span>
              <a href="tel:+15551234567" style="color:#333333;text-decoration:none;">+1 (555) 123-4567</a>
            </div>
            <div style="margin-bottom:8px;display:flex;align-items:center;">
              <span style="width:20px;color:#667eea;">🔗</span>
              <a href="https://linkedin.com/in/mariarodriguez" style="color:#333333;text-decoration:none;">linkedin.com/in/mariarodriguez</a>
            </div>
            <div style="display:flex;align-items:center;">
              <span style="width:20px;color:#667eea;">📍</span>
              <span>Miami, FL</span>
            </div>
          </div>
        </section>

        <section style="margin-bottom:25px;">
          <h3 style="margin:0 0 15px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #667eea;padding-bottom:5px;">Core Skills</h3>
          <div style="font-size:13px;">
            <div style="margin-bottom:10px;">
              <div style="display:flex;justify-content:space-between;margin-bottom:3px;">
                <span style="font-weight:500;">Talent Acquisition</span>
                <span style="color:#667eea;">95%</span>
              </div>
              <div style="background:#e9ecef;height:4px;border-radius:2px;">
                <div style="background:#667eea;height:4px;width:95%;border-radius:2px;"></div>
              </div>
            </div>
            <div style="margin-bottom:10px;">
              <div style="display:flex;justify-content:space-between;margin-bottom:3px;">
                <span style="font-weight:500;">Employee Relations</span>
                <span style="color:#667eea;">90%</span>
              </div>
              <div style="background:#e9ecef;height:4px;border-radius:2px;">
                <div style="background:#667eea;height:4px;width:90%;border-radius:2px;"></div>
              </div>
            </div>
            <div style="margin-bottom:10px;">
              <div style="display:flex;justify-content:space-between;margin-bottom:3px;">
                <span style="font-weight:500;">Performance Management</span>
                <span style="color:#667eea;">88%</span>
              </div>
              <div style="background:#e9ecef;height:4px;border-radius:2px;">
                <div style="background:#667eea;height:4px;width:88%;border-radius:2px;"></div>
              </div>
            </div>
            <div style="margin-bottom:10px;">
              <div style="display:flex;justify-content:space-between;margin-bottom:3px;">
                <span style="font-weight:500;">Compensation & Benefits</span>
                <span style="color:#667eea;">85%</span>
              </div>
              <div style="background:#e9ecef;height:4px;border-radius:2px;">
                <div style="background:#667eea;height:4px;width:85%;border-radius:2px;"></div>
              </div>
            </div>
          </div>
        </section>

        <section style="margin-bottom:25px;">
          <h3 style="margin:0 0 15px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #667eea;padding-bottom:5px;">Certifications</h3>
          <div style="font-size:12px;line-height:1.6;">
            <div style="margin-bottom:8px;">
              <div style="font-weight:600;color:#2c3e50;">SHRM-SCP</div>
              <div style="color:#6c757d;">Society for Human Resource Management</div>
            </div>
            <div style="margin-bottom:8px;">
              <div style="font-weight:600;color:#2c3e50;">PHR Certification</div>
              <div style="color:#6c757d;">HR Certification Institute</div>
            </div>
            <div>
              <div style="font-weight:600;color:#2c3e50;">Six Sigma Green Belt</div>
              <div style="color:#6c757d;">American Society for Quality</div>
            </div>
          </div>
        </section>

        <section>
          <h3 style="margin:0 0 15px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #667eea;padding-bottom:5px;">Languages</h3>
          <div style="font-size:13px;line-height:1.8;">
            <div><strong>English:</strong> Native</div>
            <div><strong>Spanish:</strong> Native</div>
            <div><strong>Portuguese:</strong> Conversational</div>
          </div>
        </section>
      </aside>

      <!-- Main content -->
      <section style="width:70%;padding:30px 35px;">
        <section style="margin-bottom:30px;">
          <h2 style="margin:0 0 15px 0;font-size:24px;font-weight:700;color:#2c3e50;border-bottom:3px solid #667eea;padding-bottom:8px;">Summary</h2>
          <p style="margin:0;font-size:15px;text-align:justify;color:#495057;">
            Strategic HR Director with 10+ years of experience leading human resources initiatives for Fortune 500 companies. Proven expertise in talent acquisition, employee engagement, performance management, and organizational development. Successfully managed HR operations for teams of 500+ employees while driving cultural transformation and improving retention rates by 35%.
          </p>
        </section>

        <section style="margin-bottom:30px;">
          <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:700;color:#2c3e50;border-bottom:3px solid #667eea;padding-bottom:8px;">Work Experience</h2>
          
          <div style="margin-bottom:25px;position:relative;padding-left:20px;">
            <div style="position:absolute;left:0;top:5px;width:10px;height:10px;background:#667eea;border-radius:50%;"></div>
            <div style="position:absolute;left:4px;top:15px;width:2px;height:calc(100% - 10px);background:#e9ecef;"></div>
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
              <h3 style="margin:0;font-size:18px;font-weight:600;color:#2c3e50;">HR Director</h3>
              <span style="background:#667eea;color:#ffffff;padding:4px 12px;border-radius:15px;font-size:12px;font-weight:500;">2019 – Present</span>
            </div>
            <p style="margin:0 0 10px 0;font-size:15px;color:#667eea;font-weight:500;">GlobalTech Corporation, Miami</p>
            <ul style="margin:0;padding-left:20px;font-size:14px;color:#495057;">
              <li>Lead comprehensive HR strategy for 500+ employee organization across multiple locations</li>
              <li>Implemented new performance management system resulting in 25% improvement in employee satisfaction</li>
              <li>Reduced employee turnover by 35% through enhanced onboarding and retention programs</li>
              <li>Managed annual HR budget of $2.8M and negotiated vendor contracts saving 20% in costs</li>
              <li>Spearheaded diversity and inclusion initiatives increasing minority representation by 40%</li>
            </ul>
          </div>

          <div style="margin-bottom:25px;position:relative;padding-left:20px;">
            <div style="position:absolute;left:0;top:5px;width:10px;height:10px;background:#764ba2;border-radius:50%;"></div>
            <div style="position:absolute;left:4px;top:15px;width:2px;height:calc(100% - 10px);background:#e9ecef;"></div>
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
              <h3 style="margin:0;font-size:18px;font-weight:600;color:#2c3e50;">Senior HR Manager</h3>
              <span style="background:#764ba2;color:#ffffff;padding:4px 12px;border-radius:15px;font-size:12px;font-weight:500;">2016 – 2019</span>
            </div>
            <p style="margin:0 0 10px 0;font-size:15px;color:#764ba2;font-weight:500;">TechStart Solutions, Orlando</p>
            <ul style="margin:0;padding-left:20px;font-size:14px;color:#495057;">
              <li>Managed full-cycle recruitment process for technical and non-technical positions</li>
              <li>Developed employee handbook and HR policies ensuring legal compliance</li>
              <li>Conducted training programs on workplace harassment and diversity awareness</li>
              <li>Collaborated with leadership team on organizational restructuring initiatives</li>
            </ul>
          </div>

          <div style="position:relative;padding-left:20px;">
            <div style="position:absolute;left:0;top:5px;width:10px;height:10px;background:#6c757d;border-radius:50%;"></div>
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
              <h3 style="margin:0;font-size:18px;font-weight:600;color:#2c3e50;">HR Generalist</h3>
              <span style="background:#6c757d;color:#ffffff;padding:4px 12px;border-radius:15px;font-size:12px;font-weight:500;">2014 – 2016</span>
            </div>
            <p style="margin:0 0 10px 0;font-size:15px;color:#6c757d;font-weight:500;">Business Dynamics Inc., Tampa</p>
            <ul style="margin:0;padding-left:20px;font-size:14px;color:#495057;">
              <li>Supported all HR functions including recruitment, onboarding, and employee relations</li>
              <li>Maintained HRIS system and generated monthly HR analytics reports</li>
              <li>Assisted with benefits administration and open enrollment processes</li>
            </ul>
          </div>
        </section>

        <section style="margin-bottom:30px;">
          <h2 style="margin:0 0 15px 0;font-size:24px;font-weight:700;color:#2c3e50;border-bottom:3px solid #667eea;padding-bottom:8px;">Projects</h2>
          <div style="margin-bottom:15px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px;">
              <h3 style="margin:0;font-size:16px;font-weight:600;color:#2c3e50;">Digital HR Transformation Initiative</h3>
              <a href="https://hr-transformation-case-study.com" style="color:#667eea;text-decoration:none;font-size:13px;">Case Study</a>
            </div>
            <p style="margin:0;font-size:14px;color:#495057;">
              Led company-wide digital transformation of HR processes, implementing cloud-based HRIS system and automated workflows. Project resulted in 50% reduction in administrative tasks and improved employee self-service capabilities.
            </p>
          </div>
        </section>

        <section style="margin-bottom:30px;">
          <h2 style="margin:0 0 15px 0;font-size:24px;font-weight:700;color:#2c3e50;border-bottom:3px solid #667eea;padding-bottom:8px;">Education</h2>
          <div style="display:grid;grid-template-columns:120px 1fr;gap:15px;font-size:14px;">
            <div style="color:#6c757d;font-weight:500;">2012 – 2014</div>
            <div>Master of Business Administration (MBA) at <strong>University of Miami</strong> <span style="float:right;color:#6c757d;">(GPA: 3.8/4.0)</span></div>
            <div style="color:#6c757d;font-weight:500;">2008 – 2012</div>
            <div>Bachelor of Science in Human Resources at <strong>Florida International University</strong> <span style="float:right;color:#6c757d;">(GPA: 3.7/4.0)</span></div>
          </div>
        </section>

        <section style="margin-bottom:30px;">
          <h2 style="margin:0 0 15px 0;font-size:24px;font-weight:700;color:#2c3e50;border-bottom:3px solid #667eea;padding-bottom:8px;">Publications</h2>
          <div style="font-size:14px;color:#495057;">
            <p style="margin:0 0 8px 0;">"The Future of Remote Work: HR Strategies for Distributed Teams" - <em>HR Management Today</em>, April 2024</p>
            <p style="margin:0;">"Building Inclusive Workplaces: A Practical Guide" - <em>Diversity & Inclusion Quarterly</em>, January 2024</p>
          </div>
        </section>

        <section>
          <h2 style="margin:0 0 15px 0;font-size:24px;font-weight:700;color:#2c3e50;border-bottom:3px solid #667eea;padding-bottom:8px;">Skills</h2>
          <div style="display:grid;grid-template-columns:140px 1fr;gap:10px;font-size:14px;">
            <div style="font-weight:600;color:#2c3e50;">HR Systems</div>
            <div style="color:#495057;">Workday, BambooHR, ADP, SuccessFactors, Greenhouse</div>
            <div style="font-weight:600;color:#2c3e50;">Specializations</div>
            <div style="color:#495057;">Talent Acquisition, Employee Relations, Performance Management, Compensation Analysis, HRIS Administration</div>
          </div>
        </section>

        <div style="text-align:center;margin-top:35px;font-size:12px;color:#adb5bd;border-top:1px solid #e9ecef;padding-top:20px;">
          Last updated: 19 Aug 2025
        </div>
      </section>
    </div>
  </main>
</body>
</html>"""
    },
    {
        "id": "t06-compact",
        "name": "Compact Professional",
        "role_category": "technical",
        "has_image_slot": False,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – David Kim</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#ffffff;color:#2c3e50;font-family:'Source Sans Pro',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.4;">
  <main style="max-width:210mm;margin:10px auto;background:#ffffff;border:1px solid #bdc3c7;">
    <div style="padding:25mm 15mm 20mm 15mm;">
      <!-- Compact Header -->
      <header style="text-align:center;margin-bottom:20px;padding-bottom:15px;border-bottom:2px solid #3498db;">
        <h1 style="margin:0 0 5px 0;font-size:28px;font-weight:700;color:#2c3e50;letter-spacing:-0.5px;">DAVID KIM</h1>
        <p style="margin:0 0 10px 0;font-size:16px;color:#3498db;font-weight:600;">DevOps Engineer</p>
        <div style="font-size:12px;color:#7f8c8d;">
          <span><a href="mailto:david.kim@email.com" style="color:#3498db;text-decoration:none;">david.kim@email.com</a></span> • 
          <span><a href="tel:+15551234567" style="color:#3498db;text-decoration:none;">+1 (555) 123-4567</a></span> • 
          <span><a href="https://github.com/davidkim" style="color:#3498db;text-decoration:none;">github.com/davidkim</a></span> • 
          <span><a href="https://linkedin.com/in/davidkim" style="color:#3498db;text-decoration:none;">linkedin.com/in/davidkim</a></span>
        </div>
      </header>

      <!-- Compact Summary -->
      <section style="margin-bottom:18px;">
        <h2 style="margin:0 0 8px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;background:#ecf0f1;padding:6px 10px;">Summary</h2>
        <p style="margin:0;font-size:13px;text-align:justify;">
          Experienced DevOps Engineer with 6+ years specializing in cloud infrastructure, CI/CD pipelines, and container orchestration. Expert in AWS, Kubernetes, Docker, and Infrastructure as Code. Proven track record of reducing deployment times by 80% and improving system reliability through automation and monitoring solutions.
        </p>
      </section>

      <!-- Compact Work Experience -->
      <section style="margin-bottom:18px;">
        <h2 style="margin:0 0 8px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;background:#ecf0f1;padding:6px 10px;">Work Experience</h2>
        
        <div style="margin-bottom:12px;">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:3px;">
            <h3 style="margin:0;font-size:14px;font-weight:600;color:#2c3e50;">Senior DevOps Engineer</h3>
            <span style="font-size:11px;color:#7f8c8d;font-weight:500;">2021 – Present</span>
          </div>
          <p style="margin:0 0 6px 0;font-size:12px;color:#3498db;font-weight:500;">CloudTech Systems, Seattle</p>
          <ul style="margin:0;padding-left:15px;font-size:12px;list-style-type:disc;">
            <li>Architected and maintained Kubernetes clusters serving 50+ microservices with 99.9% uptime</li>
            <li>Implemented GitOps workflows using ArgoCD, reducing deployment errors by 90%</li>
            <li>Automated infrastructure provisioning with Terraform, managing 200+ AWS resources</li>
            <li>Built comprehensive monitoring stack with Prometheus, Grafana, and ELK reducing MTTR by 60%</li>
          </ul>
        </div>

        <div style="margin-bottom:12px;">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:3px;">
            <h3 style="margin:0;font-size:14px;font-weight:600;color:#2c3e50;">DevOps Engineer</h3>
            <span style="font-size:11px;color:#7f8c8d;font-weight:500;">2019 – 2021</span>
          </div>
          <p style="margin:0 0 6px 0;font-size:12px;color:#3498db;font-weight:500;">StartupFlow, Portland</p>
          <ul style="margin:0;padding-left:15px;font-size:12px;list-style-type:disc;">
            <li>Migrated legacy applications to containerized architecture using Docker and Docker Compose</li>
            <li>Set up CI/CD pipelines with Jenkins and GitLab CI, enabling daily deployments</li>
            <li>Managed AWS infrastructure including EC2, RDS, S3, and CloudFormation templates</li>
          </ul>
        </div>

        <div style="margin-bottom:12px;">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:3px;">
            <h3 style="margin:0;font-size:14px;font-weight:600;color:#2c3e50;">Systems Administrator</h3>
            <span style="font-size:11px;color:#7f8c8d;font-weight:500;">2018 – 2019</span>
          </div>
          <p style="margin:0 0 6px 0;font-size:12px;color:#3498db;font-weight:500;">TechCorp Solutions, San Francisco</p>
          <ul style="margin:0;padding-left:15px;font-size:12px;list-style-type:disc;">
            <li>Maintained Linux servers and automated routine tasks using Bash and Python scripts</li>
            <li>Implemented backup strategies and disaster recovery procedures</li>
          </ul>
        </div>
      </section>

      <!-- Compact Projects -->
      <section style="margin-bottom:18px;">
        <h2 style="margin:0 0 8px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;background:#ecf0f1;padding:6px 10px;">Projects</h2>
        <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:3px;">
          <h3 style="margin:0;font-size:13px;font-weight:600;color:#2c3e50;">Multi-Cloud Infrastructure Platform</h3>
          <a href="https://github.com/davidkim/multicloud" style="color:#3498db;text-decoration:none;font-size:11px;">GitHub</a>
        </div>
        <p style="margin:0;font-size:12px;">
          Built comprehensive infrastructure platform supporting AWS, Azure, and GCP using Terraform modules. Includes automated provisioning, monitoring, and cost optimization features. Reduced infrastructure setup time from weeks to hours.
        </p>
      </section>

      <!-- Compact Skills in Grid -->
      <section style="margin-bottom:18px;">
        <h2 style="margin:0 0 8px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;background:#ecf0f1;padding:6px 10px;">Skills</h2>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;font-size:12px;">
          <div>
            <h4 style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#3498db;">Cloud Platforms</h4>
            <div>AWS, Azure, GCP</div>
          </div>
          <div>
            <h4 style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#3498db;">Containers</h4>
            <div>Docker, Kubernetes, Helm</div>
          </div>
          <div>
            <h4 style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#3498db;">CI/CD</h4>
            <div>Jenkins, GitLab CI, ArgoCD</div>
          </div>
          <div>
            <h4 style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#3498db;">IaC</h4>
            <div>Terraform, Ansible, CloudFormation</div>
          </div>
          <div>
            <h4 style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#3498db;">Monitoring</h4>
            <div>Prometheus, Grafana, ELK Stack</div>
          </div>
          <div>
            <h4 style="margin:0 0 4px 0;font-size:12px;font-weight:600;color:#3498db;">Languages</h4>
            <div>Python, Bash, Go, YAML</div>
          </div>
        </div>
      </section>

      <!-- Compact Education -->
      <section style="margin-bottom:18px;">
        <h2 style="margin:0 0 8px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;background:#ecf0f1;padding:6px 10px;">Education</h2>
        <div style="display:grid;grid-template-columns:100px 1fr;gap:8px;font-size:12px;">
          <div style="color:#7f8c8d;font-weight:500;">2014 – 2018</div>
          <div>Bachelor of Science in Computer Science at <strong>University of Washington</strong> <span style="float:right;color:#7f8c8d;">(GPA: 3.6/4.0)</span></div>
        </div>
      </section>

      <!-- Compact Publications -->
      <section style="margin-bottom:18px;">
        <h2 style="margin:0 0 8px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;background:#ecf0f1;padding:6px 10px;">Publications</h2>
        <div style="font-size:12px;">
          <p style="margin:0 0 4px 0;">"Kubernetes Security Best Practices" - <em>DevOps Weekly</em>, March 2024</p>
          <p style="margin:0;">"Infrastructure as Code: Lessons from the Trenches" - <em>Cloud Computing Journal</em>, November 2023</p>
        </div>
      </section>

      <!-- Compact Additional Skills -->
      <section>
        <h2 style="margin:0 0 8px 0;font-size:14px;font-weight:700;color:#2c3e50;text-transform:uppercase;letter-spacing:1px;background:#ecf0f1;padding:6px 10px;">Skills</h2>
        <div style="display:grid;grid-template-columns:120px 1fr;gap:6px;font-size:12px;">
          <div style="font-weight:600;color:#2c3e50;">Certifications</div>
          <div>AWS Solutions Architect, CKA (Certified Kubernetes Administrator), Terraform Associate</div>
          <div style="font-weight:600;color:#2c3e50;">Methodologies</div>
          <div>Agile, DevOps, GitOps, Infrastructure as Code, Site Reliability Engineering</div>
        </div>
      </section>

      <!-- Compact Footer -->
      <div style="text-align:center;margin-top:20px;font-size:10px;color:#95a5a6;border-top:1px solid #bdc3c7;padding-top:10px;">
        Last updated: 19 Aug 2025
      </div>
    </div>
  </main>
</body>
</html>"""
    },
    {
        "id": "t07-creative",
        "name": "Creative Portfolio",
        "role_category": "non-technical",
        "has_image_slot": True,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Emma Thompson</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#fef7f0;color:#2d3748;font-family:'Playfair Display',Georgia,serif;line-height:1.6;">
  <main style="max-width:210mm;margin:15px auto;background:#ffffff;box-shadow:0 20px 60px rgba(0,0,0,.1);">
    <!-- Creative Header with Diagonal -->
    <div style="position:relative;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);height:120px;overflow:hidden;">
      <div style="position:absolute;bottom:-50px;left:-50px;width:200px;height:200px;background:rgba(255,255,255,0.1);border-radius:50%;"></div>
      <div style="position:absolute;top:-30px;right:-30px;width:150px;height:150px;background:rgba(255,255,255,0.1);border-radius:50%;"></div>
      <div style="position:relative;z-index:2;padding:30px 40px;color:#ffffff;">
        <h1 style="margin:0 0 5px 0;font-size:32px;font-weight:400;letter-spacing:2px;">Emma Thompson</h1>
        <p style="margin:0;font-size:16px;opacity:0.9;font-style:italic;">Creative Director & Brand Strategist</p>
      </div>
    </div>

    <div style="padding:40px;">
      <!-- Profile Section with Photo -->
      <section style="display:flex;gap:30px;margin-bottom:35px;align-items:flex-start;">
        <div style="flex-shrink:0;">
          <img src="{{PHOTO_URL}}" alt="Emma Thompson" style="width:120px;height:120px;border-radius:15px;border:4px solid #667eea;box-shadow:0 10px 30px rgba(102,126,234,0.3);" />
        </div>
        <div style="flex:1;">
          <h2 style="margin:0 0 15px 0;font-size:24px;font-weight:600;color:#667eea;border-bottom:2px solid #667eea;padding-bottom:8px;display:inline-block;">Summary</h2>
          <p style="margin:0;font-size:15px;text-align:justify;color:#4a5568;">
            Award-winning Creative Director with 8+ years of experience crafting compelling brand narratives and visual identities for Fortune 500 companies. Expertise in leading creative teams, developing integrated marketing campaigns, and driving brand growth through innovative design solutions. Passionate about creating meaningful connections between brands and their audiences.
          </p>
        </div>
      </section>

      <!-- Contact Info in Creative Layout -->
      <section style="background:#f7fafc;padding:20px;border-radius:15px;margin-bottom:35px;border-left:5px solid #667eea;">
        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:15px;font-size:14px;">
          <div style="display:flex;align-items:center;gap:10px;">
            <span style="background:#667eea;color:#ffffff;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;">✉</span>
            <a href="mailto:emma.thompson@email.com" style="color:#4a5568;text-decoration:none;">emma.thompson@email.com</a>
          </div>
          <div style="display:flex;align-items:center;gap:10px;">
            <span style="background:#667eea;color:#ffffff;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;">📱</span>
            <a href="tel:+15551234567" style="color:#4a5568;text-decoration:none;">+1 (555) 123-4567</a>
          </div>
          <div style="display:flex;align-items:center;gap:10px;">
            <span style="background:#667eea;color:#ffffff;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;">🔗</span>
            <a href="https://emmathompson.design" style="color:#4a5568;text-decoration:none;">emmathompson.design</a>
          </div>
          <div style="display:flex;align-items:center;gap:10px;">
            <span style="background:#667eea;color:#ffffff;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;">📍</span>
            <span style="color:#4a5568;">Los Angeles, CA</span>
          </div>
        </div>
      </section>

      <!-- Experience with Creative Timeline -->
      <section style="margin-bottom:35px;">
        <h2 style="margin:0 0 25px 0;font-size:28px;font-weight:600;color:#667eea;text-align:center;position:relative;">
          Work Experience
          <div style="position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);width:80px;height:3px;background:linear-gradient(90deg,#667eea,#764ba2);border-radius:2px;"></div>
        </h2>
        
        <div style="position:relative;padding-left:30px;">
          <!-- Timeline line -->
          <div style="position:absolute;left:15px;top:0;bottom:0;width:2px;background:linear-gradient(180deg,#667eea,#764ba2);"></div>
          
          <div style="margin-bottom:30px;position:relative;">
            <div style="position:absolute;left:-22px;top:10px;width:14px;height:14px;background:#667eea;border-radius:50%;border:3px solid #ffffff;box-shadow:0 0 0 2px #667eea;"></div>
            <div style="background:#ffffff;padding:20px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.1);border:1px solid #e2e8f0;">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
                <h3 style="margin:0;font-size:20px;font-weight:600;color:#2d3748;">Creative Director</h3>
                <span style="background:linear-gradient(135deg,#667eea,#764ba2);color:#ffffff;padding:6px 15px;border-radius:20px;font-size:12px;font-weight:600;">2020 – Present</span>
              </div>
              <p style="margin:0 0 12px 0;font-size:16px;color:#667eea;font-weight:500;font-style:italic;">BrandCraft Agency, Los Angeles</p>
              <ul style="margin:0;padding-left:20px;font-size:14px;color:#4a5568;">
                <li>Lead creative vision for 15+ major brand campaigns with budgets exceeding $5M</li>
                <li>Managed multidisciplinary team of 12 designers, copywriters, and strategists</li>
                <li>Increased client retention rate by 40% through innovative creative solutions</li>
                <li>Won 3 Cannes Lions and 5 D&AD awards for outstanding creative work</li>
              </ul>
            </div>
          </div>

          <div style="margin-bottom:30px;position:relative;">
            <div style="position:absolute;left:-22px;top:10px;width:14px;height:14px;background:#764ba2;border-radius:50%;border:3px solid #ffffff;box-shadow:0 0 0 2px #764ba2;"></div>
            <div style="background:#ffffff;padding:20px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.1);border:1px solid #e2e8f0;">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
                <h3 style="margin:0;font-size:20px;font-weight:600;color:#2d3748;">Senior Art Director</h3>
                <span style="background:linear-gradient(135deg,#764ba2,#667eea);color:#ffffff;padding:6px 15px;border-radius:20px;font-size:12px;font-weight:600;">2017 – 2020</span>
              </div>
              <p style="margin:0 0 12px 0;font-size:16px;color:#764ba2;font-weight:500;font-style:italic;">Creative Minds Studio, San Francisco</p>
              <ul style="margin:0;padding-left:20px;font-size:14px;color:#4a5568;">
                <li>Developed visual concepts for digital and print campaigns across various industries</li>
                <li>Collaborated with clients to translate brand objectives into compelling creative executions</li>
                <li>Mentored junior designers and established creative workflow processes</li>
              </ul>
            </div>
          </div>

          <div style="position:relative;">
            <div style="position:absolute;left:-22px;top:10px;width:14px;height:14px;background:#a78bfa;border-radius:50%;border:3px solid #ffffff;box-shadow:0 0 0 2px #a78bfa;"></div>
            <div style="background:#ffffff;padding:20px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.1);border:1px solid #e2e8f0;">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
                <h3 style="margin:0;font-size:20px;font-weight:600;color:#2d3748;">Graphic Designer</h3>
                <span style="background:#a78bfa;color:#ffffff;padding:6px 15px;border-radius:20px;font-size:12px;font-weight:600;">2016 – 2017</span>
              </div>
              <p style="margin:0 0 12px 0;font-size:16px;color:#a78bfa;font-weight:500;font-style:italic;">Design Collective, Portland</p>
              <ul style="margin:0;padding-left:20px;font-size:14px;color:#4a5568;">
                <li>Created brand identities, marketing materials, and digital assets for small businesses</li>
                <li>Worked directly with clients to understand their vision and deliver creative solutions</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- Projects Showcase -->
      <section style="margin-bottom:35px;">
        <h2 style="margin:0 0 25px 0;font-size:28px;font-weight:600;color:#667eea;text-align:center;position:relative;">
          Featured Projects
          <div style="position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);width:80px;height:3px;background:linear-gradient(90deg,#667eea,#764ba2);border-radius:2px;"></div>
        </h2>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;">
          <div style="background:#ffffff;padding:20px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.1);border:1px solid #e2e8f0;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
              <h3 style="margin:0;font-size:18px;font-weight:600;color:#2d3748;">Global Rebranding Campaign</h3>
              <a href="https://portfolio.emmathompson.design/rebrand" style="color:#667eea;text-decoration:none;font-size:12px;">View Project</a>
            </div>
            <p style="margin:0;font-size:14px;color:#4a5568;">
              Complete brand overhaul for international tech company including logo design, brand guidelines, and marketing collateral. Project resulted in 60% increase in brand recognition.
            </p>
          </div>
          <div style="background:#ffffff;padding:20px;border-radius:15px;box-shadow:0 5px 20px rgba(0,0,0,0.1);border:1px solid #e2e8f0;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
              <h3 style="margin:0;font-size:18px;font-weight:600;color:#2d3748;">Award-Winning Ad Campaign</h3>
              <a href="https://portfolio.emmathompson.design/campaign" style="color:#667eea;text-decoration:none;font-size:12px;">Case Study</a>
            </div>
            <p style="margin:0;font-size:14px;color:#4a5568;">
              Integrated marketing campaign for luxury fashion brand that won Gold at Cannes Lions. Campaign generated 200M+ impressions and 25% increase in sales.
            </p>
          </div>
        </div>
      </section>

      <!-- Skills & Education Grid -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:35px;margin-bottom:35px;">
        <section>
          <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:600;color:#667eea;border-bottom:2px solid #667eea;padding-bottom:8px;">Education</h2>
          <div style="background:#f7fafc;padding:20px;border-radius:15px;">
            <div style="margin-bottom:15px;">
              <h4 style="margin:0 0 5px 0;font-size:16px;font-weight:600;color:#2d3748;">Master of Fine Arts in Graphic Design</h4>
              <p style="margin:0 0 3px 0;font-size:14px;color:#667eea;">Art Center College of Design</p>
              <p style="margin:0;font-size:12px;color:#718096;">2014 – 2016 | GPA: 3.9/4.0</p>
            </div>
            <div>
              <h4 style="margin:0 0 5px 0;font-size:16px;font-weight:600;color:#2d3748;">Bachelor of Arts in Visual Communications</h4>
              <p style="margin:0 0 3px 0;font-size:14px;color:#667eea;">UCLA</p>
              <p style="margin:0;font-size:12px;color:#718096;">2010 – 2014 | GPA: 3.7/4.0</p>
            </div>
          </div>
        </section>

        <section>
          <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:600;color:#667eea;border-bottom:2px solid #667eea;padding-bottom:8px;">Skills</h2>
          <div style="background:#f7fafc;padding:20px;border-radius:15px;">
            <div style="display:grid;grid-template-columns:auto 1fr;gap:10px;font-size:14px;">
              <div style="font-weight:600;color:#2d3748;">Design Tools</div>
              <div style="color:#4a5568;">Adobe Creative Suite, Figma, Sketch, InVision, Principle</div>
              <div style="font-weight:600;color:#2d3748;">Specializations</div>
              <div style="color:#4a5568;">Brand Identity, Art Direction, Campaign Development, Team Leadership</div>
              <div style="font-weight:600;color:#2d3748;">Awards</div>
              <div style="color:#4a5568;">3x Cannes Lions, 5x D&AD, 2x One Show, AIGA Design Award</div>
            </div>
          </div>
        </section>
      </div>

      <!-- Publications -->
      <section style="margin-bottom:35px;">
        <h2 style="margin:0 0 15px 0;font-size:24px;font-weight:600;color:#667eea;border-bottom:2px solid #667eea;padding-bottom:8px;">Publications</h2>
        <div style="background:#f7fafc;padding:20px;border-radius:15px;font-size:14px;color:#4a5568;">
          <p style="margin:0 0 10px 0;">"The Future of Brand Storytelling in Digital Age" - <em>Creative Review</em>, June 2024</p>
          <p style="margin:0;">"Building Authentic Brand Connections" - <em>Design Week</em>, February 2024</p>
        </div>
      </section>

      <!-- Final Skills Section -->
      <section>
        <h2 style="margin:0 0 15px 0;font-size:24px;font-weight:600;color:#667eea;border-bottom:2px solid #667eea;padding-bottom:8px;">Skills</h2>
        <div style="display:grid;grid-template-columns:140px 1fr;gap:10px;font-size:14px;">
          <div style="font-weight:600;color:#2d3748;">Creative Strategy</div>
          <div style="color:#4a5568;">Brand Development, Creative Concepting, Art Direction, Visual Storytelling</div>
          <div style="font-weight:600;color:#2d3748;">Leadership</div>
          <div style="color:#4a5568;">Team Management, Creative Mentoring, Client Relations, Project Management</div>
        </div>
      </section>

      <!-- Creative Footer -->
      <div style="text-align:center;margin-top:40px;padding-top:25px;border-top:2px solid #667eea;">
        <div style="font-size:12px;color:#718096;margin-bottom:10px;">Last updated: 19 Aug 2025</div>
        <div style="display:flex;justify-content:center;gap:15px;">
          <div style="width:20px;height:3px;background:#667eea;border-radius:2px;"></div>
          <div style="width:20px;height:3px;background:#764ba2;border-radius:2px;"></div>
          <div style="width:20px;height:3px;background:#a78bfa;border-radius:2px;"></div>
        </div>
      </div>
    </div>
  </main>
</body>
</html>"""
    },
    {
        "id": "t08-executive",
        "name": "Executive Professional",
        "role_category": "non-technical",
        "has_image_slot": True,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Robert Anderson</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#f8f9fa;color:#212529;font-family:'Times New Roman',Times,serif;line-height:1.6;">
  <main style="max-width:210mm;margin:20px auto;background:#ffffff;box-shadow:0 8px 32px rgba(0,0,0,.12);">
    <!-- Executive Header -->
    <header style="background:#1a365d;color:#ffffff;padding:40px 50px;position:relative;">
      <div style="display:flex;align-items:center;gap:40px;">
        <div style="flex-shrink:0;">
          <img src="{{PHOTO_URL}}" alt="Robert Anderson" style="width:140px;height:140px;border-radius:10px;border:4px solid #ffffff;box-shadow:0 8px 24px rgba(0,0,0,0.3);" />
        </div>
        <div style="flex:1;">
          <h1 style="margin:0 0 10px 0;font-size:36px;font-weight:400;letter-spacing:1px;">Robert Anderson</h1>
          <p style="margin:0 0 15px 0;font-size:20px;opacity:0.9;font-style:italic;">Chief Executive Officer</p>
          <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:8px;font-size:14px;opacity:0.9;">
            <div>📧 robert.anderson@email.com</div>
            <div>📱 +1 (555) 123-4567</div>
            <div>🔗 linkedin.com/in/robertanderson</div>
            <div>📍 New York, NY</div>
          </div>
        </div>
      </div>
      <!-- Decorative elements -->
      <div style="position:absolute;top:20px;right:30px;width:80px;height:80px;border:2px solid rgba(255,255,255,0.2);border-radius:50%;"></div>
      <div style="position:absolute;bottom:20px;right:50px;width:40px;height:40px;background:rgba(255,255,255,0.1);border-radius:50%;"></div>
    </header>

    <div style="padding:50px;">
      <!-- Executive Summary -->
      <section style="margin-bottom:40px;">
        <h2 style="margin:0 0 20px 0;font-size:28px;font-weight:400;color:#1a365d;border-bottom:3px solid #1a365d;padding-bottom:10px;text-align:center;">Executive Summary</h2>
        <div style="background:#f8f9fa;padding:30px;border-radius:10px;border-left:5px solid #1a365d;">
          <p style="margin:0;font-size:16px;text-align:justify;line-height:1.8;">
            Visionary CEO with 15+ years of executive leadership experience driving organizational transformation and sustainable growth for Fortune 500 companies. Proven track record of increasing revenue by 300%+, leading successful IPOs, and building high-performance teams across global markets. Expert in strategic planning, mergers & acquisitions, and digital transformation initiatives.
          </p>
        </div>
      </section>

      <!-- Core Competencies -->
      <section style="margin-bottom:40px;">
        <h2 style="margin:0 0 25px 0;font-size:28px;font-weight:400;color:#1a365d;border-bottom:3px solid #1a365d;padding-bottom:10px;text-align:center;">Core Competencies</h2>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:25px;">
          <div style="text-align:center;padding:20px;background:#f8f9fa;border-radius:10px;">
            <div style="font-size:24px;margin-bottom:10px;">📈</div>
            <h4 style="margin:0 0 8px 0;font-size:16px;font-weight:600;color:#1a365d;">Strategic Leadership</h4>
            <p style="margin:0;font-size:13px;color:#6c757d;">Vision Development, Strategic Planning, Change Management</p>
          </div>
          <div style="text-align:center;padding:20px;background:#f8f9fa;border-radius:10px;">
            <div style="font-size:24px;margin-bottom:10px;">💼</div>
            <h4 style="margin:0 0 8px 0;font-size:16px;font-weight:600;color:#1a365d;">Business Development</h4>
            <p style="margin:0;font-size:13px;color:#6c757d;">M&A, Partnership Development, Market Expansion</p>
          </div>
          <div style="text-align:center;padding:20px;background:#f8f9fa;border-radius:10px;">
            <div style="font-size:24px;margin-bottom:10px;">👥</div>
            <h4 style="margin:0 0 8px 0;font-size:16px;font-weight:600;color:#1a365d;">Team Leadership</h4>
            <p style="margin:0;font-size:13px;color:#6c757d;">Executive Coaching, Talent Development, Culture Building</p>
          </div>
        </div>
      </section>

      <!-- Professional Experience -->
      <section style="margin-bottom:40px;">
        <h2 style="margin:0 0 30px 0;font-size:28px;font-weight:400;color:#1a365d;border-bottom:3px solid #1a365d;padding-bottom:10px;text-align:center;">Professional Experience</h2>
        
        <div style="margin-bottom:35px;padding:30px;background:#ffffff;border:1px solid #dee2e6;border-radius:10px;box-shadow:0 4px 16px rgba(0,0,0,0.05);">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:15px;">
            <div>
              <h3 style="margin:0 0 5px 0;font-size:22px;font-weight:600;color:#1a365d;">Chief Executive Officer</h3>
              <p style="margin:0;font-size:18px;color:#6c757d;font-style:italic;">GlobalTech Industries</p>
            </div>
            <div style="text-align:right;">
              <span style="background:#1a365d;color:#ffffff;padding:8px 16px;border-radius:20px;font-size:14px;font-weight:500;">2018 – Present</span>
              <p style="margin:5px 0 0 0;font-size:13px;color:#6c757d;">New York, NY</p>
            </div>
          </div>
          <ul style="margin:0;padding-left:25px;font-size:15px;color:#495057;">
            <li style="margin-bottom:8px;">Led company through successful IPO raising $500M in capital and achieving $2B market valuation</li>
            <li style="margin-bottom:8px;">Increased annual revenue from $150M to $450M through strategic acquisitions and market expansion</li>
            <li style="margin-bottom:8px;">Built and managed executive team of 12 C-level leaders across global operations</li>
            <li style="margin-bottom:8px;">Spearheaded digital transformation initiative resulting in 40% operational efficiency improvement</li>
            <li>Established presence in 15 new international markets, increasing global footprint by 200%</li>
          </ul>
        </div>

        <div style="margin-bottom:35px;padding:30px;background:#ffffff;border:1px solid #dee2e6;border-radius:10px;box-shadow:0 4px 16px rgba(0,0,0,0.05);">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:15px;">
            <div>
              <h3 style="margin:0 0 5px 0;font-size:22px;font-weight:600;color:#1a365d;">Chief Operating Officer</h3>
              <p style="margin:0;font-size:18px;color:#6c757d;font-style:italic;">TechVentures Corp</p>
            </div>
            <div style="text-align:right;">
              <span style="background:#6c757d;color:#ffffff;padding:8px 16px;border-radius:20px;font-size:14px;font-weight:500;">2014 – 2018</span>
              <p style="margin:5px 0 0 0;font-size:13px;color:#6c757d;">San Francisco, CA</p>
            </div>
          </div>
          <ul style="margin:0;padding-left:25px;font-size:15px;color:#495057;">
            <li style="margin-bottom:8px;">Managed day-to-day operations for $200M revenue technology company with 800+ employees</li>
            <li style="margin-bottom:8px;">Implemented lean operational processes reducing costs by $25M annually</li>
            <li style="margin-bottom:8px;">Led successful acquisition of 3 strategic companies totaling $75M in value</li>
            <li>Developed and executed go-to-market strategies for 5 new product lines</li>
          </ul>
        </div>

        <div style="padding:30px;background:#ffffff;border:1px solid #dee2e6;border-radius:10px;box-shadow:0 4px 16px rgba(0,0,0,0.05);">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:15px;">
            <div>
              <h3 style="margin:0 0 5px 0;font-size:22px;font-weight:600;color:#1a365d;">Vice President of Strategy</h3>
              <p style="margin:0;font-size:18px;color:#6c757d;font-style:italic;">Innovation Partners LLC</p>
            </div>
            <div style="text-align:right;">
              <span style="background:#6c757d;color:#ffffff;padding:8px 16px;border-radius:20px;font-size:14px;font-weight:500;">2010 – 2014</span>
              <p style="margin:5px 0 0 0;font-size:13px;color:#6c757d;">Boston, MA</p>
            </div>
          </div>
          <ul style="margin:0;padding-left:25px;font-size:15px;color:#495057;">
            <li style="margin-bottom:8px;">Developed strategic plans and business models for portfolio companies</li>
            <li style="margin-bottom:8px;">Led due diligence processes for $500M+ in potential investments</li>
            <li>Advised C-suite executives on growth strategies and operational improvements</li>
          </ul>
        </div>
      </section>

      <!-- Key Achievements -->
      <section style="margin-bottom:40px;">
        <h2 style="margin:0 0 25px 0;font-size:28px;font-weight:400;color:#1a365d;border-bottom:3px solid #1a365d;padding-bottom:10px;text-align:center;">Key Achievements</h2>
        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:20px;">
          <div style="background:#f8f9fa;padding:25px;border-radius:10px;border-left:5px solid #28a745;">
            <h4 style="margin:0 0 10px 0;font-size:18px;font-weight:600;color:#1a365d;">IPO Success</h4>
            <p style="margin:0;font-size:14px;color:#495057;">Led successful public offering raising $500M and achieving 40% first-day stock price increase</p>
          </div>
          <div style="background:#f8f9fa;padding:25px;border-radius:10px;border-left:5px solid #007bff;">
            <h4 style="margin:0 0 10px 0;font-size:18px;font-weight:600;color:#1a365d;">Revenue Growth</h4>
            <p style="margin:0;font-size:14px;color:#495057;">Achieved 300% revenue growth over 5-year period through strategic initiatives and market expansion</p>
          </div>
        </div>
      </section>

      <!-- Education & Board Positions -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-bottom:40px;">
        <section>
          <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:400;color:#1a365d;border-bottom:2px solid #1a365d;padding-bottom:8px;">Education</h2>
          <div style="background:#f8f9fa;padding:25px;border-radius:10px;">
            <div style="margin-bottom:20px;">
              <h4 style="margin:0 0 5px 0;font-size:18px;font-weight:600;color:#1a365d;">Master of Business Administration</h4>
              <p style="margin:0 0 3px 0;font-size:15px;color:#6c757d;">Harvard Business School</p>
              <p style="margin:0;font-size:13px;color:#6c757d;">1998 – 2000 | Baker Scholar (Top 5%)</p>
            </div>
            <div>
              <h4 style="margin:0 0 5px 0;font-size:18px;font-weight:600;color:#1a365d;">Bachelor of Science in Economics</h4>
              <p style="margin:0 0 3px 0;font-size:15px;color:#6c757d;">Wharton School, University of Pennsylvania</p>
              <p style="margin:0;font-size:13px;color:#6c757d;">1994 – 1998 | Summa Cum Laude</p>
            </div>
          </div>
        </section>

        <section>
          <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:400;color:#1a365d;border-bottom:2px solid #1a365d;padding-bottom:8px;">Board Positions</h2>
          <div style="background:#f8f9fa;padding:25px;border-radius:10px;font-size:14px;">
            <div style="margin-bottom:15px;">
              <h4 style="margin:0 0 3px 0;font-size:16px;font-weight:600;color:#1a365d;">Board of Directors</h4>
              <p style="margin:0;color:#6c757d;">TechStart Accelerator (2020 – Present)</p>
            </div>
            <div style="margin-bottom:15px;">
              <h4 style="margin:0 0 3px 0;font-size:16px;font-weight:600;color:#1a365d;">Advisory Board Member</h4>
              <p style="margin:0;color:#6c757d;">Innovation Fund Partners (2019 – Present)</p>
            </div>
            <div>
              <h4 style="margin:0 0 3px 0;font-size:16px;font-weight:600;color:#1a365d;">Trustee</h4>
              <p style="margin:0;color:#6c757d;">Business Leadership Foundation (2018 – Present)</p>
            </div>
          </div>
        </section>
      </div>

      <!-- Projects & Publications -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-bottom:40px;">
        <section>
          <h2 style="margin:0 0 15px 0;font-size:24px;font-weight:400;color:#1a365d;border-bottom:2px solid #1a365d;padding-bottom:8px;">Projects</h2>
          <div style="margin-bottom:15px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px;">
              <h3 style="margin:0;font-size:16px;font-weight:600;color:#1a365d;">Digital Transformation Initiative</h3>
              <a href="https://case-study-digital-transformation.com" style="color:#007bff;text-decoration:none;font-size:13px;">Case Study</a>
            </div>
            <p style="margin:0;font-size:14px;color:#495057;">
              Led enterprise-wide digital transformation affecting 2,000+ employees across 12 countries. Initiative resulted in $50M cost savings and 40% productivity improvement.
            </p>
          </div>
        </section>

        <section>
          <h2 style="margin:0 0 15px 0;font-size:24px;font-weight:400;color:#1a365d;border-bottom:2px solid #1a365d;padding-bottom:8px;">Publications</h2>
          <div style="font-size:14px;color:#495057;">
            <p style="margin:0 0 10px 0;">"Leading Through Disruption: A CEO's Guide to Digital Transformation" - <em>Harvard Business Review</em>, March 2024</p>
            <p style="margin:0;">"Building Resilient Organizations in the Post-Pandemic Era" - <em>McKinsey Quarterly</em>, September 2023</p>
          </div>
        </section>
      </div>

      <!-- Skills -->
      <section>
        <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:400;color:#1a365d;border-bottom:2px solid #1a365d;padding-bottom:8px;">Skills</h2>
        <div style="display:grid;grid-template-columns:150px 1fr;gap:15px;font-size:15px;">
          <div style="font-weight:600;color:#1a365d;">Leadership</div>
          <div style="color:#495057;">Strategic Planning, Change Management, Executive Coaching, Board Relations</div>
          <div style="font-weight:600;color:#1a365d;">Business</div>
          <div style="color:#495057;">M&A, IPO Management, Financial Planning, Market Analysis, Risk Management</div>
          <div style="font-weight:600;color:#1a365d;">Industries</div>
          <div style="color:#495057;">Technology, Financial Services, Healthcare, Manufacturing, Retail</div>
        </div>
      </section>

      <!-- Executive Footer -->
      <div style="text-align:center;margin-top:50px;padding-top:30px;border-top:3px solid #1a365d;">
        <div style="font-size:13px;color:#6c757d;">Last updated: 19 Aug 2025</div>
        <div style="margin-top:15px;">
          <div style="display:inline-block;width:60px;height:2px;background:#1a365d;"></div>
        </div>
      </div>
    </div>
  </main>
</body>
</html>"""
    },
    {
        "id": "t09-chronological",
        "name": "Chronological Timeline",
        "role_category": "technical",
        "has_image_slot": False,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Lisa Wang</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#fafbfc;color:#1a202c;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;line-height:1.5;">
  <main style="max-width:210mm;margin:15px auto;background:#ffffff;box-shadow:0 4px 24px rgba(0,0,0,.08);">
    <!-- Header -->
    <header style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#ffffff;padding:35px 40px;text-align:center;">
      <h1 style="margin:0 0 8px 0;font-size:32px;font-weight:300;letter-spacing:2px;">Lisa Wang</h1>
      <p style="margin:0 0 20px 0;font-size:18px;opacity:0.9;">Machine Learning Engineer</p>
      <div style="display:flex;justify-content:center;gap:30px;font-size:14px;opacity:0.9;">
        <span>📧 <a href="mailto:lisa.wang@email.com" style="color:#ffffff;text-decoration:none;">lisa.wang@email.com</a></span>
        <span>📱 <a href="tel:+15551234567" style="color:#ffffff;text-decoration:none;">+1 (555) 123-4567</a></span>
        <span>🔗 <a href="https://github.com/lisawang" style="color:#ffffff;text-decoration:none;">github.com/lisawang</a></span>
        <span>📍 San Francisco, CA</span>
      </div>
    </header>

    <div style="padding:40px;">
      <!-- Summary -->
      <section style="margin-bottom:35px;text-align:center;">
        <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:600;color:#667eea;">Summary</h2>
        <p style="margin:0;font-size:16px;max-width:800px;margin:0 auto;text-align:justify;color:#4a5568;">
          Innovative Machine Learning Engineer with 7+ years of experience developing and deploying ML models at scale. Expertise in deep learning, computer vision, and natural language processing. Led ML initiatives that improved model accuracy by 40% and reduced inference time by 60%. Passionate about applying AI to solve real-world problems and mentoring the next generation of ML engineers.
        </p>
      </section>

      <!-- Timeline -->
      <section style="margin-bottom:35px;">
        <h2 style="margin:0 0 30px 0;font-size:24px;font-weight:600;color:#667eea;text-align:center;">Career Timeline</h2>
        
        <!-- Timeline container -->
        <div style="position:relative;max-width:900px;margin:0 auto;">
          <!-- Central timeline line -->
          <div style="position:absolute;left:50%;top:0;bottom:0;width:3px;background:linear-gradient(180deg,#667eea,#764ba2);transform:translateX(-50%);"></div>
          
          <!-- Timeline items -->
          <div style="position:relative;">
            <!-- 2021 - Present -->
            <div style="display:flex;align-items:center;margin-bottom:40px;">
              <div style="width:45%;text-align:right;padding-right:30px;">
                <div style="background:#ffffff;padding:20px;border-radius:10px;box-shadow:0 4px 16px rgba(102,126,234,0.15);border:2px solid #667eea;">
                  <div style="display:flex;justify-content:between;align-items:center;margin-bottom:10px;">
                    <h3 style="margin:0;font-size:18px;font-weight:600;color:#1a202c;">Senior ML Engineer</h3>
                  </div>
                  <p style="margin:0 0 8px 0;font-size:15px;color:#667eea;font-weight:500;">TechFlow AI, San Francisco</p>
                  <ul style="margin:0;padding-left:20px;font-size:13px;color:#4a5568;">
                    <li>Led development of computer vision models for autonomous vehicle perception</li>
                    <li>Improved object detection accuracy by 35% using advanced CNN architectures</li>
                    <li>Built MLOps pipeline processing 10TB+ of data daily with 99.9% uptime</li>
                    <li>Mentored team of 8 junior ML engineers and data scientists</li>
                  </ul>
                </div>
              </div>
              <div style="position:relative;width:10%;display:flex;justify-content:center;">
                <div style="width:20px;height:20px;background:#667eea;border-radius:50%;border:4px solid #ffffff;box-shadow:0 0 0 3px #667eea;z-index:2;"></div>
                <div style="position:absolute;top:25px;background:#667eea;color:#ffffff;padding:4px 12px;border-radius:15px;font-size:12px;font-weight:600;white-space:nowrap;">2021 – Present</div>
              </div>
              <div style="width:45%;padding-left:30px;">
                <!-- Empty for alternating layout -->
              </div>
            </div>

            <!-- 2019 - 2021 -->
            <div style="display:flex;align-items:center;margin-bottom:40px;">
              <div style="width:45%;text-align:right;padding-right:30px;">
                <!-- Empty for alternating layout -->
              </div>
              <div style="position:relative;width:10%;display:flex;justify-content:center;">
                <div style="width:20px;height:20px;background:#764ba2;border-radius:50%;border:4px solid #ffffff;box-shadow:0 0 0 3px #764ba2;z-index:2;"></div>
                <div style="position:absolute;top:25px;background:#764ba2;color:#ffffff;padding:4px 12px;border-radius:15px;font-size:12px;font-weight:600;white-space:nowrap;">2019 – 2021</div>
              </div>
              <div style="width:45%;padding-left:30px;">
                <div style="background:#ffffff;padding:20px;border-radius:10px;box-shadow:0 4px 16px rgba(118,75,162,0.15);border:2px solid #764ba2;">
                  <h3 style="margin:0 0 10px 0;font-size:18px;font-weight:600;color:#1a202c;">ML Engineer</h3>
                  <p style="margin:0 0 8px 0;font-size:15px;color:#764ba2;font-weight:500;">DataCorp Solutions, Seattle</p>
                  <ul style="margin:0;padding-left:20px;font-size:13px;color:#4a5568;">
                    <li>Developed NLP models for sentiment analysis and text classification</li>
                    <li>Built recommendation system serving 1M+ users with sub-100ms latency</li>
                    <li>Implemented A/B testing framework for ML model evaluation</li>
                    <li>Reduced model training time by 50% through distributed computing</li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- 2017 - 2019 -->
            <div style="display:flex;align-items:center;margin-bottom:40px;">
              <div style="width:45%;text-align:right;padding-right:30px;">
                <div style="background:#ffffff;padding:20px;border-radius:10px;box-shadow:0 4px 16px rgba(139,92,246,0.15);border:2px solid #8b5cf6;">
                  <h3 style="margin:0 0 10px 0;font-size:18px;font-weight:600;color:#1a202c;">Data Scientist</h3>
                  <p style="margin:0 0 8px 0;font-size:15px;color:#8b5cf6;font-weight:500;">Analytics Pro, Portland</p>
                  <ul style="margin:0;padding-left:20px;font-size:13px;color:#4a5568;">
                    <li>Built predictive models for customer churn and lifetime value</li>
                    <li>Performed statistical analysis on large datasets using Python and R</li>
                    <li>Created interactive dashboards and data visualizations</li>
                    <li>Collaborated with product teams to define KPIs and success metrics</li>
                  </ul>
                </div>
              </div>
              <div style="position:relative;width:10%;display:flex;justify-content:center;">
                <div style="width:20px;height:20px;background:#8b5cf6;border-radius:50%;border:4px solid #ffffff;box-shadow:0 0 0 3px #8b5cf6;z-index:2;"></div>
                <div style="position:absolute;top:25px;background:#8b5cf6;color:#ffffff;padding:4px 12px;border-radius:15px;font-size:12px;font-weight:600;white-space:nowrap;">2017 – 2019</div>
              </div>
              <div style="width:45%;padding-left:30px;">
                <!-- Empty for alternating layout -->
              </div>
            </div>

            <!-- Education -->
            <div style="display:flex;align-items:center;">
              <div style="width:45%;text-align:right;padding-right:30px;">
                <!-- Empty for alternating layout -->
              </div>
              <div style="position:relative;width:10%;display:flex;justify-content:center;">
                <div style="width:20px;height:20px;background:#10b981;border-radius:50%;border:4px solid #ffffff;box-shadow:0 0 0 3px #10b981;z-index:2;"></div>
                <div style="position:absolute;top:25px;background:#10b981;color:#ffffff;padding:4px 12px;border-radius:15px;font-size:12px;font-weight:600;white-space:nowrap;">2013 – 2017</div>
              </div>
              <div style="width:45%;padding-left:30px;">
                <div style="background:#ffffff;padding:20px;border-radius:10px;box-shadow:0 4px 16px rgba(16,185,129,0.15);border:2px solid #10b981;">
                  <h3 style="margin:0 0 10px 0;font-size:18px;font-weight:600;color:#1a202c;">Education</h3>
                  <p style="margin:0 0 5px 0;font-size:15px;color:#10b981;font-weight:500;">Master of Science in Computer Science</p>
                  <p style="margin:0 0 8px 0;font-size:14px;color:#4a5568;">Stanford University | GPA: 3.9/4.0</p>
                  <p style="margin:0;font-size:13px;color:#4a5568;">Specialization: Machine Learning and Artificial Intelligence</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Technical Skills -->
      <section style="margin-bottom:35px;">
        <h2 style="margin:0 0 25px 0;font-size:24px;font-weight:600;color:#667eea;text-align:center;">Technical Expertise</h2>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:25px;">
          <div style="background:#f7fafc;padding:25px;border-radius:10px;text-align:center;border-top:4px solid #667eea;">
            <h4 style="margin:0 0 15px 0;font-size:16px;font-weight:600;color:#1a202c;">Machine Learning</h4>
            <div style="font-size:13px;color:#4a5568;line-height:1.8;">
              TensorFlow, PyTorch, Scikit-learn, Keras, XGBoost, LightGBM
            </div>
          </div>
          <div style="background:#f7fafc;padding:25px;border-radius:10px;text-align:center;border-top:4px solid #764ba2;">
            <h4 style="margin:0 0 15px 0;font-size:16px;font-weight:600;color:#1a202c;">Programming</h4>
            <div style="font-size:13px;color:#4a5568;line-height:1.8;">
              Python, R, SQL, Scala, Java, C++, JavaScript
            </div>
          </div>
          <div style="background:#f7fafc;padding:25px;border-radius:10px;text-align:center;border-top:4px solid #8b5cf6;">
            <h4 style="margin:0 0 15px 0;font-size:16px;font-weight:600;color:#1a202c;">Cloud & Tools</h4>
            <div style="font-size:13px;color:#4a5568;line-height:1.8;">
              AWS, GCP, Docker, Kubernetes, Apache Spark, Airflow
            </div>
          </div>
        </div>
      </section>

      <!-- Projects -->
      <section style="margin-bottom:35px;">
        <h2 style="margin:0 0 25px 0;font-size:24px;font-weight:600;color:#667eea;text-align:center;">Featured Projects</h2>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:25px;">
          <div style="background:#ffffff;padding:25px;border-radius:10px;box-shadow:0 4px 16px rgba(0,0,0,0.08);border:1px solid #e2e8f0;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">
              <h3 style="margin:0;font-size:18px;font-weight:600;color:#1a202c;">Real-time Fraud Detection</h3>
              <a href="https://github.com/lisawang/fraud-detection" style="color:#667eea;text-decoration:none;font-size:13px;">GitHub</a>
            </div>
            <p style="margin:0;font-size:14px;color:#4a5568;">
              Built end-to-end ML pipeline for real-time fraud detection processing 100K+ transactions per second. Achieved 95% accuracy with sub-50ms latency using ensemble methods and feature engineering.
            </p>
          </div>
          <div style="background:#ffffff;padding:25px;border-radius:10px;box-shadow:0 4px 16px rgba(0,0,0,0.08);border:1px solid #e2e8f0;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">
              <h3 style="margin:0;font-size:18px;font-weight:600;color:#1a202c;">Computer Vision for Medical Imaging</h3>
              <a href="https://medical-cv-demo.com" style="color:#667eea;text-decoration:none;font-size:13px;">Demo</a>
            </div>
            <p style="margin:0;font-size:14px;color:#4a5568;">
              Developed deep learning models for medical image analysis achieving 98% accuracy in disease detection. Collaborated with radiologists to validate results and ensure clinical applicability.
            </p>
          </div>
        </div>
      </section>

      <!-- Education Details -->
      <section style="margin-bottom:35px;">
        <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:600;color:#667eea;text-align:center;">Education</h2>
        <div style="display:grid;grid-template-columns:120px 1fr;gap:15px;font-size:14px;max-width:600px;margin:0 auto;">
          <div style="color:#718096;font-weight:500;">2015 – 2017</div>
          <div>Master of Science in Computer Science at <strong>Stanford University</strong> <span style="float:right;color:#718096;">(GPA: 3.9/4.0)</span></div>
          <div style="color:#718096;font-weight:500;">2011 – 2015</div>
          <div>Bachelor of Science in Mathematics at <strong>UC Berkeley</strong> <span style="float:right;color:#718096;">(GPA: 3.8/4.0)</span></div>
        </div>
      </section>

      <!-- Publications -->
      <section style="margin-bottom:35px;">
        <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:600;color:#667eea;text-align:center;">Publications</h2>
        <div style="background:#f7fafc;padding:25px;border-radius:10px;font-size:14px;color:#4a5568;max-width:800px;margin:0 auto;">
          <p style="margin:0 0 12px 0;">"Deep Learning Approaches for Real-time Fraud Detection" - <em>IEEE Transactions on Neural Networks</em>, 2024</p>
          <p style="margin:0 0 12px 0;">"Scalable Machine Learning Pipelines for Production Systems" - <em>ACM Computing Surveys</em>, 2023</p>
          <p style="margin:0;">"Computer Vision Applications in Medical Diagnosis" - <em>Nature Machine Intelligence</em>, 2023</p>
        </div>
      </section>

      <!-- Skills -->
      <section>
        <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:600;color:#667eea;text-align:center;">Skills</h2>
        <div style="display:grid;grid-template-columns:140px 1fr;gap:12px;font-size:14px;max-width:800px;margin:0 auto;">
          <div style="font-weight:600;color:#1a202c;">Specializations</div>
          <div style="color:#4a5568;">Deep Learning, Computer Vision, NLP, MLOps, Statistical Analysis</div>
          <div style="font-weight:600;color:#1a202c;">Methodologies</div>
          <div style="color:#4a5568;">Agile Development, A/B Testing, Model Validation, Feature Engineering</div>
        </div>
      </section>

      <!-- Footer -->
      <div style="text-align:center;margin-top:40px;padding-top:25px;border-top:2px solid #667eea;">
        <div style="font-size:12px;color:#718096;">Last updated: 19 Aug 2025</div>
      </div>
    </div>
  </main>
</body>
</html>"""
    },
    {
        "id": "t10-portfolio",
        "name": "Portfolio Showcase",
        "role_category": "non-technical",
        "has_image_slot": True,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Michael Chen</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#f5f7fa;color:#2d3748;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;line-height:1.6;">
  <main style="max-width:210mm;margin:10px auto;background:#ffffff;box-shadow:0 8px 40px rgba(0,0,0,.12);">
    <!-- Portfolio Header -->
    <header style="background:linear-gradient(45deg,#667eea 0%,#764ba2 50%,#f093fb 100%);color:#ffffff;padding:40px;text-align:center;position:relative;overflow:hidden;">
      <div style="position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:rgba(255,255,255,0.1);border-radius:50%;"></div>
      <div style="position:absolute;bottom:-30px;right:-30px;width:150px;height:150px;background:rgba(255,255,255,0.1);border-radius:50%;"></div>
      <div style="position:relative;z-index:2;">
        <img src="{{PHOTO_URL}}" alt="Michael Chen" style="width:100px;height:100px;border-radius:50%;border:4px solid #ffffff;margin-bottom:20px;box-shadow:0 8px 24px rgba(0,0,0,0.2);" />
        <h1 style="margin:0 0 10px 0;font-size:32px;font-weight:300;letter-spacing:2px;">Michael Chen</h1>
        <p style="margin:0 0 20px 0;font-size:18px;opacity:0.9;">UX/UI Designer & Product Strategist</p>
        <div style="display:flex;justify-content:center;gap:25px;font-size:14px;opacity:0.9;">
          <span>📧 michael.chen@email.com</span>
          <span>📱 +1 (555) 123-4567</span>
          <span>🌐 michaelchen.design</span>
          <span>📍 Los Angeles, CA</span>
        </div>
      </div>
    </header>

    <div style="padding:40px;">
      <!-- Portfolio Summary -->
      <section style="margin-bottom:40px;text-align:center;">
        <h2 style="margin:0 0 20px 0;font-size:28px;font-weight:600;color:#667eea;position:relative;">
          Design Philosophy
          <div style="position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);width:60px;height:3px;background:linear-gradient(90deg,#667eea,#764ba2);border-radius:2px;"></div>
        </h2>
        <p style="margin:0;font-size:16px;max-width:700px;margin:0 auto;text-align:justify;color:#4a5568;">
          Passionate UX/UI Designer with 6+ years of experience creating user-centered digital experiences for startups and Fortune 500 companies. I believe great design is invisible – it solves problems so elegantly that users don't even notice the interface. My approach combines data-driven insights with human empathy to create products that people love to use.
        </p>
      </section>

      <!-- Portfolio Grid -->
      <section style="margin-bottom:40px;">
        <h2 style="margin:0 0 30px 0;font-size:28px;font-weight:600;color:#667eea;text-align:center;position:relative;">
          Featured Work
          <div style="position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);width:60px;height:3px;background:linear-gradient(90deg,#667eea,#764ba2);border-radius:2px;"></div>
        </h2>
        
        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:25px;margin-bottom:30px;">
          <!-- Portfolio Item 1 -->
          <div style="background:#ffffff;border-radius:15px;overflow:hidden;box-shadow:0 8px 32px rgba(0,0,0,0.1);transition:transform 0.3s ease;">
            <div style="height:180px;background:linear-gradient(135deg,#667eea,#764ba2);position:relative;display:flex;align-items:center;justify-content:center;">
              <div style="color:#ffffff;font-size:48px;opacity:0.8;">📱</div>
            </div>
            <div style="padding:25px;">
              <h3 style="margin:0 0 10px 0;font-size:18px;font-weight:600;color:#2d3748;">FinTech Mobile App</h3>
              <p style="margin:0 0 15px 0;font-size:14px;color:#4a5568;line-height:1.6;">
                Complete redesign of mobile banking app serving 2M+ users. Improved user satisfaction by 40% and reduced support tickets by 60%.
              </p>
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <div style="display:flex;gap:8px;">
                  <span style="background:#e2e8f0;color:#4a5568;padding:4px 8px;border-radius:12px;font-size:11px;">UI Design</span>
                  <span style="background:#e2e8f0;color:#4a5568;padding:4px 8px;border-radius:12px;font-size:11px;">Prototyping</span>
                </div>
                <a href="https://portfolio.michaelchen.design/fintech" style="color:#667eea;text-decoration:none;font-size:13px;font-weight:500;">View Case Study →</a>
              </div>
            </div>
          </div>

          <!-- Portfolio Item 2 -->
          <div style="background:#ffffff;border-radius:15px;overflow:hidden;box-shadow:0 8px 32px rgba(0,0,0,0.1);">
            <div style="height:180px;background:linear-gradient(135deg,#f093fb,#f5576c);position:relative;display:flex;align-items:center;justify-content:center;">
              <div style="color:#ffffff;font-size:48px;opacity:0.8;">🛒</div>
            </div>
            <div style="padding:25px;">
              <h3 style="margin:0 0 10px 0;font-size:18px;font-weight:600;color:#2d3748;">E-commerce Platform</h3>
              <p style="margin:0 0 15px 0;font-size:14px;color:#4a5568;line-height:1.6;">
                End-to-end design system for B2B e-commerce platform. Increased conversion rates by 35% and streamlined checkout process.
              </p>
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <div style="display:flex;gap:8px;">
                  <span style="background:#e2e8f0;color:#4a5568;padding:4px 8px;border-radius:12px;font-size:11px;">UX Research</span>
                  <span style="background:#e2e8f0;color:#4a5568;padding:4px 8px;border-radius:12px;font-size:11px;">Design System</span>
                </div>
                <a href="https://portfolio.michaelchen.design/ecommerce" style="color:#667eea;text-decoration:none;font-size:13px;font-weight:500;">View Case Study →</a>
              </div>
            </div>
          </div>

          <!-- Portfolio Item 3 -->
          <div style="background:#ffffff;border-radius:15px;overflow:hidden;box-shadow:0 8px 32px rgba(0,0,0,0.1);">
            <div style="height:180px;background:linear-gradient(135deg,#4facfe,#00f2fe);position:relative;display:flex;align-items:center;justify-content:center;">
              <div style="color:#ffffff;font-size:48px;opacity:0.8;">🎓</div>
            </div>
            <div style="padding:25px;">
              <h3 style="margin:0 0 10px 0;font-size:18px;font-weight:600;color:#2d3748;">EdTech Learning Platform</h3>
              <p style="margin:0 0 15px 0;font-size:14px;color:#4a5568;line-height:1.6;">
                Interactive learning platform for K-12 students. Improved engagement metrics by 50% through gamification and personalization.
              </p>
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <div style="display:flex;gap:8px;">
                  <span style="background:#e2e8f0;color:#4a5568;padding:4px 8px;border-radius:12px;font-size:11px;">User Testing</span>
                  <span style="background:#e2e8f0;color:#4a5568;padding:4px 8px;border-radius:12px;font-size:11px;">Interaction Design</span>
                </div>
                <a href="https://portfolio.michaelchen.design/edtech" style="color:#667eea;text-decoration:none;font-size:13px;font-weight:500;">View Case Study →</a>
              </div>
            </div>
          </div>

          <!-- Portfolio Item 4 -->
          <div style="background:#ffffff;border-radius:15px;overflow:hidden;box-shadow:0 8px 32px rgba(0,0,0,0.1);">
            <div style="height:180px;background:linear-gradient(135deg,#fa709a,#fee140);position:relative;display:flex;align-items:center;justify-content:center;">
              <div style="color:#ffffff;font-size:48px;opacity:0.8;">🏥</div>
            </div>
            <div style="padding:25px;">
              <h3 style="margin:0 0 10px 0;font-size:18px;font-weight:600;color:#2d3748;">Healthcare Dashboard</h3>
              <p style="margin:0 0 15px 0;font-size:14px;color:#4a5568;line-height:1.6;">
                Data visualization dashboard for healthcare providers. Reduced diagnosis time by 25% through intuitive information architecture.
              </p>
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <div style="display:flex;gap:8px;">
                  <span style="background:#e2e8f0;color:#4a5568;padding:4px 8px;border-radius:12px;font-size:11px;">Data Viz</span>
                  <span style="background:#e2e8f0;color:#4a5568;padding:4px 8px;border-radius:12px;font-size:11px;">Dashboard</span>
                </div>
                <a href="https://portfolio.michaelchen.design/healthcare" style="color:#667eea;text-decoration:none;font-size:13px;font-weight:500;">View Case Study →</a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Experience -->
      <section style="margin-bottom:40px;">
        <h2 style="margin:0 0 30px 0;font-size:28px;font-weight:600;color:#667eea;text-align:center;position:relative;">
          Work Experience
          <div style="position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);width:60px;height:3px;background:linear-gradient(90deg,#667eea,#764ba2);border-radius:2px;"></div>
        </h2>
        
        <div style="space-y:30px;">
          <div style="background:#f7fafc;padding:30px;border-radius:15px;border-left:5px solid #667eea;margin-bottom:25px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:15px;">
              <div>
                <h3 style="margin:0 0 5px 0;font-size:20px;font-weight:600;color:#2d3748;">Senior UX/UI Designer</h3>
                <p style="margin:0;font-size:16px;color:#667eea;font-weight:500;">TechFlow Solutions, Los Angeles</p>
              </div>
              <span style="background:#667eea;color:#ffffff;padding:6px 15px;border-radius:20px;font-size:13px;font-weight:500;">2020 – Present</span>
            </div>
            <ul style="margin:0;padding-left:20px;font-size:14px;color:#4a5568;">
              <li>Lead design for 3 major product lines serving 500K+ active users</li>
              <li>Established design system reducing development time by 40%</li>
              <li>Conducted user research and usability testing for product optimization</li>
              <li>Mentored team of 4 junior designers and collaborated with cross-functional teams</li>
            </ul>
          </div>

          <div style="background:#f7fafc;padding:30px;border-radius:15px;border-left:5px solid #764ba2;margin-bottom:25px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:15px;">
              <div>
                <h3 style="margin:0 0 5px 0;font-size:20px;font-weight:600;color:#2d3748;">UX Designer</h3>
                <p style="margin:0;font-size:16px;color:#764ba2;font-weight:500;">StartupXYZ, San Francisco</p>
              </div>
              <span style="background:#764ba2;color:#ffffff;padding:6px 15px;border-radius:20px;font-size:13px;font-weight:500;">2018 – 2020</span>
            </div>
            <ul style="margin:0;padding-left:20px;font-size:14px;color:#4a5568;">
              <li>Designed mobile-first experiences for consumer-facing applications</li>
              <li>Improved user onboarding flow resulting in 60% increase in completion rates</li>
              <li>Created wireframes, prototypes, and high-fidelity mockups</li>
              <li>Collaborated with product managers and developers in agile environment</li>
            </ul>
          </div>

          <div style="background:#f7fafc;padding:30px;border-radius:15px;border-left:5px solid #f093fb;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:15px;">
              <div>
                <h3 style="margin:0 0 5px 0;font-size:20px;font-weight:600;color:#2d3748;">Junior UI Designer</h3>
                <p style="margin:0;font-size:16px;color:#f093fb;font-weight:500;">Creative Agency, Portland</p>
              </div>
              <span style="background:#f093fb;color:#ffffff;padding:6px 15px;border-radius:20px;font-size:13px;font-weight:500;">2017 – 2018</span>
            </div>
            <ul style="margin:0;padding-left:20px;font-size:14px;color:#4a5568;">
              <li>Created visual designs for web and mobile applications</li>
              <li>Worked with clients to understand requirements and deliver solutions</li>
              <li>Developed brand identities and marketing materials</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Skills & Tools -->
      <section style="margin-bottom:40px;">
        <h2 style="margin:0 0 30px 0;font-size:28px;font-weight:600;color:#667eea;text-align:center;position:relative;">
          Skills & Tools
          <div style="position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);width:60px;height:3px;background:linear-gradient(90deg,#667eea,#764ba2);border-radius:2px;"></div>
        </h2>
        
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:25px;">
          <div style="background:#f7fafc;padding:25px;border-radius:15px;text-align:center;border-top:4px solid #667eea;">
            <h4 style="margin:0 0 15px 0;font-size:16px;font-weight:600;color:#2d3748;">Design Tools</h4>
            <div style="font-size:13px;color:#4a5568;line-height:1.8;">
              Figma, Sketch, Adobe XD, Photoshop, Illustrator, InVision, Principle
            </div>
          </div>
          <div style="background:#f7fafc;padding:25px;border-radius:15px;text-align:center;border-top:4px solid #764ba2;">
            <h4 style="margin:0 0 15px 0;font-size:16px;font-weight:600;color:#2d3748;">Research & Testing</h4>
            <div style="font-size:13px;color:#4a5568;line-height:1.8;">
              User Interviews, Usability Testing, A/B Testing, Analytics, Surveys
            </div>
          </div>
          <div style="background:#f7fafc;padding:25px;border-radius:15px;text-align:center;border-top:4px solid #f093fb;">
            <h4 style="margin:0 0 15px 0;font-size:16px;font-weight:600;color:#2d3748;">Development</h4>
            <div style="font-size:13px;color:#4a5568;line-height:1.8;">
              HTML, CSS, JavaScript, React Basics, Design Systems, Responsive Design
            </div>
          </div>
        </div>
      </section>

      <!-- Education & Achievements -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-bottom:40px;">
        <section>
          <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:600;color:#667eea;">Education</h2>
          <div style="background:#f7fafc;padding:25px;border-radius:15px;">
            <div style="margin-bottom:20px;">
              <h4 style="margin:0 0 5px 0;font-size:16px;font-weight:600;color:#2d3748;">Bachelor of Fine Arts in Graphic Design</h4>
              <p style="margin:0 0 3px 0;font-size:14px;color:#667eea;">Art Institute of California</p>
              <p style="margin:0;font-size:12px;color:#718096;">2013 – 2017 | GPA: 3.8/4.0</p>
            </div>
            <div>
              <h4 style="margin:0 0 5px 0;font-size:16px;font-weight:600;color:#2d3748;">UX Design Certificate</h4>
              <p style="margin:0 0 3px 0;font-size:14px;color:#667eea;">Google UX Design Professional Certificate</p>
              <p style="margin:0;font-size:12px;color:#718096;">2018</p>
            </div>
          </div>
        </section>

        <section>
          <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:600;color:#667eea;">Awards & Recognition</h2>
          <div style="background:#f7fafc;padding:25px;border-radius:15px;font-size:14px;">
            <div style="margin-bottom:15px;">
              <h4 style="margin:0 0 3px 0;font-size:15px;font-weight:600;color:#2d3748;">Best Mobile App Design</h4>
              <p style="margin:0;color:#4a5568;">UX Design Awards 2023</p>
            </div>
            <div style="margin-bottom:15px;">
              <h4 style="margin:0 0 3px 0;font-size:15px;font-weight:600;color:#2d3748;">Innovation in UX</h4>
              <p style="margin:0;color:#4a5568;">Design Excellence Awards 2022</p>
            </div>
            <div>
              <h4 style="margin:0 0 3px 0;font-size:15px;font-weight:600;color:#2d3748;">Rising Designer of the Year</h4>
              <p style="margin:0;color:#4a5568;">Creative Industry Awards 2021</p>
            </div>
          </div>
        </section>
      </div>

      <!-- Publications -->
      <section style="margin-bottom:40px;">
        <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:600;color:#667eea;text-align:center;">Publications</h2>
        <div style="background:#f7fafc;padding:25px;border-radius:15px;font-size:14px;color:#4a5568;text-align:center;">
          <p style="margin:0 0 10px 0;">"The Future of Mobile UX: Designing for Generation Z" - <em>UX Magazine</em>, March 2024</p>
          <p style="margin:0;">"Building Inclusive Design Systems" - <em>Design Systems Weekly</em>, November 2023</p>
        </div>
      </section>

      <!-- Skills Summary -->
      <section>
        <h2 style="margin:0 0 20px 0;font-size:24px;font-weight:600;color:#667eea;text-align:center;">Skills</h2>
        <div style="display:grid;grid-template-columns:140px 1fr;gap:12px;font-size:14px;max-width:800px;margin:0 auto;">
          <div style="font-weight:600;color:#2d3748;">Specializations</div>
          <div style="color:#4a5568;">User Experience Design, User Interface Design, Design Systems, Prototyping</div>
          <div style="font-weight:600;color:#2d3748;">Methodologies</div>
          <div style="color:#4a5568;">Design Thinking, Human-Centered Design, Agile UX, Lean UX</div>
        </div>
      </section>

      <!-- Creative Footer -->
      <div style="text-align:center;margin-top:50px;padding-top:30px;border-top:3px solid #667eea;">
        <div style="font-size:12px;color:#718096;margin-bottom:15px;">Last updated: 19 Aug 2025</div>
        <div style="display:flex;justify-content:center;gap:20px;">
          <div style="width:30px;height:4px;background:#667eea;border-radius:2px;"></div>
          <div style="width:30px;height:4px;background:#764ba2;border-radius:2px;"></div>
          <div style="width:30px;height:4px;background:#f093fb;border-radius:2px;"></div>
        </div>
      </div>
    </div>
  </main>
</body>
</html>"""
    },
    {
        "id": "t11-minimalist",
        "name": "Minimalist Clean",
        "role_category": "technical",
        "has_image_slot": False,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Anna Kowalski</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#ffffff;color:#2c3e50;font-family:'SF Pro Display',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.5;">
  <main style="max-width:210mm;margin:20px auto;background:#ffffff;">
    <div style="padding:50mm 20mm 25mm 20mm;">
      <!-- Minimalist Header -->
      <header style="margin-bottom:50px;">
        <h1 style="margin:0 0 8px 0;font-size:42px;font-weight:200;color:#2c3e50;letter-spacing:-1px;">Anna Kowalski</h1>
        <p style="margin:0 0 25px 0;font-size:18px;color:#7f8c8d;font-weight:300;">Software Architect</p>
        <div style="font-size:14px;color:#95a5a6;line-height:2;">
          <div>anna.kowalski@email.com</div>
          <div>+1 (555) 123-4567</div>
          <div>github.com/annakowalski</div>
          <div>San Francisco, CA</div>
        </div>
      </header>

      <!-- Minimalist Summary -->
      <section style="margin-bottom:45px;">
        <h2 style="margin:0 0 20px 0;font-size:16px;font-weight:600;color:#2c3e50;text-transform:uppercase;letter-spacing:2px;">Summary</h2>
        <p style="margin:0;font-size:15px;color:#34495e;font-weight:300;line-height:1.8;max-width:600px;">
          Software Architect with 10+ years of experience designing and implementing scalable distributed systems. Expertise in microservices architecture, cloud-native technologies, and leading engineering teams. Passionate about building robust, maintainable software that solves complex business problems at scale.
        </p>
      </section>

      <!-- Minimalist Experience -->
      <section style="margin-bottom:45px;">
        <h2 style="margin:0 0 30px 0;font-size:16px;font-weight:600;color:#2c3e50;text-transform:uppercase;letter-spacing:2px;">Experience</h2>
        
        <div style="margin-bottom:35px;">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px;">
            <h3 style="margin:0;font-size:18px;font-weight:400;color:#2c3e50;">Principal Software Architect</h3>
            <span style="font-size:13px;color:#95a5a6;font-weight:300;">2020 – Present</span>
          </div>
          <p style="margin:0 0 12px 0;font-size:14px;color:#7f8c8d;font-weight:400;">CloudScale Technologies</p>
          <ul style="margin:0;padding-left:0;list-style:none;font-size:14px;color:#34495e;font-weight:300;line-height:1.7;">
            <li style="margin-bottom:6px;position:relative;padding-left:15px;">
              <span style="position:absolute;left:0;top:8px;width:3px;height:3px;background:#bdc3c7;border-radius:50%;"></span>
              Architected microservices platform serving 10M+ requests per day with 99.99% uptime
            </li>
            <li style="margin-bottom:6px;position:relative;padding-left:15px;">
              <span style="position:absolute;left:0;top:8px;width:3px;height:3px;background:#bdc3c7;border-radius:50%;"></span>
              Led technical strategy for cloud migration reducing infrastructure costs by 40%
            </li>
            <li style="margin-bottom:6px;position:relative;padding-left:15px;">
              <span style="position:absolute;left:0;top:8px;width:3px;height:3px;background:#bdc3c7;border-radius:50%;"></span>
              Managed team of 15 engineers across 3 product lines
            </li>
            <li style="position:relative;padding-left:15px;">
              <span style="position:absolute;left:0;top:8px;width:3px;height:3px;background:#bdc3c7;border-radius:50%;"></span>
              Established engineering best practices and code review standards
            </li>
          </ul>
        </div>

        <div style="margin-bottom:35px;">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px;">
            <h3 style="margin:0;font-size:18px;font-weight:400;color:#2c3e50;">Senior Software Engineer</h3>
            <span style="font-size:13px;color:#95a5a6;font-weight:300;">2017 – 2020</span>
          </div>
          <p style="margin:0 0 12px 0;font-size:14px;color:#7f8c8d;font-weight:400;">TechFlow Solutions</p>
          <ul style="margin:0;padding-left:0;list-style:none;font-size:14px;color:#34495e;font-weight:300;line-height:1.7;">
            <li style="margin-bottom:6px;position:relative;padding-left:15px;">
              <span style="position:absolute;left:0;top:8px;width:3px;height:3px;background:#bdc3c7;border-radius:50%;"></span>
              Designed and implemented RESTful APIs serving 1M+ daily active users
            </li>
            <li style="margin-bottom:6px;position:relative;padding-left:15px;">
              <span style="position:absolute;left:0;top:8px;width:3px;height:3px;background:#bdc3c7;border-radius:50%;"></span>
              Optimized database queries improving application performance by 60%
            </li>
            <li style="position:relative;padding-left:15px;">
              <span style="position:absolute;left:0;top:8px;width:3px;height:3px;background:#bdc3c7;border-radius:50%;"></span>
              Mentored junior developers and conducted technical interviews
            </li>
          </ul>
        </div>

        <div style="margin-bottom:35px;">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px;">
            <h3 style="margin:0;font-size:18px;font-weight:400;color:#2c3e50;">Software Engineer</h3>
            <span style="font-size:13px;color:#95a5a6;font-weight:300;">2015 – 2017</span>
          </div>
          <p style="margin:0 0 12px 0;font-size:14px;color:#7f8c8d;font-weight:400;">StartupXYZ</p>
          <ul style="margin:0;padding-left:0;list-style:none;font-size:14px;color:#34495e;font-weight:300;line-height:1.7;">
            <li style="margin-bottom:6px;position:relative;padding-left:15px;">
              <span style="position:absolute;left:0;top:8px;width:3px;height:3px;background:#bdc3c7;border-radius:50%;"></span>
              Built full-stack web applications using React, Node.js, and PostgreSQL
            </li>
            <li style="position:relative;padding-left:15px;">
              <span style="position:absolute;left:0;top:8px;width:3px;height:3px;background:#bdc3c7;border-radius:50%;"></span>
              Implemented CI/CD pipelines and automated testing frameworks
            </li>
          </ul>
        </div>
      </section>

      <!-- Minimalist Projects -->
      <section style="margin-bottom:45px;">
        <h2 style="margin:0 0 25px 0;font-size:16px;font-weight:600;color:#2c3e50;text-transform:uppercase;letter-spacing:2px;">Projects</h2>
        <div style="margin-bottom:20px;">
          <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:5px;">
            <h3 style="margin:0;font-size:16px;font-weight:400;color:#2c3e50;">Distributed Event Processing System</h3>
            <a href="https://github.com/annakowalski/event-processor" style="color:#95a5a6;text-decoration:none;font-size:13px;">github.com</a>
          </div>
          <p style="margin:0;font-size:14px;color:#34495e;font-weight:300;line-height:1.7;">
            Open-source event processing system built with Apache Kafka and Go. Handles 100K+ events per second with guaranteed delivery and exactly-once processing semantics.
          </p>
        </div>
      </section>

      <!-- Minimalist Skills -->
      <section style="margin-bottom:45px;">
        <h2 style="margin:0 0 25px 0;font-size:16px;font-weight:600;color:#2c3e50;text-transform:uppercase;letter-spacing:2px;">Technical Skills</h2>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:30px;font-size:14px;">
          <div>
            <h4 style="margin:0 0 10px 0;font-size:13px;font-weight:500;color:#7f8c8d;text-transform:uppercase;letter-spacing:1px;">Languages</h4>
            <div style="color:#34495e;font-weight:300;line-height:1.8;">
              Go, Python, JavaScript, TypeScript, Java, SQL
            </div>
          </div>
          <div>
            <h4 style="margin:0 0 10px 0;font-size:13px;font-weight:500;color:#7f8c8d;text-transform:uppercase;letter-spacing:1px;">Platforms</h4>
            <div style="color:#34495e;font-weight:300;line-height:1.8;">
              AWS, Kubernetes, Docker, Apache Kafka, Redis
            </div>
          </div>
          <div>
            <h4 style="margin:0 0 10px 0;font-size:13px;font-weight:500;color:#7f8c8d;text-transform:uppercase;letter-spacing:1px;">Databases</h4>
            <div style="color:#34495e;font-weight:300;line-height:1.8;">
              PostgreSQL, MongoDB, Cassandra, DynamoDB
            </div>
          </div>
        </div>
      </section>

      <!-- Minimalist Education -->
      <section style="margin-bottom:45px;">
        <h2 style="margin:0 0 25px 0;font-size:16px;font-weight:600;color:#2c3e50;text-transform:uppercase;letter-spacing:2px;">Education</h2>
        <div style="display:grid;grid-template-columns:120px 1fr;gap:15px;font-size:14px;">
          <div style="color:#95a5a6;font-weight:300;">2011 – 2015</div>
          <div>
            <div style="color:#2c3e50;font-weight:400;">Bachelor of Science in Computer Science</div>
            <div style="color:#7f8c8d;font-weight:300;">Stanford University</div>
            <div style="color:#95a5a6;font-weight:300;font-size:13px;">GPA: 3.8/4.0</div>
          </div>
        </div>
      </section>

      <!-- Minimalist Publications -->
      <section style="margin-bottom:45px;">
        <h2 style="margin:0 0 25px 0;font-size:16px;font-weight:600;color:#2c3e50;text-transform:uppercase;letter-spacing:2px;">Publications</h2>
        <div style="font-size:14px;color:#34495e;font-weight:300;line-height:1.8;">
          <p style="margin:0 0 10px 0;">"Microservices Architecture Patterns for High-Scale Systems" — <em>IEEE Software</em>, 2024</p>
          <p style="margin:0;">"Event-Driven Architecture in Practice" — <em>ACM Computing Surveys</em>, 2023</p>
        </div>
      </section>

      <!-- Minimalist Skills Summary -->
      <section>
        <h2 style="margin:0 0 25px 0;font-size:16px;font-weight:600;color:#2c3e50;text-transform:uppercase;letter-spacing:2px;">Skills</h2>
        <div style="display:grid;grid-template-columns:120px 1fr;gap:15px;font-size:14px;">
          <div style="color:#7f8c8d;font-weight:400;">Architecture</div>
          <div style="color:#34495e;font-weight:300;">Microservices, Event-Driven Architecture, Domain-Driven Design, CQRS</div>
          <div style="color:#7f8c8d;font-weight:400;">Leadership</div>
          <div style="color:#34495e;font-weight:300;">Technical Strategy, Team Management, Mentoring, Code Review</div>
        </div>
      </section>

      <!-- Minimalist Footer -->
      <div style="margin-top:60px;padding-top:20px;border-top:1px solid #ecf0f1;text-align:center;">
        <div style="font-size:11px;color:#bdc3c7;font-weight:300;">Last updated: 19 Aug 2025</div>
      </div>
    </div>
  </main>
</body>
</html>"""
    },
    {
        "id": "t12-vanguard",
        "name": "Vanguard Executive",
        "role_category": "non-technical",
        "has_image_slot": True,
        "html": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>CV – Victoria Sterling</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body style="margin:0;background:#f8f9fa;color:#212529;font-family:'Playfair Display',Georgia,serif;line-height:1.6;">
  <main style="max-width:210mm;margin:15px auto;background:#ffffff;box-shadow:0 12px 48px rgba(0,0,0,.15);">
    <!-- Vanguard Header -->
    <header style="background:linear-gradient(135deg,#2c3e50 0%,#34495e 100%);color:#ffffff;padding:50px;position:relative;overflow:hidden;">
      <div style="position:absolute;top:-100px;right:-100px;width:300px;height:300px;border:2px solid rgba(255,255,255,0.1);border-radius:50%;"></div>
      <div style="position:absolute;bottom:-50px;left:-50px;width:200px;height:200px;background:rgba(255,255,255,0.05);border-radius:50%;"></div>
      <div style="position:relative;z-index:2;display:flex;align-items:center;gap:40px;">
        <div style="flex-shrink:0;">
          <img src="{{PHOTO_URL}}" alt="Victoria Sterling" style="width:160px;height:160px;border-radius:20px;border:6px solid #ffffff;box-shadow:0 12px 36px rgba(0,0,0,0.3);" />
        </div>
        <div style="flex:1;">
          <h1 style="margin:0 0 12px 0;font-size:42px;font-weight:400;letter-spacing:1px;">Victoria Sterling</h1>
          <p style="margin:0 0 20px 0;font-size:22px;opacity:0.9;font-style:italic;">Chief Financial Officer</p>
          <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px;font-size:15px;opacity:0.9;">
            <div style="display:flex;align-items:center;gap:10px;">
              <span style="font-size:18px;">📧</span>
              <span>victoria.sterling@email.com</span>
            </div>
            <div style="display:flex;align-items:center;gap:10px;">
              <span style="font-size:18px;">📱</span>
              <span>+1 (555) 123-4567</span>
            </div>
            <div style="display:flex;align-items:center;gap:10px;">
              <span style="font-size:18px;">🔗</span>
              <span>linkedin.com/in/victoriastarling</span>
            </div>
            <div style="display:flex;align-items:center;gap:10px;">
              <span style="font-size:18px;">📍</span>
              <span>New York, NY</span>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div style="padding:50px;">
      <!-- Executive Profile -->
      <section style="margin-bottom:45px;">
        <h2 style="margin:0 0 25px 0;font-size:32px;font-weight:400;color:#2c3e50;text-align:center;position:relative;">
          Executive Profile
          <div style="position:absolute;bottom:-10px;left:50%;transform:translateX(-50%);width:100px;height:4px;background:linear-gradient(90deg,#2c3e50,#34495e);border-radius:2px;"></div>
        </h2>
        <div style="background:#f8f9fa;padding:35px;border-radius:15px;border:1px solid #e9ecef;position:relative;">
          <div style="position:absolute;top:20px;right:25px;font-size:48px;opacity:0.1;color:#2c3e50;">"</div>
          <p style="margin:0;font-size:17px;text-align:justify;line-height:1.8;color:#495057;font-style:italic;">
            Visionary CFO with 12+ years of executive experience driving financial strategy and operational excellence for Fortune 100 companies. Proven expertise in capital markets, M&A transactions, and digital transformation initiatives. Led financial operations through successful IPO and multiple acquisitions totaling $2.5B in value. Recognized thought leader in sustainable finance and ESG reporting.
          </p>
        </div>
      </section>

      <!-- Key Achievements -->
      <section style="margin-bottom:45px;">
        <h2 style="margin:0 0 30px 0;font-size:32px;font-weight:400;color:#2c3e50;text-align:center;position:relative;">
          Key Achievements
          <div style="position:absolute;bottom:-10px;left:50%;transform:translateX(-50%);width:100px;height:4px;background:linear-gradient(90deg,#2c3e50,#34495e);border-radius:2px;"></div>
        </h2>
        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:30px;">
          <div style="background:#ffffff;padding:30px;border-radius:15px;box-shadow:0 8px 32px rgba(0,0,0,0.08);border-left:6px solid #27ae60;text-align:center;">
            <div style="font-size:36px;font-weight:700;color:#27ae60;margin-bottom:10px;">$2.5B</div>
            <h4 style="margin:0 0 8px 0;font-size:16px;font-weight:600;color:#2c3e50;">M&A Transactions</h4>
            <p style="margin:0;font-size:13px;color:#6c757d;">Led strategic acquisitions and partnerships</p>
          </div>
          <div style="background:#ffffff;padding:30px;border-radius:15px;box-shadow:0 8px 32px rgba(0,0,0,0.08);border-left:6px solid #3498db;text-align:center;">
            <div style="font-size:36px;font-weight:700;color:#3498db;margin-bottom:10px;">45%</div>
            <h4 style="margin:0 0 8px 0;font-size:16px;font-weight:600;color:#2c3e50;">Cost Reduction</h4>
            <p style="margin:0;font-size:13px;color:#6c757d;">Operational efficiency improvements</p>
          </div>
          <div style="background:#ffffff;padding:30px;border-radius:15px;box-shadow:0 8px 32px rgba(0,0,0,0.08);border-left:6px solid #e74c3c;text-align:center;">
            <div style="font-size:36px;font-weight:700;color:#e74c3c;margin-bottom:10px;">IPO</div>
            <h4 style="margin:0 0 8px 0;font-size:16px;font-weight:600;color:#2c3e50;">Public Offering</h4>
            <p style="margin:0;font-size:13px;color:#6c757d;">$800M successful market debut</p>
          </div>
          <div style="background:#ffffff;padding:30px;border-radius:15px;box-shadow:0 8px 32px rgba(0,0,0,0.08);border-left:6px solid #9b59b6;text-align:center;">
            <div style="font-size:36px;font-weight:700;color:#9b59b6;margin-bottom:10px;">AAA</div>
            <h4 style="margin:0 0 8px 0;font-size:16px;font-weight:600;color:#2c3e50;">Credit Rating</h4>
            <p style="margin:0;font-size:13px;color:#6c757d;">Achieved highest corporate rating</p>
          </div>
        </div>
      </section>

      <!-- Professional Experience -->
      <section style="margin-bottom:45px;">
        <h2 style="margin:0 0 35px 0;font-size:32px;font-weight:400;color:#2c3e50;text-align:center;position:relative;">
          Professional Experience
          <div style="position:absolute;bottom:-10px;left:50%;transform:translateX(-50%);width:100px;height:4px;background:linear-gradient(90deg,#2c3e50,#34495e);border-radius:2px;"></div>
        </h2>
        
        <div style="margin-bottom:40px;background:#ffffff;padding:35px;border-radius:15px;box-shadow:0 8px 32px rgba(0,0,0,0.08);border:1px solid #e9ecef;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:20px;">
            <div>
              <h3 style="margin:0 0 8px 0;font-size:24px;font-weight:600;color:#2c3e50;">Chief Financial Officer</h3>
              <p style="margin:0;font-size:18px;color:#6c757d;font-style:italic;">GlobalTech Enterprises</p>
            </div>
            <div style="text-align:right;">
              <span style="background:#2c3e50;color:#ffffff;padding:8px 20px;border-radius:25px;font-size:14px;font-weight:500;">2019 – Present</span>
              <p style="margin:8px 0 0 0;font-size:13px;color:#6c757d;">New York, NY</p>
            </div>
          </div>
          <ul style="margin:0;padding-left:25px;font-size:15px;color:#495057;line-height:1.8;">
            <li style="margin-bottom:10px;">Oversee financial operations for $3.2B revenue technology conglomerate with 8,000+ employees globally</li>
            <li style="margin-bottom:10px;">Led successful IPO raising $800M in capital and achieving 35% first-day stock price appreciation</li>
            <li style="margin-bottom:10px;">Executed 5 strategic acquisitions totaling $1.8B, expanding market presence across 3 new verticals</li>
            <li style="margin-bottom:10px;">Implemented enterprise-wide ERP system reducing financial close time from 15 to 5 days</li>
            <li>Established ESG reporting framework achieving top-tier sustainability ratings from major agencies</li>
          </ul>
        </div>

        <div style="margin-bottom:40px;background:#ffffff;padding:35px;border-radius:15px;box-shadow:0 8px 32px rgba(0,0,0,0.08);border:1px solid #e9ecef;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:20px;">
            <div>
              <h3 style="margin:0 0 8px 0;font-size:24px;font-weight:600;color:#2c3e50;">Vice President of Finance</h3>
              <p style="margin:0;font-size:18px;color:#6c757d;font-style:italic;">InnovateCorp</p>
            </div>
            <div style="text-align:right;">
              <span style="background:#6c757d;color:#ffffff;padding:8px 20px;border-radius:25px;font-size:14px;font-weight:500;">2015 – 2019</span>
              <p style="margin:8px 0 0 0;font-size:13px;color:#6c757d;">San Francisco, CA</p>
            </div>
          </div>
          <ul style="margin:0;padding-left:25px;font-size:15px;color:#495057;line-height:1.8;">
            <li style="margin-bottom:10px;">Managed financial planning and analysis for $1.5B revenue division</li>
            <li style="margin-bottom:10px;">Led due diligence for $700M acquisition of strategic competitor</li>
            <li style="margin-bottom:10px;">Restructured debt portfolio saving $25M annually in interest expenses</li>
            <li>Built financial modeling framework for new product line valuations</li>
          </ul>
        </div>

        <div style="background:#ffffff;padding:35px;border-radius:15px;box-shadow:0 8px 32px rgba(0,0,0,0.08);border:1px solid #e9ecef;">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:20px;">
            <div>
              <h3 style="margin:0 0 8px 0;font-size:24px;font-weight:600;color:#2c3e50;">Senior Finance Director</h3>
              <p style="margin:0;font-size:18px;color:#6c757d;font-style:italic;">Strategic Capital Partners</p>
            </div>
            <div style="text-align:right;">
              <span style="background:#6c757d;color:#ffffff;padding:8px 20px;border-radius:25px;font-size:14px;font-weight:500;">2012 – 2015</span>
              <p style="margin:8px 0 0 0;font-size:13px;color:#6c757d;">Boston, MA</p>
            </div>
          </div>
          <ul style="margin:0;padding-left:25px;font-size:15px;color:#495057;line-height:1.8;">
            <li style="margin-bottom:10px;">Provided financial advisory services to portfolio companies valued at $5B+</li>
            <li style="margin-bottom:10px;">Developed investment thesis and financial models for growth equity investments</li>
            <li>Supported 3 successful exits generating 4x average return for investors</li>
          </ul>
        </div>
      </section>

      <!-- Board & Advisory Positions -->
      <section style="margin-bottom:45px;">
        <h2 style="margin:0 0 30px 0;font-size:32px;font-weight:400;color:#2c3e50;text-align:center;position:relative;">
          Board & Advisory Positions
          <div style="position:absolute;bottom:-10px;left:50%;transform:translateX(-50%);width:100px;height:4px;background:linear-gradient(90deg,#2c3e50,#34495e);border-radius:2px;"></div>
        </h2>
        <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:25px;">
          <div style="background:#f8f9fa;padding:25px;border-radius:15px;border-left:5px solid #2c3e50;">
            <h4 style="margin:0 0 8px 0;font-size:18px;font-weight:600;color:#2c3e50;">Board of Directors</h4>
            <p style="margin:0 0 5px 0;font-size:15px;color:#6c757d;">FinTech Innovation Fund</p>
            <p style="margin:0;font-size:13px;color:#adb5bd;">2021 – Present</p>
          </div>
          <div style="background:#f8f9fa;padding:25px;border-radius:15px;border-left:5px solid #2c3e50;">
            <h4 style="margin:0 0 8px 0;font-size:18px;font-weight:600;color:#2c3e50;">Advisory Board Member</h4>
            <p style="margin:0 0 5px 0;font-size:15px;color:#6c757d;">Sustainable Finance Institute</p>
            <p style="margin:0;font-size:13px;color:#adb5bd;">2020 – Present</p>
          </div>
          <div style="background:#f8f9fa;padding:25px;border-radius:15px;border-left:5px solid #2c3e50;">
            <h4 style="margin:0 0 8px 0;font-size:18px;font-weight:600;color:#2c3e50;">Audit Committee Chair</h4>
            <p style="margin:0 0 5px 0;font-size:15px;color:#6c757d;">TechStart Accelerator</p>
            <p style="margin:0;font-size:13px;color:#adb5bd;">2019 – Present</p>
          </div>
          <div style="background:#f8f9fa;padding:25px;border-radius:15px;border-left:5px solid #2c3e50;">
            <h4 style="margin:0 0 8px 0;font-size:18px;font-weight:600;color:#2c3e50;">Strategic Advisor</h4>
            <p style="margin:0 0 5px 0;font-size:15px;color:#6c757d;">Women in Finance Network</p>
            <p style="margin:0;font-size:13px;color:#adb5bd;">2018 – Present</p>
          </div>
        </div>
      </section>

      <!-- Education & Certifications -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:45px;margin-bottom:45px;">
        <section>
          <h2 style="margin:0 0 25px 0;font-size:28px;font-weight:400;color:#2c3e50;">Education</h2>
          <div style="background:#f8f9fa;padding:30px;border-radius:15px;">
            <div style="margin-bottom:25px;">
              <h4 style="margin:0 0 8px 0;font-size:18px;font-weight:600;color:#2c3e50;">Master of Business Administration</h4>
              <p style="margin:0 0 5px 0;font-size:15px;color:#6c757d;">Wharton School, University of Pennsylvania</p>
              <p style="margin:0;font-size:13px;color:#adb5bd;">2008 – 2010 | Summa Cum Laude</p>
            </div>
            <div>
              <h4 style="margin:0 0 8px 0;font-size:18px;font-weight:600;color:#2c3e50;">Bachelor of Science in Finance</h4>
              <p style="margin:0 0 5px 0;font-size:15px;color:#6c757d;">New York University Stern</p>
              <p style="margin:0;font-size:13px;color:#adb5bd;">2004 – 2008 | Magna Cum Laude</p>
            </div>
          </div>
        </section>

        <section>
          <h2 style="margin:0 0 25px 0;font-size:28px;font-weight:400;color:#2c3e50;">Certifications</h2>
          <div style="background:#f8f9fa;padding:30px;border-radius:15px;font-size:15px;">
            <div style="margin-bottom:20px;">
              <h4 style="margin:0 0 5px 0;font-size:16px;font-weight:600;color:#2c3e50;">Certified Public Accountant (CPA)</h4>
              <p style="margin:0;color:#6c757d;">New York State Board of Accountancy</p>
            </div>
            <div style="margin-bottom:20px;">
              <h4 style="margin:0 0 5px 0;font-size:16px;font-weight:600;color:#2c3e50;">Chartered Financial Analyst (CFA)</h4>
              <p style="margin:0;color:#6c757d;">CFA Institute</p>
            </div>
            <div>
              <h4 style="margin:0 0 5px 0;font-size:16px;font-weight:600;color:#2c3e50;">Financial Risk Manager (FRM)</h4>
              <p style="margin:0;color:#6c757d;">Global Association of Risk Professionals</p>
            </div>
          </div>
        </section>
      </div>

      <!-- Projects & Publications -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:45px;margin-bottom:45px;">
        <section>
          <h2 style="margin:0 0 20px 0;font-size:28px;font-weight:400;color:#2c3e50;">Featured Projects</h2>
          <div style="margin-bottom:20px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
              <h3 style="margin:0;font-size:18px;font-weight:600;color:#2c3e50;">Digital Finance Transformation</h3>
              <a href="https://case-study-digital-finance.com" style="color:#6c757d;text-decoration:none;font-size:13px;">Case Study</a>
            </div>
            <p style="margin:0;font-size:14px;color:#495057;line-height:1.7;">
              Led enterprise-wide digital transformation of financial processes, implementing AI-powered forecasting and automated reporting systems. Reduced manual work by 70% and improved forecast accuracy by 35%.
            </p>
          </div>
        </section>

        <section>
          <h2 style="margin:0 0 20px 0;font-size:28px;font-weight:400;color:#2c3e50;">Publications</h2>
          <div style="font-size:14px;color:#495057;line-height:1.8;">
            <p style="margin:0 0 12px 0;">"The Future of Corporate Finance: AI and Automation" - <em>Harvard Business Review</em>, April 2024</p>
            <p style="margin:0 0 12px 0;">"ESG Reporting: From Compliance to Competitive Advantage" - <em>CFO Magazine</em>, January 2024</p>
            <p style="margin:0;">"Digital Transformation in Finance: A Practitioner's Guide" - <em>Financial Executive</em>, September 2023</p>
          </div>
        </section>
      </div>

      <!-- Skills -->
      <section>
        <h2 style="margin:0 0 25px 0;font-size:28px;font-weight:400;color:#2c3e50;text-align:center;">Skills</h2>
        <div style="display:grid;grid-template-columns:150px 1fr;gap:20px;font-size:15px;max-width:900px;margin:0 auto;">
          <div style="font-weight:600;color:#2c3e50;">Financial Strategy</div>
          <div style="color:#495057;">Capital Markets, M&A, IPO Management, Financial Planning & Analysis, Risk Management</div>
          <div style="font-weight:600;color:#2c3e50;">Leadership</div>
          <div style="color:#495057;">Executive Management, Board Relations, Stakeholder Communication, Team Development</div>
          <div style="font-weight:600;color:#2c3e50;">Technology</div>
          <div style="color:#495057;">ERP Systems, Financial Modeling, Data Analytics, Process Automation, ESG Reporting</div>
        </div>
      </section>

      <!-- Executive Footer -->
      <div style="text-align:center;margin-top:60px;padding-top:35px;border-top:4px solid #2c3e50;">
        <div style="font-size:13px;color:#6c757d;margin-bottom:20px;">Last updated: 19 Aug 2025</div>
        <div style="display:flex;justify-content:center;gap:15px;">
          <div style="width:40px;height:3px;background:#2c3e50;border-radius:2px;"></div>
          <div style="width:40px;height:3px;background:#34495e;border-radius:2px;"></div>
          <div style="width:40px;height:3px;background:#2c3e50;border-radius:2px;"></div>
        </div>
      </div>
    </div>
  </main>
</body>
</html>"""
    }
]

def get_all_templates():
    """Return all available templates"""
    return TEMPLATES

def get_template_by_id(template_id):
    """Get a specific template by ID"""
    for template in TEMPLATES:
        if template["id"] == template_id:
            return template
    return None

def get_template_preview(template_id):
    """Get template HTML for preview"""
    template = get_template_by_id(template_id)
    if template:
        return template["html"]
    return None

def get_template_with_content(template_id):
    """Get template HTML with content (same as preview for now)"""
    return get_template_preview(template_id)

def get_templates_by_category(category):
    """Get templates filtered by role category"""
    return [t for t in TEMPLATES if t["role_category"] == category]
