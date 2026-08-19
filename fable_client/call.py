"""Live Messages helper. Import only from labs that need a real key."""

from __future__ import annotations

import os
from typing import Any

from fable_client.models import DEFAULT_EFFORT, FABLE_5, FALLBACK_BETA, OPUS_FALLBACK


def load_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        raise SystemExit(
            "ANTHROPIC_API_KEY is missing. Copy .env.sample to .env and paste a key "
            "from https://platform.claude.com/settings/keys. Fixture labs do not need a key."
        )
    return key


def build_create_kwargs(
    *,
    prompt: str,
    model: str = FABLE_5,
    max_tokens: int = 512,
    effort: str = DEFAULT_EFFORT,
    with_fallbacks: bool = False,
    fallback_model: str = OPUS_FALLBACK,
) -> dict[str, Any]:
    kwargs: dict[str, Any] = {
        "model": model,
        "max_tokens": max_tokens,
        "output_config": {"effort": effort},
        "messages": [{"role": "user", "content": prompt}],
    }
    if with_fallbacks:
        kwargs["betas"] = [FALLBACK_BETA]
        kwargs["fallbacks"] = [{"model": fallback_model}]
    return kwargs
