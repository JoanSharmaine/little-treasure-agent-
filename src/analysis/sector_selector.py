"""Sector selection logic."""

from __future__ import annotations

from typing import List, Dict


POTENTIAL_SECTORS: List[str] = []


def analyze_potential_sectors(fund_data: List[Dict]) -> List[str]:
    """Very naive sector scoring logic.

    Parameters
    ----------
    fund_data : List[Dict]
        List of fund data dictionaries returned from market_data

    Returns
    -------
    List[str]
        Symbols of sectors worth monitoring.
    """
    sectors = []
    for data in fund_data:
        info = data.get("data", {})
        pe_ratio = info.get("pe_ttm") or 0
        if pe_ratio and pe_ratio < 20:  # simple filter
            sectors.append(info.get("symbol"))
    return sectors
