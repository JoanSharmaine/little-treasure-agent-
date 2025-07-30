"""Command line interface for Little Treasure Agent."""
from __future__ import annotations

import argparse
from typing import Dict

from .news import fetch_news
from .analyzer import analyze_portfolio
from .report import generate_report


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
    report = generate_report(news, analysis)
    print(report)


if __name__ == "__main__":
    main()
