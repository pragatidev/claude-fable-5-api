"""Lab 03: a classifier decline is HTTP 200. No API key."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from fable_client.refusals import handle_response
from labs._io import load_fixture


def show(name: str) -> None:
    payload = load_fixture(name)
    handled = handle_response(payload)
    print(f"--- {name}")
    print(f"ok={handled.ok} refused={handled.refused} stop={handled.stop_reason}")
    print(f"category={handled.category} model={handled.model}")
    print(f"text={handled.text!r}")


def main() -> int:
    show("success_omitted_thinking.json")
    show("refusal_pre_output.json")
    show("refusal_null_category.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
