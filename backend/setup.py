#!/usr/bin/env python3
"""
CVCompass AI Setup Script
Ensures all dependencies and directories are properly configured
"""

import os
import sys
import subprocess
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def create_directories():
    """Create necessary directories"""
    directories = [
        "data",
        "exports",
        "user_resumes",
        "saved_advice",
        "saved_interviews",
        "outputs/parsed_resumes",
        "knowledge_base/job_descriptions",
        "knowledge_base/interview_guides",
        "knowledge_base/career_roadmaps",
        "knowledge_base/resume_templates",
        "knowledge_base/skills_data",
        "knowledge_base/index",
    ]
    logger.info("📁 Creating directory structure...")
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        logger.info(f"✅ Created: {directory}")
    logger.info("📁 Directory structure ready!")

def check_python_version():
    """Check Python version compatibility"""
    logger.info("🐍 Checking Python version...")
    if sys.version_info < (3, 8):
        logger.error("❌ Python 3.8 or higher is required")
        sys.exit(1)
    logger.info(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} is compatible")

def install_requirements():
    """Install required packages"""
    logger.info("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        logger.info("✅ Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Failed to install requirements: {e}")
        logger.info("💡 Try: pip install -r requirements.txt")

def create_env_template():
    """Create .env template if it doesn't exist"""
    logger.info("🔧 Checking environment configuration...")
    env_template = """# CVCompass AI Environment Configuration
# Add your API keys below and rename this file to .env

# Primary LLM Service (Recommended)
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL=openrouter/meta-llama/llama-3.1-8b-instruct:free

# Fallback LLM Service (Optional)
HF_TOKEN=your_huggingface_token_here
HF_MODEL=HuggingFaceH4/zephyr-7b-beta

# Optional: For advanced features
GOOGLE_API_KEY=your_google_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
"""
    env_file = Path(".env")
    env_example = Path(".env.example")
    if not env_file.exists():
        if not env_example.exists():
            with open(env_example, "w") as f:
                f.write(env_template)
            logger.info("✅ Created .env.example template")
        logger.warning("⚠️ No .env file found")
        logger.info("📝 Copy .env.example to .env and add your API keys")
        logger.info("🔗 Get OpenRouter key: https://openrouter.ai/keys")
    else:
        logger.info("✅ Environment file found")

def check_api_keys():
    """Check if API keys are configured"""
    logger.info("🔑 Checking API configuration...")
    from dotenv import load_dotenv
    load_dotenv()
    openrouter_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    hf_token = os.getenv("HF_TOKEN", "").strip()
    if openrouter_key and openrouter_key != "your_openrouter_api_key_here":
        logger.info("✅ OpenRouter API key configured")
        return True
    elif hf_token and hf_token != "your_huggingface_token_here":
        logger.info("✅ Hugging Face token configured")
        return True
    else:
        logger.warning("⚠️ No API keys configured - running in demo mode")
        logger.info("💡 Add OPENROUTER_API_KEY to .env for full functionality")
        return False

def test_imports():
    """Test critical imports"""
    logger.info("🧪 Testing critical imports...")
    critical_modules = [
        "streamlit",
        "requests",
        "dotenv",
        "langchain_community",
        "sentence_transformers",
        "faiss",
        "pypdf",
        "docx",
        "fpdf2",
    ]
    failed_imports = []
    for module in critical_modules:
        try:
            if module == "dotenv":
                __import__("python_dotenv")
            elif module == "docx":
                __import__("python_docx")
            elif module == "faiss":
                __import__("faiss_cpu")
            else:
                __import__(module)
            logger.info(f"✅ {module}")
        except ImportError as e:
            logger.error(f"❌ {module}: {e}")
            failed_imports.append(module)
    if failed_imports:
        logger.error(f"❌ Failed imports: {', '.join(failed_imports)}")
        logger.info("💡 Run: pip install -r requirements.txt")
        return False
    logger.info("✅ All critical modules imported successfully")
    return True

def initialize_knowledge_base():
    """Initialize the knowledge base if needed"""
    logger.info("📚 Checking knowledge base...")
    index_path = Path("knowledge_base/index")
    if not (index_path / "index.faiss").exists():
        logger.info("🔨 Building knowledge base...")
        try:
            from build_knowledge_base import build_knowledge_base
            build_knowledge_base()
            logger.info("✅ Knowledge base built successfully")
        except Exception as e:
            logger.warning(f"⚠️ Knowledge base setup failed: {e}")
            logger.info("📝 The app will work without knowledge base (pure LLM mode)")
    else:
        logger.info("✅ Knowledge base ready")

def test_llm_connection():
    """Test LLM connectivity"""
    logger.info("🤖 Testing LLM connection...")
    try:
        from llm_client import LLMClient
        client = LLMClient()
        if client.has_openrouter or client.has_hf:
            messages = [{"role": "user", "content": "Hello"}]
            _ = client.chat(messages, max_tokens=16)
            logger.info("✅ LLM connectivity OK")
            return True
        else:
            logger.info("ℹ️ Demo mode only (no API keys)")
            return True
    except Exception as e:
        logger.warning(f"⚠️ LLM test failed: {e}")
        return False

def main():
    logger.info("🛠️ Running setup tasks...")
    create_directories()
    check_python_version()
    install_requirements()
    create_env_template()
    ok_imports = test_imports()
    if ok_imports:
        initialize_knowledge_base()
        test_llm_connection()
    logger.info("✅ Setup complete.")

if __name__ == "__main__":
    main()
