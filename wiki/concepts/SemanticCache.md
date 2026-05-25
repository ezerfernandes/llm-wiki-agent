---
title: "Semantic Cache"
type: concept
tags: [caching, system-architecture, embeddings, vector-search, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Semantic Cache

**System-level caching that hits when an incoming query is *semantically similar* (not identical) to a cached query.** Sibling to [[ExactCache|exact caching]] in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]. Huyen is **explicitly skeptical** of this pattern.

## The mechanism

Three steps:

1. Embed each query with an [[EmbeddingModel|embedding model]].
2. Vector-search the cache for the highest-similarity prior embedding.
3. If the similarity exceeds a threshold, return the cached response; otherwise, process and cache.

> *"Imagine one user asks, 'What's the capital of Vietnam?' and the model answers, 'Hanoi'. Later, another user asks, 'What's the capital city of Vietnam?', which is semantically the same question but with slightly different wording. With semantic caching, the system can reuse the answer from the first query instead of computing the new query from scratch."* — Ch 10

## Why Huyen is skeptical

> *"Compared to other caching techniques, semantic caching's value is more dubious because many of its components are prone to failure. Its success relies on high-quality embeddings, functional vector search, and a reliable similarity metric."* — Ch 10

Three named risks:

- **Embedding quality** — a bad embedding model treats unrelated queries as similar.
- **Threshold tuning** — *"setting the right similarity threshold can also be tricky, requiring a lot of trial and error."* False positives return wrong answers; false negatives waste the cache.
- **Vector-search cost** — for large caches, the search itself can rival the cost of fresh inference.

## When it might be worth it

> *"Semantic cache might still be worthwhile if the cache hit rate is high, meaning that a good portion of queries can be effectively answered by leveraging the cached results."* — Ch 10

The break-even depends on (cost of vector search) × (1 − hit rate) ≤ (cost of fresh inference) × (hit rate).

## Contrast with prompt caching

Semantic caching is **lossy by design** — it returns answers to queries that weren't *exactly* asked. [[PromptCaching|Prompt caching]] (Ch 9) is exact-prefix caching at the model-API layer and is lossless. The two are not substitutes; they sit at different layers and have different correctness properties.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ExactCache]] — the safer sibling.
- [[EmbeddingModel]] / [[VectorDatabase]] / [[SemanticSimilarity]] — required machinery.
- [[ApproximateNearestNeighbor]] — the vector-search algorithm class.
- [[PromptCaching]] — lossless model-layer alternative.
- [[CostAndLatency]] — the tradeoff axis that determines whether the pattern pays off.
