import os
import logging
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

def build_knowledge_base():
    """Build comprehensive knowledge base for career advisor"""
    logger.info("🚀 Starting knowledge base construction...")
    
    # Create directory structure
    directories = [
        "knowledge_base/job_descriptions",
        "knowledge_base/interview_guides", 
        "knowledge_base/career_roadmaps",
        "knowledge_base/resume_templates",
        "knowledge_base/skills_data",
        "knowledge_base/index"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        logger.info(f"📁 Created directory: {directory}")

    # Create comprehensive sample files
    create_comprehensive_sample_files()

    # Load documents from all directories
    loaders = [
        DirectoryLoader("knowledge_base/job_descriptions", glob="*.txt", loader_cls=TextLoader),
        DirectoryLoader("knowledge_base/interview_guides", glob="*.txt", loader_cls=TextLoader),
        DirectoryLoader("knowledge_base/career_roadmaps", glob="*.md", loader_cls=TextLoader),
        DirectoryLoader("knowledge_base/resume_templates", glob="*.txt", loader_cls=TextLoader),
        DirectoryLoader("knowledge_base/skills_data", glob="*.txt", loader_cls=TextLoader)
    ]

    docs = []
    for loader in loaders:
        try:
            if os.path.exists(loader.path):
                loaded_docs = loader.load()
                docs.extend(loaded_docs)
                logger.info(f"✅ Loaded {len(loaded_docs)} documents from {loader.path}")
        except Exception as e:
            logger.warning(f"⚠️ Warning loading from {loader.path}: {str(e)[:100]}...")

    if not docs:
        logger.error("❌ No documents found! Creating fallback documents...")
        docs = create_fallback_documents()

    logger.info(f"📚 Total documents loaded: {len(docs)}")

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(docs)
    logger.info(f"✂️ Split into {len(chunks)} chunks")

    # Initialize embeddings
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': False}
        )
        logger.info("🤖 Embeddings model loaded successfully")
    except Exception as e:
        logger.error(f"❌ Failed to load embeddings: {e}")
        raise

    # Create and save FAISS index
    try:
        logger.info("🔄 Creating FAISS index...")
        db = FAISS.from_documents(chunks, embeddings)
        db.save_local("knowledge_base/index")
        logger.info(f"✅ Knowledge base built successfully with {len(chunks)} chunks")
        
        # Test the index
        test_query = "software engineer skills"
        results = db.similarity_search(test_query, k=2)
        logger.info(f"🧪 Test query returned {len(results)} results")
        
    except Exception as e:
        logger.error(f"❌ Error creating FAISS index: {e}")
        raise

