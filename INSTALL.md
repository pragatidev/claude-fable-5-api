# Install

Python 3.10 or newer.

```bash
git clone https://github.com/pragatidev/claude-fable-5-api.git
cd claude-fable-5-api
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

macOS / Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

If `pytest` is not on PATH after install:

```bash
python -m pytest
```

Live labs: copy `.env.sample` to `.env`, then paste a key from
https://platform.claude.com/settings/keys
See `docs/ACCESS.md`. Never commit `.env`.
