# feeds.py
# Curated RSS sources for the digest, grouped by lane.
#
# ⚠️  VERIFY these URLs resolve before relying on them — feeds move/rename over
#     time. The pipeline gracefully skips any feed that fails to load, so a dead
#     URL won't break the run; it just drops that source. Add/remove freely.
#
# Each entry: {"name": display name, "url": RSS/Atom URL, "lane": one of
# "AI" | "Android" | "iOS" | "Flutter"}.

FEEDS = [
    # ---------- AI / Agents / MCP ----------
    {"name": "Simon Willison",        "url": "https://simonwillison.net/atom/everything/",     "lane": "AI"},
    {"name": "Latent Space",          "url": "https://www.latent.space/feed",                  "lane": "AI"},
    {"name": "The Batch",             "url": "https://www.deeplearning.ai/the-batch/rss.xml",  "lane": "AI"},
    {"name": "Import AI",             "url": "https://importai.substack.com/feed",             "lane": "AI"},
    {"name": "Anthropic News",        "url": "https://www.anthropic.com/rss.xml",              "lane": "AI"},

    # ---------- Android ----------
    {"name": "Android Developers Blog", "url": "https://android-developers.googleblog.com/feeds/posts/default", "lane": "Android"},
    {"name": "Android Weekly",          "url": "https://androidweekly.net/rss.xml",            "lane": "Android"},

    # ---------- iOS / Swift ----------
    {"name": "Apple Developer News",  "url": "https://developer.apple.com/news/rss/news.rss",  "lane": "iOS"},
    {"name": "Swift by Sundell",      "url": "https://www.swiftbysundell.com/rss",             "lane": "iOS"},
    {"name": "iOS Dev Weekly",        "url": "https://iosdevweekly.com/issues.rss",            "lane": "iOS"},

    # ---------- Flutter / Dart ----------
    {"name": "Flutter (Medium)",      "url": "https://medium.com/feed/flutter",                "lane": "Flutter"},
    {"name": "Dart (Medium)",         "url": "https://medium.com/feed/dartlang",               "lane": "Flutter"},
]
