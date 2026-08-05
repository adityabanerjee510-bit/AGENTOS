import typer
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def banner_():
    banner = r"""
    █████╗ ██╗███╗   ███╗ ██████╗ ██████╗ ███████╗██╗
    ██╔══██╗██║████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║
    ███████║██║██╔████╔██║██║   ██║██║  ██║█████╗  ██║
    ██╔══██║██║██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ██║
    ██║  ██║██║██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████╗
    ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝
    """
    console.print(
        Panel.fit(
            Text(banner, style="bold cyan")
            + Text("\n\nAI Model Manager CLI v1.0", style="bold yellow"),
            border_style="bright_blue",
        )
    )
    console.print(
        Panel(
            "[bold cyan]Welcome to AI Model Manager[/bold cyan]\n\n"
            "• Download AI models\n"
            "• Search Hugging Face\n"
            "• Run local models\n"
            "• Verify model files\n"
            "• Manage cache and settings\n\n"
            "[bold yellow]Type '--help' to see all available commands.[/bold yellow]",
            title="🚀 Quick Start",
            border_style="bright_green",
            width=63,      # Match your banner width
        )
    )
# def intro():
#     console.print(
#         Panel.fit(
#             "[bold cyan]Welcome to AI Model Manager[/bold cyan]\n\n"
#             "• Download AI models\n"
#             "• Search Hugging Face\n"
#             "• Run local models\n"
#             "• Verify model files\n"
#             "• Manage cache and settings\n\n"
#             "[yellow]Type '--help' to see all available commands.[/yellow]",
#             title="🚀 Quick Start",
#             border_style="bright_green",
#         )
#     )