---
title: "langchain.tools.DuckDuckGoSearchResults"
type: concept
tags: [langchain, tool, search, agent, duckduckgo]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# `langchain.tools.DuckDuckGoSearchResults`

The [[LangChain]] Python class wrapping the [[DuckDuckGoSearch|DuckDuckGo]] web search engine as an agent-callable tool. Returns the top-N search results (title + snippet + URL) as a single string the LLM can read in its Observation step.

## Usage in Hands-On LLMs Ch 7

```python
from langchain.agents import load_tools, Tool
from langchain.tools import DuckDuckGoSearchResults

search = DuckDuckGoSearchResults()
search_tool = Tool(
    name="duckduck",
    description="A web search engine. Use this to as a search engine for general queries.",
    func=search.run,
)

tools = load_tools(["llm-math"], llm=openai_llm)
tools.append(search_tool)
```

The `Tool(name, description, func)` wrapping pattern is the **canonical way** to expose any callable to an agent — what the LLM sees in its prompt is the `name` (matched against `Action: ...`) and the `description` (the LLM reads this when choosing which tool to call).

## Why this pattern matters

The three fields of `Tool(...)` are the **interface contract** between the agent's LLM and the underlying function:

| Field | Role | LLM sees it as |
|---|---|---|
| `name` | The tool's identifier | The string the LLM must emit after `Action:` to call this tool |
| `description` | What the tool does (free text) | The prompt-level documentation the LLM reads to choose the right tool |
| `func` | The Python callable | Invisible to the LLM; called by `AgentExecutor` when the tool name matches |

A **bad description** is the most common cause of bad tool selection — if the LLM doesn't know what a tool does, it won't pick it correctly.

## Position in the agent example

Ch 7 uses `DuckDuckGoSearchResults` alongside `llm-math` as the **two-tool inventory** for the MacBook Pro example. The agent uses it in cycle 1 (look up price), then `llm-math` in cycle 2 (convert USD to EUR). This is the **minimal multi-tool ReAct agent** — enough tools to require selection (the LLM must choose between them at each step) without the inventory-size complexity Huyen Ch 6 names for [[Gorilla|1,645-tool inventories]].

## Connections

- [[LangChain]] — the framework.
- [[DuckDuckGoSearch]] — the underlying search engine.
- [[LLMMathTool]] — the calculator tool paired with this one in Ch 7.
- [[LangChainAgent]] — the agent that orchestrates the tool calls.
- [[ToolInventory]] / [[ToolUse]] — the broader agent-design concepts.
- [[react|ReAct]] — the prompting pattern this tool plays into (Observation step).
- [[KnowledgeAugmentation]] — Huyen Ch 6's tool category this belongs to.
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

Ch 7's worked search-tool wrapping. The chapter chose this specific tool because (a) DuckDuckGo requires no API key — reproducible by every reader — and (b) `Tool(name, description, func)` is the **simplest possible interface** for exposing a callable to an agent, making the wrapping pattern transparent. The chapter's broader point about [[ToolUse|tool use]] — *"imagine we extend this with dozens of other tools, like a search engine or a weather API. Suddenly, the capabilities of LLMs increase significantly"* — is operationalized by this one wrapping.
