---
title: "N-gram Overlap"
type: concept
tags: [evaluation, contamination, methodology]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# N-gram Overlap

A **[[DataContamination|data-contamination]] detection method** that flags evaluation samples whose n-gram (n-token) sequences appear in training data. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "If a sequence of 13 tokens in an evaluation sample is also in the training data, the model has likely seen this evaluation sample during training. This evaluation sample is considered dirty."

## The trade-off

| Method | Accuracy | Cost | Requires |
|---|---|---|---|
| **N-gram overlap** | More accurate | Expensive — compare each eval sample with entire training data | Access to training data |
| **[[Perplexity\|Perplexity]]** | Less accurate | Cheap | Just the model |

N-gram overlap is the gold standard for contamination detection, but it requires both the eval set *and* the training data. For [[OpenSourceModel|open]] or [[OpenModel|open]] models, it's feasible; for [[CommercialModel|commercial models]], it's not.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[DataContamination]] — what it detects.
- [[Perplexity]] — the cheaper alternative.
- [[BenchmarkDecontamination]] — what you do once contamination is found.
