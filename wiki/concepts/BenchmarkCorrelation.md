---
title: "Benchmark Correlation"
type: concept
tags: [benchmark, evaluation, methodology, leaderboard]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Benchmark Correlation

The **Pearson correlation between models' scores across benchmarks**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "An important aspect of benchmark selection that is often overlooked is benchmark correlation. It is important because if two benchmarks are perfectly correlated, you don't want both of them. Strongly correlated benchmarks can exaggerate biases."

## The Galambosi 2024 analysis

Computed in January 2024 by [[BalazsGalambosi]] for the [[OpenLLMLeaderboard|Open LLM Leaderboard]]'s 6 benchmarks (Table 4-5 in Ch 4):

| | ARC-C | HellaSwag | MMLU | TruthfulQA | WinoGrande | GSM-8K |
|---|---|---|---|---|---|---|
| **ARC-C** | 1.000 | 0.481 | 0.867 | 0.481 | 0.886 | 0.744 |
| **HellaSwag** | 0.481 | 1.000 | 0.611 | 0.423 | 0.484 | 0.355 |
| **MMLU** | 0.867 | 0.611 | 1.000 | 0.551 | 0.901 | 0.794 |
| **TruthfulQA** | 0.481 | 0.423 | 0.551 | 1.000 | 0.500 | 0.455 |
| **WinoGrande** | 0.886 | 0.484 | 0.901 | 0.500 | 1.000 | 0.798 |
| **GSM-8K** | 0.744 | 0.355 | 0.794 | 0.455 | 0.798 | 1.000 |

## What jumps out

- **[[ARCC]] / [[mmlu|MMLU]] / [[WinoGrande]]** are mutually correlated at ≈0.87-0.90 — all test reasoning. Including all three triple-counts that capability.
- **[[TruthfulQA]]** is only moderately correlated (~0.5) with everything else — *"suggesting that improving a model's reasoning and math capabilities doesn't always improve its truthfulness."*
- **[[HellaSwag]]** is moderate across the board — commonsense is partially independent of reasoning.

## Implication for leaderboard design

If your leaderboard's average score is dominated by 3 reasoning-correlated benchmarks plus 3 weakly-correlated ones, the reasoning signal is **overweighted by construction** — even if all benchmarks are weighted equally in the formula.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[BalazsGalambosi]] — who computed it.
- [[Leaderboard]] / [[BenchmarkAggregation]] — what this analysis informs.
- [[ARCC]] / [[mmlu|MMLU]] / [[WinoGrande]] / [[TruthfulQA]] / [[HellaSwag]] / [[GSM8K]] — the 6 benchmarks analyzed.
