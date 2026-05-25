---
title: "ChromaDB"
type: entity
tags: [product, vector-database, embeddings, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch04-rag-feature-pipeline]
last_updated: 2026-05-22
---

## What it is
Chroma (ChromaDB) is an open-source embedding database designed for AI applications, with a Python-native API and a focus on developer ergonomics. It pairs naturally with LangChain and LlamaIndex.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists Chroma among the vector-DB alternatives evaluated against [[Qdrant]] per the Superlinked Vector DB Comparison; the book picks Qdrant for higher RPS / lower latency. Ch. 4 ([[leh-ch04-rag-feature-pipeline]]) reiterates Chroma in the broader vector-DB landscape.

## Connections
- [[Qdrant]] — chosen vector DB.
- [[Pinecone]] / [[Milvus]] / [[Weaviate]] / [[Pgvector]] / [[RedisVectorSearch]] — peer vector DBs.
- [[VectorDatabase]] — category.
- [[LangChain]] — common upstream framework.
