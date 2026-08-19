# Currency file. Re-read at record time.

Last checked: 2026-08-19.

Every number and ID on screen in this course must match this file on the record day.
A prior script is not a source.

## Model IDs

| Name | Alias to type | Notes |
|---|---|---|
| Claude Fable 5 | `claude-fable-5` | Generally available. Lab default. |
| Claude Mythos 5 | `claude-mythos-5` | Project Glasswing only. Not a lab. |
| Fallback target | `claude-opus-4-8` | Documented Fable 5 fallback at research time. |
| Opus 5 | confirm on platform.claude.com | Launched 24 July 2026 as a cheaper near-peer. Vendor catalog in-repo did not yet list an alias on 2026-08-19. Do not invent a string. |

Do not append a date suffix.

## Betas (confirm or drop)

| Header | Used for |
|---|---|
| `server-side-fallback-2026-06-01` | Server-side `fallbacks` on Claude API and Claude Platform on AWS |
| `fallback-credit-2026-06-01` | Cache credit on a manual retry |
| `task-budgets-2026-03-13` | `output_config.task_budget` (minimum 20,000). If this header is gone, teach the loop without it. |

Not available: server-side `fallbacks` on Amazon Bedrock, Vertex AI, Microsoft Foundry, or the Batches API. Use client middleware there.

## Pricing (USD per million tokens)

Source to re-open: https://platform.claude.com/docs/en/about-claude/pricing (or the live pricing page Anthropic points to that day).

Research-time figures used in `fable_client/cost.py`:

- Fable 5: 10 input / 50 output
- Opus 4.8: 5 input / 25 output

If the page moved, update `cost.py` and this table on the same day.

## Access and retention

- Fable 5 generally available on the Claude API, Claude Platform, Claude.ai, Claude Code, Claude Cowork, Amazon Bedrock, Google Cloud, Microsoft Foundry.
- Mythos 5: Project Glasswing only.
- Covered Model: 30-day data retention required. Not available under zero data retention. Wrong org config returns 400.
- Export controls: applied 12 June 2026, lifted 30 June 2026, access restored 1 July 2026.
- Biology safeguard false-positive cut: 6 August 2026.
- Do not teach a Fable 5.1 or silent-routing rumor as fact.

## Thinking

- Always on. `thinking: {type: "disabled"}` returns 400. Omit the field.
- Raw chain of thought is never returned.
- Default display is `omitted` (empty thinking text). Use `display: "summarized"` only if the lecture shows a summary.
