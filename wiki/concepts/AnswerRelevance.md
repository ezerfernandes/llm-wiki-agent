---
title: "Answer Relevance"
type: concept
tags: [evaluation, rag, metric, ragas, llm-as-judge]
sources: [hands-on-llm-ch08-semantic-search-and-rag, 2408.08849-ecg-chat]
last_updated: 2026-05-23
---

# Answer Relevance

**Answer relevance** is a [[RAGAS|Ragas]] metric that measures **how relevant the generated answer is to the question** — does it actually address what was asked, or does it answer an adjacent question? Named in Ch 8 of *Hands-On LLMs* as one of two Ragas metrics beyond the [[NelsonFLiu|Liu]] / Zhang / [[PercyLiang|Liang]] 2023 four-axis [[RAGEvaluation|RAG-evaluation taxonomy]].

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

> *"It also scores some additional useful metrics like: ... **Answer relevance** — How relevant the answer is to the question."* — Ch 8

Sibling Ragas metric: [[Faithfulness]] (answer ↔ context consistency).

## Position vs other axes

Answer relevance is the **question-side** of the RAG answer-quality space:

| Metric | Asks |
|---|---|
| **Answer relevance** | *Does the answer address the question?* |
| **[[Faithfulness]]** | *Is the answer consistent with the retrieved context?* |
| **[[PerceivedUtility]]** | *Is the answer helpful?* (Liu et al. 2023 — human-judged useful-ness) |

The pathological cases:

- High answer relevance + low faithfulness → the answer addresses the question but **invents details** not in the context (classic [[Hallucination|hallucination]]).
- Low answer relevance + high faithfulness → the answer is **truthful but off-topic** — it cites the docs faithfully but doesn't answer the user's actual question.
- High both → the answer addresses the question using context the system retrieved.

## How Ragas computes it

The Ragas answer-relevance metric typically:

1. Use an LLM to generate **N hypothetical questions** that the given answer could plausibly be answering.
2. **Embed** each generated question and the original user question.
3. **Cosine-similarity** between the generated questions and the original — high mean similarity → the answer is on-topic for the original question.

This is the structural reason answer relevance is automatable by [[llmasjudge|LLM-as-a-judge]] — the "generate questions from answer" → similarity-check pattern is closed-loop and reference-free.

## Connections

- [[RAGAS]] — the parent metric framework.
- [[RAGEvaluation]] — the broader multi-axis surface.
- [[Faithfulness]] — the sibling Ragas metric Ch 8 also names.
- [[ContextPrecision]] / [[ContextRecall]] — Ragas metrics on the retrieval side (mentioned in [[2408.08849-ecg-chat|ECG-Chat's]] seven-metric coverage but not in Ch 8).
- [[CosineSimilarity]] — the underlying similarity measure for answer-relevance computation.
- [[Embedding]] — the substrate.
- [[llmasjudge]] — the automation mechanism.
- [[GroundedGeneration]] — the generation step answer relevance scores.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
