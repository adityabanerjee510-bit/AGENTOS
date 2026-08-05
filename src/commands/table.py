from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

COMMANDS = {
    "📥 download": "Download a model",
    "🔍 search": "Search Hugging Face",
    "📂 list": "Installed models",
    "ℹ info": "Model information",
    "🗑 remove": "Delete model",
    "✔ verify": "Verify model files",
    "▶ run": "Run local model",
    "⬆ update": "Update model",
    "⚙ config": "Settings",
    "🩺 doctor": "Check environment",
    "🧹 cache": "Manage cache",
    "❓ help": "Show help",
    "🚪 exit": "Exit Application",
}
def display_table():
    table = Table(
        title="[bold bright_yellow]📋 AVAILABLE COMMANDS[/bold bright_yellow]",
        title_style="bold bright_yellow",
        box=box.DOUBLE,
        border_style="bright_cyan",
        header_style="bold bright_cyan",
        show_header=True,
        show_lines=True,
        pad_edge=True,
        expand=False,
    )

    table.add_column(
        "COMMAND",
        style="bold bright_cyan",
        justify="left",
        width=22,
    )

    table.add_column(
        "DESCRIPTION",
        style="white",
        justify="left",
        width=38,
    )
    for command, description in COMMANDS.items():
        table.add_row(command, description)

    console.print(table)