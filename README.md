# PySherlock

> Evidence-first debugging control plane for local repositories.

## Milestone 1: evidence capture

PySherlock now provides a safe foundation for AI-assisted debugging. It runs an allow-listed command in a local repository, captures stdout, stderr, exit status and duration, redacts common token-like values, and writes a versioned JSON evidence report.

It does **not** call an AI model, modify the target repository, or automatically push code. Those capabilities require later milestones and explicit approval boundaries.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e . pytest

pysherlock --repo ./demo -- python failing_command.py
```

The command exits non-zero because the demo intentionally fails. PySherlock writes the report to:

```text
demo/.pysherlock/evidence.json
```

Use a different report path with `--output`, and set a command timeout with `--timeout`.

## Safety boundary

- Shell execution is not used.
- Only `python`, `python3`, `pytest`, `pip`, and `pip3` are allowed in v1.
- Outputs are redacted heuristically before persistence.
- No AI call, code modification, merge, push, or external side effect occurs.

## Roadmap

Later milestones will add repository inspection, failure reproduction, evidence-backed hypotheses, minimal patch proposals, verification, adversarial review, and a human-approved final decision.

## Development

```bash
pip install -e . pytest ruff
pytest -q
ruff check src tests
```
