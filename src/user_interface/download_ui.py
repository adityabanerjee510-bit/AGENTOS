from rich.console import Console
from rich.panel import Panel
from rich.status import Status
import questionary
import time
from src.commands.download import download_model
console = Console()

def download_ui():
    while True:
        console.clear()

        console.print(
            Panel.fit(
                "[bold cyan]📥 Download Model[/bold cyan]",
                border_style="cyan",
            )
        )

        model = questionary.text(
            "Enter Hugging Face Model ID ",
            instruction="(Type 'back' to return) :"
        ).ask()
        folder = questionary.text(
            "Enter Local Folder Path to Save Model :"
        ).ask()

        if model is None or model.lower() == "back":
            return

        console.print(f"\n[green]Model:[/green] {model}\n")

        option = questionary.select(
            "Choose an option",
            choices=[
                "Start Download",
                "Change Model",
                "Back to Main Menu",
            ],
        ).ask()

        if option == "Back to Main Menu":
            return

        if option == "Change Model":
            model = questionary.text(
                        "Enter Hugging Face Model ID ",
                        instruction="(Type 'back' to return) :"
                    ).ask()
            folder = questionary.text(
                        "Enter Local Folder Path to Save Model :"
                    ).ask()

        
        local_dir = folder if folder else "E:/AI_MODELS"

        console.clear()

        console.print(
            Panel.fit(
                f"[bold cyan]Downloading[/bold cyan]\n\n{model}",
                border_style="green",
            )
        )
        download_model(repo_id=model, local_dir=local_dir)

        with console.status(
            "[bold green]Downloading model...",
            spinner="dots"
        ):
            time.sleep(5)

        console.print(
            Panel.fit(
                "[bold green]✔ Download Complete[/bold green]",
                border_style="green",
            )
        )

        if questionary.confirm("Download another model?").ask():
            continue

        return