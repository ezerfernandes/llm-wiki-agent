---
title: "MATH benchmark"
type: concept
tags: [benchmark, math, reasoning]
sources: [2605.06651v2-ai-co-mathematician, dspy-tutorial-math]
last_updated: 2026-05-24
---

# MATH benchmark

Hendrycks et al. 2021 competition-math benchmark of 12,500 problems drawn from AMC/AIME-style high-school competitions. Originally one of the canonical measures of LLM mathematical reasoning; cited in [[2605.06651v2-ai-co-mathematician]] §4 as an early influential measure whose ceiling has been reached by frontier systems.

## Subsets

The dataset is partitioned into seven topical subjects: **algebra**, counting & probability, geometry, intermediate algebra, number theory, prealgebra, precalculus. Each problem ships with a worked-solution answer and a difficulty level (1–5).

## DSPy integration

The [[DSPy]] framework ships `dspy.datasets.MATH` as an in-framework dataset loader exposing the seven topical subsets via `MATH(subset='algebra')` etc. The loader provides train/dev splits as `list[dspy.Example]` plus a built-in `dataset.metric` callable that grades a `Prediction.answer` field against the gold answer. This is the framework's canonical benchmark for [[chainofthought|chain-of-thought]]-style reasoning tasks.

## Use as a DSPy benchmark

[[dspy-tutorial-math]] is the **canonical wiki receipt for MATH as a [[MIPROv2|MIPROv2]] optimization target**. The tutorial uses the 350-train / 350-dev algebra subset, a single-line program `dspy.ChainOfThought("question -> answer")`, [[GPT|GPT-4o-mini]] student + [[GPT|GPT-4o]] teacher, `auto="medium"`, `max_bootstrapped_demos=4, max_labeled_demos=4`, and reports a **74.0% → 88.57% lift** on the dev set — +14.6 points absolute, ~20% relative. This is the **first wiki receipt where CoT is the entire program**: no retrieval, no tools, no history.

The result fits the [[MIPROv2|MIPROv2 `auto="medium"`]] cross-task pattern: the optimizer's lift is roughly proportional to the headroom of the baseline. MATH's 74% baseline sits between the RAG-task plateau (~10-point lift on 50%+ baselines) and the agent-task lift (~5× lift on near-zero baselines), and the 14.6-point lift is consistent with that headroom argument.

## Connections

- [[2605.06651v2-ai-co-mathematician]] — cites MATH as the early-influential-but-now-saturated benchmark whose successor generation includes [[FrontierMath]] / [[IMOProofBench]] / [[PutnamBench]].
- [[dspy-tutorial-math]] — the canonical wiki MIPROv2-optimization receipt on the MATH algebra subset.
- [[GSM8K]] — sibling math-reasoning benchmark (grade-school word problems, easier than MATH).
- [[FrontierMath]] / [[IMOProofBench]] / [[PutnamBench]] — current-generation harder math benchmarks.
- [[chainofthought|`dspy.ChainOfThought`]] — the canonical *start-simple* module for MATH-shaped tasks in DSPy.
- [[MIPROv2]] — the optimizer used in the canonical wiki MATH receipt.
- [[DSPy]] — exposes MATH via `dspy.datasets.MATH(subset=...)`.
