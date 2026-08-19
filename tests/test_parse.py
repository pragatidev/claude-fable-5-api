from __future__ import annotations

import pytest

from fable_client.parse import first_text, is_refusal, refusal_category, served_model, stop_reason


def test_success_skips_empty_thinking(load_fixture):
    payload = load_fixture("success_omitted_thinking.json")
    assert payload["content"][0]["type"] == "thinking"
    assert first_text(payload) == "API connection confirmed. Model id is claude-fable-5."
    assert stop_reason(payload) == "end_turn"
    assert is_refusal(payload) is False
    assert served_model(payload) == "claude-fable-5"


def test_refusal_raises(load_fixture):
    payload = load_fixture("refusal_pre_output.json")
    assert is_refusal(payload) is True
    assert refusal_category(payload) == "cyber"
    with pytest.raises(ValueError, match="refused"):
        first_text(payload)


def test_refusal_null_category(load_fixture):
    payload = load_fixture("refusal_null_category.json")
    assert is_refusal(payload) is True
    assert refusal_category(payload) is None
    with pytest.raises(ValueError, match="unspecified"):
        first_text(payload)


def test_fallback_fixture_still_has_text(load_fixture):
    payload = load_fixture("fallback_served.json")
    assert first_text(payload) == "Fallback model answered after a classifier decline."
    assert served_model(payload) == "claude-opus-4-8"
