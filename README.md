# PySherlock

> An evidence-first debugging control plane for Codex and other coding agents.

For debugging case studies and paid repo-rescue enquiries, see [Paid Debugging Lab](https://github.com/copley/paid-debugging-lab).

## Why PySherlock exists

Codex and other coding agents can inspect code, run commands, and propose fixes. PySherlock does not try to replace them.

PySherlock provides the controlled workflow around an agent:

```text
failure → reproduce → collect evidence → diagnose → propose patch → verify → review → human decision
```

Its job is to make AI-assisted debugging repeatable, auditable, and safe—not merely plausible.

## Milestone 1: evidence capture

The current CLI runs an allow-listed command in a local repository and produces a versioned JSON evidence report containing:

- command and working directory;
- stdout and stderr;
- exit status, duration, and timeout state;
- heuristic redaction of common token-like values;
- an explicit outcome and limitations.

It does **not** call an AI model, modify the target repository, or automatically push code. Those capabilities require later milestones and explicit approval boundaries.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e . pytest

pysherlock --repo ./demo -- python failing_command.py
```

The demo intentionally fails. PySherlock writes its evidence report to:

```text
demo/.pysherlock/evidence.json
```

Use `--output` to choose another report path and `--timeout` to set the command timeout.

## Safety boundary

- Shell execution is not used.
- Only `python`, `python3`, `pytest`, `pip`, and `pip3` are allowed in v1.
- Outputs are redacted heuristically before persistence.
- No AI call, code modification, merge, push, or external side effect occurs.
- A human remains responsible for accepting any later diagnosis or patch.

## Roadmap

Future milestones will add:

1. repository inspection and reproducible failure capture;
2. AI-assisted, evidence-backed hypotheses;
3. minimal patch proposals in isolated worktrees;
4. targeted verification and adversarial review;
5. cost budgets, approval gates, and a durable decision record.

## Development

```bash
pip install -e . pytest ruff
pytest -q
ruff check src tests
```
