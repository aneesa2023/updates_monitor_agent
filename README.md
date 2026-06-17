# AI + Mobile Digest (Claude → Slack)

A scheduled news/updates brief. GitHub Actions runs on a cron, pulls curated RSS
feeds, asks Claude to surface the most significant items across **AI / Android /
iOS / Flutter** (new tools, releases, practices, deprecations), and posts a clean
digest to Slack via an incoming webhook. No always-on server.

## Files
- `digest.py` — the pipeline (fetch → dedupe → Claude → Slack).
- `feeds.py` — editable RSS source list. **Verify the URLs resolve.**
- `requirements.txt` — Python deps.
- `.github/workflows/digest.yml` — cron schedule + run + dedup commit.
- `seen.json` — auto-created dedup state (committed by the workflow).

## Setup
1. **Slack webhook:** api.slack.com/apps → Create New App → From scratch → enable
   **Incoming Webhooks** → Add New Webhook to Workspace → pick your channel →
   copy the `https://hooks.slack.com/services/...` URL.
2. **Anthropic key:** console.anthropic.com → API keys → create one (add credits).
3. **Repo:** put these files in a (private) GitHub repo.
4. **Secrets:** repo → Settings → Secrets and variables → Actions → add
   `ANTHROPIC_API_KEY` and `SLACK_WEBHOOK_URL`.
5. **Customize** `feeds.py`.
6. **Test:** Actions tab → run the workflow manually (mode = daily), check Slack.
   Or locally: `pip install -r requirements.txt`, set the two env vars, then
   `DIGEST_MODE=daily python digest.py`.
7. **Schedule:** edit the cron times in `digest.yml` for your timezone.

## Tuning
- Model: `digest.py` defaults to `claude-sonnet-4-6`. For lower cost switch to
  `claude-haiku-4-5-20251001`.
- Ranking/format: edit `SYSTEM_PROMPT`, `DAILY_TASK`, `WEEKLY_TASK` in `digest.py`.
- Volume: adjust `LOOKBACK_DAYS`, `MAX_CANDIDATES`, item counts in the tasks.
