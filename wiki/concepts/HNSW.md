---
title: "HNSW"
type: concept
tags: [vector-search, ann, retrieval, algorithms]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# HNSW

**HNSW** (Hierarchical Navigable Small World; Malkov & Yashunin 2016) is the dominant [[ApproximateNearestNeighbor|ANN]] algorithm for production vector search. It constructs a **multi-layer graph** where nodes represent vectors and edges connect similar vectors, then performs nearest-neighbor search by **traversing graph edges** from a coarse top layer down to a dense bottom layer.

## Why it wins on the four-metric trade-off

Per [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]:

> *"A detailed index like HNSW provides high accuracy and fast query times but requires significant time and memory to build."*

That profile — high recall + high QPS at the cost of build time and memory — is exactly what a *"build once, query forever"* RAG corpus wants. HNSW is the de facto default in modern vector databases.

## Implementations

- [[Hnswlib]] — open-source reference implementation by the original authors.
- [[FAISS]] — Facebook AI Similarity Search includes HNSW.
- [[Milvus]] — vector DB with HNSW indexing.
- [[Qdrant]] / [[Weaviate]] / [[Pinecone]] — all support HNSW.

## Connections

- [[ApproximateNearestNeighbor]] — the parent family.
- [[VectorDatabase]] — production storage layer.
- [[EmbeddingBasedRetrieval]] — the retrieval family HNSW serves.
- [[LSH]] — the lighter, less-accurate alternative.
- [[ProductQuantization]] / [[IVF]] — complementary techniques often combined with HNSW.
- [[Hnswlib]] / [[FAISS]] / [[Milvus]] — implementations.
- [[ai-engineering-ch06-rag-agents]] — primary source.
