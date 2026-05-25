---
title: "Agentic RAG"
type: concept
tags: [rag, agents, advanced-rag, tool-use, autonomy]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
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