def create_comprehensive_sample_files():
    """Create comprehensive sample files for all career domains"""
    
    # Job Descriptions
    job_descriptions = {
        "software_engineer.txt": """=== SOFTWARE ENGINEER ===

ROLE OVERVIEW:
Software Engineers design, develop, and maintain software applications and systems. They work with various programming languages and technologies to create solutions that meet business requirements.

REQUIRED SKILLS:
- Programming Languages: Python, Java, JavaScript, C++, Go
- Web Technologies: HTML, CSS, React, Node.js, Angular
- Databases: SQL, PostgreSQL, MongoDB, Redis
- Cloud Platforms: AWS, Azure, Google Cloud Platform
- Version Control: Git, GitHub, GitLab
- DevOps: Docker, Kubernetes, CI/CD pipelines
- Testing: Unit testing, Integration testing, Test-driven development

RESPONSIBILITIES:
- Design and develop scalable software applications
- Write clean, maintainable, and efficient code
- Collaborate with cross-functional teams
- Participate in code reviews and pair programming
- Debug and troubleshoot software issues
- Implement security best practices
- Optimize application performance
- Document code and technical specifications

CAREER PROGRESSION:
Junior Developer → Software Engineer → Senior Engineer → Lead Engineer → Engineering Manager/Principal Engineer

SALARY RANGE:
- Entry Level: $60,000 - $80,000
- Mid Level: $80,000 - $120,000  
- Senior Level: $120,000 - $180,000+

INTERVIEW TOPICS:
- Data structures and algorithms
- System design and architecture
- Object-oriented programming principles
- Database design and optimization
- API design and RESTful services
""",
        
        "data_scientist.txt": """=== DATA SCIENTIST ===

ROLE OVERVIEW:
Data Scientists analyze complex data to extract insights and build predictive models that drive business decisions. They combine statistical analysis, machine learning, and domain expertise.

REQUIRED SKILLS:
- Programming: Python, R, SQL, Scala
- Machine Learning: scikit-learn, TensorFlow, PyTorch, Keras
- Data Manipulation: Pandas, NumPy, dplyr
- Visualization: Matplotlib, Seaborn, Plotly, Tableau, Power BI
- Statistics: Hypothesis testing, regression, time series analysis
- Big Data: Spark, Hadoop, Kafka
- Cloud: AWS SageMaker, Azure ML, Google AI Platform
- Databases: SQL, NoSQL, data warehousing

RESPONSIBILITIES:
- Collect, clean, and preprocess large datasets
- Perform exploratory data analysis
- Build and deploy machine learning models
- Create data visualizations and dashboards
- Communicate findings to stakeholders
- A/B testing and experimental design
- Collaborate with engineering teams for model deployment

CAREER PROGRESSION:
Data Analyst → Data Scientist → Senior Data Scientist → Principal Data Scientist → Chief Data Officer

SALARY RANGE:
- Entry Level: $70,000 - $95,000
- Mid Level: $95,000 - $140,000
- Senior Level: $140,000 - $200,000+

INTERVIEW TOPICS:
- Statistical concepts and hypothesis testing
- Machine learning algorithms and when to use them
- Data preprocessing and feature engineering
- Model evaluation and validation techniques
- SQL and database querying
""",

        "product_manager.txt": """=== PRODUCT MANAGER ===

ROLE OVERVIEW:
Product Managers drive product strategy, roadmap, and feature definition. They work cross-functionally to deliver products that meet customer needs and business objectives.

REQUIRED SKILLS:
- Strategic thinking and market analysis
- User experience and design thinking
- Data analysis and metrics interpretation
- Agile/Scrum methodologies
- Stakeholder management
- Technical understanding (not coding required)
- Communication and presentation skills
- Project management tools: Jira, Asana, Trello

RESPONSIBILITIES:
- Define product vision, strategy, and roadmap
- Gather and prioritize product requirements
- Work with engineering, design, and marketing teams
- Conduct market research and competitive analysis
- Analyze user feedback and usage data
- Manage product launches and go-to-market strategy
- Monitor product metrics and KPIs

CAREER PROGRESSION:
Associate PM → Product Manager → Senior PM → Principal PM → VP of Product → CPO

SALARY RANGE:
- Entry Level: $80,000 - $110,000
- Mid Level: $110,000 - $160,000
- Senior Level: $160,000 - $250,000+

INTERVIEW TOPICS:
- Product sense and case studies
- Analytical and problem-solving skills
- Technical understanding
- Leadership and communication
- Strategy and roadmap planning
"""
    }
    
    # Career Roadmaps
    career_roadmaps = {
        "software_engineering_roadmap.md": """# Software Engineering Career Roadmap

## Phase 1: Foundation (0-2 years)
### Technical Skills
- Master one programming language (Python/Java/JavaScript)
- Learn data structures and algorithms
- Understand basic computer science concepts
- Learn version control (Git)
- Basic web development (HTML, CSS, JavaScript)

### Practical Experience
- Build personal projects
- Contribute to open source
- Complete coding challenges
- Create a portfolio website

### Soft Skills
- Problem-solving methodology
- Basic debugging techniques
- Time management
- Communication skills

## Phase 2: Growth (2-4 years)
### Technical Skills
- Master additional programming languages
- Learn system design principles
- Database design and optimization
- API development and integration
- Testing frameworks and methodologies
- Cloud platforms (AWS/Azure/GCP)

### Practical Experience
- Work on team projects
- Mentor junior developers
- Lead small features or modules
- Participate in architectural decisions

### Soft Skills
- Code review skills
- Technical documentation
- Stakeholder communication
- Project planning

## Phase 3: Senior Level (4+ years)
### Technical Skills
- Advanced system design
- Performance optimization
- Security best practices
- DevOps and deployment strategies
- Emerging technologies

### Leadership Skills
- Technical leadership
- Mentoring and coaching
- Cross-functional collaboration
- Strategic thinking

### Career Paths
- Technical Track: Principal Engineer, Staff Engineer, Distinguished Engineer
- Management Track: Engineering Manager, Director of Engineering, VP Engineering
- Specialized Roles: Solutions Architect, DevOps Engineer, Security Engineer
""",

        "data_science_roadmap.md": """# Data Science Career Roadmap

## Phase 1: Foundation (0-1 year)
### Mathematical Foundation
- Statistics and probability
- Linear algebra basics
- Calculus fundamentals

### Programming Skills
- Python programming
- SQL for data querying
- Excel/Google Sheets proficiency

### Data Analysis
- Pandas for data manipulation
- NumPy for numerical computing
- Basic data visualization with Matplotlib

### Learning Resources
- Online courses (Coursera, edX, Udacity)
- Practice datasets (Kaggle, UCI ML Repository)
- Books: "Python for Data Analysis" by Wes McKinney

## Phase 2: Intermediate (1-2 years)
### Machine Learning
- Supervised learning algorithms
- Unsupervised learning techniques
- Model evaluation and validation
- Feature engineering

### Tools and Libraries
- scikit-learn for machine learning
- Advanced visualization (Seaborn, Plotly)
- Jupyter notebooks mastery
- Introduction to big data tools

### Practical Experience
- Kaggle competitions
- Personal data science projects
- Internships or entry-level positions

## Phase 3: Advanced (2+ years)
### Deep Learning
- Neural networks and deep learning
- TensorFlow or PyTorch
- Computer vision or NLP specialization

### Production Skills
- Model deployment and MLOps
- Cloud platforms (AWS SageMaker, Azure ML)
- Docker and containerization
- API development for models

### Specialization Areas
- Computer Vision
- Natural Language Processing
- Time Series Analysis
- Recommendation Systems
- Business Intelligence

### Career Advancement
- Lead data science projects
- Mentor junior data scientists
- Contribute to data strategy
- Present findings to executives
"""
    }
    
    # Interview Guides
    interview_guides = {
        "behavioral_interview_guide.txt": """=== BEHAVIORAL INTERVIEW GUIDE ===

STAR METHOD:
Situation - Context and background
Task - What you needed to accomplish
Action - Steps you took
Result - Outcome and impact

COMMON BEHAVIORAL QUESTIONS:

1. Tell me about yourself
- Keep it professional and relevant
- Highlight key experiences
- Connect to the role you're applying for

2. Why do you want this job?
- Research the company and role
- Show genuine interest
- Connect your goals with the position

3. Describe a challenging situation
- Choose a relevant professional example
- Focus on problem-solving process
- Highlight positive outcome

4. Tell me about a time you failed
- Show accountability and learning
- Explain what you learned
- Demonstrate growth mindset

5. How do you handle conflict?
- Show emotional intelligence
- Focus on resolution and collaboration
- Provide specific example

6. Where do you see yourself in 5 years?
- Align with career progression at company
- Show ambition but be realistic
- Demonstrate long-term thinking

PREPARATION TIPS:
- Prepare 5-7 stories using STAR method
- Practice out loud
- Research the company culture
- Prepare questions to ask interviewer
- Show enthusiasm and authenticity
""",

        "technical_interview_guide.txt": """=== TECHNICAL INTERVIEW GUIDE ===

CODING INTERVIEW PREPARATION:

Data Structures to Master:
- Arrays and Strings
- Linked Lists
- Stacks and Queues
- Trees and Binary Search Trees
- Graphs
- Hash Tables
- Heaps

Algorithm Patterns:
- Two Pointers
- Sliding Window
- Binary Search
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Dynamic Programming
- Recursion and Backtracking

SYSTEM DESIGN INTERVIEW:

Key Concepts:
- Scalability and Load Balancing
- Database Design (SQL vs NoSQL)
- Caching Strategies
- Microservices Architecture
- API Design
- Security Considerations

Common System Design Questions:
- Design a URL shortener (like bit.ly)
- Design a social media feed
- Design a chat application
- Design a ride-sharing service
- Design a video streaming platform

PROBLEM-SOLVING APPROACH:
1. Clarify requirements and constraints
2. Think through examples and edge cases
3. Discuss approach before coding
4. Write clean, readable code
5. Test your solution
6. Discuss optimizations

INTERVIEW TIPS:
- Think out loud
- Ask clarifying questions
- Start with brute force, then optimize
- Consider edge cases
- Communicate clearly
- Stay calm under pressure
"""
    }
    
    # Resume Templates
    resume_templates = {
        "software_engineer_resume_template.txt": """=== SOFTWARE ENGINEER RESUME TEMPLATE ===

[Your Name]
[Phone] | [Email] | [LinkedIn] | [GitHub] | [Location]

PROFESSIONAL SUMMARY
Results-driven Software Engineer with [X] years of experience developing scalable web applications and systems. Expertise in [primary technologies] with a strong foundation in [key areas]. Passionate about clean code, best practices, and continuous learning.

TECHNICAL SKILLS
• Programming Languages: [e.g., Python, JavaScript, Java, C++]
• Web Technologies: [e.g., React, Node.js, HTML5, CSS3]
• Databases: [e.g., PostgreSQL, MongoDB, Redis]
• Cloud & DevOps: [e.g., AWS, Docker, Kubernetes, Jenkins]
• Tools & Frameworks: [e.g., Git, Jest, Flask, Django]

PROFESSIONAL EXPERIENCE

[Job Title] | [Company Name] | [Location] | [Dates]
• [Specific achievement with metrics, e.g., "Improved API response time by 40% by implementing caching strategies"]
• [Technical contribution, e.g., "Developed and deployed microservices handling 100K+ daily requests"]
• [Leadership/collaboration example, e.g., "Led code reviews for team of 5 developers, improving code quality"]
• [Problem-solving example with impact]

[Previous Job Title] | [Company Name] | [Location] | [Dates]
• [Achievement with quantifiable result]
• [Technical skill demonstration]
• [Collaboration or leadership example]

PROJECTS
[Project Name] | [Technologies Used] | [Date]
• [Brief description of project and your role]
• [Key technical achievements or challenges overcome]
• [Link to GitHub repo or live demo if available]

EDUCATION
[Degree] in [Field] | [University Name] | [Location] | [Year]
• Relevant coursework: [List 3-4 relevant courses]
• GPA: [If 3.5 or higher]

CERTIFICATIONS (if applicable)
• [Certification Name] | [Issuing Organization] | [Date]
""",

        "data_scientist_resume_template.txt": """=== DATA SCIENTIST RESUME TEMPLATE ===

[Your Name]
[Phone] | [Email] | [LinkedIn] | [GitHub] | [Portfolio] | [Location]

PROFESSIONAL SUMMARY
Data Scientist with [X] years of experience extracting insights from complex datasets and building machine learning models. Expertise in [key skills] with proven track record of driving business impact through data-driven solutions.

TECHNICAL SKILLS
• Programming: Python, R, SQL, [other languages]
• Machine Learning: scikit-learn, TensorFlow, PyTorch, XGBoost
• Data Analysis: Pandas, NumPy, SciPy, Statsmodels
• Visualization: Matplotlib, Seaborn, Plotly, Tableau, Power BI
• Big Data: Spark, Hadoop, [cloud platforms]
• Databases: PostgreSQL, MongoDB, [data warehouses]

PROFESSIONAL EXPERIENCE

[Job Title] | [Company Name] | [Location] | [Dates]
• [Quantified business impact, e.g., "Increased revenue by $2M through predictive modeling"]
• [Technical achievement, e.g., "Built recommendation system improving user engagement by 25%"]
• [Data pipeline or infrastructure work]
• [Stakeholder communication example]

PROJECTS
[Project Name] | [Technologies] | [Date]
• [Project description and business problem solved]
• [Technical approach and methods used]
• [Results and impact achieved]

EDUCATION
[Degree] in [Field] | [University] | [Year]
• Relevant coursework: Statistics, Machine Learning, Data Mining
"""
    }
    
    # Skills Data
    skills_data = {
        "programming_skills.txt": """=== PROGRAMMING SKILLS DATABASE ===

PYTHON:
- Beginner: Basic syntax, variables, control structures, functions
- Intermediate: OOP, file handling, libraries (requests, json), exception handling
- Advanced: Decorators, generators, context managers, metaclasses, async programming
- Expert: Performance optimization, memory management, custom C extensions

JAVASCRIPT:
- Beginner: ES6 syntax, DOM manipulation, event handling, basic async
- Intermediate: Promises, closures, prototypes, modules, npm packages
- Advanced: React/Vue/Angular, Node.js, webpack, testing frameworks
- Expert: Performance optimization, advanced patterns, full-stack architecture

SQL:
- Beginner: SELECT, INSERT, UPDATE, DELETE, basic joins
- Intermediate: Complex joins, subqueries, window functions, indexes
- Advanced: Query optimization, stored procedures, triggers, performance tuning
- Expert: Database design, advanced analytics, query plan analysis

JAVA:
- Beginner: OOP basics, collections, exception handling
- Intermediate: Streams, lambdas, concurrency basics, Maven/Gradle
- Advanced: Spring framework, JVM tuning, design patterns
- Expert: Microservices, distributed systems, performance optimization
""",

        "soft_skills.txt": """=== SOFT SKILLS DATABASE ===

COMMUNICATION:
- Written: Technical documentation, email etiquette, proposal writing
- Verbal: Presentations, meetings, technical explanations to non-technical audiences
- Active listening: Understanding requirements, feedback incorporation
- Cross-cultural: Working with diverse, global teams

LEADERSHIP:
- Team leadership: Mentoring, coaching, delegation
- Project leadership: Planning, coordination, risk management
- Technical leadership: Architecture decisions, code reviews, best practices
- Thought leadership: Innovation, industry expertise, knowledge sharing

PROBLEM-SOLVING:
- Analytical thinking: Breaking down complex problems
- Creative solutions: Innovative approaches, out-of-the-box thinking
- Debugging: Systematic troubleshooting, root cause analysis
- Decision making: Evaluating options, risk assessment

TIME MANAGEMENT:
- Prioritization: Urgent vs important, impact assessment
- Planning: Sprint planning, milestone setting, resource allocation
- Productivity: Focus techniques, distraction management
- Work-life balance: Sustainable pace, stress management
"""
    }
    
    # Write all files
    all_files = {
        **{f"knowledge_base/job_descriptions/{k}": v for k, v in job_descriptions.items()},
        **{f"knowledge_base/career_roadmaps/{k}": v for k, v in career_roadmaps.items()},
        **{f"knowledge_base/interview_guides/{k}": v for k, v in interview_guides.items()},
        **{f"knowledge_base/resume_templates/{k}": v for k, v in resume_templates.items()},
        **{f"knowledge_base/skills_data/{k}": v for k, v in skills_data.items()}
    }
    
    for file_path, content in all_files.items():
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                logger.info(f"📝 Created: {file_path}")
        except Exception as e:
            logger.error(f"❌ Failed to create {file_path}: {e}")

