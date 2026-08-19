"""Lab 06: one well-specified feature plan. Needs ANTHROPIC_API_KEY."""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
load_dotenv(ROOT / ".env")

from fable_client.call import build_create_kwargs, load_api_key
from fable_client.parse import first_text, is_refusal

SYSTEM = (
    "You are a senior software engineer. Return an implementation plan only: "
    "one-sentence summary, ordered steps, likely files, at most three risks, "
    "and concrete tests. Do not narrate options you will not pursue."
)

FEATURE = (
    "Add a password-reset flow to a small Django app. "
    "Users receive a token by email and land on a form to set a new password."
)


def main() -> int:
    load_api_key()
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    kwargs = build_create_kwargs(prompt=FEATURE, max_tokens=2048, effort="high")
    kwargs["system"] = SYSTEM
    print("note: a hard Fable turn can run many minutes. This lab is a short plan.")
    response = client.messages.create(**kwargs)
    if is_refusal(response):
        print("refused. check stop_reason and do not treat this as a plan.")
        return 2
    print(first_text(response))
    print(f"\nmodel={response.model} in={response.usage.input_tokens} out={response.usage.output_tokens}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
