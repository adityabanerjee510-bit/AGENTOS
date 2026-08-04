from huggingface_hub import HfApi

api = HfApi()

info = api.model_info("HuggingFaceTB/SmolLM2-135M-Instruct")

required_bytes = sum(
    file.size or 0
    for file in info.siblings
)

print(required_bytes)