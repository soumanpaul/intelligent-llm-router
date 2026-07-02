"""Load and prepare router training datasets from Hugging Face."""

from datasets import DatasetDict, load_dataset


def load_router_dataset(dataset_id: str) -> DatasetDict:
    """Load a classification dataset for router training."""
    return load_dataset(dataset_id)
