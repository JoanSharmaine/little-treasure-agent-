"""News fetching utilities for Little Treasure Agent."""

from __future__ import annotations

import feedparser
from typing import List


RSS_FEEDS = [
    "https://rss.cnn.com/rss/money_news_international.rss",
    "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
]


def fetch_latest(limit: int = 10) -> List[dict]:
    """Fetch latest finance related news from predefined RSS feeds.

    Parameters
    ----------
    limit : int
        Maximum number of articles to return.

    Returns
    -------
    List[dict]
        Parsed news entries with title, link, and summary.
    """
    articles = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title"),
                "link": entry.get("link"),
                "summary": entry.get("summary"),
            })
            if len(articles) >= limit:
                return articles
    return articles

if __name__ == "__main__":
    for article in fetch_latest():
        print(article["title"])
