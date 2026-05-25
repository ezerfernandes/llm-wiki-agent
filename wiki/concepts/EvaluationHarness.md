---
title: "Evaluation Harness"
type: concept
tags: [evaluation, tooling, benchmark]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Evaluation Harness

A **tool that helps you run a model against many benchmarks**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "A tool that helps you evaluate a model on multiple benchmarks is an evaluation harness."

## Two main public harnesses

| Harness | Maintainer | # benchmarks (Ch 4 era) |
|---|---|---|
| **[[lm-evaluation-harness]]** | [[EleutherAI]] | 400+ |
| **[[OpenAIEvals]]** | [[openai\|OpenAI]] | ≈500 (plus user-registered) |

## What harnesses solve

- Standard prompt formatting across benchmarks.
- Standard scoring code.
- Caching, retries, parallelism.
- Compute budget management (some benchmarks are expensive).

## What they don't solve

- Choosing *which* benchmarks to run.
- Aggregating across benchmarks (that's [[BenchmarkAggregation|aggregation]] / [[Leaderboard|leaderboard]] territory).
- Compute cost — Stanford spent $80K-$100K running HELM on 30 models.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[lm-evaluation-harness]] / [[OpenAIEvals]] — canonical implementations.
- [[PublicBenchmark]] — what harnesses run.
- [[CustomLeaderboard]] — typically built on top of a harness.
- [[ModelSelectionWorkflow]] — step 2's primary tooling.
