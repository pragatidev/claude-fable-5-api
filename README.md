# Claude Fable 5 API

Companion repo for the Udemy course **Claude Fable 5 API for Software Engineers**.

Clone this folder. Run the tests. Then call `claude-fable-5`.

This is not a chatbot demo pack. The product is a small Python client that:

1. Sends a Messages request to `claude-fable-5`
2. Reads text without assuming `content[0]` is text
3. Treats `stop_reason: "refusal"` as HTTP 200, not a crash
4. Opts into a fallback model
5. Prints a cost receipt from token counts

## Quick start (no API key)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS / Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest
python labs/02_parse_response.py
python labs/03_refusals.py
python labs/04_fallbacks.py
```

You should see a green pytest run. Offline labs use `fixtures/`.

## Live labs (needs a key)

The key lives in **`.env` in this repo root**. That file is gitignored. Do not push it.

1. Copy the sample: `copy .env.sample .env` (Windows) or `cp .env.sample .env` (macOS / Linux)
2. Create a key at https://platform.claude.com/settings/keys
3. Paste it as `ANTHROPIC_API_KEY=sk-ant-...` in `.env`
4. Your workspace must allow 30-day retention. Fable 5 is not available under zero data retention.

Full steps: `docs/ACCESS.md`.

```bash
python labs/01_first_call.py
python labs/05_effort.py
python labs/06_feature_plan.py
python labs/07_model_choice.py
```

## Layout

```
fable_client/     reusable parse, cost, refusal, fallback helpers
labs/             one script per lecture demo
fixtures/         real-shaped Messages JSON (no live call)
exercises/        S2 coding exercise (starter fails, solution passes)
tests/            pytest, no key required
docs/CURRENCY.md  re-read before any record session
```

## Course map

| Section | What you do here |
|---|---|
| S1 | What you need, clone, `pytest` |
| S2 | What Fable 5 is, why it exists, Mythos vs Opus, then first call + parse + exercise 2A |
| S3 | Refusals, fallbacks, effort |
| S4 | Feature plan, model choice, capstone starter |
| S5 | Keep the client |

IDs, betas, and rates change. `docs/CURRENCY.md` is the owner.

## License

MIT. See `LICENSE`.
