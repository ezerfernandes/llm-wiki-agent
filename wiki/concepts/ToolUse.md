---
title: "Tool Use"
type: concept
tags: [agents, tools, llm, tool-use, function-calling]
sources: [hands-on-llm-ch07-advanced-text-generation, ai-engineering-ch06-rag-agents]
last_updated: 2026-05-23
---

# Tool Use

**Tool use** is the general technique of giving an LLM access to external functions (calculators, search engines, APIs, code interpreters, etc.) that it can call to extend its capability surface. The **action half** of [[react|ReAct]]'s Thought / Action / Observation cycle. Treated extensively in [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]] and [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]].

## Why tool use matters

The motivating use case Ch 7 names is calculator-assisted math — *"LLMs are notoriously bad at mathematical problems and often fail at solving simple math-based tasks but they could do much more if we provide access to a calculator."* The structural generalization: any capability the LLM lacks (precise arithmetic, real-time information, code execution, persistent storage, world-mutating actions) can be exposed as a tool.

## The three tool categories (Huyen Ch 6)

Per [[ToolInventory|Huyen Ch 6]]:

| Category | Examples | Risk profile |
|---|---|---|
| **[[KnowledgeAugmentation|Knowledge augmentation]]** | Search engines, retrievers, SQL readers, email readers | Low (read-only) |
| **[[CapabilityExtension|Capability extension]]** | Calculators, code interpreters, OCR, translators | Low / medium |
| **[[WriteAction|Write actions]]** | SQL writes, email sends, bank transfers | **High — irreversible** |

Ch 7's two-tool agent (DuckDuckGo + llm-math) lives entirely in the first two categories — *low-stakes* tools.

## Tool-use frameworks

| Framework | Tool API |
|---|---|
| [[LangChain]] | `langchain.tools.Tool(name, description, func)` — wrap any callable; `load_tools([...], llm=llm)` for built-ins |
| [[DSPy]] | `dspy.Tool(func)` — wrap any callable; `dspy.ToolCalls` as a Signature output type |
| [[ModelContextProtocol|MCP]] | Protocol-level tool descriptor (standalone tool server) |
| OpenAI / Anthropic native | `tools=[...]` in chat-completion API; JSON-schema-typed |

## The ReAct pattern

[[react|ReAct]] (Yao et al. 2022) is the canonical tool-use prompting pattern: the LLM thinks, calls a tool, observes the result, then thinks again. Ch 7's LangChain `create_react_agent` is one operationalization; `dspy.ReAct` is another.

## The safety / reliability concern

Tool use is **the surface where LLM applications can take consequential real-world actions** — and where the *"no [[humanintheloop|human in the loop]]"* problem becomes most acute. Per Ch 7's parting caveat:

> *"By creating this relatively autonomous behavior, we are not involved in the intermediate steps. As such, there is no human in the loop to judge the quality of the output or reasoning process. This double-edged sword requires a careful system design to improve its reliability."*

This is the [[CompoundErrorAccumulation|compound-error-accumulation]] argument Huyen Ch 6 makes, applied to tool-using agents specifically.

## Connections

- [[ToolInventory]] — the design surface for choosing which tools to give an agent.
- [[Agent]] / [[AgenticAI]] / [[LangChainAgent]] — the systems that use tools.
- [[react|ReAct]] — the canonical tool-use prompting pattern.
- [[FunctionCalling]] — the API surface that exposes tools.
- [[DuckDuckGoSearchResults]] / [[LLMMathTool]] — the two tools Ch 7 uses.
- [[KnowledgeAugmentation]] / [[CapabilityExtension]] / [[WriteAction]] — Huyen Ch 6's tool taxonomy.
- [[humanintheloop]] / [[CompoundErrorAccumulation]] — the reliability concerns tool use surfaces.
- [[hands-on-llm-ch07-advanced-text-generation]] / [[ai-engineering-ch06-rag-agents]] — primary sources.

## From Hands-On LLMs Ch 7

Ch 7 frames tool use as the **capability multiplier** for LLMs and the structural justification for the **Agents** section: *"agents are systems that leverage a language model to determine which actions they should take and in what order."* The DuckDuckGo + llm-math two-tool demonstration is the chapter's argument that even small tool inventories can dramatically extend what an LLM can answer (real-time prices, exact arithmetic).
