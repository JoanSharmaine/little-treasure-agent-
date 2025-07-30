"""Portfolio analysis utilities."""
from __future__ import annotations

from typing import Dict, List, Tuple
import pandas as pd

from .data import get_fund_data


def analyze_portfolio(holdings: Dict[str, float]) -> pd.DataFrame:
    """Analyze a simple holdings dictionary and return daily changes.

    Parameters
    ----------
    holdings : Dict[str, float]
        Mapping of symbol to quantity held.

    Returns
    -------
    pd.DataFrame
        DataFrame summarizing latest price and allocation.
    """
    records: List[Dict[str, float]] = []
    total_value = 0.0
    for symbol, qty in holdings.items():
        data = get_fund_data(symbol, start=None, end=None)
        if data.empty:
            price = 0.0
        else:
            price = data["Close"].iloc[-1]
        value = price * qty
        total_value += value
        records.append({"symbol": symbol, "price": price, "quantity": qty, "value": value})

    df = pd.DataFrame(records)
    if total_value > 0:
        df["allocation"] = df["value"] / total_value
    else:
        df["allocation"] = 0.0
    return df


def suggest_rebalance(df: pd.DataFrame) -> List[Tuple[str, float]]:
    """Suggest trades to rebalance portfolio to equal weights."""
    if df.empty:
        return []
    n = len(df)
    target = 1.0 / n
    suggestions: List[Tuple[str, float]] = []
    for _, row in df.iterrows():
        diff = target - row["allocation"]
        if abs(diff) < 0.01:
            continue
        trade_qty = diff * df["value"].sum() / row["price"]
        suggestions.append((row["symbol"], trade_qty))
    return suggestions
