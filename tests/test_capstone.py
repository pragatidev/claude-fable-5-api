from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load(path: Path):
    spec = importlib.util.spec_from_file_location("capstone_mod", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_starter_not_done():
    starter = _load(ROOT / "labs" / "08_capstone" / "starter" / "client.py")
    with pytest.raises(NotImplementedError):
        starter.handle({"stop_reason": "end_turn", "content": []})


def test_solution_handles_all_fixtures(load_fixture):
    solution = _load(ROOT / "labs" / "08_capstone" / "solution" / "client.py")
    ok = solution.handle(load_fixture("success_omitted_thinking.json"))
    assert ok["ok"] is True
    assert ok["refused"] is False
    refused = solution.handle(load_fixture("refusal_pre_output.json"))
    assert refused["ok"] is False
    assert refused["refused"] is True
    assert refused["text"] == ""
    body = solution.fallback_body("Hello")
    assert body["model"] == "claude-fable-5"
    assert body["fallbacks"][0]["model"] == "claude-opus-4-8"
