"""Sector utility functions."""
from __future__ import annotations

from typing import List, Dict
import yfinance as yf

# Map simple sector names to representative ETF tickers
SECTOR_ETFS: Dict[str, str] = {
    "technology": "XLK",
    "financials": "XLF",
    "healthcare": "XLV",
    "industrials": "XLI",
    "energy": "XLE",
}


def identify_top_sectors(limit: int = 3) -> List[str]:
    """Return sectors with the best performance over the last day."""
    changes: List[tuple[str, float]] = []
    for name, ticker in SECTOR_ETFS.items():
        data = yf.Ticker(ticker).history(period="2d")
        if len(data) < 2:
            continue
        pct = (data["Close"].iloc[-1] / data["Close"].iloc[-2]) - 1
        changes.append((name, pct))
    changes.sort(key=lambda x: x[1], reverse=True)
    return [name for name, _ in changes[:limit]]
