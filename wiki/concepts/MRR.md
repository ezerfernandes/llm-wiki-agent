---
title: "MRR (Mean Reciprocal Rank)"
type: concept
tags: [evaluation, retrieval, ranking, metric]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# MRR

**MRR** (Mean Reciprocal Rank) is the simplest **rank-sensitive** retrieval evaluation metric: for each query, take `1 / (rank of the first relevant document)`, then average over the query set. Named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] alongside [[NDCG]] and [[MAP]] for ranking-aware retrieval evaluation.

## Formula

$$\text{MRR} = \frac{1}{|Q|} \sum_{q \in Q} \frac{1}{\text{rank}_q}$$

where `rank_q` is the rank of the first relevant document for query `q` (or `∞` if no relevant document is retrieved → contribution 0).

## When MRR is the right choice

MRR is the canonical metric for **first-correct-answer** tasks — question answering, factoid lookup, FAQ search. If the user reads only the first result, the metric should reflect that. MRR ignores all but the highest-ranked relevant document, which is appropriate when only the top result is consumed.

## Position relative to [[MAP]] and [[NDCG]]

- **MRR** — only the *first* relevant rank matters.
- **[[MAP]]** — averages precision *across* relevant ranks (binary relevance).
- **[[NDCG]]** — discounts gains by log-rank (graded relevance).

## Connections

- [[rag]] — application surface, especially for QA-style RAG.
- [[NDCG]] / [[MAP]] — sibling rank-sensitive metrics.
- [[ContextPrecision]] / [[ContextRecall]] — rank-insensitive RAG metrics.
- [[QuestionAnswering]] — the task family where MRR is most appropriate.
- [[ai-engineering-ch06-rag-agents]] — primary source.
