---
title: "Reference-Based Metric"
type: concept
tags: [evaluation, metric, taxonomy]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Reference-Based Metric

A metric that **requires [[ReferenceData|reference data]]** to compute a score. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]: *"Metrics that require references are reference-based, and metrics that don't are reference-free."*

## Examples (Ch 3)

- [[ExactMatch]] — does the response match a reference?
- [[bleu|BLEU]] / [[ROUGE]] / [[METEOR]] / [[TER]] / [[CIDEr]] — [[LexicalSimilarity|lexical-similarity]] metrics.
- [[BERTScore]] / [[MoverScore]] — [[SemanticSimilarity|semantic-similarity]] metrics.
- [[BLEURT]] — a learned [[ReferenceBasedJudge|reference-based judge]].

## Trade-offs vs reference-free

| Property | Reference-based | [[ReferenceFreeMetric\|Reference-free]] |
|---|---|---|
| Needs ground-truth | Yes | No |
| Cost to scale | Bottlenecked by reference data | Scales with model inference only |
| Production-time usability | Limited (no references) | Yes |
| Sensitive to reference quality | Yes | No |
| Correlation with human judgment | Variable; bad refs → bad metric (Freitag et al. 2023) | Variable; depends on the judge/method |

## The reference-quality problem

Ch 3 flags reference-based metrics' Achilles heel: their reliability depends on reference data being correct and exhaustive. Adept's [[Fuyu]] image-captioning result and the [[WMT2023]] bad-reference finding are Ch 3's canonical examples.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[ReferenceFreeMetric]] — the complementary category.
- [[ReferenceData]] — what reference-based metrics consume.
- [[SimilarityMeasurement]] / [[ExactMatch]] / [[LexicalSimilarity]] / [[SemanticSimilarity]] — concrete reference-based families.
