"""CLI entry point for router evaluation."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate a trained LLM router.")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/default.yaml"),
        help="Path to evaluation configuration YAML.",
    )
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=None,
        help="Checkpoint directory to evaluate.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raise NotImplementedError(f"Evaluation pipeline not implemented yet ({args.config}, {args.checkpoint}).")


if __name__ == "__main__":
    main()
