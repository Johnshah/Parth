"""Voice interface for PARTH"""
import logging

class VoiceInterface:
    def __init__(self, parth_ai, logger=None):
        self.parth = parth_ai
        self.logger = logger or logging.getLogger(__name__)
    
    def run(self):
        """Run voice interface"""
        self.logger.info("🎙️  Voice interface starting...")
        self.logger.warning("⚠️  Voice features require Whisper and TTS models")
        self.logger.info("For now, falling back to chat interface...")
        
        # Fallback to chat interface
        from .chat_interface import ChatInterface
        chat = ChatInterface(self.parth, self.logger)
        chat.run()
