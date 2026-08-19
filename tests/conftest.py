from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@pytest.fixture
def fixtures_dir() -> Path:
    return ROOT / "fixtures"


@pytest.fixture
def load_fixture(fixtures_dir: Path):
    def _load(name: str) -> dict:
        return json.loads((fixtures_dir / name).read_text(encoding="utf-8"))

    return _load
