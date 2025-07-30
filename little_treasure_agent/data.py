"""Market data utilities."""
from __future__ import annotations

from datetime import datetime
from typing import Optional

import yfinance as yf


def get_fund_data(symbol: str, start: Optional[str] = None, end: Optional[str] = None):
    """Retrieve historical price data for a fund, ETF or stock symbol.

    Parameters
    ----------
    symbol : str
        Ticker symbol to fetch.
    start : Optional[str]
        Optional start date in ``YYYY-MM-DD`` format.
    end : Optional[str]
        Optional end date in ``YYYY-MM-DD`` format.
    """
    start_dt = datetime.strptime(start, "%Y-%m-%d") if start else None
    end_dt = datetime.strptime(end, "%Y-%m-%d") if end else None
    ticker = yf.Ticker(symbol)
    return ticker.history(start=start_dt, end=end_dt)
