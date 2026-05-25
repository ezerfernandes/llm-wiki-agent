---
title: "DSPy Tutorial — Yahoo Finance ReAct Agent"
type: source
tags: [dspy, tutorial, react, agent, tools, langchain, finance, yfinance, yahoo-finance]
date: 2026-05-24
source_file: raw/dspy-yahoo-finance-react-tutorial.md
---

## Summary

Official [[DSPy]] tutorial demonstrating a **three-tool [[react|ReAct]] agent** for **real-time financial analysis**: one [[LangChain]] tool (`YahooFinanceNewsTool`, converted to a [[DSPyTools|`dspy.Tool`]] via `Tool.from_langchain(...)`) plus two plain Python callables (`get_stock_price`, `compare_stocks`) wrapping the [[yfinance]] library. The full agent is a `dspy.Module` whose `forward` delegates to `dspy.ReAct(signature="financial_query -> analysis_response", tools=[...], max_iters=6)`. **First wiki receipt of `dspy.Tool.from_langchain(...)`** — the third documented construction path for [[DSPyTools|`dspy.Tool`]] alongside auto-wrapping plain Python callables and `dspy.Tool.from_mcp_tool(...)`. Also the **first wiki receipt of `allow_tool_async_sync_conversion=True` set as a global `dspy.configure(...)` flag** (the [[DSPyTools|DSPy Tools page]] presents it only as a per-block `dspy.context(...)` opt-in). No dataset, no optimizer, no benchmark — pure programming-stage walkthrough.

## Key Claims

- **`dspy.Tool.from_langchain(langchain_tool)` is a one-line LangChain→DSPy bridge.** The tutorial passes `YahooFinanceNewsTool()` straight through and gets back a `dspy.Tool` indistinguishable in the call site from a plain-function-wrapped tool — same Signature surface, same [[react|`dspy.ReAct`]] composition, same execution semantics. This is the **same decoupling pattern** the [[DSPyTools|Tools page]] documents for [[ModelContextProtocol|MCP]] via `Tool.from_mcp_tool(...)` ([[DSPyMCP]]).
- **Mixing tool-origin types in one ReAct toolset is supported and idiomatic.** The agent's `self.tools` list contains a LangChain-derived `Tool` instance and two raw Python callables side-by-side; [[react|`dspy.ReAct`]] auto-wraps the latter and treats both kinds uniformly.
- **`allow_tool_async_sync_conversion=True` is settable on the global config.** Up to this point the wiki only recorded the per-`with`-block form: `with dspy.context(allow_tool_async_sync_conversion=True): ...` ([[DSPyTools]]). This tutorial uses the **process-lifetime** form: `dspy.configure(lm=lm, allow_tool_async_sync_conversion=True)`. Both forms exist; the global form is appropriate when most/all tools in a program are async-backed (LangChain tools commonly are).
- **`max_iters=6`** is the explicit per-agent iteration budget — higher than the `max_iters=5` default-style example in [[DSPyTools]] but lower than the [[dspy-tutorial-rag-as-agent|HoVer multi-hop tutorial]] which leaves `max_iters` at its default. Six iterations is enough budget for a *fetch-news → fetch-price → fetch-comparison → reason → answer* loop on a moderately complex query.
- **Signature is a one-line string**: `"financial_query -> analysis_response"`. No `dspy.Signature` class, no field-level docstrings, no Pydantic types — the simplest legal Signature form. Consistent with the [[dspy-modules|`dspy.ReAct`]] canonical example pattern.
- **Tool surface is what the LM sees.** The `get_stock_price` and `compare_stocks` callables carry one-line docstrings (`"Get current stock price and basic info."` / `"Compare multiple stocks (comma-separated)."`) and explicit type hints (`ticker: str -> str`, `tickers: str -> str`). These four surfaces (name, docstring, type-hinted args, return type) are the **prompt-engineering interface for tool selection** the [[DSPyTools|Tools page]] makes explicit.
- **Tools return JSON-as-string, not structured objects.** Both helper functions `return json.dumps(...)` so the observation that flows back into the next ReAct reasoning step is text — consistent with [[react|ReAct]]'s think-act-observe convention where the *observe* slot is rendered into the prompt as a string.
- **Error handling lives in the tool, not the agent.** Each helper wraps its body in `try/except Exception as e: return f"Error: {str(e)}"`. The error message is **returned as a string** so [[react|ReAct]] sees it as a normal observation and can reason about whether to retry, adapt, or surface the failure — the wiki's first concrete receipt of *"tool-side error-as-observation"* as a [[react|ReAct]] integration pattern.
- **Sample output exposes a real production limitation honestly.** The tutorial's own sample response says *"the inability to access the latest news means that any significant developments...are unknown"* — the agent admits when the LangChain Yahoo Finance News tool fails and proceeds with only the price data it does have. This is the **first wiki receipt of a DSPy tutorial whose sample output documents a partial tool failure** rather than a clean success path.

