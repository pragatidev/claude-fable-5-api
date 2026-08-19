from __future__ import annotations

from fable_client.models import FABLE_5, FALLBACK_BETA, OPUS_FALLBACK
from fable_client.refusals import fallback_request_body, handle_response


def test_handle_success(load_fixture):
    result = handle_response(load_fixture("success_omitted_thinking.json"))
    assert result.ok is True
    assert result.refused is False
    assert "claude-fable-5" in result.text


def test_handle_refusal(load_fixture):
    result = handle_response(load_fixture("refusal_pre_output.json"))
    assert result.ok is False
    assert result.refused is True
    assert result.text == ""
    assert result.category == "cyber"


def test_fallback_body_shape():
    body = fallback_request_body(
        model=FABLE_5,
        fallback_model=OPUS_FALLBACK,
        max_tokens=128,
        messages=[{"role": "user", "content": "Hi"}],
        fallback_beta=FALLBACK_BETA,
    )
    assert body["model"] == FABLE_5
    assert body["fallbacks"] == [{"model": OPUS_FALLBACK}]
    assert FALLBACK_BETA in body["betas"]
