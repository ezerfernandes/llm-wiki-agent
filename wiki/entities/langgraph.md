---
title: "LangGraph"
type: entity
tags: [tool, framework, llm, agent, open-source, langchain]
sources: [leh-ch09-rag-inference-pipeline]
last_updated: 2026-05-22
---

## What it is
LangGraph is an open-source library from the [[LangChain]] team for building stateful, multi-actor LLM applications as graphs (nodes + edges) — the canonical way to express agent loops, RAG sub-graphs, and human-in-the-loop steps in the LangChain ecosystem.

## In LLM Engineer's Handbook
Ch. 9 ([[leh-ch09-rag-inference-pipeline]]) references LangGraph (`langgraph`) alongside [[LangChain]] when introducing `PromptTemplate` and LCEL `prompt | model` composition: the chapter uses these primitives directly while keeping the rest of the RAG pipeline framework-light, but notes LangGraph as the natural next step if richer state management or agent loops are needed.

## Connections
- [[LangChain]] — parent ecosystem.
- [[LangSmith]] — sibling observability product from the same team.
- [[LlamaIndex]] — peer framework.
- [[Agent]] — LangGraph's primary use case.
- [[rag]] — LangGraph can orchestrate RAG sub-graphs.