## Key Quotes

> "Tool Integration: Seamlessly combine LangChain tools with DSPy ReAct"

> "Real-time Data: Access current market data and news"

> "Intelligent Reasoning: ReAct framework provides step-by-step analysis"

> "Many Langchain tools use async operations for better performance."

## Code Receipt — minimum reproducible agent

```python
import dspy
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from dspy.adapters.types.tool import Tool
import json
import yfinance as yf

lm = dspy.LM(model='openai/gpt-4o-mini')
dspy.configure(lm=lm, allow_tool_async_sync_conversion=True)

yahoo_finance_tool = YahooFinanceNewsTool()
finance_news_tool = Tool.from_langchain(yahoo_finance_tool)

def get_stock_price(ticker: str) -> str:
    """Get current stock price and basic info."""
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    info = stock.info
    current = hist['Close'].iloc[-1]
    prev = info.get('previousClose', current)
    pct = (current - prev) / prev * 100 if prev else 0
    return json.dumps({"ticker": ticker, "price": round(current, 2),
                       "change_percent": round(pct, 2),
                       "company": info.get('longName', ticker)})

def compare_stocks(tickers: str) -> str:
    """Compare multiple stocks (comma-separated)."""
    out = []
    for t in [s.strip().upper() for s in tickers.split(',')]:
        stock = yf.Ticker(t)
        hist = stock.history(period="1d")
        info = stock.info
        current = hist['Close'].iloc[-1]
        prev = info.get('previousClose', current)
        pct = (current - prev) / prev * 100 if prev else 0
        out.append({"ticker": t, "price": round(current, 2),
                    "change_percent": round(pct, 2)})
    return json.dumps(out)

class FinancialAnalysisAgent(dspy.Module):
    def __init__(self):
        super().__init__()
        self.tools = [finance_news_tool, get_stock_price, compare_stocks]
        self.react = dspy.ReAct(
            signature="financial_query -> analysis_response",
            tools=self.tools,
            max_iters=6,
        )
    def forward(self, financial_query: str):
        return self.react(financial_query=financial_query)

agent = FinancialAnalysisAgent()
print(agent(financial_query=
    "What's the latest news about Apple (AAPL) and how might it affect the stock price?"
).analysis_response)
```

## Import-Path Footnote

The tutorial uses `from dspy.adapters.types.tool import Tool` — the **module-path import** for `dspy.Tool`. This is the first wiki receipt of this import form; every prior DSPy tutorial uses the top-level `dspy.Tool` reference. Both forms refer to the same class; `dspy.adapters.types.tool.Tool` is the canonical module location and `dspy.Tool` is re-exported. The tutorial's module-path import is **necessary** here only because `Tool.from_langchain(...)` is invoked as a classmethod; `dspy.Tool.from_langchain(...)` would work identically.

## Position in the DSPy Tutorial Corpus

This is the **seventh wiki-corpus DSPy tutorial** and the **third agent-shaped one** (after [[dspy-customer-service-agent|customer-service agent]] and [[dspy-tutorial-rag-as-agent|HoVer multi-hop RAG-as-agent]]). Coverage map:

