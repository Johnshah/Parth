"""Task Planner - Breaks down complex tasks"""
import logging
from typing import Dict, List
from dataclasses import dataclass, field

@dataclass
class TaskPlan:
    goal: str
    tasks: List[Dict] = field(default_factory=list)
    complexity: str = "simple"
    estimated_time: int = 0
    
    def dict(self):
        return {
            "goal": self.goal,
            "tasks": self.tasks,
            "complexity": self.complexity,
            "estimated_time": self.estimated_time
        }

class TaskPlanner:
    def __init__(self, config, logger=None):
        self.config = config
        self.logger = logger or logging.getLogger(__name__)
    
    async def create_plan(self, user_input: str, intent: Dict) -> TaskPlan:
        """Create a task execution plan"""
        # Simplified task planning
        plan = TaskPlan(goal=user_input)
        
        # Analyze intent and create tasks
        if intent.get("primary_intent") == "device_control":
            plan.tasks = [{"type": "device_control", "action": user_input}]
        elif "code" in user_input.lower() or "app" in user_input.lower():
            plan.tasks = [{"type": "code_generation", "specification": user_input}]
        else:
            plan.tasks = [{"type": "conversation", "input": user_input}]
        
        return plan
