# feeds.py
# Curated RSS sources for the digest, grouped by lane and by source TYPE so the
# digest pulls from a diverse mix rather than one kind of voice:
#   • Official / labs   — vendor announcements, releases, deprecations
#   • Independent       — expert blogs with analysis and practices
#   • Newsletter        — human-curated weekly roundups
#   • Community          — Reddit / Hacker News pulse (higher noise, high signal)
#   • Releases           — GitHub release feeds = direct version/deprecation signal
#
# Schema (unchanged, drop-in): {"name", "url", "lane"} where lane is one of
# "AI" | "Android" | "iOS" | "Flutter".
#
# Notes:
#   - Most URLs were verified live in June 2026; ones marked "# verify" follow a
#     reliable pattern (GitHub .atom, Reddit .rss, hnrss) but weren't fetched —
#     confirm in a browser. The pipeline skips any feed that fails, so a wrong
#     URL degrades gracefully (you'll see a "skip" line in the logs).
#   - Community + HN feeds are higher-volume. If a digest gets noisy, comment
#     them out or tune the hnrss "points" threshold upward.
#   - More feeds = more candidate items per run = more tokens. The MAX_CANDIDATES
#     cap bounds it, but this is exactly why a relevance pre-filter is worth
#     adding next.

FEEDS = [
    # ======================= AI / Agents / MCP =======================
    # -- Official / labs --
    {"name": "Anthropic News",        "url": "https://www.anthropic.com/rss.xml",                 "lane": "AI"},
    {"name": "OpenAI News",           "url": "https://openai.com/news/rss.xml",                   "lane": "AI"},
    {"name": "Hugging Face Blog",     "url": "https://huggingface.co/blog/feed.xml",              "lane": "AI"},
    {"name": "Google AI",             "url": "https://blog.google/technology/ai/rss/",            "lane": "AI"},
    {"name": "Google DeepMind",       "url": "https://deepmind.google/discover/blog/feed.xml",    "lane": "AI"},
    # -- Independent / analysis --
    {"name": "Simon Willison",        "url": "https://simonwillison.net/atom/everything/",        "lane": "AI"},
    {"name": "Latent Space",          "url": "https://www.latent.space/feed",                     "lane": "AI"},
    {"name": "The Batch",             "url": "https://www.deeplearning.ai/the-batch/rss.xml",     "lane": "AI"},
    {"name": "Import AI",             "url": "https://importai.substack.com/feed",                "lane": "AI"},
    {"name": "Ahead of AI (Raschka)", "url": "https://magazine.sebastianraschka.com/feed",        "lane": "AI"},
    # -- Community / releases --
    {"name": "HN: MCP",               "url": "https://hnrss.org/newest?q=Model+Context+Protocol", "lane": "AI"},  # verify + tune
    {"name": "HN: AI agents",         "url": "https://hnrss.org/newest?q=AI+agents&points=50",    "lane": "AI"},  # verify + tune
    {"name": "MCP spec releases",     "url": "https://github.com/modelcontextprotocol/modelcontextprotocol/releases.atom", "lane": "AI"},  # verify repo path

    # -- Curated blogs (added on request) --
    {"name": "Pragmatic Engineer",   "url": "https://newsletter.pragmaticengineer.com/feed",     "lane": "AI"},
    {"name": "One Useful Thing",      "url": "https://www.oneusefulthing.org/feed",               "lane": "AI"},
    {"name": "Interconnects (Lambert)","url": "https://www.interconnects.ai/feed",                "lane": "AI"},
    {"name": "Hamel Husain (evals)",  "url": "https://hamel.dev/index.xml",                       "lane": "AI"},  # verify

    # ============================ Android ============================
    # -- Official --
    {"name": "Android Developers Blog",   "url": "https://android-developers.googleblog.com/feeds/posts/default", "lane": "Android"},
    {"name": "Android Developers (Medium)","url": "https://medium.com/feed/androiddevelopers",   "lane": "Android"},
    {"name": "Kotlin Blog (JetBrains)",   "url": "https://blog.jetbrains.com/kotlin/feed/",      "lane": "Android"},
    # -- Newsletter --
    {"name": "Android Weekly",            "url": "https://androidweekly.net/rss.xml",            "lane": "Android"},
    # -- Independent --
    {"name": "ProAndroidDev",             "url": "https://proandroiddev.com/feed",               "lane": "Android"},
    # -- Cross-platform mobile --
    {"name": "ProMobile.Dev",             "url": "https://promobile.dev/feed",                   "lane": "Android"},
    # -- Community --
    {"name": "r/androiddev",              "url": "https://www.reddit.com/r/androiddev/.rss",     "lane": "Android"},  # verify

    # -- Curated blogs (added on request) --
    {"name": "Jake Wharton",          "url": "https://jakewharton.com/atom.xml",                 "lane": "Android"},  # verify
    {"name": "Chris Banes",           "url": "https://chrisbanes.me/feed.xml",                   "lane": "Android"},  # verify

    # ============================= iOS / Swift =======================
    # -- Official --
    {"name": "Apple Developer News",  "url": "https://developer.apple.com/news/rss/news.rss",    "lane": "iOS"},
    {"name": "Swift.org Blog",        "url": "https://www.swift.org/atom.xml",                   "lane": "iOS"},
    # -- Newsletter --
    {"name": "iOS Dev Weekly",        "url": "https://iosdevweekly.com/issues.rss",              "lane": "iOS"},
    # -- Independent --
    {"name": "Swift by Sundell",      "url": "https://www.swiftbysundell.com/rss",               "lane": "iOS"},
    {"name": "Hacking with Swift",    "url": "https://www.hackingwithswift.com/articles/rss",    "lane": "iOS"},
    {"name": "SwiftLee",              "url": "https://www.avanderlee.com/feed",                  "lane": "iOS"},
    {"name": "NSHipster",             "url": "https://nshipster.com/feed.xml",                   "lane": "iOS"},  # verify
    # -- Community --
    {"name": "r/iOSProgramming",      "url": "https://www.reddit.com/r/iOSProgramming/.rss",     "lane": "iOS"},  # verify

    # -- Curated blogs (added on request) --
    {"name": "Use Your Loaf",         "url": "https://useyourloaf.com/blog/rss.xml",             "lane": "iOS"},
    {"name": "Point-Free",            "url": "https://www.pointfree.co/feed/atom.xml",           "lane": "iOS"},  # verify
    {"name": "Donny Wals",            "url": "https://www.donnywals.com/feed/",                  "lane": "iOS"},  # verify

    # =========================== Flutter / Dart ======================
    # -- Official --
    {"name": "Flutter (Medium)",      "url": "https://medium.com/feed/flutter",                  "lane": "Flutter"},
    {"name": "Dart (Medium)",         "url": "https://medium.com/feed/dartlang",                 "lane": "Flutter"},
    # -- Independent --
    {"name": "Code With Andrea",      "url": "https://codewithandrea.com/rss.xml",               "lane": "Flutter"},  # verify
    # -- Releases --
    {"name": "Flutter releases",      "url": "https://github.com/flutter/flutter/releases.atom", "lane": "Flutter"},
    # -- Community --
    {"name": "r/FlutterDev",          "url": "https://www.reddit.com/r/FlutterDev/.rss",         "lane": "Flutter"},  # verify
    # -- Curated blogs (added on request) --
    {"name": "Flutter Community",     "url": "https://medium.com/feed/flutter-community",        "lane": "Flutter"},
    {"name": "Reso Coder",            "url": "https://resocoder.com/feed",                       "lane": "Flutter"},  # verify

    # ===================== Engineering (big-tech blogs) ==============
    # Cross-cutting; high-volume. Comment out this whole block to mute it, or
    # trim to the mobile-strong subset. For one-feed coverage instead, use
    # Big Tech Digest: https://bigtechdigest.substack.com/feed
    # -- Strongest mobile-engineering content --
    {"name": "Engineering at Meta",   "url": "https://engineering.fb.com/feed/",                 "lane": "Engineering"},
    {"name": "Airbnb Engineering",    "url": "https://medium.com/feed/airbnb-engineering",       "lane": "Engineering"},
    {"name": "Pinterest Engineering", "url": "https://medium.com/feed/pinterest-engineering",    "lane": "Engineering"},
    {"name": "Lyft Engineering",      "url": "https://eng.lyft.com/feed",                        "lane": "Engineering"},
    {"name": "Uber Engineering",      "url": "https://www.uber.com/blog/engineering/rss/",       "lane": "Engineering"},  # verify (flaky)
    {"name": "LinkedIn Engineering",  "url": "https://www.linkedin.com/blog/engineering/rss",    "lane": "Engineering"},  # verify
    {"name": "Dropbox Tech",          "url": "https://dropbox.tech/feed",                        "lane": "Engineering"},  # verify
    {"name": "Reddit Engineering",    "url": "https://www.reddit.com/r/RedditEng/.rss",          "lane": "Engineering"},  # verify
    {"name": "DoorDash Engineering",  "url": "https://doordash.engineering/feed/",               "lane": "Engineering"},  # verify
    # -- Systems / infra / platform (broader, higher-volume) --
    {"name": "Netflix TechBlog",      "url": "https://netflixtechblog.com/feed",                 "lane": "Engineering"},
    {"name": "Cloudflare Blog",       "url": "https://blog.cloudflare.com/rss/",                 "lane": "Engineering"},
    {"name": "Spotify Engineering",   "url": "https://engineering.atspotify.com/feed/",          "lane": "Engineering"},
    {"name": "Slack Engineering",     "url": "https://slack.engineering/feed/",                  "lane": "Engineering"},
    {"name": "AWS Architecture",      "url": "https://aws.amazon.com/blogs/architecture/feed/",  "lane": "Engineering"},
    {"name": "Stripe Blog",           "url": "https://stripe.com/blog/feed.rss",                 "lane": "Engineering"},  # verify
    {"name": "GitHub Engineering",    "url": "https://github.blog/engineering/feed/",            "lane": "Engineering"},  # verify
    {"name": "Discord Engineering",   "url": "https://discord.com/blog/rss.xml",                 "lane": "Engineering"},  # verify
    {"name": "Shopify Engineering",   "url": "https://shopify.engineering/blog.atom",            "lane": "Engineering"},  # verify
    {"name": "Figma Engineering",     "url": "https://www.figma.com/blog/feed/",                 "lane": "Engineering"},  # verify

    # ===================== Your own blog (uncomment + set handle) =====
    # {"name": "My Hashnode",         "url": "https://YOUR-HANDLE.hashnode.dev/rss.xml",         "lane": "AI"},
]