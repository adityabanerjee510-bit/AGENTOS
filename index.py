from huggingface_hub import HfApi

# Files that are NOT needed for transformers
IGNORE_PATTERNS = [
    "original/",
    ".git/",
]

api = HfApi()


def format_size(size: int) -> str:
    """Convert bytes into human-readable size."""
    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def get_model_size(repo_id: str):
    """
    Returns:
        total_size (bytes)
        required_files
    """

    info = api.model_info(
        repo_id,
        files_metadata=True,
    )

    total = 0
    required_files = []

    for file in info.siblings:

        filename = file.rfilename

        # Skip folders/files we don't need
        if any(filename.startswith(pattern) for pattern in IGNORE_PATTERNS):
            continue

        if file.size is None:
            continue

        total += file.size

        required_files.append(
            {
                "name": filename,
                "size": file.size,
            }
        )

    return total, required_files


if __name__ == "__main__":

    repo = "meta-llama/Llama-3.2-1B"

    total, files = get_model_size(repo)

    print(f"\nModel : {repo}\n")

    for f in files:
        print(f"{f['name']:<45}{format_size(f['size'])}")

    print("-" * 60)
    print("Total :", format_size(total))