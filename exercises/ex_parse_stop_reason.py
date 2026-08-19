"""Coding exercise 2A starter.

Given a Messages-shaped dict, return the first text block.
If stop_reason is refusal, raise ValueError.
Do not index content[0] as text.
"""

from __future__ import annotations

from typing import Any


def get_text_or_raise(response: dict[str, Any]) -> str:
    # TODO: branch on stop_reason, then return the first type==text block.
    raise NotImplementedError
