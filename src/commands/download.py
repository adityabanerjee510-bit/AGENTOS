from huggingface_hub import snapshot_download

def download_model(repo_id: str, local_dir: str):
    """
    Downloads a model from Hugging Face Hub using the snapshot_download function.
    """
    # Example usage of snapshot_download
    snapshot_download(
        repo_id=repo_id,
        local_dir=local_dir
    )