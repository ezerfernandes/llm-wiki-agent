---
title: "Simpson's Paradox"
type: concept
tags: [statistics, paradox, evaluation, methodology]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Simpson's Paradox

A phenomenon in which **model A performs better than model B on aggregated data but worse on every subset of data**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Model A performs better than model B on aggregated data but worse than model B on every subset of data."

## The renal-calculi example (Ch 4 Table 4-6)

| | Group 1 | Group 2 | Overall |
|---|---|---|---|
| **Model A** | 93% (81/87) | 73% (192/263) | 78% (273/350) |
| **Model B** | 87% (234/270) | 69% (55/80) | 83% (289/350) |

Model A beats B in both groups but loses overall — because A and B were evaluated on different subset distributions. The data is from Charig et al. 1986 on kidney-stone treatments.

## Why this matters for AI evaluation

If your model-A vs model-B comparison uses different prompt distributions per model (e.g. you tested A more on hard prompts), the aggregate ranking can be misleading. **The cure is [[DataSlicing|slicing]]** — evaluate on every subset and present per-slice + aggregate results.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[DataSlicing]] — the methodology that prevents this.
- [[EvaluationPipeline]] — parent process.
- [[BiasVarianceTradeoff]] — related statistical phenomenon.
