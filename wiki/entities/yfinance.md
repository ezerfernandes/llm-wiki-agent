---
title: "yfinance"
type: entity
tags: [library, python, open-source, finance, market-data]
sources: [dspy-yahoo-finance-react-tutorial]
last_updated: 2026-05-24
---

# yfinance

Open-source Python library that scrapes / wraps [[YahooFinance|Yahoo Finance]] to provide free programmatic access to market data — historical OHLCV, current quotes, company metadata, dividends, splits. Distributed on PyPI; `pip install yfinance`. Canonical entry points: `yf.Ticker(symbol)` returns a per-ticker object whose `.history(period=..., interval=...)` yields a [[pandas|Pandas]] DataFrame of OHLCV bars and whose `.info` returns a dict of company / instrument metadata (`longName`, `previousClose`, market-cap, sector, etc.).

## Receipt of usage

First wiki receipt: [[dspy-yahoo-finance-react-tutorial|DSPy Yahoo Finance ReAct tutorial]]. The tutorial uses yfinance as the **data substrate for two [[DSPyTools|`dspy.Tool`]] helpers** — `get_stock_price(ticker)` and `compare_stocks(tickers)` — that wrap `yf.Ticker(t).history(period="1d")` + `.info` into JSON-string returns consumable as [[react|ReAct]] observations:

```python
import yfinance as yf

stock = yf.Ticker("AAPL")
hist = stock.history(period="1d")
info = stock.info
current_price = hist['Close'].iloc[-1]
previous_close = info.get('previousClose', current_price)
```

## Connections

- [[YahooFinance]] — the upstream data source yfinance wraps.
- [[pandas|Pandas]] — `.history()` returns a Pandas DataFrame.
- [[LangChain]] — LangChain's community tool ecosystem includes `YahooFinanceNewsTool`, which complements yfinance's price-and-metadata surface with news scraping; both surfaces compose in the DSPy ReAct agent.
- [[dspy-yahoo-finance-react-tutorial]] — first wiki receipt; uses yfinance in two DSPy tool functions.
- [[DSPyTools]] — the wrapper that turns yfinance-calling functions into LM-callable tools.
- [[ToolUse]] — yfinance-as-a-DSPy-tool is a concrete tool-use receipt.
