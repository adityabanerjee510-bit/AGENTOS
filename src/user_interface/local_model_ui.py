from pathlib import Path
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

STORAGE = Path(r"E:\AI_Models")
PROJECTS = Path(r"D:\AI_Projects")


def run_ui():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]🚀 Run AI Model[/bold cyan]",
            border_style="cyan",
        )
    )

    if not STORAGE.exists():
        console.print("[red]No model storage directory found.[/red]")
        questionary.press_any_key_to_continue().ask()
        return

    models = [p.name for p in STORAGE.iterdir() if p.is_dir()]

    if not models:
        console.print("[red]No downloaded models found.[/red]")
        questionary.press_any_key_to_continue().ask()
        return

    model = questionary.select(
        "Select AI Model",
        choices=models,
    ).ask()

    project_name = questionary.text(
        "Project Name:",
        validate=lambda x: len(x.strip()) > 0 or "Project name required",
    ).ask()

    framework = questionary.select(
        "Framework",
        choices=[
            "LangChain",
            "Transformers",
            "FastAPI + LangChain",
            "CLI Assistant",
        ],
    ).ask()

    device = questionary.select(
        "Device",
        choices=[
            "Auto",
            "GPU",
            "CPU",
        ],
    ).ask()

    console.print()

    table = Table(title="Run Configuration")

    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Model", model)
    table.add_row("Project", project_name)
    table.add_row("Framework", framework)
    table.add_row("Device", device)

    console.print(table)

    if not questionary.confirm("Generate project?").ask():
        return

    project_dir = PROJECTS / project_name
    project_dir.mkdir(parents=True, exist_ok=True)

    (project_dir / "app").mkdir(exist_ok=True)
    (project_dir / "models").mkdir(exist_ok=True)
    (project_dir / "data").mkdir(exist_ok=True)

    with open(project_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(f"# {project_name}\n\n")
        f.write(f"Model: {model}\n")
        f.write(f"Framework: {framework}\n")

    with open(project_dir / "requirements.txt", "w", encoding="utf-8") as f:
        f.write(
            "langchain\n"
            "langchain-huggingface\n"
            "transformers\n"
            "torch\n"
        )

    with open(project_dir / "main.py", "w", encoding="utf-8") as f:
        f.write(
f'''from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

pipe = pipeline(
    "text-generation",
    model=r"{STORAGE / model}",
)

llm = HuggingFacePipeline(pipeline=pipe)

while True:
    prompt = input(">>> ")

    if prompt.lower() == "exit":
        break

    print(llm.invoke(prompt))
'''
        )

    console.print()

    console.print(
        Panel.fit(
            f"""[bold green]✔ Project Generated Successfully[/bold green]

Project Name : {project_name}
Model        : {model}
Framework    : {framework}

Location

{project_dir}
""",
            border_style="green",
        )
    )

    questionary.press_any_key_to_continue(
        "Press any key to return..."
    ).ask()