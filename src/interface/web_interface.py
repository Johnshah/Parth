"""Web interface for PARTH"""
import logging

class WebInterface:
    def __init__(self, parth_ai, port=8080, public=False):
        self.parth = parth_ai
        self.port = port
        self.public = public
        self.logger = logging.getLogger(__name__)
    
    def run(self):
        """Run web interface"""
        self.logger.info(f"🌐 Web interface would start on http://localhost:{self.port}")
        self.logger.warning("⚠️  Web interface requires additional setup")
        self.logger.info("For now, falling back to chat interface...")
        
        # Fallback to chat interface
        from .chat_interface import ChatInterface
        chat = ChatInterface(self.parth, self.logger)
        chat.run()
