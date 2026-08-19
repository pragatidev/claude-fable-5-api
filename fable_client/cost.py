"""Token cost helper.

Rates live in docs/CURRENCY.md. This module reads them from a small table so a
lecture can print our own receipt without hard-coding a number in a script that
will rot. Update CURRENCY.md at record time, then this table.
"""

from __future__ import annotations

from dataclasses import dataclass

# USD per million tokens. Source: Anthropic pricing page, noted in docs/CURRENCY.md
# as of 2026-08-19. Re-read that file before recording.
FABLE_INPUT_PER_MTOK = 10.0
FABLE_OUTPUT_PER_MTOK = 50.0
OPUS_48_INPUT_PER_MTOK = 5.0
OPUS_48_OUTPUT_PER_MTOK = 25.0


@dataclass(frozen=True)
class CostReceipt:
    input_tokens: int
    output_tokens: int
    input_usd: float
    output_usd: float
    total_usd: float
    model_id: str


def estimate_cost_usd(
    input_tokens: int,
    output_tokens: int,
    *,
    model_id: str = "claude-fable-5",
    input_per_mtok: float | None = None,
    output_per_mtok: float | None = None,
) -> CostReceipt:
    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("token counts must be >= 0")
    if model_id == "claude-opus-4-8":
        in_rate = OPUS_48_INPUT_PER_MTOK if input_per_mtok is None else input_per_mtok
        out_rate = OPUS_48_OUTPUT_PER_MTOK if output_per_mtok is None else output_per_mtok
    else:
        in_rate = FABLE_INPUT_PER_MTOK if input_per_mtok is None else input_per_mtok
        out_rate = FABLE_OUTPUT_PER_MTOK if output_per_mtok is None else output_per_mtok
    input_usd = input_tokens * in_rate / 1_000_000
    output_usd = output_tokens * out_rate / 1_000_000
    return CostReceipt(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        input_usd=input_usd,
        output_usd=output_usd,
        total_usd=input_usd + output_usd,
        model_id=model_id,
    )
