#!/usr/bin/env python3
"""
PARTH - Personal Advanced Reasoning & Task Handling Intelligence
Main entry point for the AI assistant system

Author: Prabhu
License: Apache 2.0
"""

import os
import sys
import argparse
import logging
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from core.parth_core import ParthAI
from core.config_manager import ConfigManager
from interface.voice_interface import VoiceInterface
from interface.chat_interface import ChatInterface
from interface.web_interface import WebInterface
from utils.system_info import SystemInfo
from utils.logger import setup_logger


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="PARTH - Personal Advanced Reasoning & Task Handling Intelligence"
    )
    
    parser.add_argument(
        "--mode",
        choices=["voice", "chat", "web", "api"],
        default="chat",
        help="Interface mode (default: chat)"
    )
    
    parser.add_argument(
        "--voice",
        action="store_true",
        help="Enable voice interface (wake word activation)"
    )
    
    parser.add_argument(
        "--background",
        action="store_true",
        help="Run in background mode (no GUI)"
    )
    
    parser.add_argument(
        "--model-size",
        choices=["small", "medium", "large", "auto"],
        default="auto",
        help="AI model size (default: auto-detect based on device)"
    )
    
    parser.add_argument(
        "--quantization",
        choices=["4bit", "8bit", "none"],
        default="4bit",
        help="Model quantization for memory efficiency (default: 4bit)"
    )
    
    parser.add_argument(
        "--performance-mode",
        action="store_true",
        help="Enable performance mode (higher resource usage)"
    )
    
    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Port for web interface (default: 8080)"
    )
    
    parser.add_argument(
        "--public",
        action="store_true",
        help="Make web interface publicly accessible"
    )
    
    parser.add_argument(
        "--config",
        type=str,
        default="config/config.yaml",
        help="Path to configuration file"
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging"
    )
    
    parser.add_argument(
        "--username",
        type=str,
        default="Prabhu",
        help="User's name (default: Prabhu)"
    )
    
    return parser.parse_args()


def display_banner():
    """Display PARTH startup banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║   ██████╗  █████╗ ██████╗ ████████╗██╗  ██╗                 ║
    ║   ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║  ██║                 ║
    ║   ██████╔╝███████║██████╔╝   ██║   ███████║                 ║
    ║   ██╔═══╝ ██╔══██║██╔══██╗   ██║   ██╔══██║                 ║
    ║   ██║     ██║  ██║██║  ██║   ██║   ██║  ██║                 ║
    ║   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝                 ║
    ║                                                               ║
    ║   Personal Advanced Reasoning & Task Handling Intelligence   ║
    ║                                                               ║
    ║   🧠 JARVIS-Level AI Assistant                               ║
    ║   🎙️  Voice & Text Interface                                 ║
    ║   📱 Multi-Device Control                                     ║
    ║   🤖 75+ AI Models Orchestration                             ║
    ║   🔒 100% Free & Open Source                                 ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    """Main entry point"""
    # Parse arguments
    args = parse_arguments()
    
    # Setup logging
    log_level = logging.DEBUG if args.debug else logging.INFO
    logger = setup_logger("parth", log_level)
    
    # Display banner
    if not args.background:
        display_banner()
    
    logger.info("🚀 Initializing PARTH AI System...")
    
    # Get system information
    sys_info = SystemInfo()
    logger.info(f"📊 System: {sys_info.platform} | RAM: {sys_info.ram_gb}GB | CPU: {sys_info.cpu_cores} cores")
    
    # Load configuration
    logger.info(f"⚙️  Loading configuration from {args.config}")
    config = ConfigManager(args.config)
    
    # Update config with command line arguments
    config.set("user.name", args.username)
    config.set("ai.model_size", args.model_size)
    config.set("ai.quantization", args.quantization)
    config.set("performance.mode", "high" if args.performance_mode else "balanced")
    
    # Initialize PARTH core
    logger.info("🧠 Initializing AI core...")
    try:
        parth = ParthAI(config=config, logger=logger)
        logger.info("✅ PARTH AI core initialized successfully")
    except Exception as e:
        logger.error(f"❌ Failed to initialize PARTH AI: {e}")
        sys.exit(1)
    
    # Greet user
    greeting = f"Hello {args.username}! I'm Parth, your personal AI assistant. How can I help you today?"
    logger.info(f"💬 {greeting}")
    
    # Start appropriate interface
    try:
        if args.mode == "web" or args.public:
            logger.info(f"🌐 Starting web interface on port {args.port}...")
            interface = WebInterface(parth, port=args.port, public=args.public)
            interface.run()
            
        elif args.mode == "voice" or args.voice:
            logger.info("🎙️  Starting voice interface...")
            interface = VoiceInterface(parth, logger=logger)
            interface.run()
            
        elif args.mode == "chat":
            logger.info("💬 Starting chat interface...")
            interface = ChatInterface(parth, logger=logger)
            interface.run()
            
        elif args.mode == "api":
            logger.info("🔌 Starting API server...")
            from interface.api_server import APIServer
            server = APIServer(parth, port=args.port)
            server.run()
            
    except KeyboardInterrupt:
        logger.info("\n👋 Shutting down PARTH... Goodbye!")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Error running PARTH: {e}")
        if args.debug:
            raise
        sys.exit(1)


if __name__ == "__main__":
    main()
