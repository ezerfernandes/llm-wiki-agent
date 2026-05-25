---
title: "ANN-Benchmarks"
type: concept
tags: [benchmark, vector-search, ann]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# ANN-Benchmarks

**ANN-Benchmarks** is the canonical comparison harness for [[ApproximateNearestNeighbor|ANN]] algorithms, named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]. It runs candidate libraries ([[FAISS]], [[Annoy]], [[Hnswlib]], [[ScaNN]], and many others) on multiple datasets and reports four metrics that capture the universal index trade-off space:

| Metric | What it measures |
|---|---|
| **Recall** | Fraction of true nearest neighbors found by the algorithm. |
| **Queries per second (QPS)** | Query throughput — crucial for high-traffic RAG. |
| **Build time** | Time to construct the index — matters when data changes frequently. |
| **Index size** | Memory footprint — sets the scalability ceiling. |

## Why all four matter

No algorithm dominates on all four. [[HNSW]] excels at recall and QPS at the cost of build time and memory; [[LSH]] is the opposite. [[ProductQuantization]] + [[IVF]] (the [[FAISS]] backbone) trades recall for radically smaller index size. ANN-Benchmarks lets practitioners visualize the Pareto frontier and pick the right point for their workload.

## Connections

- [[ApproximateNearestNeighbor]] — the algorithm family ANN-Benchmarks evaluates.
- [[HNSW]] / [[LSH]] / [[ProductQuantization]] / [[IVF]] / [[Annoy]] — algorithms compared.
- [[FAISS]] / [[ScaNN]] / [[Hnswlib]] — libraries compared.
- [[BEIRBenchmark]] — sibling benchmark for retrieval *systems*.
- [[MTEB]] — sibling benchmark for embedding *models*.
- [[VectorDatabase]] — the production stack ANN-Benchmarks informs.
- [[ai-engineering-ch06-rag-agents]] — primary source.
