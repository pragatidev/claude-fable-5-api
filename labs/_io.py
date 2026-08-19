"""Shared lab helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures"


def load_fixture(name: str) -> dict[str, Any]:
    path = FIXTURES / name
    return json.loads(path.read_text(encoding="utf-8"))
