---
title: "WildBench"
type: concept
tags: [benchmark, real-user-prompts, evaluation, free-form]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# WildBench

**WildBench** (Lin, Deng, Chandu, Brahman, Ravichander, Pyatkin, Dziri, Le Bras & Choi, arXiv:2406.04770, 2024) — *"Benchmarking LLMs with challenging tasks from real users in the wild"* — uses real user prompts collected from deployed LM applications as the evaluation distribution. Free-form natural-language responses, LM-judge scoring.

## In Zhang et al. 2026

[[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] include WildBench as one of four Study 2 single-agent prompt-optimization tasks. **Average gain across all six optimizers on Claude Haiku: −0.82 pts** — the worst of the four tasks. Best single-method gain: **+0.7 pts** ([[OPRO]]) — below the 2-pt [[HeadroomTest|headroom threshold]].

WildBench is a canonical Study 2 **negative example**: accepts free-form natural language → model's zero-shot is already near-optimal for the format → no [[CanButDoesntPattern|"can but doesn't" gap]] for optimization to unlock.

## Results

**Claude Haiku** (Table 2):

| Method | WildBench |
|---|---|
| Zero-Shot | 68.9 |
| [[APE]] | 68.0 |
| [[OPRO]] | 69.0 |
| [[EvoPrompt]] | 68.3 |
| [[PromptBreeder]] | 68.5 |
| DSPy-style | 65.1 |
| [[PROSEOptimizer\|PROSE]] | **69.6** |

**Nova Lite** (Table 4):

| Method | WildBench |
|---|---|
| Zero-Shot | 64.6 |
| PromptBreeder | **65.6** |
| Most others | ≤64.6 |

WildBench is one of three **free-form** tasks (alongside [[FeedbackBench]] and [[XSum]]) for which the [[CoinFlipOptimization|coin-flip aggregate]] holds.

## Connections

- [[2604.14585-prompt-optimization-coin-flip]] — canonical source for WildBench's role as a free-form task.
- [[FeedbackBench]] / [[XSum]] — sibling free-form failure tasks.
- [[HelpSteer2]] — the structured-output counterexample.
- [[CanButDoesntPattern]] — the property WildBench lacks.
- [[HeadroomTest]] — diagnostic that flags WildBench as not worth optimizing.
- [[CoinFlipOptimization]] — the failure pattern WildBench instantiates.
