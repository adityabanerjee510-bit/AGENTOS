import typer
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from src.user_interface.search_ui import search_ui

from src.user_interface.download_ui import download_ui

# from src.user_interface.local_model_ui import run_ui

app = typer.Typer(help="AI Model Manager CLI")
console = Console()

# COMMANDS = [
#     "download",
#     "search",
#     "list",
#     "info",
#     "remove",
#     "verify",
#     "run",
#     "update",
#     "config",
#     "doctor",
#     "cache",
#     "help",
#     "exit",
# ]


def home():
    while True:
        console.clear()

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

        table = Table(
            title="Available Commands",
            show_header=True,
            header_style="bold magenta",
        )

        table.add_column("Command", style="cyan")
        table.add_column("Description")

        table.add_row("download", "Download a model")
        table.add_row("search", "Search Hugging Face")
        table.add_row("list", "Installed models")
        table.add_row("info", "Model information")
        table.add_row("remove", "Delete model")
        table.add_row("verify", "Verify model files")
        table.add_row("run", "Load model")
        table.add_row("update", "Update model")
        table.add_row("config", "Settings")
        table.add_row("doctor", "Check environment")
        table.add_row("cache", "Manage cache")
        table.add_row("help", "Show help")
        table.add_row("exit", "Exit Application")

        console.print(table)

        answers = questionary.text(
            "Select Your Command :"
        ).ask()  # Default storage path
        command = answers

        console.print(f"\n[bold green]command :[/bold green] {command}\n")

        # ---------------- Command Routing ---------------- #

        if command == "download":
            download_ui()

        elif command == "search":
            search_ui()

        elif command == "list":
            console.print("[yellow]List UI Coming Soon[/yellow]")

        elif command == "info":
            console.print("[yellow]Info UI Coming Soon[/yellow]")

        elif command == "remove":
            console.print("[yellow]Remove UI Coming Soon[/yellow]")

        elif command == "verify":
            console.print("[yellow]Verify UI Coming Soon[/yellow]")

        elif command == "run":
            run_ui()

        elif command == "update":
            console.print("[yellow]Update UI Coming Soon[/yellow]")

        elif command == "config":
            console.print("[yellow]Config UI Coming Soon[/yellow]")

        elif command == "doctor":
            console.print("[yellow]Doctor UI Coming Soon[/yellow]")

        elif command == "cache":
            console.print("[yellow]Cache UI Coming Soon[/yellow]")

        elif command == "help":
            console.print("[yellow]Help UI Coming Soon[/yellow]")

        elif command == "exit":
            console.print("\n[bold red]Goodbye! 👋[/bold red]")
            raise typer.Exit()

        questionary.press_any_key_to_continue(
            "Press any key to return to the main menu..."
        ).ask()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Starts the interactive AI Model Manager.
    """
    if ctx.invoked_subcommand is None:
        home()


if __name__ == "__main__":
    app()