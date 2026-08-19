"""Read a Claude Messages response without assuming content[0] is text.

Fable 5 thinking is always on. Default display is omitted, so the first block
is often type=thinking with empty text. A classifier decline is HTTP 200 with
stop_reason=refusal. Indexing content[0].text blindly crashes both cases.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence


def _as_mapping(response: Any) -> Mapping[str, Any]:
    if isinstance(response, Mapping):
        return response
    # SDK objects expose the same fields as attributes.
    return {
        "stop_reason": getattr(response, "stop_reason", None),
        "stop_details": getattr(response, "stop_details", None),
        "content": getattr(response, "content", None),
        "model": getattr(response, "model", None),
        "usage": getattr(response, "usage", None),
    }


def _block_type(block: Any) -> str:
    if isinstance(block, Mapping):
        return str(block.get("type") or "")
    return str(getattr(block, "type", "") or "")


def _block_text(block: Any) -> str:
    if isinstance(block, Mapping):
        return str(block.get("text") or "")
    return str(getattr(block, "text", "") or "")


def stop_reason(response: Any) -> str | None:
    value = _as_mapping(response).get("stop_reason")
    return str(value) if value is not None else None


def is_refusal(response: Any) -> bool:
    return stop_reason(response) == "refusal"


def refusal_category(response: Any) -> str | None:
    """Informational only. Can be null even on a refusal. Branch on stop_reason."""
    details = _as_mapping(response).get("stop_details")
    if details is None:
        return None
    if isinstance(details, Mapping):
        cat = details.get("category")
        return str(cat) if cat is not None else None
    cat = getattr(details, "category", None)
    return str(cat) if cat is not None else None


def served_model(response: Any) -> str | None:
    value = _as_mapping(response).get("model")
    return str(value) if value is not None else None


def iter_content(response: Any) -> Sequence[Any]:
    content = _as_mapping(response).get("content") or []
    if isinstance(content, Sequence) and not isinstance(content, (str, bytes)):
        return content
    return []


def first_text(response: Any) -> str:
    """First text block. Skips thinking, fallback, and tool blocks.

    Raises ValueError on a refusal so callers cannot treat empty content as success.
    """
    if is_refusal(response):
        category = refusal_category(response) or "unspecified"
        raise ValueError(f"refused ({category})")
    for block in iter_content(response):
        if _block_type(block) == "text":
            return _block_text(block)
    return ""
