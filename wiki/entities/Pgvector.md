---
title: "pgvector"
type: entity
tags: [tool, vector-database, postgresql, extension, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch04-rag-feature-pipeline]
last_updated: 2026-05-22
---

## What it is
`pgvector` is a PostgreSQL extension that adds vector data types and HNSW/IVF indexes for similarity search, letting an existing Postgres database double as a vector store.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists pgvector among the vector-DB alternatives evaluated against [[Qdrant]] per the Superlinked Vector DB Comparison. Ch. 4 ([[leh-ch04-rag-feature-pipeline]]) re-mentions pgvector when surveying the vector-DB landscape.

## Connections
- [[PostgreSQL]] — host database for the extension.
- [[Qdrant]] — chosen vector DB.
- [[Pinecone]] / [[Milvus]] / [[Weaviate]] / [[ChromaDB]] / [[RedisVectorSearch]] — peer vector DBs.
- [[VectorDatabase]] — category.
