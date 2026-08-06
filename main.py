import typer
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
# aditya commit
from src.commands.banner import banner_

from src.user_interface.search_ui import search_ui

from src.user_interface.download_ui import download_ui

from   src.commands.table import display_table


class Questions:
    def select_command(self):
        answers = questionary.text(
                    "Select Your Command :"
                ).ask()  # Default storage path
        return answers

    # def run(self):
    #     print("Run Question")

    # def search(self):
    #     print("Search Question")

app = typer.Typer(help="AI Model Manager CLI")
console = Console()

def home():
    while True:
        console.clear()

        banner_()

        questions = Questions()
        command = questions.select_command()

        if command is None:
            continue

        command = command.strip().lower()

        
        if command == "":
            console.print("[red]Please enter a command.[/red]")
            questionary.press_any_key_to_continue().ask()
            continue

        if command == "--help":
            display_table()
            command = questions.select_command()

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

        elif command == "update":
            console.print("[yellow]Update UI Coming Soon[/yellow]")

        elif command == "config":
            console.print("[yellow]Config UI Coming Soon[/yellow]")

        elif command == "doctor":
            console.print("[yellow]Doctor UI Coming Soon[/yellow]")

        elif command == "cache":
            console.print("[yellow]Cache UI Coming Soon[/yellow]")

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