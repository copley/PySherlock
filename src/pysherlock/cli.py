"""Command-line interface for PySherlock milestone 1."""

from __future__ import annotations

import argparse
from pathlib import Path

from .report import build_report, write_report
from .runner import CommandNotAllowedError, run_command


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Capture evidence from a failed local command.")
    parser.add_argument("--repo", required=True, type=Path, help="Path to the target repository.")
    parser.add_argument("--output", type=Path, default=Path(".pysherlock/evidence.json"))
    parser.add_argument("--timeout", type=int, default=60, help="Command timeout in seconds.")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="Allow-listed command, after --.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        raise SystemExit("Provide a command after --, for example: -- python -m pytest")
    try:
        execution = run_command(command, args.repo, args.timeout)
    except (CommandNotAllowedError, ValueError) as error:
        raise SystemExit(f"PySherlock refused to run the command: {error}") from error

    report = build_report(args.repo, execution)
    output = args.output if args.output.is_absolute() else args.repo / args.output
    write_report(report, output)
    print(f"Evidence report written to {output}")
    return 0 if report.outcome == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
