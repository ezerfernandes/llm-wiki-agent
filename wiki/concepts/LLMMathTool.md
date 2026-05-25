---
title: "llm-math (LangChain built-in calculator tool)"
type: concept
tags: [langchain, tool, calculator, agent]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# `llm-math` — LangChain Built-in Calculator Tool

**`load_tools(["llm-math"], llm=llm)`** loads [[LangChain]]'s built-in **calculator tool** — a small wrapper that uses an LLM to convert natural-language math into an executable Python expression and then computes it. Ch 7's worked example uses it to convert *"$2,249.00 USD at 0.85 EUR per USD"* into `2249 * 0.85` → `1911.65`.

## Why this tool exists

Per [[hands-on-llm-ch07-advanced-text-generation|Ch 7]]:

> *"LLMs are notoriously bad at mathematical problems and often fail at solving simple math-based tasks but they could do much more if we provide access to a calculator."*

The calculator is the **canonical [[CapabilityExtension|capability-extension]] tool** (per [[ai-engineering-ch06-rag-agents|Huyen Ch 6's]] taxonomy) — it adds an arithmetic-evaluation capability the LLM does not have natively.

## Worked usage

```python
from langchain.agents import load_tools
tools = load_tools(["llm-math"], llm=openai_llm)
tools.append(search_tool)   # plus the DuckDuckGo tool

agent = create_react_agent(openai_llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
agent_executor.invoke({"input": "What is the current price of a MacBook Pro in USD? How much would it cost in EUR if the exchange rate is 0.85 EUR for 1 USD?"})
```

The agent uses `llm-math` in the **second** ReAct cycle after [[DuckDuckGoSearchResults]] has returned the USD price in the first.

## How `llm-math` works internally

The tool is a small chain:

1. **Translate** — an LLM call converts the natural-language math (*"2249 USD times 0.85"*) into a Python expression (`2249 * 0.85`).
2. **Execute** — Python's `numexpr` library evaluates the expression deterministically.
3. **Return** — the numeric result is passed back as an Observation in the ReAct trajectory.

The `llm` kwarg in `load_tools(["llm-math"], llm=llm)` is the **translator LLM**, not the agent LLM — they can be the same or different.

## Position in the agent tool surface

Per Ch 7, `llm-math` is one of a wider taxonomy of pre-built [[LangChain]] tools — search engines, weather APIs, etc. *"Imagine we extend this with dozens of other tools, like a search engine or a weather API. Suddenly, the capabilities of LLMs increase significantly."*

## Connections

- [[LangChain]] — the framework.
- [[LangChainAgent]] — the agent that orchestrates this tool.
- [[DuckDuckGoSearchResults]] — the search-tool peer used in the same Ch 7 example.
- [[ToolInventory]] / [[ToolUse]] — the agent-design pattern this tool participates in.
- [[CapabilityExtension]] — Huyen Ch 6's tool-category name for calculators / code interpreters / OCR.
- [[react|ReAct]] — the framework that drives the tool selection.
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

Ch 7's worked calculator tool. The chapter uses it to demonstrate how a simple add-on tool can extend an LLM's capability surface — *"the calculator tool"* is the most pedagogically efficient example of [[ToolUse|tool use]] because LLM arithmetic-failures are well known and well-motivated. The pairing with [[DuckDuckGoSearchResults]] is the chapter's argument that **the value of agents is in tool composition**, not in any single tool.
