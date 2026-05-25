---
title: "BLEURT"
type: concept
tags: [evaluation, metric, llm-as-judge, reference-based]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# BLEURT

**BLEURT** — *Bilingual Evaluation Understudy with Representations from Transformers* (Sellam et al. 2020) — is a learned [[ReferenceBasedJudge|reference-based judge]]. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "BLEURT (Sellam et al., 2020) takes in a (candidate response, reference response) pair and outputs a similarity score between the candidate and reference response."

## The score-range warning

Ch 3 footnote: *"The BLEURT score range is confusing. It's approximately between -2.5 and 1.0. This highlights the challenge of criteria ambiguity with AI judges: the score range can be arbitrary."*

Compared to [[bleu|BLEU]]'s familiar [0, 100], [[ROUGE]]'s [0, 1], or [[BERTScore]]'s [-1, 1], BLEURT's [-2.5, 1.0] range is a concrete instance of [[EvaluationCriteriaAmbiguity|criteria ambiguity]] — the score is meaningful but its scale is not standardized to other metrics.

## How BLEURT differs from BLEU and BERTScore

| Metric | Type | Substrate | Range |
|---|---|---|---|
| [[bleu\|BLEU]] | Lexical n-gram precision | None (surface) | [0, 100] |
| [[BERTScore]] | Embedding cosine | [[bert\|BERT]] embeddings | ≈[-1, 1] |
| **BLEURT** | Learned reference-similarity | Pretrained Transformer + supervised fine-tune | ≈[-2.5, 1.0] |

BLEURT is **learned**: it was fine-tuned on human-rated translation pairs to predict the human score. This makes it a hybrid of [[ReferenceBasedJudge|reference-based judges]] (it takes references) and [[LLMAsAJudge|AI-as-judge]] (it's a learned model).

## Position

Sibling to [[Prometheus2|Prometheus]] in the [[ReferenceBasedJudge|reference-based judge]] category. BLEURT is older and outputs a scalar similarity; Prometheus is newer and outputs a 1-5 rubric quality score given a reference.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[ReferenceBasedJudge]] — parent category.
- [[Prometheus2]] — sibling reference-based judge.
- [[bleu|BLEU]] / [[BERTScore]] / [[ROUGE]] — sibling-but-different similarity metrics.
- [[EvaluationCriteriaAmbiguity]] — the score-range issue BLEURT exemplifies.
- [[LLMAsAJudge]] — broader paradigm.
