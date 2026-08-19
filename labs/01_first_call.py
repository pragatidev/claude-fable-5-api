"""Lab 01: first Messages call to claude-fable-5.

Needs ANTHROPIC_API_KEY in repo-root .env (copy .env.sample).
Fixture labs (02, 03, 04) do not.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
load_dotenv(ROOT / ".env")

from fable_client.call import build_create_kwargs, load_api_key
from fable_client.models import FABLE_5
from fable_client.parse import first_text, stop_reason


def main() -> int:
    load_api_key()
    try:
        import anthropic
    except ImportError as exc:
        raise SystemExit("pip install -r requirements.txt") from exc

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    kwargs = build_create_kwargs(
        prompt="Reply in one sentence to confirm the API connection is working.",
        max_tokens=128,
        effort="low",
    )
    # Fable 5 thinking is always on. Do not pass thinking: disabled (400).
    response = client.messages.create(**kwargs)
    print(f"requested_model: {FABLE_5}")
    print(f"served_model:    {response.model}")
    print(f"stop_reason:     {stop_reason(response)}")
    print(f"input_tokens:    {response.usage.input_tokens}")
    print(f"output_tokens:   {response.usage.output_tokens}")
    print(f"text:            {first_text(response)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
