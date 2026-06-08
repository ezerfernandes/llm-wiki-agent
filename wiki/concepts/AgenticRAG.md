---
title: "Agentic RAG"
type: concept
tags: [rag, agents, advanced-rag, tool-use, autonomy]
sources: [hands-on-llm-ch08-semantic-search-and-rag, agentic-design-patterns-ch14-rag]
last_updated: 2026-06-07
---

# Agentic RAG

**Agentic RAG** is the most-delegated point on Ch 8 of *Hands-On LLMs*'s Advanced-RAG continuum — the LLM operates as an **agent** over multiple data sources, deciding when to retrieve, what to retrieve, and (with **read+write tool symmetry**) when to take actions beyond just retrieval. The transition from RAG to agent is gradual: query rewriting → multi-query → multi-hop → query routing → agentic RAG.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names agentic RAG as the natural continuation of the Advanced-RAG continuum:

> *"You may be able to now see that the list of previous enhancements slowly delegates more and more responsibility to the LLM to solve more and more complex problems. This relies on the LLM's capability to gauge the required information needs as well as its ability to utilize multiple data sources. This new nature of the LLM starts to become closer and closer to an agent that acts on the world. The data sources can also now be abstracted into tools. We saw, for example, that we can search Notion, but by the same token, we should be able to post to Notion as well."* — Ch 8

The **read+write tool symmetry** observation is load-bearing: once retrieval is abstracted as a tool, the LLM can have arbitrary other tools (write actions, calculations, web searches, APIs) — the *RAG-system* designation no longer holds in any structural sense; it has become a [[react|ReAct]]-style agent.

## The capability ceiling caveat

Ch 8 explicitly warns about the **agent capability cliff** — the same warning [[hands-on-llm-ch07-advanced-text-generation|Ch 7]] gave about ReAct:

> *"Not all LLMs will have the RAG capabilities mentioned here. At the time of writing, likely only the largest managed models may be able to attempt this behavior. Thankfully, Cohere's Command R+ excels at these tasks and is available as an open-weights model as well."* — Ch 8

This is consistent with [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]'s [[CompoundErrorAccumulation|compound-error-accumulation]] warning: each delegated step is an LLM call with non-zero error rate; long chains multiply error.

## Position in the Advanced-RAG continuum

| Technique | Delegation level | Read or read+write? |
|---|---|---|
| [[QueryRewriting]] | Low — rephrase user query | Read |
| [[MultiQueryRAG]] | Mid — parallel decomposition | Read |
| [[MultiHopRAG]] | Mid — sequential decomposition | Read |
| [[QueryRouting]] | High — multi-source selection | Read |
| **Agentic RAG** | **Highest — full agent over tools** | **Read + write** |

## From [[agentic-design-patterns-ch14-rag|Agentic Design Patterns (Gulli) Ch 14]]

[[AntonioGulli|Gulli]] frames Agentic RAG as the evolution where an *"agent — a specialized AI component — acts as a critical **gatekeeper and refiner** of knowledge. Rather than passively accepting the initially retrieved data, this agent actively interrogates its quality, relevance, and completeness."* The contrast diagram (Fig.2) is stark: **Naive RAG** is a fixed pipeline (query → vectors → chunks → feed to model); **Agentic RAG** *"picks tools to call,"* fanning out to multiple sources before synthesizing.

The chapter enumerates **four concrete scenarios** the agentic layer enables:

| # | Capability | Worked example | Maps to pattern |
|---|---|---|---|
| 1 | **Reflection & source validation** | Discard a stale 2020 blog post in favor of the authoritative 2025 policy doc by analyzing metadata | [[Reflection]] |
| 2 | **Reconcile knowledge conflicts** | Choose the finalized financial report (€65,000) over the initial proposal (€50,000) as the more reliable source | [[RAGEvaluation]] / [[EvaluationAndMonitoring]] |
| 3 | **Multi-step reasoning** | Decompose "compare our product's features+pricing to Competitor X's" into distinct sub-queries, then synthesize a structured comparative context | [[Planning]] / [[MultiHopRAG]] |
| 4 | **Identify knowledge gaps + use external tools** | Internal base (updated weekly) lacks yesterday's market reaction → activate a live web-search API | [[ToolUse]] / [[Routing]] |

**Challenges Gulli names** (consistent with the wiki's [[CompoundErrorAccumulation|compound-error]] caveat): the agentic layer adds significant **complexity and cost** (decision logic + tool integrations = engineering effort + compute), increased **latency** from reflection/tool-use/multi-step cycles, and the agent itself as a **new error source** — *"a flawed reasoning process could cause it to get stuck in useless loops, misinterpret a task, or improperly discard relevant information."* This is the Gulli-book counterpart to Ch 8's *Hands-On LLMs* "agent capability cliff" — both warn that delegation buys reliability only when the underlying reasoning is strong enough.

## Connection to [[react|ReAct]]

Agentic RAG is **structurally indistinguishable from a [[react|ReAct]] agent whose tool inventory includes retrieval**. The differences:

- An agentic RAG system **frames itself** as RAG-with-extensions; its primary tool is retrieval.
- A general ReAct agent has retrieval as one tool among many (search, calculator, code execution, file I/O).

The distinction is operational rather than architectural — both are LLMs in a Thought → Action → Observation loop.

## Connections

- [[rag]] — the parent technique family.
- [[QueryRewriting]] / [[MultiQueryRAG]] / [[MultiHopRAG]] / [[QueryRouting]] — earlier points on the Advanced-RAG continuum.
- [[Agent]] / [[AgenticAI]] — the broader category agentic RAG belongs to.
- [[react|ReAct]] — the architecturally-equivalent agent framework (when retrieval is the primary tool).
- [[ToolUse]] — the substrate that makes agentic RAG possible.
- [[CompoundErrorAccumulation]] — the failure mode the capability-ceiling caveat names.
- [[CommandR]] — Cohere's flagship LLM that Ch 8 names as the open-weights model capable of agentic RAG.
- [[ai-engineering-ch06-rag-agents]] — Huyen Ch 6's *"RAG can be seen as a special case of agent where the retriever is a tool"* observation.
- [[hands-on-llm-ch07-advanced-text-generation]] — Ch 7's prior agent-capability-cliff observation.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
- [[agentic-design-patterns-ch14-rag]] — [[AntonioGulli|Gulli's]] four-scenario "agent as knowledge gatekeeper" framing (reflection/source-validation, conflict reconciliation, multi-step decomposition, tool-augmented gap-filling).
- [[Reflection]] / [[Planning]] / [[ToolUse]] / [[Routing]] / [[EvaluationAndMonitoring]] — the [[AgenticDesignPatterns|design patterns]] the four Agentic-RAG scenarios compose.
