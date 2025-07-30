"""Command line interface for Little Treasure Agent."""
from __future__ import annotations

import argparse
from typing import Dict

from .news import fetch_news
from .analyzer import analyze_portfolio, suggest_rebalance
from .report import generate_report
from .sectors import identify_top_sectors


def main() -> None:
    parser = argparse.ArgumentParser(description="Little Treasure Agent")
    parser.add_argument("--holdings", nargs="*", default=[], help="Holdings as SYMBOL=QTY")
    args = parser.parse_args()

    holdings: Dict[str, float] = {}
    for item in args.holdings:
        symbol, qty = item.split("=")
        holdings[symbol.upper()] = float(qty)

    news = fetch_news()
    analysis = analyze_portfolio(holdings)
    suggestions = suggest_rebalance(analysis)
    sectors = identify_top_sectors()
    report = generate_report(news, analysis)
    if sectors:
        report += "\n\n推荐关注板块: " + ", ".join(sectors)
    if suggestions:
        trades = "; ".join(f"{sym}:{qty:+.2f}" for sym, qty in suggestions)
        report += f"\n\n调仓建议: {trades}"
    print(report)


if __name__ == "__main__":
    main()
