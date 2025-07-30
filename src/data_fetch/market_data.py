"""Market data retrieval utilities."""

from __future__ import annotations

import requests
from typing import List, Dict


def fetch_xueqiu_fund(symbol: str) -> Dict:
    """Fetch fund data from Xueqiu.

    Parameters
    ----------
    symbol : str
        Fund or ETF symbol on Xueqiu.

    Returns
    -------
    Dict
        Raw JSON response from Xueqiu.
    """
    url = f"https://stock.xueqiu.com/v5/stock/f10/cn/{symbol}.json"
    headers = {
        "User-Agent": "Mozilla/5.0",
    }
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code != 200:
        return {}
    return resp.json()


def fetch_sector_etfs() -> List[str]:
    """Return example sector ETF symbols to monitor."""
    return ["SH513100", "SZ159949", "SH510300"]
