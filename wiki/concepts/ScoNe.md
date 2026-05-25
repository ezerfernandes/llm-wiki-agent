---
title: "ScoNe"
type: concept
tags: [benchmark, nli, negation, mipro]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# ScoNe

**S**coped **N**egation **e**ntailment benchmark (She, Potts, Bowman & Geiger, ACL 2023). Natural language inference task in which the model must reason about **logical puzzles with nested negation** — entailment relationships that flip with the scope of negation operators.

Used by the [[2406.11695-mipro|MIPRO paper]] as one of seven [[DSPyOptimizerBenchmark|optimizer benchmark tasks]] — picked because *"we use ScoNe... an entailment task in which LMs must reason about logical puzzles with nested negation"* to **assess whether optimizers can express data-specific nuances that are not evident from the program itself**.

## Program structure

Single-stage [[chainofthought|Chain-of-Thought]] DSPy program; 1 module, 1 LM call, Exact Match metric. Demo bootstrapping uses GPT-4o as teacher (not Llama-3-8B) because of the task's difficulty.

## Results (Table 2)

| Optimizer | Train | Dev | Test |
|---|---|---|---|
| N/A baseline | 57.0 | 56.2 | 69.1 |
| Module-Level OPRO -G | 70.0 | 67.4 | 76.1 |
| Module-Level OPRO | 69.1 | 67.6 | 73.5 |
| 0-Shot MIPRO | 66.3 | 65.2 | 71.5 |
| 0-Shot MIPRO++ | 69.0 | 66.9 | 75.7 |
| Bootstrap RS | 74.9 | 69.6 | 75.4 |
| Bayesian Bootstrap | 75.4 | 67.4 | 77.4 |
| **MIPRO** | 74.6 | 69.8 | **79.4** |

## Two important findings on ScoNe

1. **Grounding hurts.** Module-Level OPRO **−G** (the "no grounding" ablation) **beats** the grounded Module-Level OPRO — 76.1 vs 73.5 test. This is the paper's main exhibit for **Lesson 4** (*"The best proposal strategy varies by task"*) and the motivation for **MIPRO++** (which learns *whether* to ground per-task and so recovers ScoNe at 75.7).

2. **0-Shot MIPRO++ outperforms 0-Shot MIPRO** specifically here — the Bayesian model over proposer hyperparameters learns that grounding isn't useful for ScoNe, and the model's importance scores back this out (dataset summary low; tip-choice high).

## Connections

- [[2406.11695-mipro]] — the canonical source.
- [[DSPyOptimizerBenchmark]] — the seven-task benchmark.
- [[MIPROv2|MIPRO]] — the optimizer family.
- [[ChristopherPotts]] — ScoNe co-author and senior MIPRO author.
- [[NaturalLanguageInference]] — parent task family.
- [[chainofthought|Chain-of-Thought]] — per-module strategy.
