---
title: "LlamaIndex"
type: entity
tags: [tool, framework, llm, rag, open-source]
sources: [leh-ch09-rag-inference-pipeline, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

## What it is
LlamaIndex (formerly GPT Index) is an open-source data framework for LLM applications, focused on connecting custom data sources to LLMs via ingestion, indexing, retrieval, and query composition. It is a primary peer of [[LangChain]].

## In LLM Engineer's Handbook
Ch. 9 ([[leh-ch09-rag-inference-pipeline]]) name-checks LlamaIndex (alongside [[LangChain]] and Haystack) as the kind of framework whose internal abstractions the LLM Twin's five-line `rag()` function reproduces. The authors mention these frameworks to position their from-scratch RAG implementation as deliberately equivalent in spirit but more visible in mechanics.

## Connections
- [[LangChain]] — peer framework.
- [[rag]] — primary domain.
- [[langgraph]] — LangChain's agent layer (peer comparison surface).
- [[Qdrant]] / [[Pinecone]] / [[Weaviate]] — typical vector-DB backends.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 names LlamaIndex alongside [[LangChain]], [[Flowise]], [[Langflow]], and [[Haystack]] as one of the canonical [[AIPipelineOrchestration|AI pipeline orchestration]] tools — distinct from general workflow orchestrators like [[Airflow]] / [[Metaflow]] that operate on batch DAGs rather than on synchronous request-shaped inference pipelines.

LlamaIndex's specialty (data-indexing for retrieval-heavy applications) makes it a particularly common choice when the AI app's chain is dominated by [[rag|RAG]] over private/proprietary corpora.
