# Access setup

Live labs read **one file**: `.env` in the repo root (next to `README.md`).
That file is local only. Git ignores it. It must never be pushed.

## Get a key

1. Sign in to Claude Platform.
2. Open https://platform.claude.com/settings/keys
3. Create a key. Copy it once. It starts with `sk-ant-`.
4. Confirm the workspace is not on zero data retention. Fable 5 is a Covered Model. A ZDR org gets 400.

## Put it in this repo

From the repo root:

```bash
# Windows
copy .env.sample .env

# macOS / Linux
cp .env.sample .env
```

Open `.env` and replace the placeholder:

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

with the key you copied. No quotes. No spaces around `=`.

## Check it

```bash
python labs/01_first_call.py
```

You should see `served_model: claude-fable-5`. Offline labs (`02`, `03`, `04`) and `pytest` do not need this file.

Claude.ai, Claude Code, Amazon Bedrock, Vertex AI, and Microsoft Foundry are valid doors.
This course records the Claude API path. Other doors are named, not labbed.

Mythos 5 (`claude-mythos-5`) is Project Glasswing only. There is no lab for it.
