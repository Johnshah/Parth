"""Chat interface for PARTH"""
import asyncio
import logging
from rich.console import Console
from rich.markdown import Markdown

class ChatInterface:
    def __init__(self, parth_ai, logger=None):
        self.parth = parth_ai
        self.logger = logger or logging.getLogger(__name__)
        self.console = Console()
        self.running = True
    
    def run(self):
        """Run chat interface"""
        self.console.print(f"\n💬 [bold green]Chat with {self.parth.ai_name}![/bold green]")
        self.console.print(f"[dim]Type 'exit' or 'quit' to end the conversation[/dim]\n")
        
        try:
            while self.running:
                # Get user input
                user_input = self.console.input(f"[bold blue]{self.parth.user_name}:[/bold blue] ")
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    self.console.print(f"\n[bold green]{self.parth.ai_name}:[/bold green] Goodbye, {self.parth.user_name}! 👋")
                    break
                
                if not user_input.strip():
                    continue
                
                # Process input
                self.console.print(f"[bold green]{self.parth.ai_name}:[/bold green] ", end="")
                response = asyncio.run(self.parth.process_input(user_input))
                self.console.print(response.text)
                self.console.print()
                
        except KeyboardInterrupt:
            self.console.print(f"\n\n[bold green]{self.parth.ai_name}:[/bold green] Goodbye, {self.parth.user_name}! 👋")
        except Exception as e:
            self.logger.error(f"Error in chat interface: {e}")
            raise
