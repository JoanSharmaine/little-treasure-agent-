"""Portfolio analysis module."""

from __future__ import annotations

from typing import List, Dict


def analyze_positions(positions: List[Dict]) -> List[str]:
    """Analyse positions and provide rebalance suggestions.

    Parameters
    ----------
    positions : List[Dict]
        List of holdings with symbol and quantity.

    Returns
    -------
    List[str]
        Simple text suggestions for each position.
    """
    suggestions = []
    for pos in positions:
        if pos.get("profit", 0) < -0.05:
            suggestions.append(f"Consider reducing {pos['symbol']} due to drawdown")
        elif pos.get("profit", 0) > 0.1:
            suggestions.append(f"Take some profit on {pos['symbol']}")
    return suggestions
