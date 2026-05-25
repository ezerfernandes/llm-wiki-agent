---
title: "Yahoo Finance"
type: entity
tags: [data-source, finance, news, market-data, web-service]
sources: [dspy-yahoo-finance-react-tutorial]
last_updated: 2026-05-24
---

# Yahoo Finance

Long-running consumer finance portal (`finance.yahoo.com`) providing free real-time and historical equity / index / FX / crypto quotes, company filings, analyst estimates, and a continuous financial-news stream. Operated by Yahoo (currently owned by [[Apollo|Apollo Global Management]] via the 2021 spin-out from Verizon). No official public API; programmatic access happens via community libraries that scrape the public endpoints — most prominently [[yfinance]] for market data and the [[LangChain]] community tool `YahooFinanceNewsTool` for the news stream.

## Receipt of usage

First wiki receipt: [[dspy-yahoo-finance-react-tutorial|DSPy Yahoo Finance ReAct tutorial]]. The tutorial exposes **two distinct Yahoo Finance surfaces** to a [[DSPy]] [[react|ReAct]] agent:
- **Market data** — via [[yfinance]] (`yf.Ticker.history(...)` / `.info`) for current price + percent change + company metadata.
- **News stream** — via LangChain's `langchain_community.tools.yahoo_finance_news.YahooFinanceNewsTool`, bridged into DSPy through `dspy.Tool.from_langchain(...)`.

The sample output documents that the news tool can fail at runtime ("the inability to access the latest news means..."); Yahoo Finance access via scraping is therefore **not guaranteed** — the agent must handle partial-data conditions.

## Connections

- [[yfinance]] — the dominant community Python library scraping Yahoo Finance market data.
- [[LangChain]] — its `langchain-community` package ships `YahooFinanceNewsTool` for the news stream.
- [[dspy-yahoo-finance-react-tutorial]] — first wiki receipt; uses both surfaces.
- [[BloombergGPT]] — institutional analog of *"finance-domain LLM context"*; Bloomberg's data is paid and closed, Yahoo's is free and scraped — different tier of the same domain.
