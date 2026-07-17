# PySherlock

> An AI debugging control plane for reproducible, evidence-based software diagnosis.

## Status

PySherlock is currently in the design stage. This repository will evolve from an earlier GPT-powered Python debugging assistant into a focused tool for investigating failed repositories and CI jobs safely.

It will not claim that an AI patch is correct merely because it looks plausible. Every recommendation must be tied to evidence, verification, and a human approval boundary.

## The problem

AI coding agents can inspect code, run commands, and propose fixes. The difficult engineering work is controlling that process:

- collecting the right evidence;
- reproducing the real failure;
- separating hypotheses from facts;
- testing a minimal fix;
- reviewing the fix for regressions and safety;
- retaining a durable record of why the decision was made.

PySherlock is intended to provide that control layer.

## V1 goal

A Python CLI that accepts:

- a local Git repository;
- a failing command and/or failure log;
- optional execution and budget settings;

and runs specialised AI-assisted debugging stages to produce a structured evidence report.

The v1 output will be a diagnosis, a verified patch proposal, or an explicit decision to abstain and escalate. It will not automatically merge or push code.

## Planned foundation

- Python package managed with `pyproject.toml`
- Typed domain models and configuration
- Structured logging and JSON evidence reports
- Clear CLI commands
- Unit and integration tests
- Docker-based execution sandbox
- GitHub Actions CI

## Planned debugging pipeline

```text
Repository inspection
  → Failure reproduction
  → Evidence collection
  → Competing hypotheses
  → Minimal patch proposal
  → Targeted verification
  → Adversarial review
  → Final decision
```

Each stage must record its inputs, commands run, findings, confidence, and limitations.

## Safe agent orchestration

PySherlock will use multiple specialist roles, but orchestration is not a substitute for judgement.

Planned safeguards:

- isolated Git worktrees/branches for proposed changes;
- allow-listed commands and timeouts;
- token and cost budgets;
- secret detection and redaction;
- test and review gates before a patch is accepted;
- no automatic merge, push, or external side effect without explicit human approval;
- a clear `abstain` outcome when the evidence is insufficient.

## Proving it works

The repository will include deliberately broken demo fixtures and benchmark scenarios, such as:

- failing GitHub Actions jobs;
- Python dependency conflicts;
- Docker build/runtime failures;
- API integration failures;
- flaky browser-automation tests.

For each scenario, PySherlock will be measured on:

- whether it reproduced the failure;
- whether its root-cause explanation was correct;
- whether a proposed patch passed verification;
- whether the review stage rejected unsafe or incomplete fixes;
- elapsed time and AI cost per outcome.

## Employer-ready evidence

The finished project will include:

- an architecture diagram;
- sample structured evidence reports;
- terminal demonstrations and screenshots;
- an honest account of limitations and failure modes;
- reproducible benchmark results.

## Scope

PySherlock is not intended to be a generic “autonomous coding agent.” It is a narrow, auditable debugging workflow for Python, Docker, and GitHub Actions failures.

## License

MIT License
