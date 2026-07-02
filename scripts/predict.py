"""CLI entry point for routing a single prompt."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Route a prompt with the trained LLM router.")
    parser.add_argument("prompt", help="User prompt to classify and route.")
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=Path("outputs/checkpoints/best"),
        help="Checkpoint directory for inference.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raise NotImplementedError(
        f"Inference pipeline not implemented yet ({args.prompt!r}, {args.checkpoint})."
    )


if __name__ == "__main__":
    main()
