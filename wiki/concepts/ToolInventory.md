---
title: "Tool Inventory"
type: concept
tags: [agents, tools, planning]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Tool Inventory

**Tool inventory** is the set of tools an agent has access to. Per [[ChipHuyen|Huyen]] in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]:

> *"Since an agent's tool inventory determines what an agent can do, it's important to think through what and how many tools to give an agent. More tools give an agent more capabilities. However, the more tools there are, the more challenging it is to understand and utilize them well."*

## Three categories

Huyen organizes tools into three families:

1. **[[KnowledgeAugmentation|Knowledge augmentation]]** — text retrievers, image retrievers, SQL executors, web browsers, internal people search, Slack retrieval, email readers.
2. **[[CapabilityExtension|Capability extension]]** — calculators, [[CodeInterpreter|code interpreters]], image captioners, OCR, translators, LaTeX compilers, [[DALLE|DALL-E]] for image generation.
3. **[[WriteAction|Write actions]]** — tools that mutate state (SQL writes, email sends, bank transfers).

## The inventory-size trade-off

A canonical wiki signal of this trade-off — from agents Huyen cites:

| Agent | Tools | Source |
|---|---|---|
| [[Toolformer]] | 5 | Schick et al. 2023 |
| [[Chameleon]] | 13 | Lu et al. 2023 |
| [[Gorilla]] | 1,645 APIs | Patil et al. 2023 |

More tools → more capability ceiling, but harder selection and longer tool-description prompts. Tool descriptions for a 1,645-API inventory cannot fit in any model's context — Gorilla must use retrieval *over its own tool inventory* to handle this.

## Tactical guidance

Per Ch 6 — *"how to decide"*:

- **Ablation study**: drop each tool, measure performance impact. If a tool can be removed without a performance drop, remove it.
- **Tool-call distribution**: plot which tools are most/least used.
- **Per-tool error analysis**: find tools the agent frequently misuses; rewrite, replace, or remove them.
- **Comparison**: evaluate the agent with different tool subsets.

## AI-created tools

[[VoyagerAgent|Voyager]] (Wang et al. 2023) introduced a **skill manager** that adds new agent-created skills (coding programs) back to the inventory — a tool inventory that grows during operation.

[[Chameleon]] introduced **tool transition** analysis — the conditional probability of using tool Y after tool X. Frequently-paired tools can be combined into a composite tool.

## Connections

- [[Agent]] — what a tool inventory is part of.
- [[KnowledgeAugmentation]] / [[CapabilityExtension]] / [[WriteAction]] — the three tool categories.
- [[Toolformer]] / [[Chameleon]] / [[Gorilla]] — concrete inventories at different scales.
- [[VoyagerAgent]] — AI-created-tool extension.
- [[FunctionCalling]] — the API surface that exposes tool inventories.
- [[Planning]] — the agent subsystem that selects tools from the inventory.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch07-advanced-text-generation]] — Ch 7's two-tool LangChain inventory (DuckDuckGo + llm-math).

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

Ch 7 of *Hands-On LLMs* operationalizes the tool-inventory concept as a **two-tool [[LangChain]] inventory** in the worked [[LangChainAgent|`create_react_agent` + `AgentExecutor`]] receipt:

```python
from langchain.agents import load_tools, Tool
from langchain.tools import DuckDuckGoSearchResults
search = DuckDuckGoSearchResults()
search_tool = Tool(name="duckduck", description="A web search engine. Use this to as a search engine for general queries.", func=search.run)
tools = load_tools(["llm-math"], llm=openai_llm)
tools.append(search_tool)
```

Both tools sit in **non-write-action** categories (per Huyen Ch 6's taxonomy): [[DuckDuckGoSearchResults|DuckDuckGo]] is [[KnowledgeAugmentation|knowledge augmentation]]; [[LLMMathTool|llm-math]] is [[CapabilityExtension|capability extension]]. The chapter's broader claim — *"imagine we extend this with dozens of other tools, like a search engine or a weather API. Suddenly, the capabilities of LLMs increase significantly"* — points at the inventory-size frontier Huyen names with [[Gorilla]] (1,645 APIs). Ch 7 stays at the **minimal multi-tool** end (2 tools — enough to require selection but small enough to fit in the ReAct prompt).
