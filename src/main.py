"""Entry point for the Little Treasure Agent CLI."""

from __future__ import annotations

import json
from pathlib import Path

from .news.news_fetcher import fetch_latest
from .data_fetch.market_data import fetch_xueqiu_fund, fetch_sector_etfs
from .analysis.sector_selector import analyze_potential_sectors
from .analysis.portfolio import analyze_positions
from .report.daily_report import generate_markdown_report


POSITIONS_FILE = Path("positions.json")


def load_positions() -> list:
    if POSITIONS_FILE.exists():
        return json.loads(POSITIONS_FILE.read_text())
    return []


def main() -> None:
    """Run daily analysis and output markdown report."""
    news = fetch_latest()
    symbols = fetch_sector_etfs()
    fund_data = [fetch_xueqiu_fund(sym) for sym in symbols]
    sectors = analyze_potential_sectors(fund_data)
    positions = load_positions()
    tips = analyze_positions(positions)
    tips.extend([f"Monitor sector {s}" for s in sectors])
    report = generate_markdown_report(news, tips)
    print(report)


if __name__ == "__main__":
    main()
