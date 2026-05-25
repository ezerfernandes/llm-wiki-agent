---
title: "Perceived Utility"
type: concept
tags: [evaluation, rag, metric, verifiability, user-judgment]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Perceived Utility

**Perceived utility** is the second axis of the four-axis [[RAGEvaluation|RAG-evaluation taxonomy]] defined by [[NelsonFLiu|Nelson F. Liu]], Tianyi Zhang, and [[PercyLiang|Percy Liang]] in *"Evaluating verifiability in generative search engines"* (arXiv:2304.09848, 2023):

> *"Perceived utility: Whether the generated answer is helpful and informative."* — Ch 8 quoting the paper

## What it measures

Perceived utility is the **user-judged usefulness** of the answer — does it actually help the user accomplish their task? It is intentionally **separated from factuality and verifiability**: a hallucinated answer can have high perceived utility if it sounds plausible and addresses the user's question; a correctly-cited answer can have low perceived utility if it's terse or dodges the question.

The decoupling is important because it surfaces the **fluency-utility correlation hazard** — users tend to rate fluent answers as useful, regardless of whether the answer is supported. This is the structural reason perceived utility alone is **insufficient** for RAG evaluation; it must be paired with citation-based verifiability axes ([[CitationRecall]], [[CitationPrecision]]).

## Position vs the other axes

| Axis | What it captures | Risk of user-rating bias |
|---|---|---|
| [[Fluency]] | Text well-formed-ness | Low (close to surface) |
| **Perceived utility** | User-judged helpfulness | **High — confounded with fluency** |
| [[CitationRecall]] | Claims-have-citations | Low (mechanical check) |
| [[CitationPrecision]] | Citations-support-claims | Low (mechanical check) |

The four-axis taxonomy works as a **system** because the two citation axes are the antidote to perceived-utility's bias.

## Connections

- [[RAGEvaluation]] — the parent four-axis taxonomy.
- [[Fluency]] — sibling non-citation axis (correlated risk).
- [[CitationRecall]] / [[CitationPrecision]] — sibling citation axes (the antidote).
- [[Faithfulness]] / [[AnswerRelevance]] — Ragas metrics that touch the same user-judgment space.
- [[llmasjudge]] — the automation path.
- [[NelsonFLiu]] / [[PercyLiang]] — paper authors.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
