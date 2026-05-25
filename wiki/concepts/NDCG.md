---
title: "NDCG (Normalized Discounted Cumulative Gain)"
type: concept
tags: [evaluation, retrieval, ranking, metric]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# NDCG

**NDCG** (Normalized Discounted Cumulative Gain) is the canonical **rank-sensitive** evaluation metric for retrieval — used when *"you care about the ranking of the retrieved documents, for example, more relevant documents should be ranked first"* ([[ai-engineering-ch06-rag-agents|Huyen Ch 6]]).

## How it works

For a list of `k` retrieved documents with graded relevance scores:

- **Cumulative Gain (CG)**: sum of relevance scores.
- **Discounted CG (DCG)**: sum of `relevance_i / log_2(i + 1)` — higher ranks get higher weight.
- **Normalized DCG (NDCG)**: DCG divided by the **ideal DCG** (the DCG of the best possible ranking) — bounds the metric to [0, 1].

## Position relative to [[ContextPrecision|precision]] / [[ContextRecall|recall]]

[[ContextPrecision|Context precision]] and [[ContextRecall|context recall]] treat all relevant retrievals as equal. NDCG, [[MAP]], and [[MRR]] go further: they reward putting the *most* relevant document first. For RAG with a small `k` (e.g. top-3), this matters less; for ranking applications and for RAG with a [[ReRanking|reranker]] in the loop, it matters a lot.

## Connections

- [[rag]] — application surface.
- [[MAP]] / [[MRR]] — other rank-sensitive retrieval metrics.
- [[ContextPrecision]] / [[ContextRecall]] — rank-insensitive RAG retrieval metrics.
- [[ReRanking]] — the system component whose output NDCG most directly evaluates.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8's reranker-lift benchmark anchor.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names NDCG as **the graded-relevance alternative to [[MAP]]**:

> *"Another metric commonly used for search systems is normalized discounted cumulative gain (nDCG), which is more nuanced in that the relevance of documents is not binary (relevant versus not relevant) and one document can be labeled as more relevant than another in the test suite and scoring mechanism."* — Ch 8

**nDCG@10 is the metric the [[MIRACL]] benchmark reports**, which Ch 8 cites for its **headline reranker-efficacy claim**:

> *"On a multilingual benchmark like MIRACL, a reranker can boost performance from 36.5 to 62.8, measured as nDCG@10."* — Ch 8

The **36.5 → 62.8 jump** is the wiki's anchor for the reranker-lift effect size on production-grade multilingual benchmarks (cf. [[ReRanking]]).
