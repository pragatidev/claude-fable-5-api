"""Capstone solution. Do not peek until you have tried the starter."""

from __future__ import annotations

from typing import Any

from fable_client.models import FABLE_5, FALLBACK_BETA, OPUS_FALLBACK
from fable_client.refusals import fallback_request_body, handle_response


def handle(response: Any) -> dict[str, Any]:
    result = handle_response(response)
    return {
        "ok": result.ok,
        "text": result.text,
        "refused": result.refused,
        "category": result.category,
        "model": result.model,
        "stop_reason": result.stop_reason,
    }


def fallback_body(prompt: str) -> dict[str, Any]:
    return fallback_request_body(
        model=FABLE_5,
        fallback_model=OPUS_FALLBACK,
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
        fallback_beta=FALLBACK_BETA,
    )
