---
title: "Benchmark Aggregation"
type: concept
tags: [benchmark, leaderboard, evaluation, methodology]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Benchmark Aggregation

The question of **how to combine multiple benchmark scores into a single leaderboard ranking**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]], two questions every [[Leaderboard|leaderboard]] design must answer:

1. What benchmarks to include?
2. **How to aggregate the results to rank models?**

## Three known aggregation methods

| Method | User | Property |
|---|---|---|
| **Simple averaging** | [[OpenLLMLeaderboard|HuggingFace Open LLM Leaderboard]] | Easy; treats benchmark scales as comparable |
| **[[MeanWinRate\|Mean win rate]]** | [[HELMLite]] | Scale-invariant; rewards beating opponents |
| **Weighted combination** | Custom | You apply your own importance weights |

## Why simple averaging is problematic

> "Averaging means treating all benchmark scores equally, i.e., treating an 80% score on TruthfulQA the same as an 80% score on GSM-8K, even if an 80% score on TruthfulQA might be much harder to achieve than an 80% score on GSM-8K. This also means giving all benchmarks the same weight, even if, for some tasks, truthfulness might weigh a lot more than being able to solve grade school math problems."

## Why weighting matters

Two failure modes simple averaging masks:
- **Difficulty mismatch** — 80% on different benchmarks represents very different model quality.
- **Importance mismatch** — your application may care 10× more about truthfulness than math.
- **[[BenchmarkCorrelation|Correlation duplication]]** — three reasoning-correlated benchmarks triple-count reasoning.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Leaderboard]] — the surface aggregation produces.
- [[MeanWinRate]] — one specific aggregation method.
- [[BenchmarkCorrelation]] — the issue that motivates careful weighting.
- [[CustomLeaderboard]] — where you choose your own aggregation.
