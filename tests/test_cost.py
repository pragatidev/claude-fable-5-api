from __future__ import annotations

import pytest

from fable_client.cost import estimate_cost_usd


def test_fable_one_million_each():
    receipt = estimate_cost_usd(1_000_000, 1_000_000, model_id="claude-fable-5")
    assert receipt.input_usd == 10.0
    assert receipt.output_usd == 50.0
    assert receipt.total_usd == 60.0


def test_opus_fallback_rates():
    receipt = estimate_cost_usd(1_000_000, 1_000_000, model_id="claude-opus-4-8")
    assert receipt.input_usd == 5.0
    assert receipt.output_usd == 25.0


def test_rejects_negative():
    with pytest.raises(ValueError):
        estimate_cost_usd(-1, 0)
