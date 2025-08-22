import logging
from llm_client import LLMClient

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CareerAdvisor:
    """
    Strict, hosted-LLM-only advisor.
    All methods call LLMClient.chat(..., require_hosted=True).
    """

    def __init__(self):
        self.llm = LLMClient()

    # ---------- General Q&A (Career Guide) ----------
    def ask(self, question: str) -> str:
        system = (
            "You are an expert career coach for AI/ML and software roles. "
            "Answer concisely with action-focused bullet points and concrete steps. "
            "Prefer checklists, examples, and short templates over long prose."
        )
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": question.strip()},
        ]
        return self.llm.chat(messages, temperature=0.5, max_tokens=1400, require_hosted=True)

    # ---------- Resume Analyzer ----------
    def analyze_resume_text(self, resume_text: str) -> str:
        system = (
            "You are a precise resume reviewer for AI/ML, data, and SWE roles. "
            "Return only Markdown with short bullets, concrete metrics, and ATS-aware keywords."
        )
        prompt = f"""
Review the resume content below.

<RESUME>
{resume_text[:20000]}
</RESUME>

Return these sections:

### Summary
- 2–3 lines on profile and seniority.

### Strengths
- 4–6 bullets focused on impact, scale, and tech.

### Gaps / Risks
- 4–6 bullets with clear fixes (what to add/show/quantify).

### ATS Keywords to Add
- Comma-separated role-specific skills/tools.

### 3 Impact Edits
- Rewrite three weak bullets with quantified results (Before → After).
"""
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ]
        return self.llm.chat(messages, temperature=0.4, max_tokens=1600, require_hosted=True)

    # ---------- Interview Prep (technical → DSA only) ----------
    def interview_prep_dsa(self, role: str, seniority: str, company_type: str) -> str:
        prompt = f"""
You are an expert coding interview coach.
Create a STRICTLY DSA/CODING interview prep roadmap (no behavioral/system design unless essential).

Context:
- Target Role: {role}
- Seniority Level: {seniority}
- Company Type: {company_type}

Requirements:
1) Output FORMAT:
   - Section A: "Readiness Check"
   - Section B: "Core Data Structures"
   - Section C: "Core Algorithms"
   - Section D: "Company-Style Focus"
   - Section E: "7–14–28 Day Plan"
   - Section F: "Validation"
2) Keep it role-aware and seniority-appropriate.
3) Constrain to coding/DSA only. No filler.
Return only Markdown.
"""
        messages = [
            {"role": "system", "content": "You are a rigorous coding interview coach. Produce only coding/DSA content."},
            {"role": "user", "content": prompt},
        ]
        return self.llm.chat(messages, temperature=0.5, max_tokens=2200, require_hosted=True)

    # ---------- Interview Prep (non-technical → no DSA) ----------
    def interview_prep_general(self, role: str, seniority: str, company_type: str) -> str:
        prompt = f"""
Act as a senior interview coach. Build an INTERVIEW PREP GUIDE with the sections below.

Context:
- Target Role: {role}
- Seniority Level: {seniority}
- Company Type: {company_type}

Sections (use these exact headings):
### Role Understanding
- What the role values at this seniority and company type.

### Core Competencies
- Skills and artifacts interviewers probe (no coding/DSA).

### Behavioral & Situational
- Story patterns to prepare, with STAR prompts.

### Case/Exercise Prep
- If relevant, describe the kind of case/exercise and how to practice.

### 30-60-90 Narrative
- A crisp plan aligned to {company_type} context.

### 14-Day Plan
- Concrete daily actions to get interview-ready.

Rules:
- No DSA content.
- Short, action-focused bullets; avoid long paragraphs.
- Tailor all advice to the 3 inputs above.
Return only Markdown.
"""
        messages = [
            {"role": "system", "content": "You are a pragmatic, concise interview coach."},
            {"role": "user", "content": prompt},
        ]
        return self.llm.chat(messages, temperature=0.5, max_tokens=2000, require_hosted=True)

    # ---------- Role Roadmap (stage-wise, NOT hardcoded) ----------
    def stage_roadmap(self, role: str, seniority: str, company_type: str) -> str:
        """
        Generate a stage-wise learning/skills roadmap (Stages 1–7) in the same structure as the
        Data Scientist sample the user provided — but fully LLM-generated and tailored to inputs.
        """
        prompt = f"""
Create a STAGE-WISE roadmap for a candidate preparing for the role below.
It must follow EXACTLY these headings and order, with 4–6 concise bullets per sub-section:

📌 Stage 1: Foundations
- Mathematics/Statistics or other fundamentals (role-appropriate)
- Programming stack (role-appropriate)
- Data handling or domain basics (role-appropriate)

📌 Stage 2: Core Technical
- Supervised / primary techniques relevant to the role
- Unsupervised / secondary techniques (if applicable)
- Model evaluation / quality metrics for the role

📌 Stage 3: Advanced Skills
- Deepening into advanced tech used in {role}
- Big data / tooling, cloud (tailored to {company_type})
- Engineering basics needed to deliver in production

📌 Stage 4: Specialized Knowledge
- 3–4 specialty tracks (e.g., NLP, CV, Recommenders, Time Series) adapted to {role}

📌 Stage 5: Business & Soft Skills
- Communication / storytelling to non-technical stakeholders
- Role-aligned tooling for insights / decisions
- Domain knowledge examples (tailored to {company_type})

📌 Stage 6: Projects & Portfolio
- Project ideas with brief outcomes
- Public artifacts (Kaggle/GitHub/demos) that match {role}

📌 Stage 7: Career Prep
- Resume/LinkedIn tailoring for {role} at {company_type}
- Interview prep topics aligned to {seniority}
- Networking suggestions

Context:
- Target Role: {role}
- Seniority Level: {seniority}
- Company Type: {company_type}

Rules:
- Do NOT copy any content verbatim from prior examples.
- NO generic filler. Keep it concrete and role-specific.
- Output in Markdown only.
"""
        messages = [
            {"role": "system", "content": "You are a senior career mentor. Produce stage-wise roadmaps in crisp, actionable bullets."},
            {"role": "user", "content": prompt},
        ]
        return self.llm.chat(messages, temperature=0.5, max_tokens=2200, require_hosted=True)
