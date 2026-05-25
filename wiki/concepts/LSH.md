---
title: "LSH (Locality-Sensitive Hashing)"
type: concept
tags: [vector-search, ann, retrieval, algorithms, hashing]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# LSH

**LSH** (Locality-Sensitive Hashing; Indyk & Motwani 1999) is the foundational [[ApproximateNearestNeighbor|ANN]] algorithm. It hashes similar vectors into the same buckets, then restricts the similarity search to within-bucket candidates — *"trading some accuracy for efficiency"* ([[ai-engineering-ch06-rag-agents|Huyen Ch 6]]).

## Position relative to [[HNSW]]

Per Huyen's index trade-off characterization:

> *"A simpler index like LSH is quicker and less memory-intensive to create, but it results in slower and less accurate queries."*

LSH is the **fast-build, low-memory** end of the index spectrum. It's preferred when the corpus changes frequently and the index must be rebuilt often, or when memory constraints rule out a richer structure like [[HNSW]].

## Generality

LSH is *"a powerful and versatile algorithm that works with more than just vectors"* — the same idea applies to set similarity (MinHash), string similarity, and other domains. The vector-search application is just the most prominent in the RAG era.

## Implementations

- [[FAISS]] — Facebook AI Similarity Search includes LSH.
- [[Annoy]] — Spotify's library also implements LSH variants.

## Connections

- [[ApproximateNearestNeighbor]] — the parent family.
- [[HNSW]] — the high-recall, expensive-build alternative.
- [[ProductQuantization]] / [[IVF]] — sibling ANN techniques.
- [[FAISS]] / [[Annoy]] — implementations.
- [[VectorDatabase]] — production storage layer.
- [[EmbeddingBasedRetrieval]] — the retrieval family LSH serves.
- [[ai-engineering-ch06-rag-agents]] — primary source.
