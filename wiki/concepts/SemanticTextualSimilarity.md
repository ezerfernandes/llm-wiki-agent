---
title: "Semantic Textual Similarity"
type: concept
tags: [nlp, text-pair-regression, application]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# Semantic Textual Similarity

**Semantic textual similarity (STS)** measures the meaning-similarity of a pair of sentences as a continuous value — a canonical *text-pair regression* task. Per [[d2l-nlp-applications]] §`finetuning-bert`: "in the Semantic Textual Similarity Benchmark dataset, the similarity score of a pair of sentences is an ordinal scale ranging from 0 (no meaning overlap) to 5 (meaning equivalence)" (Cer, Diab, Agirre et al. 2017).

## Examples (STS-B)

| Sentence 1 | Sentence 2 | Score |
|---|---|---|
| "A plane is taking off." | "An air plane is taking off." | 5.000 |
| "A woman is eating something." | "A woman is eating meat." | 3.000 |
| "A woman is dancing." | "A man is talking." | 0.000 |

## Fine-tuning [[BERT]]

Same input template as [[NaturalLanguageInference|NLI]] — `[CLS] A [SEP] B [SEP]` with segment ids — but the head outputs a single continuous value (regression), trained with mean squared error instead of cross-entropy.

## Connections

- [[NaturalLanguageInference]] — the closely-related *classification* twin task.
- [[BERT]] / [[FineTuningBert]] — the canonical model template.
- [[d2l-nlp-applications]] §`finetuning-bert`.
