---
title: "Haystack"
type: entity
tags: [llm-app, orchestrator, rag, open-source, deepset, agentic-design-patterns]
sources: [ai-engineering-ch10-architecture-feedback, agentic-design-patterns-appendices-bg]
last_updated: 2026-06-07
---

# Haystack

Open-source LLM orchestration / [[rag|RAG]] framework from **deepset** (Berlin). Cited in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] as one of the named AI orchestration tools:

> *"There are many AI orchestration tools, including LangChain, LlamaIndex, Flowise, Langflow, and Haystack."* — Ch 10

## Position

Haystack is one of the older entries in the LLM-orchestration space, with strong roots in retrieval / RAG pipelines (deepset's pre-LLM business was open-domain question-answering). It is the **EU-origin** alternative to the US-dominated landscape ([[LangChain]], [[LlamaIndex]]) and has been adopted by a number of European enterprises for that reason among others.

## In Agentic Design Patterns — Appendix C
[[agentic-design-patterns-appendices-bg|Appendix C]] (Gulli) describes Haystack as an open-source framework engineered for **scalable, production-ready search systems** powered by language models. Its architecture is composed of **modular, interoperable nodes** that form pipelines for document retrieval, question answering, and summarization. Main strength: **performance and scalability** for large-scale information-retrieval tasks (enterprise-grade). Trade-off: a design optimized for search pipelines can be **more rigid** for implementing highly dynamic, creative agentic behaviors.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[AIPipelineOrchestration]] — product category.
- [[LangChain]] / [[LlamaIndex]] — code-first peer orchestrators.
- [[Flowise]] / [[Langflow]] — visual-builder peer orchestrators.
- [[rag]] — Haystack's historical core competency.
