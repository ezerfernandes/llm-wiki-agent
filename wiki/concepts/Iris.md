---
title: "Iris"
type: concept
tags: [benchmark, classification, tabular, fisher]
sources: [2407.10930-better-together, 2406.11695-mipro]
last_updated: 2026-05-22
---

# Iris

The classic 150-example flower-classification dataset (Fisher 1936/1988; UCI Machine Learning Repository, CC BY 4.0): predict species ∈ {*setosa*, *versicolor*, *virginica*} from `petal_length`, `petal_width`, `sepal_length`, `sepal_width` (all in cm).

## In [[2407.10930-better-together|Soylu, Potts & Khattab (2024)]] — BetterTogether

The **extrapolation task** of the [[BetterTogether]] benchmark — included to test whether the alternation pattern generalizes outside QA / math to feature-based tabular classification. Implemented as a single-module CoT program over a [[DSPySignatures|signature]] `petal_length, petal_width, sepal_length, sepal_width → answer`. Three 50-example splits (train / dev / test); 15/35 sub-sample for prompt-opt train/val.

The **largest *relative* gains in the paper** appear here — **3.5–88%** over the better baseline:
- mistral-7b: Θ → Π reaches **66.7** (vs Π-only 57.3).
- llama-2-7b: vanilla scores **0.0%**; Π → Θ → Π lifts it to **65.3** — the *only* path that succeeds because weight-first strategies have no bootstrap traces.
- llama-3-8b: Π → Π wins (82.0); BetterTogether configurations close behind.

Iris is the **canonical illustration of the "prompts-first unlocks fine-tuning"** half of the BetterTogether thesis: when vanilla zero-shot fails outright, only the Π → Θ direction can build a usable SFT dataset.

## In [[2406.11695-mipro|Opsahl-Ong et al. (2024)]] — MIPRO

Iris is one of seven tasks in the [[DSPyOptimizerBenchmark]] and the **sibling** of [[IrisTypo]] — the same dataset and program but with a misspelled seed instruction ("versicolour" vs the correct "versicolor"). The misspelling was *"initially accidental"* but kept *"as a realistic test for optimization from a misspelled prompt."* On the typo variant, MIPRO **corrects the seed prompt's spelling error** as part of optimization (Lesson 3).

On vanilla Iris (no typo), the demos-only baselines win — Bootstrap RS reaches **94.1 test** vs MIPRO's 88.6 — because the rules are easy to convey via examples once the prompt is spelled correctly.

## Connections
- [[2407.10930-better-together]]
- [[2406.11695-mipro]] — uses Iris (and its [[IrisTypo|misspelled-prompt variant]]) as MIPRO benchmark tasks.
- [[IrisTypo]] — the typo variant.
- [[DSPyOptimizerBenchmark]] — the MIPRO benchmark this is part of.
- [[BetterTogether]]
- [[chainofthought|Chain-of-Thought]] — the single module's strategy.
- [[DSPySignatures]] — the typed signature pattern used.
