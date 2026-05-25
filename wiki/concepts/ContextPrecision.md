---
title: "Context Precision"
type: concept
tags: [evaluation, rag, retrieval, metric]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Context Precision

**Context precision** (a.k.a. *context relevance*) is one of two core RAG retrieval evaluation metrics named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]: **out of all the documents retrieved, what percentage is relevant to the query?**

## Definition

$$\text{Context Precision} = \frac{\text{relevant retrieved}}{\text{total retrieved}}$$

## Why it's easier to compute than [[ContextRecall|context recall]]

[[ChipHuyen|Huyen]] explicitly notes:

> *"In production, some RAG frameworks only support context precision, not context recall. To compute context recall for a given query, you need to annotate the relevance of all documents in your database to that query. Context precision is simpler to compute. You only need to compare the retrieved documents to the query, which can be done by an AI judge."*

Context precision is **per-retrieval-result**, while context recall is **per-corpus** — the latter requires labeling every document's relevance to every test query, which doesn't scale.

## When precision matters more than recall

For a generative model with a finite context window, every retrieved-but-irrelevant document **directly wastes context budget** and can also distract the model (Liu et al. 2023 "lost in the middle"). Precision is the right metric when context space is the constraint, especially for short-context models or expensive APIs.

## Connections

- [[ContextRecall]] — the complementary metric.
- [[rag]] — the application family.
- [[NDCG]] / [[MAP]] / [[MRR]] — rank-sensitive retrieval metrics.
- [[Precision]] / [[Recall]] — the classical-classification ancestors.
- [[LLMAsAJudge]] — the technique used to compute precision at scale.
- [[ai-engineering-ch06-rag-agents]] — primary source.
