"""Lab 04: fallback request shape + a served-by fixture. No API key."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from fable_client.models import FABLE_5, FALLBACK_BETA, OPUS_FALLBACK
from fable_client.parse import first_text, served_model
from fable_client.refusals import fallback_request_body, handle_response
from labs._io import load_fixture


def main() -> int:
    body = fallback_request_body(
        model=FABLE_5,
        fallback_model=OPUS_FALLBACK,
        max_tokens=256,
        messages=[{"role": "user", "content": "Hello"}],
        fallback_beta=FALLBACK_BETA,
    )
    print("server_side_fallback_body:")
    print(json.dumps(body, indent=2))
    print()
    print("not_on: Amazon Bedrock, Vertex AI, Microsoft Foundry (use client middleware)")
    print()
    payload = load_fixture("fallback_served.json")
    handled = handle_response(payload)
    print(f"served_model: {served_model(payload)}")
    print(f"ok={handled.ok} text={first_text(payload)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
