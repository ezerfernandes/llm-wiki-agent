---
title: "JailbreakBench"
type: concept
tags: [benchmark, jailbreak, llm-safety, adversarial, red-teaming]
sources: [2603.19247-prompt-optimization-jailbreaking]
last_updated: 2026-05-22
---

# JailbreakBench

**JailbreakBench** is a curated open robustness benchmark for jailbreaking LLMs, introduced by **Chao, Debenedetti, Robey, Andriushchenko, Croce, Sehwag, Dobriban, Flammarion, Pappas, Tramèr, Hassani & Wong (2024)** at NeurIPS Datasets and Benchmarks Track. Referenced as `Chao et al., 2024` in [[2603.19247-prompt-optimization-jailbreaking]].

## Purpose

A **standardized behavioral-harm dataset** for jailbreak attack/defense evaluation. Provides:

- A fixed list of `(behavior, category)` adversarial queries.
- A protocol for scoring whether a model output enacts the behavior.
- A leaderboard with consistent prompts so attack/defense papers are directly comparable.

It is one of the two community-standard static jailbreak benchmarks ([[HarmfulQA]] is the other).

## How it's used in this wiki

[[2603.19247-prompt-optimization-jailbreaking]] uses JailbreakBench as **one of two seed pools** for adaptive prompt search — 150 prompts evenly drawn from JailbreakBench + [[HarmfulQA]] for training, with held-out evaluation on the rest of the seed distribution.

This is a **deliberate reuse**: the paper treats both benchmarks as *seed distributions* for an adaptive optimizer rather than as evaluation targets in their own right. The contrast is the headline finding — static evaluation on either benchmark underestimates the residual danger surface that an adaptive optimizer can reach starting from the *same* prompts.

## Connections

- [[2603.19247-prompt-optimization-jailbreaking]] — primary wiki source.
- [[HarmfulQA]] — sibling benchmark; joint use in this paper.
- [[Jailbreak]] — broader phenomenon.
- [[CodeAttack]] — single-vector attack family, complementary to JailbreakBench's broader category coverage.
- [[redteaming|Red Teaming]] — evaluation methodology.
- [[AttackSuccessRate]] — JailbreakBench's standard scalar metric.
- [[DangerScore]] — the *continuous* [0, 1] judge metric this paper substitutes for the binary ASR JailbreakBench typically reports.
