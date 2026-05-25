---
title: "Approximate Nearest Neighbor (ANN)"
type: concept
tags: [vector-search, retrieval, algorithms, rag]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Approximate Nearest Neighbor

**Approximate Nearest Neighbor (ANN)** search is the family of algorithms that finds *approximately* the k closest vectors to a query vector in sub-linear time — trading some recall for orders-of-magnitude speed-up over exact [[KNN|k-NN]]. ANN is the structural enabler of [[EmbeddingBasedRetrieval|embedding-based retrieval]] at production scale; without it, vector search would be O(N) per query.

## Why naive k-NN doesn't scale

Exact k-NN computes the similarity between the query and *every* vector in the database, ranks all of them, and returns the top k. Per [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]: *"This naive solution ensures that the results are precise, but it's computationally heavy and slow. It should be used only for small datasets."*

## The main ANN algorithm families (per Huyen)

| Algorithm | Approach |
|---|---|
| [[LSH]] (Indyk & Motwani 1999) | Hash similar vectors into the same buckets; trade accuracy for efficiency. |
| [[HNSW]] (Malkov & Yashunin 2016) | Multi-layer graph; nearest-neighbor search via graph traversal. |
| [[ProductQuantization]] (Jégou et al. 2011) | Decompose each vector into lower-dimensional subvectors; compute distances on the compressed representation. |
| [[IVF]] (Sivic & Zisserman 2003) | K-means cluster the vectors; query the closest centroids' clusters. |
| [[Annoy]] (Bernhardsson, Spotify 2013) | Multiple random-split binary trees; traverse to gather candidates. |
| SPTAG | [[microsoft\|Microsoft]] space-partition tree + graph. |
| FLANN | Fast Library for Approximate Nearest Neighbors. |

## The four-metric trade-off

The [[ANNBenchmarks]] website compares ANN algorithms on **recall**, **queries-per-second (QPS)**, **build time**, and **index size** — the universal trade-off space:

- More-detailed indexes ([[HNSW]]) → higher recall + faster query, but slower build + more memory.
- Simpler indexes ([[LSH]]) → faster build + less memory, but lower recall + slower query.

There is no universal best; index choice depends on whether your data is static (build-once, query-often → HNSW) or dynamic (rebuild-often → LSH).

## Implementations

- [[FAISS]] (Facebook AI Similarity Search) — implements LSH, HNSW, IVF, PQ.
- [[ScaNN]] (Google) — Scalable Nearest Neighbors.
- [[Annoy]] (Spotify) — open-source tree-based ANN.
- [[Hnswlib]] — reference HNSW implementation.
- [[Milvus]] — vector DB that implements HNSW.

## Connections

- [[EmbeddingBasedRetrieval]] — the retrieval family ANN enables at scale.
- [[VectorDatabase]] — production storage layer for vectors + ANN index.
- [[Embedding]] — the substrate.
- [[HNSW]] / [[LSH]] / [[ProductQuantization]] / [[IVF]] / [[Annoy]] — specific algorithms.
- [[FAISS]] / [[ScaNN]] / [[Hnswlib]] — implementations.
- [[ANNBenchmarks]] — comparison harness.
- [[rag]] — the application surface.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8's scale-out anchor.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 introduces ANN as **the scale-out alternative to naive NumPy distance computation**:

> *"The most straightforward way to find the nearest neighbors is to calculate the distances between the query and the archive. That can easily be done with NumPy and is a reasonable approach if you have thousands or tens of thousands of vectors in your archive. As you scale beyond to the millions of vectors, an optimized approach for retrieval is to rely on approximate nearest neighbor search libraries like [[Annoy]] or [[FAISS]]."* — Ch 8

The chapter's structural taxonomy is **simpler than [[ai-engineering-ch06-rag-agents|Huyen Ch 6's]]** five-algorithm-family decomposition — Ch 8 names just Annoy + FAISS as representative libraries and notes the GPU / clustering scale-out. The full algorithm-family taxonomy ([[LSH]] / [[HNSW]] / [[IVF]] / [[ProductQuantization|PQ]] / Annoy) is on this page already from Huyen's coverage.
