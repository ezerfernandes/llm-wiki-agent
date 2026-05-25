---
title: "DuckDuckGo Search"
type: entity
tags: [search-engine, web-search, privacy, tool]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# DuckDuckGo Search

**DuckDuckGo** is a privacy-focused web search engine (duckduckgo.com) that does not track users or log queries. From an LLM-agent perspective it is one of the most commonly wrapped **web search tools** because its query API is unauthenticated and free (no API key required), making it the easiest [[KnowledgeAugmentation|knowledge-augmentation]] tool to give an [[Agent|agent]] in tutorial material.

## In Hands-On LLMs Ch 7

[[hands-on-llm-ch07-advanced-text-generation|Ch 7]] uses DuckDuckGo as the chapter's worked **web search tool** — wrapped via [[DuckDuckGoSearchResults|`langchain.tools.DuckDuckGoSearchResults`]] and registered as a custom [[LangChain]] `Tool` for use inside the ReAct agent example (the MacBook Pro price-conversion benchmark).

```python
from langchain.tools import DuckDuckGoSearchResults
search = DuckDuckGoSearchResults()
search_tool = Tool(
    name="duckduck",
    description="A web search engine. Use this to as a search engine for general queries.",
    func=search.run,
)
```

The agent uses it in the first ReAct cycle to look up *"current price of MacBook Pro in USD"*, returning **$2,249.00**, which the [[LLMMathTool|llm-math]] tool then converts to EUR in the second cycle.

## Connections

- [[DuckDuckGoSearchResults]] — the [[LangChain]] Python class wrapping DuckDuckGo for tool use.
- [[LangChain]] — the framework providing the wrapper.
- [[LangChainAgent]] — the agent that orchestrates the search calls.
- [[ToolInventory]] / [[ToolUse]] — the agent-design concepts.
- [[KnowledgeAugmentation]] — Huyen Ch 6's tool category DuckDuckGo belongs to.
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

Ch 7's worked search-tool. The chapter chose DuckDuckGo (vs Google / Bing) explicitly because it requires no API key — *"a web search engine. Use this to as a search engine for general queries"* — making the tutorial reproducible without account creation. The choice is pedagogically motivated: the *idea* of giving an agent web access matters, not the specific search backend.
