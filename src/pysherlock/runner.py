"""Safe command execution for evidence collection."""

from __future__ import annotations

import subprocess
import time
from pathlib import Path

from .models import ExecutionResult
from .redaction import redact


class CommandNotAllowedError(ValueError):
    """Raised when the requested program is outside the v1 allow-list."""


DEFAULT_ALLOWED_PROGRAMS = frozenset({"python", "python3", "pytest", "pip", "pip3"})


def run_command(
    command: list[str],
    repository: Path,
    timeout_seconds: int = 60,
    allowed_programs: frozenset[str] = DEFAULT_ALLOWED_PROGRAMS,
) -> ExecutionResult:
    """Run one allow-listed command without a shell and capture redacted output."""
    if not command:
        raise ValueError("A command is required.")
    if command[0] not in allowed_programs:
        allowed = ", ".join(sorted(allowed_programs))
        raise CommandNotAllowedError(f"Program '{command[0]}' is not allowed. Allowed: {allowed}")
    if timeout_seconds < 1:
        raise ValueError("timeout_seconds must be at least 1.")
    if not repository.is_dir():
        raise ValueError(f"Repository path does not exist or is not a directory: {repository}")

    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=repository,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
        return ExecutionResult(
            command=command,
            working_directory=str(repository.resolve()),
            exit_code=completed.returncode,
            timed_out=False,
            duration_ms=round((time.monotonic() - started) * 1000),
            stdout=redact(completed.stdout),
            stderr=redact(completed.stderr),
        )
    except subprocess.TimeoutExpired as error:
        stdout = error.stdout or ""
        stderr = error.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        return ExecutionResult(
            command=command,
            working_directory=str(repository.resolve()),
            exit_code=None,
            timed_out=True,
            duration_ms=round((time.monotonic() - started) * 1000),
            stdout=redact(stdout),
            stderr=redact(stderr),
        )
