# Little Treasure Agent

A modular finance agent for generating daily market summaries and portfolio tips.

## Features

- Fetches financial news using RSS feeds
- Retrieves fund and ETF data from Xueqiu
- Analyses potential sectors and existing positions
- Generates a markdown "情侣日报"
- Command line interface, can be extended to a web panel

## Usage

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the agent:

```bash
python -m src.main
```

Place your holdings in `positions.json` with format:

```json
[
  {"symbol": "AAPL", "profit": 0.05}
]
```
