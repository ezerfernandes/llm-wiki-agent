---
title: "ScaNN"
type: concept
tags: [vector-search, ann, library, google]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# ScaNN

**ScaNN** (Scalable Nearest Neighbors; Sun et al. 2020) is [[google|Google]]'s open-source vector-search library, the major non-[[FAISS]] alternative in the [[ApproximateNearestNeighbor|ANN]] ecosystem. Mentioned in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] alongside [[FAISS]], [[Annoy]], and [[Hnswlib]] as one of the four canonical vector search libraries.

## Position

ScaNN is a **library** (like [[FAISS]]), not a database. It provides ANN search primitives that other systems build on. Within [[google|Google]]'s own stack, it powers retrieval inside several products and research codebases.

## Connections

- [[google|Google]] — developer.
- [[ApproximateNearestNeighbor]] — the family.
- [[FAISS]] — the main competing ANN library.
- [[Annoy]] / [[Hnswlib]] — sibling libraries.
- [[VectorDatabase]] — the layer built on top.
- [[EmbeddingBasedRetrieval]] — the application.
- [[ai-engineering-ch06-rag-agents]] — primary source.
