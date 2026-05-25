---
title: "Superlinked"
type: entity
tags: [company, tool, vector-database, embeddings, framework]
sources: [leh-ch02-tooling-and-installation, leh-ch04-rag-feature-pipeline, leh-ch09-rag-inference-pipeline]
last_updated: 2026-05-22
---

## What it is
Superlinked is a company that builds a Python framework for **multi-modal, multi-attribute embeddings** — letting an application embed multiple fields (content, category, recency) into a single vector space and query them with a structured DSL. They also publish a widely-cited Vector DB Comparison.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) cites the **Superlinked Vector DB Comparison** as the source the authors used to pick [[Qdrant]] over [[Pinecone]] / [[Weaviate]] / [[Milvus]] / [[ChromaDB]] / [[Pgvector]] / [[RedisVectorSearch]] based on RPS / latency / index-time trade-offs. Ch. 9 ([[leh-ch09-rag-inference-pipeline]]) proposes Superlinked's `TextSimilaritySpace` + `CategoricalSimilaritySpace` + `Index` API as the future-improvement path for multi-index embeddings over content + platform + recency in the LLM Twin retrieval module.

## Connections
- [[Qdrant]] / [[Pinecone]] / [[Weaviate]] / [[Milvus]] / [[ChromaDB]] / [[Pgvector]] — vector DBs in the Superlinked comparison.
- [[VectorDatabase]] — domain.
- [[rag]] — Superlinked's primary application area.
- [[Embedding]] — multi-attribute embedding is Superlinked's core idea.