def create_fallback_documents():
    """Create fallback documents if file loading fails"""
    return [
        Document(
            page_content="Software engineering requires programming skills in languages like Python, Java, JavaScript. Key concepts include algorithms, data structures, system design, and software architecture. Career progression typically goes from junior to senior to lead engineer.",
            metadata={"source": "software_engineering_fallback", "type": "career_info"}
        ),
        Document(
            page_content="Data science involves statistics, machine learning, and programming. Popular tools include Python, R, SQL, pandas, scikit-learn. Career path includes data analyst, data scientist, senior data scientist, and principal data scientist roles.",
            metadata={"source": "data_science_fallback", "type": "career_info"}
        ),
        Document(
            page_content="Resume best practices include quantifying achievements, using action verbs, optimizing for ATS systems, and tailoring content to specific roles. Keep it concise, professional, and error-free.",
            metadata={"source": "resume_tips_fallback", "type": "resume_advice"}
        ),
        Document(
            page_content="Interview preparation should include behavioral questions using STAR method, technical questions relevant to the role, and company research. Practice coding problems and system design for technical roles.",
            metadata={"source": "interview_prep_fallback", "type": "interview_advice"}
        ),
        Document(
            page_content="LinkedIn optimization includes professional headline, compelling summary, complete profile sections, regular posting, networking, and keyword optimization for discoverability.",
            metadata={"source": "linkedin_tips_fallback", "type": "linkedin_advice"}
        )
    ]

if __name__ == "__main__":
    try:
        build_knowledge_base()
        logger.info("🎉 Knowledge base construction completed successfully!")
    except Exception as e:
        logger.error(f"💥 Knowledge base construction failed: {e}")
        raise