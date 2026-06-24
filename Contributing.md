# Contributing

Thanks for helping grow the digest! The most useful contributions are **feeds**
and **topic packs**.

## Adding a feed

Edit `feeds.py` and add an entry to the right lane:

```python
{"name": "Source Name", "url": "https://example.com/rss.xml", "lane": "AI"},
```

Before opening a PR:

- **Verify the URL resolves** and returns RSS/Atom (paste it in a browser, or in
  any RSS reader). The pipeline skips dead feeds, but let's not ship broken ones.
- **Pick the closest existing lane** (`AI`, `Android`, `iOS`, `Flutter`,
  `Engineering`) or propose a new one (see below).
- **Keep it on-topic and reputable.** First-party blogs, well-known independent
  experts, official release feeds, and curated newsletters are ideal. Avoid
  low-signal aggregators and SEO farms.
- **No duplicates** — check the source isn't already listed.

## Proposing a new topic / lane

Want a lane this template doesn't cover (DevOps, Data Eng, Security, Web, Game
Dev, ML research...)? Open an issue or PR that:

1. Adds the lane to the relevant entries in `feeds.py`.
2. Adds the lane name to the daily and weekly task prompts in `digest.py` (search
   for the lane list in `DAILY_TASK` / `WEEKLY_TASK`).
3. Seeds it with 3–6 solid feeds.

Topic packs that are self-contained and well-curated are very welcome — they let
others adopt a whole subject area in one go.

## Respecting sources

Only add feeds the publisher offers publicly. Don't add feeds that require
authentication, scrape paywalled content, or violate a source's terms.

## Code changes

For changes to `digest.py` (filtering, formatting, delivery), please describe the
behavior change and test it with a manual `workflow_dispatch` run or locally with
`DIGEST_MODE=daily python digest.py`.