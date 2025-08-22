from dotenv import load_dotenv
load_dotenv()


#!/usr/bin/env python3
"""
CVCompass AI Launch Script
Easy way to start the application with proper setup
"""

import os
import sys
import subprocess
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def check_setup():
    """Quick setup check"""
    logger.info("🔍 Checking setup...")
    
    # Check if key files exist
    required_files = ["app.py", "requirements.txt", "llm_client.py", "career_advisor.py"]
    missing_files = [f for f in required_files if not Path(f).exists()]
    
    if missing_files:
        logger.error(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    
    # Check if directories exist
    if not Path("data").exists():
        logger.info("🔧 Running first-time setup...")
        try:
            from setup import main as setup_main
            setup_main()
        except ImportError:
            logger.warning("⚠️ Setup script not found, creating basic directories...")
            Path("data").mkdir(exist_ok=True)
            Path("exports").mkdir(exist_ok=True)
    
    # Check environment
    env_file = Path(".env")
    if not env_file.exists():
        logger.info("📝 Environment file (.env) not found")
        logger.info("💡 The app will run in demo mode")
        logger.info("🔗 For full features, get API key: https://openrouter.ai/keys")
    
    return True

def launch_streamlit():
    """Launch Streamlit application"""
    logger.info("🚀 Launching CVCompass AI...")
    
    try:
        # Set Streamlit configuration
        os.environ["STREAMLIT_THEME_BASE"] = "dark"
        os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
        os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
        
        # Launch with optimal settings
        cmd = [
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--theme.base", "dark",
            "--theme.primaryColor", "#ec4899",
            "--theme.backgroundColor", "#0f1419", 
            "--theme.secondaryBackgroundColor", "#1a1f2e",
            "--theme.textColor", "#e2e8f0",
            "--server.headless", "true",
            "--server.fileWatcherType", "poll",
            "--browser.gatherUsageStats", "false"
        ]
        
        logger.info("🌐 Starting web interface...")
        logger.info("📱 Open your browser to the URL shown below")
        logger.info("⏹️  Press Ctrl+C to stop")
        logger.info("=" * 50)
        
        subprocess.run(cmd)
        
    except KeyboardInterrupt:
        logger.info("\n⏹️ Application stopped by user")
    except FileNotFoundError:
        logger.error("❌ Streamlit not found. Install with: pip install streamlit")
    except Exception as e:
        logger.error(f"❌ Failed to launch: {e}")

def show_banner():
    """Show application banner"""
    banner = """
╔══════════════════════════════════════════════════════╗
║                 CVCompass AI                         ║
║              Career Assistant                        ║
║                                                      ║
║  🎯 AI-Powered Resume Builder                       ║
║  📊 Resume Analysis & Optimization                  ║
║  💬 Interview Preparation                           ║
║  🚀 Career Guidance & Roadmaps                     ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
"""
    print(banner)

def main():
    """Main launch function"""
    show_banner()
    
    if not check_setup():
        logger.error("❌ Setup check failed")
        sys.exit(1)
    
    try:
        launch_streamlit()
    except Exception as e:
        logger.error(f"❌ Launch failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()