---
title: "Amazon Mechanical Turk"
type: entity
tags: [service, crowdsourcing, annotation, amazon]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Amazon Mechanical Turk

[[Amazon]]'s crowdsourced-task marketplace. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]], Mechanical Turk is a **canonical baseline that GPT-4 beats on annotation accuracy** — at least on the [[INFOBench]] task:

> "GPT-4 isn't as accurate as human experts, but it's more accurate than annotators recruited through Amazon Mechanical Turk."

## Significance

Historically, Mechanical Turk has been the default crowdsourced-annotation surface for ML datasets. The Ch 4 finding that GPT-4 beats it on at least one annotation task is part of a broader trend that pushes [[LLMAsAJudge|AI judges]] to replace crowdsourced annotators where quality permits.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Amazon]] — parent organization.
- [[LLMAsAJudge]] — the technique that displaces Mechanical Turk for many annotation tasks.
- [[INFOBench]] — the benchmark on which this comparison was made.
- [[ComparisonData]] — Ch 2 had ScaleAI / LMSYS comparison-data labor costs as the broader benchmark.
