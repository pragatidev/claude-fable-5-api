from __future__ import annotations

import runpy
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "script",
    ["02_parse_response.py", "03_refusals.py", "04_fallbacks.py"],
)
def test_offline_lab_exits_zero(script, monkeypatch, capsys):
    monkeypatch.chdir(ROOT)
    monkeypatch.syspath_prepend(str(ROOT))
    # run_path with __main__ executes the file body
    try:
        runpy.run_path(str(ROOT / "labs" / script), run_name="__main__")
    except SystemExit as exc:
        assert exc.code in (0, None)
    out = capsys.readouterr().out
    assert out.strip() != ""
