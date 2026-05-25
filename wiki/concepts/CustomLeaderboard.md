---
title: "Custom Leaderboard"
type: concept
tags: [leaderboard, evaluation, methodology, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Custom Leaderboard

A **private leaderboard you build over public benchmarks for your own application**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "When evaluating models for a specific application, you're basically creating a private leaderboard that ranks models based on your evaluation criteria."

## How to build one

1. **Gather application-relevant benchmarks.** Coding agent → code benchmarks ([[HumanEval]], [[MBPP]]). Writing assistant → creative-writing benchmarks. Look for the latest — old benchmarks saturate.
2. **Vet each benchmark's reliability.** *"Because anyone can create and publish a benchmark, many benchmarks might not be measuring what you expect them to measure."*
3. **Get scores.** Use a public score if available and reliable. Otherwise run via an [[EvaluationHarness|evaluation harness]] — *"Running benchmarks can be expensive."*
4. **Aggregate.** Weigh benchmarks by importance. Not all use the same scale (accuracy vs F1 vs BLEU) — choose between averaging, [[MeanWinRate|mean win rate]], or weighted combinations.

## The goal

> "As you evaluate models using public benchmarks, keep in mind that the goal of this process is to select a small subset of models to do more rigorous experiments using your own benchmarks and metrics."

The custom leaderboard is **step 2** of the [[ModelSelectionWorkflow|model-selection workflow]] — narrow to promising candidates. Step 3 (private experiments) goes deeper with proprietary data.

## Public-benchmark caveat

Even custom leaderboards over public benchmarks suffer from [[DataContamination|data contamination]]. *"Public benchmarks are unlikely to represent your application's needs perfectly, but also because they are likely contaminated."* This pushes serious teams to step 3 — private benchmarks.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Leaderboard]] — parent concept.
- [[ModelSelectionWorkflow]] — where this fits in the workflow.
- [[EvaluationHarness]] / [[lm-evaluation-harness]] / [[OpenAIEvals]] — tools to run benchmarks.
- [[BenchmarkAggregation]] / [[MeanWinRate]] — the aggregation choice.
- [[DataContamination]] — limitation that motivates private benchmarks.
