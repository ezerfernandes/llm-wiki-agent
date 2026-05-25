---
title: "Tavily"
type: entity
tags: [tool, search-engine, web-search, ai-search, retrieval]
sources: [dspy-observability-tutorial]
last_updated: 2026-05-24
---

# Tavily

AI-powered web search engine providing **real-time information from the web**, designed as a retrieval primitive for LLM applications. Per the [[dspy-observability-tutorial|DSPy observability tutorial]]: *"Tavily is an AI-powered search engine that provides real-time information from the web."*

## Role in the DSPy observability tutorial

Tavily appears as the **fix** for a [[DSPyObservability|stale-retrieval diagnosis]]. The tutorial's worked example uses a [[ColBERTv2]]-backed Wikipedia retrieval whose underlying dump pre-dates 2024, causing a [[react|`dspy.ReAct`]] agent to return outdated answers (Shohei Ohtani's pre-Dodgers team). After [[MLflow]] tracing surfaces the bug, the resolution is to **wrap a Tavily search call as a [[DSPyTools|`dspy.Tool`]]** and substitute it into the agent's tool list:

```python
agent = dspy.ReAct("question -> answer", tools=[tavily_search])
```

The substitution alone fixes the bug — the rest of the program (signature, optimizer state, evaluation harness) is unchanged.

## Position vs other retrieval tools in the corpus

| Tool | Backing data | Freshness | Wiki page |
|---|---|---|---|
| [[ColBERTv2]] | Static Wikipedia dump (typically 2018-vintage in DSPy demos) | Frozen at dump date | [[ColBERTv2]] |
| **Tavily** | Live web | Real-time | This page |

Tavily is the **freshness counterpoint** to ColBERTv2 in the [[DSPy]] tutorial corpus: same `dspy.Tool` integration seam, opposite freshness posture. For questions whose answer depends on recent world state, swapping ColBERTv2 → Tavily is the canonical fix.

## API surface

The tutorial does not include the Tavily API key wiring in detail. Tavily exposes a standard HTTP API with bearer-token authentication; the [[DSPyTools|`dspy.Tool`]] wrapper is a plain callable around the HTTP client.

## Tracked sources

- **[[dspy-observability-tutorial]]** (2026-05-24) — first wiki receipt; documents Tavily as the recommended web-search [[DSPyTools|`dspy.Tool`]] for fixing stale-retrieval bugs.
