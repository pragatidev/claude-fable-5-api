from __future__ import annotations

from fable_client.models import FABLE_5, MYTHOS_5, OPUS_FALLBACK, fable_or_opus_rule


def test_ids_are_aliases_not_dated():
    assert FABLE_5 == "claude-fable-5"
    assert MYTHOS_5 == "claude-mythos-5"
    assert OPUS_FALLBACK == "claude-opus-4-8"
    assert "-" in FABLE_5
    assert "2026" not in FABLE_5


def test_choice_rule_names_a_skip():
    rule = fable_or_opus_rule()
    assert rule.model_id == FABLE_5
    assert "ceiling" in rule.use_when
    assert "cheaper" in rule.skip_when
