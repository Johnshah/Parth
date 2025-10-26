"""Configuration Manager for PARTH"""

import yaml
import json
from pathlib import Path
from typing import Any, Dict, Optional
import logging


class ConfigManager:
    """Manages PARTH configuration"""
    
    def __init__(self, config_path: str = "config/config.yaml"):
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self.logger = logging.getLogger(__name__)
    
    def _load_config(self) -> Dict:
        """Load configuration from file"""
        if not self.config_path.exists():
            # Create default configuration
            default_config = self._get_default_config()
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            self._save_config(default_config)
            return default_config
        
        with open(self.config_path, 'r') as f:
            if self.config_path.suffix == '.yaml':
                return yaml.safe_load(f) or {}
            elif self.config_path.suffix == '.json':
                return json.load(f)
            else:
                return {}
    
    def _get_default_config(self) -> Dict:
        """Get default configuration"""
        return {
            "user": {
                "name": "Prabhu",
                "timezone": "auto"
            },
            "ai": {
                "name": "Parth",
                "model_size": "auto",
                "quantization": "4bit",
                "max_context_length": 4096
            },
            "personality": {
                "formality": "balanced",
                "verbosity": "moderate",
                "humor": "occasional",
                "proactivity": "high",
                "empathy": True
            },
            "voice": {
                "enabled": True,
                "wake_word": "Parth",
                "language": "en",
                "voice_id": "default"
            },
            "device_control": {
                "android": {
                    "enabled": True,
                    "permissions": ["all"]
                },
                "desktop": {
                    "enabled": True,
                    "permissions": ["files", "apps"]
                }
            },
            "privacy": {
                "local_only": True,
                "encryption": True,
                "log_conversations": True
            },
            "performance": {
                "mode": "balanced",
                "cache_models": True,
                "parallel_tasks": 3
            }
        }
    
    def _save_config(self, config: Dict):
        """Save configuration to file"""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, 'w') as f:
            if self.config_path.suffix == '.yaml':
                yaml.dump(config, f, default_flow_style=False)
            elif self.config_path.suffix == '.json':
                json.dump(config, f, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by dot-notation key"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """Set configuration value by dot-notation key"""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        self._save_config(self.config)
    
    def reload(self):
        """Reload configuration from file"""
        self.config = self._load_config()
