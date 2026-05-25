---
title: "Reference-Free Metric"
type: concept
tags: [evaluation, metric, taxonomy]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Reference-Free Metric

A metric that does **not require [[ReferenceData|reference data]]**. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]: *"Metrics that require references are reference-based, and metrics that don't are reference-free."*

## Examples

- [[Perplexity]] — depends only on the model and the input text.
- [[FunctionalCorrectness]] — depends on whether the generated output passes test cases (no reference output needed).
- [[LLMAsAJudge|AI-as-judge]] — when used to score a response on its own (Ch 3's pattern #1).
- [[RewardModel]] — scores (prompt, response) without a reference.

## Why they matter in production

Per Ch 3: *"AI judges are fast, easy to use, and relatively cheap compared to human evaluators. They can also work without reference data, which means they can be used in production environments where there is no reference data."* This is the killer property for in-flight evaluation: when a user sends a query and you want to evaluate the response before showing it, there is no reference response yet.

## Reference-free metrics can beat reference-based ones

Freitag et al. (2023) on the WMT 2023 Metrics shared task found that *"reference-free metrics were strong contenders for reference-based metrics in terms of correlation to human judgment"* — driven in part by how often the reference data itself is wrong.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[ReferenceBasedMetric]] — the complementary category.
- [[Perplexity]] / [[FunctionalCorrectness]] / [[LLMAsAJudge]] / [[RewardModel]] — concrete reference-free metrics.
