"""Simple CLI entry point for the calculator.

Usage examples:
  python -m src.main add 2 3
  python -m src.main divide 6 3
"""

from __future__ import annotations

import argparse
import sys
from typing import Callable, Dict

from src.operations import add, divide, multiply, subtract


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calc",
        description="Basic calculator",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    def op_parser(name: str) -> argparse.ArgumentParser:
        p = sub.add_parser(name)
        p.add_argument("a", type=float)
        p.add_argument("b", type=float)
        return p

    op_parser("add")
    op_parser("subtract")
    op_parser("multiply")
    op_parser("divide")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    ops: Dict[str, Callable[[float, float], float]] = {
        "add": lambda x, y: float(add(x, y)),
        "subtract": lambda x, y: float(subtract(x, y)),
        "multiply": lambda x, y: float(multiply(x, y)),
        "divide": divide,
    }

    try:
        result = ops[args.cmd](args.a, args.b)
    except ValueError as exc:  # e.g., divide by zero
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    print(result)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
