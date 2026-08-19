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

Live labs: copy `.env.example` to `.env` and add `ANTHROPIC_API_KEY`.
See `docs/ACCESS.md`.
