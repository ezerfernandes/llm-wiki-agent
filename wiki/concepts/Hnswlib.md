---
title: "Hnswlib"
type: concept
tags: [vector-search, ann, library]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Hnswlib

**Hnswlib** is the **reference open-source implementation of [[HNSW]]** by the original algorithm authors (Malkov & Yashunin). Mentioned in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] alongside [[FAISS]], [[Annoy]], and [[ScaNN]] as one of the four canonical vector-search libraries.

## Position

Where [[FAISS]] is a multi-algorithm library and [[Annoy]] is tree-based, Hnswlib is **single-purpose** — it implements only HNSW, but does so as the authors intended and at high quality. Production HNSW indexes in vector DBs like [[Milvus]] often build on (or reimplement) Hnswlib semantics.

## Connections

- [[HNSW]] — the algorithm Hnswlib implements.
- [[ApproximateNearestNeighbor]] — the parent family.
- [[FAISS]] / [[ScaNN]] / [[Annoy]] — peer ANN libraries.
- [[Milvus]] — vector DB that uses HNSW-style indexing.
- [[EmbeddingBasedRetrieval]] / [[VectorDatabase]] — the application stack.
- [[ai-engineering-ch06-rag-agents]] — primary source.
