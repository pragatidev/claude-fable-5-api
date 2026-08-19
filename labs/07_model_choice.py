"""Lab 07: same short prompt on Fable and the documented Opus fallback.

Needs ANTHROPIC_API_KEY. Prints our tokens. Confirm the Opus ID in docs/CURRENCY.md.
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
load_dotenv(ROOT / ".env")

from fable_client.call import build_create_kwargs, load_api_key
from fable_client.cost import estimate_cost_usd
from fable_client.models import FABLE_5, OPUS_FALLBACK, fable_or_opus_rule
from fable_client.parse import first_text, stop_reason

PROMPT = "In one sentence, what is stop_reason refusal on Claude Fable 5?"


def run(client, model: str) -> None:
    kwargs = build_create_kwargs(prompt=PROMPT, model=model, max_tokens=128, effort="low")
    started = time.perf_counter()
    response = client.messages.create(**kwargs)
    elapsed = time.perf_counter() - started
    receipt = estimate_cost_usd(
        response.usage.input_tokens,
        response.usage.output_tokens,
        model_id=model,
    )
    print(f"--- {model}")
    print(f"stop={stop_reason(response)} seconds={elapsed:.2f}")
    print(f"in={receipt.input_tokens} out={receipt.output_tokens} est_usd={receipt.total_usd:.6f}")
    print(first_text(response))
    print()


def main() -> int:
    load_api_key()
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    for model in (FABLE_5, OPUS_FALLBACK):
        run(client, model)
    rule = fable_or_opus_rule()
    print(f"keep {rule.model_id} for: {rule.use_when}")
    print(f"skip it when: {rule.skip_when}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
