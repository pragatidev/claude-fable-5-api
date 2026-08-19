"""Coding exercise 2A solution."""

from __future__ import annotations

from typing import Any


def get_text_or_raise(response: dict[str, Any]) -> str:
    if response.get("stop_reason") == "refusal":
        details = response.get("stop_details") or {}
        category = details.get("category") if isinstance(details, dict) else None
        raise ValueError(f"refused ({category or 'unspecified'})")
    for block in response.get("content") or []:
        if isinstance(block, dict) and block.get("type") == "text":
            return str(block.get("text") or "")
    return ""
