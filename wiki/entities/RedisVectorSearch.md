---
title: "Redis Vector Search"
type: entity
tags: [tool, vector-database, redis, in-memory, search]
sources: [leh-ch02-tooling-and-installation]
last_updated: 2026-05-22
---

## What it is
Redis Vector Search (via RediSearch / Redis Stack) lets the in-memory key-value store Redis index vector embeddings and perform similarity search using HNSW or FLAT indices.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists Redis Vector Search among the vector-DB alternatives evaluated against [[Qdrant]] (via the Superlinked Vector DB Comparison) — Qdrant is selected for its RPS / latency / index-time profile, but Redis is acknowledged as a viable choice especially when Redis is already in the stack.

## Connections
- [[Qdrant]] — chosen vector DB.
- [[Pinecone]] / [[Weaviate]] / [[Milvus]] / [[ChromaDB]] / [[Pgvector]] — peer vector DBs.
- [[VectorDatabase]] — category.
