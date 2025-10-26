"""Context Manager - Maintains conversation context"""
import logging
from collections import deque
from typing import List, Dict

class ContextManager:
    def __init__(self, config, logger=None, max_history=20):
        self.config = config
        self.logger = logger or logging.getLogger(__name__)
        self.history = deque(maxlen=max_history)
    
    def add_user_message(self, message: str):
        """Add user message to context"""
        self.history.append({"role": "user", "content": message})
    
    def add_ai_message(self, message: str):
        """Add AI message to context"""
        self.history.append({"role": "assistant", "content": message})
    
    def get_recent_history(self, limit: int = 10) -> str:
        """Get recent conversation history as string"""
        recent = list(self.history)[-limit:]
        return "\n".join([f"{msg['role']}: {msg['content']}" for msg in recent])
    
    def get_context_size(self) -> int:
        """Get size of context"""
        return len(self.history)
    
    def clear_context(self):
        """Clear conversation context"""
        self.history.clear()
