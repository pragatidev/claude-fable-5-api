"""Turn a Messages response into an application result.

A Fable 5 classifier decline is not an HTTP error. Treat it as a first-class
state, then optionally retry on the fallback model.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from fable_client.parse import first_text, is_refusal, refusal_category, served_model, stop_reason


@dataclass(frozen=True)
class HandledResponse:
    ok: bool
    text: str
    stop_reason: str | None
    category: str | None
    model: str | None
    refused: bool


def handle_response(response: Any) -> HandledResponse:
    reason = stop_reason(response)
    model = served_model(response)
    if is_refusal(response):
        return HandledResponse(
            ok=False,
            text="",
            stop_reason=reason,
            category=refusal_category(response),
            model=model,
            refused=True,
        )
    return HandledResponse(
        ok=True,
        text=first_text(response),
        stop_reason=reason,
        category=None,
        model=model,
        refused=False,
    )


def fallback_request_body(
    *,
    model: str,
    fallback_model: str,
    max_tokens: int,
    messages: list[dict[str, Any]],
    fallback_beta: str,
) -> dict[str, Any]:
    """Body shape for server-side fallbacks (Claude API / Claude Platform on AWS).

    Not valid on Amazon Bedrock, Vertex AI, or Microsoft Foundry. Those need
    client-side middleware. See docs/CURRENCY.md.
    """
    return {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages,
        "betas": [fallback_beta],
        "fallbacks": [{"model": fallback_model}],
    }
