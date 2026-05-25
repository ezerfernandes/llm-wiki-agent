---
title: "BEIR (Benchmarking IR)"
type: concept
tags: [benchmark, retrieval, evaluation, rag]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# BEIR

**BEIR** (Benchmarking IR; Thakur et al. 2021) is the canonical multi-task evaluation harness for **retrieval systems**, supporting 14 common retrieval benchmarks across diverse domains. Named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] alongside [[MTEB]] as one of the two reference benchmarks for retrieval — BEIR for *retrieval systems*, MTEB for *embedding models*.

## What BEIR covers

BEIR spans heterogeneous IR tasks — factoid QA, fact verification, scientific document retrieval, news, biomedical — to test **zero-shot retrieval generalization**. A retriever trained on MSMARCO that does well on BEIR has demonstrated cross-domain robustness, not just MSMARCO overfitting.

## Position relative to [[MTEB]]

| Benchmark | Evaluates | Source |
|---|---|---|
| **BEIR** | Retrieval *systems* (end-to-end retriever output) | Thakur et al. 2021 |
| **[[MTEB]]** | Embedding *models* (across many tasks: classification, clustering, retrieval, etc.) | Muennighoff et al. 2023 |

BEIR is the right benchmark when you're choosing or comparing **a retriever** (sparse, dense, hybrid). MTEB is the right benchmark when you're choosing or comparing **an embedding model**.

## Connections

- [[rag]] — the application family BEIR most directly evaluates.
- [[MTEB]] — sibling benchmark for embeddings.
- [[ANNBenchmarks]] — sibling benchmark for ANN libraries.
- [[ContextPrecision]] / [[ContextRecall]] / [[NDCG]] / [[MAP]] / [[MRR]] — the metrics BEIR computes.
- [[TermBasedRetrieval]] / [[EmbeddingBasedRetrieval]] / [[HybridSearch]] — retrieval families compared on BEIR.
- [[ai-engineering-ch06-rag-agents]] — primary source.
