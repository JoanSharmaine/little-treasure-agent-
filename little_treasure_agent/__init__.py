"""Little Treasure Agent package."""

from .news import fetch_news
from .data import get_fund_data
from .analyzer import analyze_portfolio
from .report import generate_report
from .watchlist import Watchlist

__all__ = [
    "fetch_news",
    "get_fund_data",
    "analyze_portfolio",
    "generate_report",
    "Watchlist",
]
