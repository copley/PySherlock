from pathlib import Path

import pytest

from pysherlock.runner import CommandNotAllowedError, run_command


def test_captures_failure_and_redacts_output(tmp_path: Path) -> None:
    result = run_command(
        ["python", "-c", "print('token=sk-abcdefghijklmnopqrstuvwxyz'); raise SystemExit(2)"],
        tmp_path,
    )
    assert result.exit_code == 2
    assert "[REDACTED]" in result.stdout


def test_rejects_program_outside_allow_list(tmp_path: Path) -> None:
    with pytest.raises(CommandNotAllowedError):
        run_command(["bash", "-c", "echo unsafe"], tmp_path)
