---
title: "Context Recall"
type: concept
tags: [evaluation, rag, retrieval, metric]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Context Recall

**Context recall** is one of two core RAG retrieval evaluation metrics named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]: **out of all the documents relevant to the query, what percentage is retrieved?**

## Definition

$$\text{Context Recall} = \frac{\text{relevant retrieved}}{\text{total relevant in corpus}}$$

## Why it doesn't scale as cleanly as [[ContextPrecision|context precision]]

To compute context recall, you must **annotate the relevance of every document in the corpus** to every test query — a labeling cost that scales as `|test queries| × |corpus|`. Per [[ChipHuyen|Huyen]]:

> *"In production, some RAG frameworks only support context precision, not context recall."*

Workarounds:

- **Pooled judging**: union retrievers' top-k results, label only the union; estimate recall from the pool.
- **AI judges**: use an LM to label per-document relevance.
- **Use a small reference corpus** where exhaustive labeling is feasible (e.g. [[BEIRBenchmark|BEIR]]).

## When recall matters more than precision

For multi-hop QA or for tasks where missing the relevant document means the model cannot answer at all, **high recall is the hard constraint**. Precision can be raised post hoc by reranking; recall cannot — a document not retrieved cannot be reranked into the top k.

## Connections

- [[ContextPrecision]] — the complementary metric.
- [[rag]] — the application family.
- [[NDCG]] / [[MAP]] / [[MRR]] — rank-sensitive retrieval metrics.
- [[Precision]] / [[Recall]] — classical-classification ancestors.
- [[BEIRBenchmark]] — benchmark with reference corpora suitable for recall estimation.
- [[ai-engineering-ch06-rag-agents]] — primary source.
