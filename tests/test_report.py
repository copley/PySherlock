import json
from pathlib import Path

from pysherlock.report import build_report, write_report
from pysherlock.runner import run_command


def test_writes_versioned_json_report(tmp_path: Path) -> None:
    report = build_report(tmp_path, run_command(["python", "-c", "print('ok')"], tmp_path))
    output = tmp_path / "evidence.json"
    write_report(report, output)
    stored = json.loads(output.read_text())
    assert stored["schema_version"] == "1.0"
    assert stored["outcome"] == "passed"
