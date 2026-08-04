from huggingface_hub import HfApi
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import questionary

console = Console()
api = HfApi()


def format_size(size_bytes):
    if not size_bytes:
        return "Unknown"

    return f"{size_bytes / (1024 ** 3):.2f} GB"


def get_model_size(repo_id):
    try:
        info = api.model_info(repo_id)

        total_size = 0

        for file in info.siblings:
            if file.size:
                total_size += file.size

        return format_size(total_size)

    except Exception:
        return "Unknown"


def get_parameters(info):
    if info.card_data:

        for key in [
            "model_size",
            "parameters",
            "parameter_count",
            "params",
        ]:
            if key in info.card_data:
                return str(info.card_data[key])

    repo = info.id.lower()

    for tag in [
        "0.5b",
        "1b",
        "1.1b",
        "1.5b",
        "2b",
        "3b",
        "4b",
        "7b",
        "8b",
        "9b",
        "13b",
        "14b",
        "27b",
        "32b",
        "70b",
    ]:
        if tag in repo:
            return tag.upper()

    return "Unknown"


def search_ui():

    while True:

        console.clear()

        console.print(
            Panel.fit(
                "[bold cyan]🔍 Search Hugging Face Models[/bold cyan]",
                border_style="cyan",
            )
        )

        keyword = questionary.text(
            "Search:",
            instruction="Type 'back' to return",
        ).ask()

        if keyword is None:
            return

        if keyword.lower() == "back":
            return

        console.print("\nSearching...\n")

        try:

            models = list(
                api.list_models(
                    search=keyword,
                    full=True,
                    limit=20,
                )
            )

            if not models:
                console.print("[red]No models found.[/red]")
                questionary.press_any_key_to_continue().ask()
                continue

            table = Table(title=f"Search Results ({len(models)})")

            table.add_column("#", style="cyan")
            table.add_column("Repository")
            table.add_column("Params")
            table.add_column("Downloads")
            table.add_column("Likes")

            for i, model in enumerate(models, start=1):

                params = get_parameters(model)

                table.add_row(
                    str(i),
                    model.id,
                    params,
                    str(model.downloads or 0),
                    str(model.likes or 0),
                )

            console.print(table)

            choice = questionary.select(
                "Select a model",
                choices=[
                    model.id for model in models
                ] + ["Back"],
            ).ask()

            if choice == "Back":
                continue

            info = api.model_info(choice)

            console.clear()

            detail = Table(
                title="Model Information",
                show_header=False,
            )

            detail.add_column("Field", style="cyan")
            detail.add_column("Value")

            detail.add_row("Repository", info.id)
            detail.add_row("Parameters", get_parameters(info))
            detail.add_row("Size", get_model_size(info.id))
            detail.add_row("Downloads", str(info.downloads))
            detail.add_row("Likes", str(info.likes))
            detail.add_row("Library", str(info.library_name))
            detail.add_row("Pipeline", str(info.pipeline_tag))
            detail.add_row("License", str(info.card_data.get("license", "Unknown")) if info.card_data else "Unknown")

            console.print(detail)

            action = questionary.select(
                "Next",
                choices=[
                    "Search Again",
                    "Back to Main Menu",
                ],
            ).ask()

            if action == "Back to Main Menu":
                return

        except Exception as e:

            console.print(f"[red]{e}[/red]")
            questionary.press_any_key_to_continue().ask()