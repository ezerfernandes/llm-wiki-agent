---
title: "Heart Disease"
type: concept
tags: [benchmark, classification, uci, mipro, answer-ensemble]
sources: [2406.11695-mipro]
last_updated: 2026-05-22
---

# Heart Disease

The UCI Heart Disease classification dataset (Detrano et al. 1989, *American Journal of Cardiology* 64:304–10). Binary classification given **13 categorical and continuous clinical features**. Used by the [[2406.11695-mipro|MIPRO paper]] as one of the seven [[DSPyOptimizerBenchmark|optimizer-benchmark tasks]].

## Program structure

The DSPy program is an **Answer Ensemble** with 2 modules and 4 LM calls — three [[chainofthought|Chain-of-Thought]] clinical opinions are generated, then aggregated by a final-judgment module.

## Why it tests conditional rules

The paper hypothesizes that *"it may be harder to find a small number of crucial patterns in Heart Disease, and we thus test a program that generates three clinical opinions using Chain-of-Thought LM calls and then generates a final judgment accordingly."* The features (chest pain type, exercise-induced angina, ST depression slope, etc.) span clinical heuristics that the LM does not necessarily know from pretraining; the proposer LM must learn to inject the rules.

## Results (Table 2)

| Optimizer | Train | Test |
|---|---|---|
| N/A baseline | 23.3 | 26.8 |
| 0-Shot MIPRO | 26.8 | 25.8 |
| Bootstrap RS | 78.4 | **79.2** |
| MIPRO | 75.2 | 74.2 |

Heart Disease is **one of the two tasks** (with vanilla [[Iris]]) where joint MIPRO does *not* significantly beat the demos-only Bootstrap RS baseline. The paper attributes this to *"initializing our optimizers with a simple seed instruction that does not convey any classification criteria, which current instruction optimizers have a limited ability to infer"* — i.e. **without a non-trivial seed instruction, instruction optimization cannot learn complex clinical rules from scratch**. This is the converse of [[IrisTypo]]: instructions matter for tasks with conditional rules, but only if there's enough scaffolding for the proposer to start from.

## Connections

- [[2406.11695-mipro]] — the canonical source.
- [[DSPyOptimizerBenchmark]] — the seven-task benchmark.
- [[MIPROv2|MIPRO]] — the optimizer.
- [[chainofthought|Chain-of-Thought]] — per-module strategy in the Answer-Ensemble program.
- [[Iris]] — sibling tabular-classification benchmark.
- [[HotPotQAConditional]] — sibling conditional-rules benchmark.
