---
title: "Average Precision"
type: concept
tags: [evaluation, retrieval, metric, ir, ranking]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Average Precision

**Average Precision (AP)** is the **per-query** retrieval evaluation metric: for a single query, AP averages the [[PrecisionAtK|precision-at-k]] values at the positions where relevant documents appear. The mean of AP across all queries is **[[MAP|Mean Average Precision (MAP)]]**.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 walks AP step-by-step as the building block of [[MAP]]:

> *"To score a search system on this query, we can focus on scoring the relevant documents. Let's start by looking at a query that only has one relevant document in the test suite. The first one is easy: the search system placed the relevant result (the only available one for this query) at the top. This gets the system the perfect score of 1."*

The construction:

1. **Walk the result list from rank 1 to k.** At each rank, look up whether the document is relevant (per the [[RelevanceJudgment|relevance judgments]]).
2. **At each position where a relevant document appears, record [[PrecisionAtK|precision-at-k]]** = (number of relevant results so far) / (current position).
3. **Average those precision values.** Non-relevant positions are skipped.

## Worked example

Suppose the relevant judgments mark documents `[1, 2, 3]` as relevant for the query, and the system returns documents `[d3, d_other_a, d1, d_other_b, d2]`:

| Position | Document | Relevant? | Precision-at-k |
|---|---|---|---|
| 1 | d3 | ✓ | 1/1 = 1.0 |
| 2 | d_other_a | ✗ | (skip) |
| 3 | d1 | ✓ | 2/3 ≈ 0.667 |
| 4 | d_other_b | ✗ | (skip) |
| 5 | d2 | ✓ | 3/5 = 0.6 |

AP for this query = (1.0 + 0.667 + 0.6) / 3 = **0.756**.

## Why it penalizes low ranks

The precision-at-k denominator grows with k, so a relevant document appearing later contributes a smaller precision value to the average. This is the structural reason AP **rewards putting relevant documents at the top of the list**:

- Relevant document at position 1 → contributes 1.0 to the average.
- Relevant document at position 10 → contributes ≤ 0.1.

A system that ranks correctly wins on AP even if both systems retrieve the same set of relevant documents.

## Position relative to other rank-sensitive metrics

| Metric | Granularity | Aggregates over |
|---|---|---|
| **Average Precision** | **Per-query** | **Positions of relevant documents** |
| [[MAP]] | All queries | Mean of AP across queries |
| [[MRR]] | All queries | Reciprocal of first-relevant rank |
| [[NDCG]] | All queries | Graded-relevance log-discount |

## Connections

- [[MAP]] — the cross-query aggregation built on top of AP.
- [[PrecisionAtK]] — the per-position primitive AP averages.
- [[NDCG]] / [[MRR]] — sibling rank-sensitive metrics.
- [[Precision]] / [[Recall]] — the classification-level metrics AP generalizes.
- [[InformationRetrieval]] — the parent field.
- [[RelevanceJudgment]] — the ground-truth annotations AP scores against.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
