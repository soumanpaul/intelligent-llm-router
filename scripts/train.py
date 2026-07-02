"""CLI entry point for router fine-tuning."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fine-tune the LLM router model.")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/default.yaml"),
        help="Path to training configuration YAML.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raise NotImplementedError(f"Training pipeline not implemented yet ({args.config}).")


if __name__ == "__main__":
    main()
