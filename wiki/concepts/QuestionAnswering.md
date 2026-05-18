---
title: "Question Answering"
type: concept
tags: [nlp, application, token-level]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# Question Answering

The NLP task of producing an answer to a natural-language question. The most-studied modern variant — *extractive* QA on the **[[SQuAD]] v1.1** dataset (Rajpurkar, Zhang, Lopyrev & Liang 2016) — frames the answer as a span of text from a given passage.

Per [[d2l-nlp-applications]] §`finetuning-bert`:
> "The answer to every question is just a segment of text (text span) from the passage that the question is about."

## Fine-tuning [[BERT]] for span QA

- **Input**: `[CLS] Q [SEP] P [SEP]` with segment ids 0 (question) / 1 (passage).
- **Two independent linear heads** transform each passage token's BERT representation into a scalar — start-score $s_i$ and end-score $e_i$.
- **Softmax over positions** yields per-token start / end probabilities.
- **Prediction**: $\arg\max_{i \le j} (s_i + e_j)$ — the valid span that maximizes the sum.
- **Training objective**: maximize log-likelihood of ground-truth start and end positions.

## Token-level vs sequence-level

QA is a canonical **token-level** application — unlike sentiment / NLI which use only the `[CLS]` aggregate vector, QA applies an FC head independently to *every* passage token's BERT representation.

## Connections

- [[SQuAD]] — the canonical benchmark.
- [[BERT]] / [[FineTuningBert]] / [[ClsToken]] — the modern recipe.
- [[NLP]].
- [[d2l-nlp-applications]] §`finetuning-bert`.
