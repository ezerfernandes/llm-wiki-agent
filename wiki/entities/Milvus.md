---
title: "Milvus"
type: entity
tags: [product, vector-database, search, open-source]
sources: [leh-ch02-tooling-and-installation, leh-ch04-rag-feature-pipeline, ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

## What it is
Milvus is an open-source vector database from Zilliz designed for billion-scale similarity search, with multiple ANN index types and distributed deployment.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists Milvus among the vector-DB alternatives evaluated against [[Qdrant]] per the Superlinked Vector DB Comparison; the book picks Qdrant. Ch. 4 ([[leh-ch04-rag-feature-pipeline]]) re-cites Milvus in the same vector-DB landscape.

## Connections
- [[Qdrant]] — chosen vector DB.
- [[Pinecone]] / [[Weaviate]] / [[ChromaDB]] / [[Pgvector]] / [[RedisVectorSearch]] — peer vector DBs.
- [[VectorDatabase]] — category.
- [[Superlinked]] — comparison author.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

Ch 6 cites Milvus as one of the vector databases that **implements [[HNSW]]** for ANN search — *"HNSW... is implemented in FAISS and Milvus."* In Huyen's evaluation rubric, Milvus is one of the open-source vector DBs to assess by: retrieval mechanisms supported, embedding models supported, scalability, indexing time, query latency per algorithm, and (if managed) pricing structure. The wiki's [[VectorDatabase]] page records the full Ch 6 evaluation checklist.
