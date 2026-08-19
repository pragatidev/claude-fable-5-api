"""Lab 02: walk a real-shaped fixture. No API key."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from fable_client.parse import first_text, is_refusal, served_model, stop_reason
from labs._io import load_fixture


def main() -> int:
    payload = load_fixture("success_omitted_thinking.json")
    print("fixture:         success_omitted_thinking.json")
    print(f"block_types:     {[b.get('type') for b in payload['content']]}")
    print(f"first_block:     {payload['content'][0]}")
    print("do_not_do:       payload['content'][0]['text']  # this is a thinking block")
    print(f"stop_reason:     {stop_reason(payload)}")
    print(f"is_refusal:      {is_refusal(payload)}")
    print(f"served_model:    {served_model(payload)}")
    print(f"first_text:      {first_text(payload)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
