"""Memory Manager - Handles short and long-term memory"""
import logging
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

class MemoryManager:
    def __init__(self, config, logger=None):
        self.config = config
        self.logger = logger or logging.getLogger(__name__)
        self.memory_dir = Path("data/memory")
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        
    def save_interaction(self, user_input: str, ai_response: str, intent: Dict, timestamp=None):
        """Save interaction to memory"""
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        
        interaction = {
            "timestamp": timestamp,
            "user_input": user_input,
            "ai_response": ai_response,
            "intent": intent
        }
        
        # Append to daily log
        log_file = self.memory_dir / f"{datetime.now().strftime('%Y-%m-%d')}.jsonl"
        with open(log_file, 'a') as f:
            f.write(json.dumps(interaction) + '\n')
    
    def get_user_preferences(self, user_name: str) -> Optional[Dict]:
        """Get user preferences"""
        prefs_file = self.memory_dir / f"{user_name}_preferences.json"
        if prefs_file.exists():
            with open(prefs_file, 'r') as f:
                return json.load(f)
        return None
    
    def save_user_preferences(self, user_name: str, preferences: Dict):
        """Save user preferences"""
        prefs_file = self.memory_dir / f"{user_name}_preferences.json"
        with open(prefs_file, 'w') as f:
            json.dump(preferences, f, indent=2)
    
    def get_memory_size(self) -> int:
        """Get total memory size"""
        total = sum(f.stat().st_size for f in self.memory_dir.glob('*') if f.is_file())
        return total
    
    def save_all(self):
        """Save all memory to disk"""
        self.logger.info("💾 Memory saved")
