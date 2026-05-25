---
title: "Reciprocal Rank Fusion (RRF)"
type: concept
tags: [retrieval, search, rag, ensemble]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Reciprocal Rank Fusion

**Reciprocal Rank Fusion (RRF)** (Cormack et al. 2009) is the standard algorithm for combining rankings from multiple retrievers into a single fused ranking. It is the algorithmic substrate for **parallel [[HybridSearch|hybrid search]]** — running [[TermBasedRetrieval|term-based]] and [[EmbeddingBasedRetrieval|embedding-based]] retrievers simultaneously and fusing their outputs — described in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]].

## The formula

For a document `D` ranked by `n` retrievers:

$$\text{Score}(D) = \sum_{i=1}^{n} \frac{1}{k + r_i(D)}$$

where:

- `n` = number of ranked lists (one per retriever).
- `r_i(D)` = rank of document `D` by retriever `i`.
- `k` = constant to avoid division by zero and dampen the influence of lower-ranked documents. Typical value: **k = 60**.

## Why the `1/(k + rank)` form

The reciprocal weighting heavily rewards top ranks (rank-1 = 1/61; rank-100 = 1/160) — a document ranked first by *any* retriever gets a strong push in the fused ranking. The `k` constant controls how steeply the score decays: smaller `k` makes the fusion more top-rank-biased.

## Intuition

If a document ranks first by one retriever and second by another retriever (with simplified `k=0`): score = 1/1 + 1/2 = 1.5. The fused ranking surfaces documents that multiple retrievers agree are relevant, even if no single retriever ranks them first.

## Connections

- [[HybridSearch]] — the application of RRF in production RAG.
- [[rag]] — the parent application.
- [[TermBasedRetrieval]] / [[EmbeddingBasedRetrieval]] — the two retrievers RRF most commonly fuses.
- [[ReRanking]] — RRF can be viewed as a *parallel* rerank, vs sequential rerank.
- [[ai-engineering-ch06-rag-agents]] — primary source.
