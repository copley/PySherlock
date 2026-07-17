"""Evidence report construction and persistence."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from .models import EvidenceReport, ExecutionResult


def build_report(repository: Path, execution: ExecutionResult) -> EvidenceReport:
    outcome = "passed" if execution.exit_code == 0 and not execution.timed_out else "failed"
    limitations = [
        "Milestone 1 captures command evidence only; it does not diagnose or change code.",
        "Output is redacted heuristically and must still be reviewed before sharing.",
    ]
    return EvidenceReport(
        schema_version="1.0",
        created_at=datetime.now(UTC).isoformat(),
        repository=str(repository.resolve()),
        execution=execution,
        outcome=outcome,
        limitations=limitations,
    )


def write_report(report: EvidenceReport, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
