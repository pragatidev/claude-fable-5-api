"""Model IDs used in this course.

Verify every string against docs/CURRENCY.md before a record session.
Do not invent a date suffix. Use the alias as published.
"""

from __future__ import annotations

from dataclasses import dataclass

# Anthropic Messages aliases. Source: platform.claude.com models overview, checked 2026-08-19.
FABLE_5 = "claude-fable-5"
MYTHOS_5 = "claude-mythos-5"  # Project Glasswing only. Not a lab in this course.
OPUS_FALLBACK = "claude-opus-4-8"  # Documented Fable 5 fallback target at research time.

# Effort values Fable 5 accepts inside output_config.
EFFORT_LEVELS = ("low", "medium", "high", "xhigh", "max")
DEFAULT_EFFORT = "high"

# Server-side fallback beta. Confirm the header has not moved (docs/CURRENCY.md).
FALLBACK_BETA = "server-side-fallback-2026-06-01"

# Covered Model rule at research time: 30-day retention, not available under ZDR.
RETENTION_DAYS = 30
ZERO_DATA_RETENTION_OK = False


@dataclass(frozen=True)
class ModelChoice:
    """One line you can defend after the S4 choice lab."""

    model_id: str
    use_when: str
    skip_when: str


def fable_or_opus_rule() -> ModelChoice:
    return ModelChoice(
        model_id=FABLE_5,
        use_when="ceiling jobs you have measured on your own files",
        skip_when="short calls, classification, or any job a cheaper Opus seat already handles",
    )
