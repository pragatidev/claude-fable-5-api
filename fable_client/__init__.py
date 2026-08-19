"""Claude Fable 5 lab client. Parse first. Call second. Never index content[0] blindly."""

from fable_client.cost import estimate_cost_usd
from fable_client.models import FABLE_5, OPUS_FALLBACK, ModelChoice
from fable_client.parse import first_text, is_refusal, refusal_category, served_model, stop_reason
from fable_client.refusals import handle_response

__all__ = [
    "FABLE_5",
    "OPUS_FALLBACK",
    "ModelChoice",
    "estimate_cost_usd",
    "first_text",
    "handle_response",
    "is_refusal",
    "refusal_category",
    "served_model",
    "stop_reason",
]
