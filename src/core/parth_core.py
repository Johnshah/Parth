"""
PARTH Core - Main AI Intelligence System
Orchestrates multiple AI models and handles all reasoning and decision making
"""

import logging
from typing import Dict, List, Any, Optional
import asyncio
from dataclasses import dataclass

from .model_orchestrator import ModelOrchestrator
from .memory_manager import MemoryManager
from .task_planner import TaskPlanner
from .context_manager import ContextManager


@dataclass
class ParthResponse:
    """Response from PARTH AI"""
    text: str
    audio: Optional[bytes] = None
    actions: List[Dict[str, Any]] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.actions is None:
            self.actions = []
        if self.metadata is None:
            self.metadata = {}


class ParthAI:
    """
    PARTH - Personal Advanced Reasoning & Task Handling Intelligence
    
    Main AI system that coordinates:
    - Natural language understanding
    - Multi-model AI orchestration
    - Task planning and execution
    - Memory and context management
    - Device control and automation
    """
    
    def __init__(self, config, logger=None):
        """
        Initialize PARTH AI system
        
        Args:
            config: Configuration manager instance
            logger: Logger instance (optional)
        """
        self.config = config
        self.logger = logger or logging.getLogger(__name__)
        
        # Get user information
        self.user_name = config.get("user.name", "Prabhu")
        self.ai_name = "Parth"
        
        # Initialize components
        self.logger.info("🧠 Initializing AI components...")
        
        # Model orchestrator - manages all AI models
        self.model_orchestrator = ModelOrchestrator(config, self.logger)
        
        # Memory manager - handles short and long-term memory
        self.memory_manager = MemoryManager(config, self.logger)
        
        # Task planner - breaks down complex tasks
        self.task_planner = TaskPlanner(config, self.logger)
        
        # Context manager - maintains conversation context
        self.context_manager = ContextManager(config, self.logger)
        
        # Load initial personality and preferences
        self._load_personality()
        self._load_user_preferences()
        
        self.logger.info("✅ PARTH AI core initialized")
    
    def _load_personality(self):
        """Load AI personality settings"""
        self.personality = {
            "formality": self.config.get("personality.formality", "balanced"),
            "verbosity": self.config.get("personality.verbosity", "moderate"),
            "humor": self.config.get("personality.humor", "occasional"),
            "proactivity": self.config.get("personality.proactivity", "high"),
            "empathy": self.config.get("personality.empathy", True),
        }
        self.logger.debug(f"Loaded personality: {self.personality}")
    
    def _load_user_preferences(self):
        """Load user preferences from memory"""
        self.user_preferences = self.memory_manager.get_user_preferences(self.user_name)
        if not self.user_preferences:
            self.user_preferences = {
                "name": self.user_name,
                "communication_style": "friendly",
                "notification_preferences": "important_only",
                "privacy_level": "high",
            }
            self.memory_manager.save_user_preferences(self.user_name, self.user_preferences)
    
    async def process_input(self, user_input: str, 
                           input_type: str = "text",
                           context: Optional[Dict] = None) -> ParthResponse:
        """
        Process user input and generate response
        
        Args:
            user_input: User's text or voice input
            input_type: Type of input (text, voice, etc.)
            context: Additional context information
            
        Returns:
            ParthResponse with text, optional audio, and actions
        """
        self.logger.info(f"📥 Processing input from {self.user_name}: {user_input[:100]}...")
        
        # Update context
        self.context_manager.add_user_message(user_input)
        
        # Detect intent and extract entities
        intent = await self._detect_intent(user_input)
        self.logger.debug(f"Detected intent: {intent}")
        
        # Check if this is a command that requires immediate action
        if intent.get("requires_action"):
            response = await self._handle_action(intent, user_input, context)
        else:
            response = await self._generate_response(intent, user_input, context)
        
        # Save to memory
        self.memory_manager.save_interaction(
            user_input=user_input,
            ai_response=response.text,
            intent=intent,
            timestamp=None  # Will use current time
        )
        
        # Update context with AI response
        self.context_manager.add_ai_message(response.text)
        
        return response
    
    async def _detect_intent(self, user_input: str) -> Dict:
        """
        Detect user's intent from input
        
        Args:
            user_input: User's input text
            
        Returns:
            Dictionary with intent, entities, and metadata
        """
        # Get conversation history for context
        history = self.context_manager.get_recent_history(limit=5)
        
        # Use model orchestrator to understand intent
        intent_prompt = f"""
        Analyze the user's input and determine their intent.
        
        User: {self.user_name}
        Input: {user_input}
        
        Recent conversation:
        {history}
        
        Determine:
        1. Primary intent (question, command, conversation, task, etc.)
        2. Entities mentioned (files, apps, people, etc.)
        3. Emotion/tone
        4. Whether immediate action is required
        5. Task complexity (simple, moderate, complex)
        
        Return as JSON.
        """
        
        # Use a fast reasoning model for intent detection
        intent_result = await self.model_orchestrator.generate(
            prompt=intent_prompt,
            model_type="reasoning",
            max_tokens=500,
            temperature=0.3
        )
        
        # Parse intent (simplified - actual implementation would be more robust)
        try:
            import json
            intent = json.loads(intent_result)
        except:
            # Fallback intent structure
            intent = {
                "primary_intent": "conversation",
                "entities": [],
                "emotion": "neutral",
                "requires_action": False,
                "complexity": "simple"
            }
        
        return intent
    
    async def _handle_action(self, intent: Dict, user_input: str, context: Optional[Dict]) -> ParthResponse:
        """
        Handle actions that require device control or system operations
        
        Args:
            intent: Detected intent
            user_input: Original user input
            context: Additional context
            
        Returns:
            ParthResponse with action results
        """
        self.logger.info(f"⚡ Handling action: {intent.get('primary_intent')}")
        
        # Create task plan
        task_plan = await self.task_planner.create_plan(user_input, intent)
        
        # Execute tasks
        results = []
        for task in task_plan.tasks:
            result = await self._execute_task(task)
            results.append(result)
        
        # Generate response based on results
        response_text = self._format_action_response(results, intent)
        
        return ParthResponse(
            text=response_text,
            actions=results,
            metadata={"intent": intent, "task_plan": task_plan.dict()}
        )
    
    async def _execute_task(self, task: Dict) -> Dict:
        """
        Execute a specific task
        
        Args:
            task: Task dictionary with type and parameters
            
        Returns:
            Result dictionary
        """
        task_type = task.get("type")
        
        if task_type == "device_control":
            from device_control.controller import DeviceController
            controller = DeviceController(self.config, self.logger)
            result = await controller.execute(task)
            
        elif task_type == "web_search":
            from agents.web_agent import WebAgent
            agent = WebAgent(self.config, self.logger)
            result = await agent.search(task.get("query"))
            
        elif task_type == "code_generation":
            result = await self.model_orchestrator.generate_code(task)
            
        elif task_type == "file_operation":
            from device_control.file_manager import FileManager
            manager = FileManager(self.config, self.logger)
            result = await manager.execute(task)
            
        else:
            result = {"status": "unsupported", "task_type": task_type}
        
        return result
    
    async def _generate_response(self, intent: Dict, user_input: str, context: Optional[Dict]) -> ParthResponse:
        """
        Generate conversational response
        
        Args:
            intent: Detected intent
            user_input: User's input
            context: Additional context
            
        Returns:
            ParthResponse with generated text
        """
        # Get conversation history
        history = self.context_manager.get_recent_history(limit=10)
        
        # Build prompt with personality
        system_prompt = f"""
        You are Parth, a highly advanced AI assistant. You are helping {self.user_name}.
        
        Personality:
        - Communication style: {self.personality['formality']}
        - Verbosity: {self.personality['verbosity']}
        - Use humor: {self.personality['humor']}
        - Proactivity: {self.personality['proactivity']}
        - Show empathy: {self.personality['empathy']}
        
        Always:
        - Address the user as {self.user_name}
        - Be helpful, honest, and respectful
        - Show appropriate emotional intelligence
        - Explain your reasoning when needed
        - Ask clarifying questions if unsure
        
        Conversation history:
        {history}
        
        User's message: {user_input}
        
        Respond naturally as Parth:
        """
        
        # Generate response using best model
        response_text = await self.model_orchestrator.generate(
            prompt=system_prompt,
            model_type="reasoning",
            max_tokens=1000,
            temperature=0.7
        )
        
        return ParthResponse(
            text=response_text,
            metadata={"intent": intent}
        )
    
    def _format_action_response(self, results: List[Dict], intent: Dict) -> str:
        """Format action results into natural language response"""
        # This would be more sophisticated in actual implementation
        success_count = sum(1 for r in results if r.get("status") == "success")
        total = len(results)
        
        if success_count == total:
            return f"All done, {self.user_name}! I've completed all {total} tasks successfully."
        elif success_count > 0:
            return f"I've completed {success_count} out of {total} tasks. Some actions encountered issues."
        else:
            return f"I'm sorry, {self.user_name}. I encountered difficulties completing those tasks. Let me explain what happened..."
    
    def get_status(self) -> Dict:
        """Get current status of PARTH system"""
        return {
            "ai_name": self.ai_name,
            "user_name": self.user_name,
            "models_loaded": self.model_orchestrator.get_loaded_models(),
            "memory_size": self.memory_manager.get_memory_size(),
            "context_size": self.context_manager.get_context_size(),
            "personality": self.personality,
        }
    
    async def shutdown(self):
        """Gracefully shutdown PARTH system"""
        self.logger.info("🛑 Shutting down PARTH AI...")
        await self.model_orchestrator.unload_all()
        self.memory_manager.save_all()
        self.logger.info("✅ PARTH AI shutdown complete")
