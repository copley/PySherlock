"""Conservative redaction for common secrets in reports."""

from __future__ import annotations

import re

_PATTERNS = (
    re.compile(r"(?i)(api[_-]?key|token|password|secret)\s*([:=])\s*([^\s'\"]+)"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
)


def redact(text: str) -> str:
    """Redact token-like values before they are persisted to a report."""
    redacted = text
    for pattern in _PATTERNS:
        redacted = pattern.sub(_replace, redacted)
    return redacted


def _replace(match: re.Match[str]) -> str:
    if match.lastindex and match.lastindex >= 2:
        return f"{match.group(1)}{match.group(2)}[REDACTED]"
    return "[REDACTED]"
