# Little Treasure Agent

This project provides a small command-line assistant for daily financial summaries. It fetches key headlines, pulls price data via `yfinance`, analyses a list of holdings and suggests a simple equal-weight rebalancing strategy. The output is a short Markdown bulletin in Chinese.

## Usage

Install requirements and run the CLI with your holdings expressed as `SYMBOL=QTY` pairs:

```bash
pip install -r requirements.txt
python -m little_treasure_agent.cli --holdings AAPL=10 NVDA=5
```

The script will print a markdown report including news, portfolio allocation and recommended trades.

## Disclaimer

This repository is a toy demonstration and **does not constitute financial advice**. Data is fetched from public APIs and may be inaccurate. Use at your own risk.
