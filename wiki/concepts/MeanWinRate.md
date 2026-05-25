---
title: "Mean Win Rate"
type: concept
tags: [evaluation, aggregation, leaderboard, methodology]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Mean Win Rate

A **leaderboard-aggregation method**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "HELM authors … decided to shun averaging in favor of mean win rate, which they defined as 'the fraction of times a model obtains a better score than another model, averaged across scenarios'."

## How it differs from averaging

| Method | Formula | Sensitivity |
|---|---|---|
| **Averaging** | mean(scores across benchmarks) | Treats 80% on hard benchmark = 80% on easy one |
| **Mean win rate** | mean(fraction of opponent-models beaten per benchmark) | Order-preserving — benchmark scales don't dominate |

Mean win rate is more robust to **benchmark scale differences** — different benchmarks use accuracy, F1, BLEU, pass@k — adding them is apples-to-oranges, but counting wins is scale-invariant.

## Where it's used

- **[[HELMLite]]** (Stanford) — the published example.

Compare to **simple averaging** used by [[OpenLLMLeaderboard]] (HuggingFace).

## Position

Conceptually adjacent to [[ComparativeEvaluation|comparative evaluation]] — both reduce a model to its pairwise outcome rate rather than its score. Difference: comparative evaluation is *between models* on *individual queries*; mean win rate is *between models* on *aggregate benchmark scores*.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[HELMLite]] — canonical use site.
- [[Leaderboard]] / [[BenchmarkAggregation]] — parent concept.
- [[ComparativeEvaluation]] / [[WinRate]] — related comparative paradigms from Ch 3.
- [[OpenLLMLeaderboard]] — sibling leaderboard using averaging instead.
