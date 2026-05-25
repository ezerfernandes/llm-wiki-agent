---
title: "GSM8K"
type: concept
tags: [benchmark, math, arithmetic]
sources: [2605.06651v2-ai-co-mathematician, 2407.10930-better-together, ai-engineering-ch04-evaluate-ai-systems, hands-on-llm-ch12-fine-tuning-generation-models, dspy-optimizer-tracking-tutorial]
last_updated: 2026-05-24
---

# GSM8K

Grade-school math word-problem benchmark (Cobbe et al. 2021); cited in [[2605.06651v2-ai-co-mathematician]] §4 as one of the predecessors to current math benchmarks ([[FrontierMath]], [[IMOProofBench]], [[PutnamBench]]) and influential in measuring early LLM progress.

## In [[2407.10930-better-together|Soylu, Potts & Khattab (2024)]] — BetterTogether

One of three benchmark tasks. Implemented as a **1-module CoT** DSPy program that generates a reasoning string followed by an answer; accuracy measured by extracting the last number on the first line and comparing to the ground truth. 1000 train / 500 dev / 1319 test. **Smallest [[BetterTogether]] gains across the three tasks** — 2.5–10% over the better baseline — because the 1-module program has little "compound" structure for the prompt–weight alternation to exploit. Best configurations: Θ → Π wins on mistral-7b (48.3) and llama-3-8b (78.9); Π → Θ wins on llama-2-7b (27.3).

## Connections
- [[2605.06651v2-ai-co-mathematician]]
- [[MATH-benchmark|MATH]]
- [[2407.10930-better-together]] — uses GSM8K as the *arithmetic-reasoning* benchmark in the BetterTogether evaluation.
- [[BetterTogether]] — the optimizer evaluated on GSM8K.
- [[chainofthought|Chain-of-Thought]] — the single module strategy.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

GSM8K (Cobbe et al. 2021, [[openai|OpenAI]]) was one of the **original 6 benchmarks** on HuggingFace's [[OpenLLMLeaderboard|Open LLM Leaderboard]] and one of only two ([[mmlu|MMLU]] is the other) shared with [[stanforduniversity|Stanford]]'s [[HELMLite]]. Per Ch 4:

> "Measuring the ability to solve a diverse set of math problems typically encountered in grade school curricula."

**Saturated by mid-2024.** HuggingFace replaced GSM8K with [[MATHLevel5]] (the hardest tier of competitive-math problems) in the **June 2024 leaderboard refresh**. Per the [[BenchmarkCorrelation|Galambosi 2024 correlation analysis]], GSM8K correlates strongly with [[ARCC]] (0.744), [[mmlu|MMLU]] (0.794), and [[WinoGrande]] (0.798) — all reasoning-correlated benchmarks.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names GSM8k in **Table 12-1** as one of six canonical public benchmarks for evaluating generative LLMs (alongside [[MMLU]], [[GLUE]], [[TruthfulQA]], [[HellaSwag]], [[HumanEval]]) and as one of the six aggregated by the [[OpenLLMLeaderboard|Open LLM Leaderboard]]. Description: *"grade-school math word problems."*

Ch 12 also surfaces a **DPO-data-engineering** receipt: when filtering the `argilla/distilabel-intel-orca-dpo-pairs` dataset for the chapter's worked preference-tuning recipe, the filter excludes any example with `in_gsm8k_train=True` — preventing leakage of GSM8k training data into the preference-tuning dataset.

## In [[dspy-optimizer-tracking-tutorial|DSPy Optimizer Tracking tutorial]] (2026)

First wiki receipt of GSM8K loaded via DSPy's **in-framework dataset module** — `from dspy.datasets.gsm8k import GSM8K, gsm8k_metric` — exposing both the dataset (`gsm8k.train` / `gsm8k.dev`) and a built-in metric (`gsm8k_metric`) ready to pass into any [[DSPyOptimizers|optimizer]]. The tutorial's worked example: `dspy.ChainOfThought("question -> answer")` optimized by `dspy.MIPROv2(metric=gsm8k_metric, auto="light")` over `gpt-4o`. This is the **first wiki MIPROv2 receipt on GSM8K** and the first MIPROv2 receipt using `gpt-4o` (rather than `gpt-4o-mini` or a Llama student) as the task LM. No headline accuracy is reported — the tutorial's scope is the [[MLflow]] tracking surface, not the optimization gain. The recipe complements the prior wiki [[chainofthought|CoT]]-on-GSM8K receipt from [[2407.10930-better-together]] (Soylu/Potts/Khattab 2024), which used a 1-module CoT DSPy program and reported small (2.5–10%) [[BetterTogether]] lifts because the 1-module shape leaves little compound structure to exploit.