| Tutorial | Task shape | Tools | Optimizer | Lift |
|---|---|---|---|---|
| [[dspy-conversation-history]] | Multi-turn chatbot | — | — | — |
| [[dspy-customer-service-agent]] | 7-tool [[react\|ReAct]] over Pydantic domain | 7 Python tools | — | — |
| [[dspy-custom-module]] | 3-stage [[rag\|RAG]] template | [[ColBERTv2]] | — | — |
| [[dspy-tutorial-rag-as-agent]] | Multi-hop ReAct | 2 Wikipedia tools | [[MIPROv2]] medium + teacher/student | 8% → 41.67% |
| [[dspy-entity-extraction-tutorial]] | Decoder-LM NER | — | MIPROv2 medium | 86% → 93% |
| [[dspy-rag-tutorial]] | Single-hop RAG | retrieval | MIPROv2 medium | 42% → 61.1% |
| [[dspy-tutorial-math]] | Single-step [[chainofthought\|CoT]] | — | MIPROv2 medium + teacher/student | 74.0% → 88.57% |
| **dspy-yahoo-finance-react-tutorial** *(this page)* | **3-tool [[react\|ReAct]] over real-time market data** | **1 LangChain + 2 yfinance** | **— (no opt)** | **—** |

**What this tutorial uniquely contributes** to the DSPy-tutorial corpus:

