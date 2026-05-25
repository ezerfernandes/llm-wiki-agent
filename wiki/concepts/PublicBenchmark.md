---
title: "Public Benchmark"
type: concept
tags: [benchmark, evaluation, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Public Benchmark

An externally-developed, publicly-available evaluation dataset. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]], there are **thousands** of public benchmarks:

> "Google's BIG-bench (2022) alone has 214 benchmarks. … EleutherAI's lm-evaluation-harness supports over 400 benchmarks. OpenAI's evals lets you run any of the approximately 500 existing benchmarks."

## Three structural problems

1. **Saturation.** Models reach near-perfect scores → the benchmark stops differentiating. [[GSM8K]] saturated within a year; [[mmlu|MMLU]] too. Forces creation of harder successors ([[MATHLevel5]], [[MMLUPro]], [[GPQA]]).
2. **[[DataContamination|Contamination]].** *"A benchmark stops being useful as soon as it becomes public."* — Huyen's friend. [[openai|OpenAI]]'s Brown et al. 2020 analysis found **13 GPT-3 benchmarks ≥40% in training data**.
3. **Coverage mismatch.** No public benchmark perfectly represents your application's needs.

## Useful, but not sufficient

> "Public benchmarks will help you filter out bad models, but they won't help you find the best models for your application."

After public-benchmark filtering, you should run your own [[EvaluationPipeline|evaluation pipeline]] on your own [[PrivateBenchmark|private benchmark]].

## Position in workflow

Step 2 of the [[ModelSelectionWorkflow|four-step model-selection workflow]] uses public benchmarks to narrow candidates. Step 3 moves to private benchmarks for the final pick.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[PrivateBenchmark]] — the complement.
- [[Leaderboard]] / [[CustomLeaderboard]] — aggregation surfaces.
- [[EvaluationHarness]] / [[lm-evaluation-harness]] / [[OpenAIEvals]] — tools to run public benchmarks.
- [[DataContamination]] — the deepest problem.
- [[BenchmarkSaturation]] — the second-deepest problem.
- [[bigbench]] / [[mmlu|MMLU]] / [[HumanEval]] — high-profile examples.
