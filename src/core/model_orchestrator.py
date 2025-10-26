"""
Model Orchestrator - Manages and coordinates multiple AI models
Intelligently selects and uses the best model(s) for each task
"""

import logging
from typing import Dict, List, Optional, Any
import asyncio
from pathlib import Path


class ModelOrchestrator:
    """
    Orchestrates multiple AI models for different tasks
    Handles model loading, unloading, and intelligent selection
    """
    
    def __init__(self, config, logger=None):
        self.config = config
        self.logger = logger or logging.getLogger(__name__)
        
        self.loaded_models = {}
        self.model_registry = self._initialize_model_registry()
        self.device = self._detect_device()
        
        # Load initial models based on device capabilities
        self._load_initial_models()
    
    def _initialize_model_registry(self) -> Dict:
        """Initialize registry of available models"""
        return {
            # Reasoning models
            "reasoning": [
                {
                    "name": "Meta-Llama-3.1-8B-Instruct",
                    "size": "8B",
                    "repo": "meta-llama/Meta-Llama-3.1-8B-Instruct",
                    "quantization": ["4bit", "8bit"],
                    "capabilities": ["reasoning", "conversation", "coding"],
                },
                {
                    "name": "Mistral-7B-Instruct-v0.3",
                    "size": "7B",
                    "repo": "mistralai/Mistral-7B-Instruct-v0.3",
                    "quantization": ["4bit", "8bit"],
                    "capabilities": ["reasoning", "fast_response"],
                },
                {
                    "name": "Phi-3-mini-4k-instruct",
                    "size": "3.8B",
                    "repo": "microsoft/Phi-3-mini-4k-instruct",
                    "quantization": ["4bit"],
                    "capabilities": ["reasoning", "fast", "mobile_optimized"],
                },
            ],
            
            # Code generation models
            "coding": [
                {
                    "name": "CodeLlama-7b-Instruct",
                    "size": "7B",
                    "repo": "codellama/CodeLlama-7b-Instruct-hf",
                    "quantization": ["4bit", "8bit"],
                    "capabilities": ["code_generation", "debugging"],
                },
                {
                    "name": "DeepSeek-Coder-6.7B-Instruct",
                    "size": "6.7B",
                    "repo": "deepseek-ai/deepseek-coder-6.7b-instruct",
                    "quantization": ["4bit"],
                    "capabilities": ["code_generation", "multilingual"],
                },
                {
                    "name": "WizardCoder-Python-7B-V1.0",
                    "size": "7B",
                    "repo": "WizardLM/WizardCoder-Python-7B-V1.0",
                    "quantization": ["4bit"],
                    "capabilities": ["python_expert", "code_generation"],
                },
            ],
            
            # Vision models
            "vision": [
                {
                    "name": "LLaVA-1.5-7B",
                    "size": "7B",
                    "repo": "llava-hf/llava-1.5-7b-hf",
                    "quantization": ["4bit"],
                    "capabilities": ["image_understanding", "vqa"],
                },
                {
                    "name": "CLIP-ViT-L-14",
                    "size": "427M",
                    "repo": "openai/clip-vit-large-patch14",
                    "quantization": [],
                    "capabilities": ["image_text_matching", "zero_shot"],
                },
            ],
            
            # Embedding models
            "embedding": [
                {
                    "name": "bge-large-en-v1.5",
                    "size": "335M",
                    "repo": "BAAI/bge-large-en-v1.5",
                    "quantization": [],
                    "capabilities": ["semantic_search", "rag"],
                },
            ],
        }
    
    def _detect_device(self) -> str:
        """Detect compute device (CPU, CUDA, MPS, etc.)"""
        try:
            import torch
            if torch.cuda.is_available():
                device = "cuda"
                self.logger.info(f"🎮 GPU detected: {torch.cuda.get_device_name(0)}")
            elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
                device = "mps"
                self.logger.info("🍎 Apple Metal GPU detected")
            else:
                device = "cpu"
                self.logger.info("💻 Using CPU")
        except ImportError:
            device = "cpu"
            self.logger.warning("⚠️  PyTorch not found, defaulting to CPU")
        
        return device
    
    def _load_initial_models(self):
        """Load initial models based on device capabilities"""
        # Get device RAM
        import psutil
        ram_gb = psutil.virtual_memory().total / (1024**3)
        self.logger.info(f"💾 Available RAM: {ram_gb:.1f}GB")
        
        # Load models based on available resources
        model_size_pref = self.config.get("ai.model_size", "auto")
        quantization = self.config.get("ai.quantization", "4bit")
        
        if model_size_pref == "auto":
            if ram_gb >= 24:
                model_size = "large"
            elif ram_gb >= 12:
                model_size = "medium"
            else:
                model_size = "small"
        else:
            model_size = model_size_pref
        
        self.logger.info(f"📊 Using model size preference: {model_size} with {quantization} quantization")
        
        # For now, we'll use placeholder implementations
        # Actual model loading would use transformers library
        self.logger.info("🤖 Models will be loaded on-demand to save resources")
    
    async def generate(self, prompt: str, 
                      model_type: str = "reasoning",
                      max_tokens: int = 500,
                      temperature: float = 0.7,
                      **kwargs) -> str:
        """
        Generate text using appropriate model
        
        Args:
            prompt: Input prompt
            model_type: Type of model to use
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            
        Returns:
            Generated text
        """
        # Get or load appropriate model
        model = await self._get_model(model_type)
        
        # Generate (placeholder - actual implementation would use the model)
        # For now, return a simulated response
        if "intent" in prompt.lower() or "json" in prompt.lower():
            # Intent detection response
            response = '''{
                "primary_intent": "conversation",
                "entities": [],
                "emotion": "neutral",
                "requires_action": false,
                "complexity": "simple"
            }'''
        else:
            # Conversational response
            response = f"I understand, Prabhu. I'm processing your request using my {model_type} capabilities. [This is a placeholder response - actual model integration would happen here]"
        
        return response
    
    async def generate_code(self, task: Dict) -> Dict:
        """
        Generate code for a task
        
        Args:
            task: Task specification
            
        Returns:
            Generated code and metadata
        """
        model = await self._get_model("coding")
        
        # Placeholder implementation
        return {
            "status": "success",
            "code": "# Generated code would appear here",
            "language": task.get("language", "python"),
            "explanation": "Code generated successfully"
        }
    
    async def _get_model(self, model_type: str):
        """Get or load model of specified type"""
        if model_type in self.loaded_models:
            return self.loaded_models[model_type]
        
        # Load model (placeholder)
        self.logger.info(f"📦 Loading {model_type} model...")
        
        # Actual implementation would load from HuggingFace or local cache
        self.loaded_models[model_type] = {"type": model_type, "loaded": True}
        
        return self.loaded_models[model_type]
    
    def get_loaded_models(self) -> List[str]:
        """Get list of currently loaded models"""
        return list(self.loaded_models.keys())
    
    async def unload_all(self):
        """Unload all models to free memory"""
        self.logger.info("🧹 Unloading all models...")
        self.loaded_models.clear()
