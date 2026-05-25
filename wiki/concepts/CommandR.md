---
title: "Command R / Command R+"
type: concept
tags: [model, llm, cohere, open-weights, rag, agents]
sources: [hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Command R / Command R+

**Command R** (35B) and **Command R+** (104B) are [[Cohere|Cohere's]] flagship LLM family, **explicitly designed for [[rag|RAG]] and [[Agent|agentic]] workloads** — with built-in support for grounded generation with citations, multi-step tool use, and multi-query / multi-hop retrieval planning.

## Open weights with conditions

Per [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]: *"Cohere's Command R, the Mistral models, Microsoft's Phi, and Meta's Llama models are all examples of open models."* Command R / R+ are **open-weights** but with a non-OSI-strict commercial license — weights are released for community use; commercial production deployment requires Cohere's licensing.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names **Command R+** as the open-weights model capable of [[AgenticRAG|agentic RAG]]:

> *"Not all LLMs will have the RAG capabilities mentioned here. At the time of writing, likely only the largest managed models may be able to attempt this behavior. Thankfully, Cohere's Command R+ excels at these tasks and is available as an open-weights model as well."* — Ch 8

This positions Command R+ uniquely: a **frontier-capability** model (agentic RAG, multi-hop planning) with **open weights** — at the time of *Hands-On LLMs* publication, the largest open-weights model with this capability. Models like Llama 2 and Mistral were open-weights but not agentic-RAG-capable; GPT-4 / Claude 3 were agentic-RAG-capable but closed-weights.

## Default for `co.chat`

Cohere's managed `co.chat` endpoint (see [[CohereChat]]) defaults to a Command model family — which is the structural reason Ch 8's worked managed-RAG examples produce **automatic span-level citations**: Command models are trained to emit citation metadata as part of the response protocol, not via post-hoc parsing.

## Connections

- [[Cohere]] — producer.
- [[CohereChat]] — the managed API endpoint Command R+ powers.
- [[rag]] / [[GroundedGeneration]] / [[CitationGeneration]] — the application family Command R+ is designed for.
- [[AgenticRAG]] — the capability ceiling Command R+ is named as crossing.
- [[OpenSourceLLM]] — the model-distribution category.
- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1 names Command R among open-weights model families.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8 names Command R+ as the agentic-RAG-capable open-weights model.
