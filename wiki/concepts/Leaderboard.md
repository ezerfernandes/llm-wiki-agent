---
title: "Leaderboard"
type: concept
tags: [benchmark, leaderboard, evaluation, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Leaderboard

A **ranked list of models** built by aggregating performance across a chosen subset of benchmarks. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Aggregating benchmark results to rank models gives you a leaderboard."

## Two design questions every leaderboard answers

1. **What benchmarks to include?**
2. **How to aggregate the results into a ranking?**

## Major public leaderboards

| Leaderboard | Host | Aggregation | # benchmarks |
|---|---|---|---|
| **[[OpenLLMLeaderboard|Open LLM Leaderboard]]** | [[HuggingFace]] | Simple averaging | 6 (refreshed June 2024) |
| **[[HELMLite]]** | [[stanforduniversity\|Stanford]] | [[MeanWinRate\|Mean win rate]] | 10 |
| **[[ChatbotArena]]** | [[LMSYS]] | [[BradleyTerry\|Bradley-Terry]] from pairwise votes | — (live) |
| **[[AlpacaEval]]** | Various | AI-judge win rate vs reference | 1 (its own) |

## Why leaderboards aren't enough

Per Ch 4, several structural limitations:

- **Coverage stops short.** Open LLM Leaderboard launched with 4 benchmarks, expanded to 6, completely refreshed in June 2024 with MMLU-Pro / GPQA / MuSR / BBH / MATH-lvl5 / IFEval. *"A small set of benchmarks is not nearly enough to represent the vast capabilities and different failure modes of foundation models."*
- **Selection isn't transparent.** *"If leaderboard developers can't explain their benchmark selection processes, it might be because it's really hard to do so."*
- **Selection isn't standardized.** Open LLM and HELM Lite share only [[mmlu|MMLU]] and [[GSM8K]] (Ch 4 era).
- **[[BenchmarkCorrelation|Strongly-correlated benchmarks exaggerate biases.]]** ARC-C / MMLU / WinoGrande all ≈0.87-0.90 correlated.
- **Compute constraints exclude expensive benchmarks.** HELM Lite excluded MS MARCO; HuggingFace excluded [[HumanEval]] due to compute requirements.
- **Saturation forces refreshes.** [[GSM8K]] and [[mmlu|MMLU]] saturated → replaced by [[MATHLevel5]] and [[MMLUPro]] within a year.

## What it's good for

Public leaderboards help you **filter out bad models**, not find the best one for *your* application. *"A model that ranks high on a public leaderboard will likely, but far from always, perform well for your application."*

You should follow up with a **[[CustomLeaderboard|custom leaderboard]]** over your own evaluation pipeline.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[OpenLLMLeaderboard]] / [[HELMLite]] / [[ChatbotArena]] / [[AlpacaEval]] — major public leaderboards.
- [[BenchmarkAggregation]] / [[MeanWinRate]] — aggregation methods.
- [[BenchmarkCorrelation]] — the selection-correlation analysis.
- [[ModelSelectionWorkflow]] — leaderboards feed step 2.
- [[CustomLeaderboard]] — what you build for your application.
