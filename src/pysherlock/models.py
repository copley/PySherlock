"""Typed data structures emitted by the first PySherlock milestone."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class ExecutionResult:
    command: list[str]
    working_directory: str
    exit_code: int | None
    timed_out: bool
    duration_ms: int
    stdout: str
    stderr: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class EvidenceReport:
    schema_version: str
    created_at: str
    repository: str
    execution: ExecutionResult
    outcome: str
    limitations: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "created_at": self.created_at,
            "repository": self.repository,
            "execution": self.execution.to_dict(),
            "outcome": self.outcome,
            "limitations": self.limitations,
        }
