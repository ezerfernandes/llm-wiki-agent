---
title: "Precision at K"
type: concept
tags: [evaluation, retrieval, metric, ir, ranking]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Precision at K

**Precision-at-k** is the position-level building block of [[AveragePrecision|average precision]] and [[MAP|MAP]]:

$$\text{P@k} = \frac{\text{number of relevant results at position} \le k}{k}$$

Ch 8 of *Hands-On LLMs* introduces this primitive en route to [[MAP]]:

> *"Looking at the first position, we have a relevant result leading to a precision at position 1 of 1.0 (calculated as the number of relevant results at position 1, divided by the position we're currently looking at)."* — Ch 8

## Intuition

If the system returns 3 relevant documents in the top 5 results, P@5 = 3/5 = 0.6. P@k is **the fraction of the top-k results that are relevant** — the simplest possible rank-aware quality measure.

## Why precision-at-k matters

P@k is the **operational quality measure** for first-page search experience. If a user looks at the top 10 results, they care about P@10. If only the top 3 are surfaced (chat-style RAG context), P@3 is what counts. The metric is intrinsically tied to **how many results the consumer actually looks at**.

## Limitations

P@k alone has two failure modes:

1. **Ignores positions within the top-k.** P@3 = 1.0 for a system returning `[relevant, relevant, relevant]` and a system returning `[relevant, relevant, relevant]` — but also for many less-favorable orderings if the relevant counts match.
2. **Ignores recall.** A system that returns 3 relevant of 1000 total relevant documents in the corpus has the same P@3 as a system that returns 3 of 3 total relevant. Recall-at-k complements P@k.

This is why [[AveragePrecision|average precision]] and [[NDCG]] exist — they encode both position-within-top-k and graded relevance.

## In RAG vs search

| Application | Practical k |
|---|---|
| First-page web search | k = 10 |
| Featured-snippet search | k = 1 or 3 |
| RAG context construction | k = 3–10 (the number of chunks stuffed into the LLM prompt) |
| Vector-DB-as-knowledge-base | k = 5–20 (more candidates → more reranker work) |

The choice of k is application-driven.

## Connections

- [[AveragePrecision]] — the per-query aggregation built on P@k.
- [[MAP]] — the cross-query aggregation.
- [[Precision]] — the underlying classification metric P@k specializes (relevance is a binary class).
- [[Recall]] — the complementary metric (often paired as "recall-at-k").
- [[InformationRetrieval]] — the parent field.
- [[NDCG]] — the rank-sensitive metric that generalizes P@k to graded relevance.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
