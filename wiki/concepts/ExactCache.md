---
title: "Exact Cache"
type: concept
tags: [caching, system-architecture, performance, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Exact Cache

**System-level caching that hits only when the *exact* same query is re-requested.** One of the two system-caching mechanisms named in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] (the other is [[SemanticCache|semantic caching]]). Distinct from [[KVCache|KV cache]] and [[PromptCaching|prompt cache]], which live inside the model API.

## The mechanism

> *"With exact caching, cached items are used only when these exact items are requested. For example, if a user asks a model to summarize a product, the system checks the cache to see if a summary of this exact product exists. If yes, fetch this summary. If not, summarize the product and cache the summary."* — Ch 10

Exact caching also serves embedding-based retrieval: cache the result of a vector search keyed on the query — fetch on repeat, populate on miss.

## Where it pays off

> *"Caching is especially appealing for queries that involve multiple steps (e.g., chain-of-thought) and/or time-consuming actions (e.g., retrieval, SQL execution, or web search)."* — Ch 10

The leverage scales with the cost of the steps being cached, not just the LLM call itself.

## Storage choices

- **In-memory** — fastest; limited size.
- **Redis / Postgres** — larger; sub-ms to ms latency.
- **Tiered** — hot in memory, warm in Redis, cold in object storage.

## Eviction policies

Standard [[CacheReplacementPolicy|cache replacement policies]] apply: **LRU** (Least Recently Used), **LFU** (Least Frequently Used), **FIFO**. Choice depends on access pattern.

## Cacheability prediction

Not every query is worth caching:

- **User-specific** — *"What's the status of my recent order?"* — caching is useless (and dangerous; see below).
- **Time-sensitive** — *"How's the weather?"* — caches go stale fast.

> *"Many teams train a classifier to predict whether a query should be cached."* — Ch 10

## The personalization-leak risk

Ch 10's footnote-grade warning, paraphrased:

> *"Imagine you work for an e-commerce site, and user X asks a seemingly generic question such as: 'What is the return policy for electronics products?' Because your return policy depends on the user's membership, the system first retrieves user X's information and then generates a response containing X's information. Mistaking this query for a generic question, the system caches the answer. Later, when user Y asks the same question, the cached result is returned, revealing X's information to Y."*

**Implication**: caching keys must include personalization scope (user tier, region, account state), not just the literal query string. Otherwise the cache becomes a data-leak vector.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[SemanticCache]] — sibling system-caching mechanism (vector-similarity hit).
- [[KVCache]] / [[PromptCaching]] — sit inside the model API; complementary, not substitutes.
- [[CacheReplacementPolicy]] / [[CacheHit]] / [[CacheMiss]] — classical caching vocabulary.
- [[DataLeakage]] — the personalization-leak failure mode.
- [[chainofthought]] — multi-step pattern where caching pays off.
