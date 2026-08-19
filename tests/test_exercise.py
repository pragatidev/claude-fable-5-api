from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_starter_is_not_implemented():
    starter = _load(ROOT / "exercises" / "ex_parse_stop_reason.py")
    with pytest.raises(NotImplementedError):
        starter.get_text_or_raise({"stop_reason": "end_turn", "content": []})


def test_solution_passes_fixtures(load_fixture):
    solution = _load(ROOT / "exercises" / "solutions" / "ex_parse_stop_reason.py")
    success = load_fixture("success_omitted_thinking.json")
    assert "claude-fable-5" in solution.get_text_or_raise(success)
    with pytest.raises(ValueError, match="refused"):
        solution.get_text_or_raise(load_fixture("refusal_pre_output.json"))
