---
title: "Iris-Typo"
type: concept
tags: [benchmark, classification, mipro, robustness, instruction-correction]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# Iris-Typo

A variant of [[Iris]] introduced by the [[2406.11695-mipro|MIPRO paper]] in which the **seed prompt contains a misspelling**: classify the flower as "*versicolour*" rather than the correct "*versicolor*". The misspelling was **initially accidental** in the paper's experiment harness — the authors kept it deliberately as *"a realistic test for optimization from a misspelled prompt"*.

## Result

The MIPRO paper's **Lesson 3** rests largely on this finding: in Iris-Typo, **the instruction optimizer learns to correct the misspelled seed prompt**, restoring task accuracy. The relevant sentence:

> *"In the Iris-Typo setting, our instruction optimizer even helps correct mistakes in the seed prompt."*

## Results (Table 2)

| Optimizer | Train | Test |
|---|---|---|
| N/A baseline | 34.7 | 32 |
| Module-Level OPRO | 32.5 | — |
| 0-Shot MIPRO | 56.8 | 56.7 |
| Bootstrap RS | 58.9 | 58.7 |
| Bayesian Bootstrap | — | — |
| **MIPRO** | **69.1** | **68.7** |

MIPRO lifts the baseline from 32 to **68.7** — a 36-point absolute gain on a task where the *only* obstacle was a typo in the prompt.

## What this implies for prompt engineering

Iris-Typo is the wiki's reference example of **automated prompt repair** — instruction optimization being usable as a *correction* layer over a hand-written seed prompt, not just an *augmentation* layer. The implication for practitioners: hand-written seed prompts can be safely shipped as approximate starting points, and the optimizer will repair small lexical errors in addition to discovering more sophisticated phrasing.

## Connections

- [[2406.11695-mipro]] — the canonical source.
- [[Iris]] — the parent benchmark.
- [[DSPyOptimizerBenchmark]] — the seven-task benchmark this variant belongs to.
- [[HotPotQAConditional]] — sibling "instructions-matter-most" benchmark (different cause: conditional rules).
- [[MIPROv2|MIPRO]] — the optimizer.
- [[PromptOptimization]] — parent task.
