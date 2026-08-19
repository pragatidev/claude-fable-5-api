"""Lab 05: same prompt at two effort levels.

Needs ANTHROPIC_API_KEY. Prints tokens only. No invented benchmark.
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
from fable_client.cost import estimate_cost_usd
from fable_client.parse import first_text, stop_reason

PROMPT = (
    "In four short bullets, list what a software engineer must check "
    "on a Claude Messages API response before reading content. "
    "Do not name model SKUs."
)


def run_one(client, effort: str) -> None:
    kwargs = build_create_kwargs(prompt=PROMPT, max_tokens=1024, effort=effort)
    response = client.messages.create(**kwargs)
    receipt = estimate_cost_usd(
        response.usage.input_tokens,
        response.usage.output_tokens,
        model_id=response.model,
    )
    print(f"--- effort={effort}")
    print(f"stop={stop_reason(response)} in={receipt.input_tokens} out={receipt.output_tokens}")
    print(f"est_usd={receipt.total_usd:.6f} (see docs/CURRENCY.md)")
    print(first_text(response))
    print()


def main() -> int:
    load_api_key()
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    for effort in ("low", "xhigh"):
        run_one(client, effort)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
