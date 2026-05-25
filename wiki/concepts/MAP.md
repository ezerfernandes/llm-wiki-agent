---
title: "MAP (Mean Average Precision)"
type: concept
tags: [evaluation, retrieval, ranking, metric]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# MAP

**MAP** (Mean Average Precision) is a **rank-sensitive** retrieval evaluation metric. For each query, *Average Precision* averages the precision at each rank where a relevant document appears; MAP averages this over the query set. Named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] alongside [[NDCG]] and [[MRR]] for evaluation scenarios where document ranking matters.

## Intuition

A query for which the *first* retrieved document is relevant has higher Average Precision than a query for which only the *fifth* retrieved document is relevant — even if both queries eventually retrieve all relevant documents in the top-10. MAP penalizes putting relevant documents low in the ranking.

## Position relative to [[NDCG]]

- **MAP** assumes **binary relevance** (relevant or not).
- **[[NDCG]]** supports **graded relevance** (e.g. perfect / good / fair / bad) and is the more common modern choice when graded judgments are available.

## Connections

- [[rag]] — application surface.
- [[NDCG]] / [[MRR]] — sibling rank-sensitive metrics.
- [[ContextPrecision]] / [[ContextRecall]] — the rank-insensitive RAG metrics.
- [[ReRanking]] — the system component MAP evaluates.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8 walks the construction step-by-step.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 dedicates a section to walking MAP **step-by-step** as the chapter's worked retrieval-evaluation metric.

The construction:

1. **[[PrecisionAtK|Precision at position k]]** = (number of relevant results at position ≤ k) / k.
2. **[[AveragePrecision|Average precision (AP)]]** for a single query = average of precision values at each position where a relevant document appears.
3. **MAP** = mean of AP across all queries in the test suite.

Ch 8's most-quoted observation on the naming:

> *"You may be wondering why the same operation is called 'mean' and 'average.' It's likely an aesthetic choice because MAP sounds better than average average precision."* — Ch 8

**Three IR components required** (per Ch 8):

> *"Evaluating search systems needs three major components: a text archive, a set of queries, and relevance judgments indicating which documents are relevant for each query."*

See [[RelevanceJudgment]] for the annotation requirement and [[InformationRetrieval]] for the broader IR-evaluation context.

Ch 8 frames [[NDCG]] as the graded-relevance alternative: *"normalized discounted cumulative gain (nDCG), which is more nuanced in that the relevance of documents is not binary (relevant versus not relevant) and one document can be labeled as more relevant than another."*

**Recommended reading**: Ch 8 points at the *"Evaluation in Information Retrieval"* chapter of *Introduction to Information Retrieval* (Manning / Raghavan / Schütze, Cambridge University Press) — the canonical academic reference.