1. **First receipt of `Tool.from_langchain(...)`** — the LangChain→DSPy tool bridge.
2. **First receipt of an external-data-source tool ecosystem** ([[yfinance]] + LangChain community tools) — prior agent tutorials use only Python-internal data ([[dspy-customer-service-agent]]'s Pydantic domain) or DSPy's own retrieval clients ([[ColBERTv2]] in [[dspy-tutorial-rag-as-agent]]).
3. **First receipt of `allow_tool_async_sync_conversion=True` on `dspy.configure(...)`** — the global form, not the per-`with`-block form.
4. **First DSPy tutorial whose sample output documents partial tool failure** rather than success-path-only output — the agent reports it could not fetch news and reasons from price data alone.
5. **First finance-domain DSPy tutorial** in the wiki, adding to the domain coverage (general QA, customer service, entity extraction, math, multi-hop QA).

## Tool-Origin Construction Paths — wiki state after this ingest

[[DSPyTools|`dspy.Tool`]] now has **three** documented construction paths in the wiki:

| Path | Source | First-receipt page |
|---|---|---|
| **Auto-wrap a plain Python callable** | `dspy.ReAct(..., tools=[fn])` or `dspy.Tool(fn)` | [[dspy-tools]] / [[react]] |
| **`Tool.from_mcp_tool(session, mcp_tool)`** | [[ModelContextProtocol\|MCP]] server descriptor | [[dspy-mcp]] / [[DSPyMCP]] |
| **`Tool.from_langchain(langchain_tool)`** | [[LangChain]] tool instance | **this tutorial** |

All three paths produce instances **indistinguishable** in downstream composition — [[react|`dspy.ReAct`]] consumes them uniformly, [[DSPyAdapters|Adapters]] serialize them uniformly, manual [[DSPyPredict|`dspy.Predict`]] with `tools: list[dspy.Tool]` input accepts any mixture. The `dspy.Tool` wrapper is therefore the **single integration point** between DSPy programs and the **outside tool ecosystem** — [[LangChain]] community tools, [[ModelContextProtocol|MCP]] servers, plain Python — without bespoke per-source plumbing.

## Connections

- [[DSPy]] — the framework being demonstrated.
- [[react|`dspy.ReAct`]] — the agent loop module; `max_iters=6`, one-line string Signature.
- [[DSPyTools|`dspy.Tool`]] — the tool wrapper; this tutorial adds the **third construction path** (`Tool.from_langchain`).
- [[DSPyModules]] — `FinancialAnalysisAgent` is a `dspy.Module` subclass with a `forward` method delegating to `dspy.ReAct`.
- [[DSPySignatures]] — `"financial_query -> analysis_response"` is the minimal one-line Signature.
- [[DSPyLM]] — `dspy.LM(model='openai/gpt-4o-mini')` is the configured language model.
- [[LangChain]] — source of the `YahooFinanceNewsTool`; converted via `Tool.from_langchain`.
- [[LangChainAgent]] — peer-framework agent abstraction; this tutorial shows the **inverse direction**: a LangChain tool consumed *by* a DSPy agent rather than a LangChain agent.
- [[yfinance]] — the Yahoo Finance Python library used by the two helper tools (`yf.Ticker(...)`, `.history(period="1d")`, `.info`). **New entity.**
- [[YahooFinance]] — the data source; the LangChain community tool wraps Yahoo Finance News. **New entity.**
- [[openai|OpenAI]] — provider for the `gpt-4o-mini` LM.
- [[GPT|GPT-4o-mini]] — the LM under the hood; same student model as the other recent DSPy tutorials.
- [[DSPyMCP]] / [[ModelContextProtocol]] — analogous tool-origin decoupling for MCP; the `Tool.from_langchain` path is the **LangChain analog** of `Tool.from_mcp_tool`.
- [[dspy-tools]] — canonical page for `dspy.Tool` API surface; this tutorial supplements with the LangChain bridge.
- [[dspy-tutorial-rag-as-agent]] / [[dspy-customer-service-agent]] — the wiki's other two ReAct-agent tutorials; this is the third, distinguished by real-time external-data tools and LangChain integration.
- [[2210.03629]] *(if present)* / the [[react|ReAct]] page — Yao et al. 2022 ReAct paper; the prompting pattern this tutorial operationalizes through DSPy.
- [[ToolUse]] — the wiki's general tool-use concept; this tutorial is a small, runnable receipt.

## Contradictions

None with the existing wiki. The tutorial **resolves a latent ambiguity** in the [[DSPyTools|DSPy Tools page]]:
- The Tools page presents `allow_tool_async_sync_conversion` only via `dspy.context(...)` (a per-block context manager). This tutorial documents it as a `dspy.configure(...)` kwarg (process-lifetime). Both forms are legal; the Tools page is incomplete on the configure-time form.

It also **extends** rather than contradicts the [[DSPyTools|Tools page]]'s tool-origin discussion: the Tools page lists plain Python and MCP as construction sources; LangChain via `Tool.from_langchain` is a third source not enumerated in that page's text.

## Scope-Limit Gaps

- **No optimizer.** The tutorial doesn't run [[MIPROv2]] / [[GEPA]] / [[BootstrapFewShot]] against the agent — there's no labeled financial-query dataset, no metric, no train/dev split. Compare with [[dspy-tutorial-rag-as-agent]], which optimizes a multi-hop ReAct agent over [[HoVer]] for an 8% → 41.67% lift.
- **No metric.** No evaluation harness — the tutorial demonstrates the **programming stage** only, not the **evaluation** or **optimization** stages of the DSPy three-stage workflow.
- **No assertions / guardrails.** No [[DSPyAssert]] / [[DSPyGuardrails]] usage; the financial-advice domain would plausibly benefit from output validation (no hard buy/sell recommendations, no specific price predictions, etc.).
- **No `trajectory` inspection.** [[react|`dspy.ReAct`]] returns a `result.trajectory` field recording every think-act-observe step (see [[DSPyTools]]); the tutorial doesn't print or analyze it.
- **No `dspy.inspect_history()`.** No exposed prompt; readers can't see how the LM sees the three tools or how the *thought→action→observation* messages are formatted.
- **No cost / latency characterization.** `max_iters=6` could mean six round-trips through `gpt-4o-mini` plus six tool calls per query; the tutorial doesn't characterize the cost envelope.
- **Tool failure handling is silent.** The sample output reveals the news tool failed, but the agent still produced a response. There's no explicit retry / fallback policy at the agent level — the tutorial leaves graceful-degradation behavior to ReAct's reasoning step alone.
- **No mixture with manual handling.** The [[DSPyTools|Tools page]]'s **paired** rubric (managed `dspy.ReAct` vs manual `dspy.Predict` with `tools: list[dspy.Tool]` input) — this tutorial picks the managed path without comment.
- **Async surface not exercised.** The `allow_tool_async_sync_conversion=True` flag is enabled but the tutorial code calls the agent synchronously; the async-call path (`tool.acall(...)`) is not demonstrated.
