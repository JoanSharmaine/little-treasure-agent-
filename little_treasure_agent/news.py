"""News fetching utilities."""
from typing import List
import feedparser

NEWS_SOURCES = [
    # Google News RSS feed focused on financial topics
    "https://news.google.com/rss/search?q=%E6%94%BF%E7%AD%96+OR+%E9%87%91%E8%9E%8D%E7%A7%91%E6%8A%80+OR+%E7%A8%B3%E5%AE%9A%E5%B8%81+OR+%E7%94%B5%E5%95%86&hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
    "https://news.google.com/rss/search?q=finance+policy+OR+fintech+OR+stablecoin+OR+industry&hl=en-US&gl=US&ceid=US:en",
]

def fetch_news(limit: int = 5) -> List[str]:
    """Fetch latest financial news headlines from RSS feeds.

    Parameters
    ----------
    limit : int
        Maximum number of news items to return.

    Returns
    -------
    List[str]
        A list of news headlines.
    """
    headlines: List[str] = []
    for url in NEWS_SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit]:
            headlines.append(entry.title)
    return headlines[:limit]
