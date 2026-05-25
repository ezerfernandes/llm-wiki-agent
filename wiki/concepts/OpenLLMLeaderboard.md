---
title: "Open LLM Leaderboard"
type: concept
tags: [leaderboard, evaluation, huggingface]
sources: [ai-engineering-ch04-evaluate-ai-systems, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Open LLM Leaderboard

[[HuggingFace]]'s flagship **open-LLM ranking leaderboard**, launched in 2023. Discussed at length in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]].

## Evolution

- **2023 launch** — 4 benchmarks.
- **Late 2023 expansion** — 6 benchmarks: [[ARCC]], [[mmlu|MMLU]], [[HellaSwag]], [[TruthfulQA]], [[WinoGrande]], [[GSM8K]].
- **June 2024 refresh** — *fully replaced* benchmark set because most had saturated. New set:
  - [[MATHLevel5]] (replacing [[GSM8K]])
  - [[MMLUPro]] (replacing [[mmlu|MMLU]])
  - [[GPQA]] — graduate-level Q&A
  - [[MuSR]] — multistep chain-of-thought reasoning
  - [[BigBenchHard|BBH]] — reasoning subset of BIG-bench
  - [[IFEval]] — instruction-following

## Aggregation

**Simple averaging** across all benchmarks — *"treating all benchmark scores equally, i.e., treating an 80% score on TruthfulQA the same as an 80% score on GSM-8K."* Ch 4 critiques this as not weighing benchmark difficulty.

Compare to [[HELMLite]] which uses [[MeanWinRate|mean win rate]] instead.

## Notable exclusions

- **[[HumanEval]]** — *"Hugging Face opted out of HumanEval due to its large compute requirements — you need to generate a lot of completions."*

## Benchmark choice rationale

[[LewisTunstall]] (HuggingFace) responded on Discord to Huyen's question about benchmark selection: *"they were guided by the benchmarks that the then popular models used."*

## Position

The wiki's canonical leaderboard reference for [[OpenWeight|open-weight]] models. Compare to [[ChatbotArena]] (human comparative voting), [[AlpacaEval]] (AI-judge win rate vs reference), [[HELMLite]] (Stanford, mean-win-rate aggregation).

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[HuggingFace]] — host.
- [[Leaderboard]] — parent concept.
- [[ARCC]] / [[mmlu|MMLU]] / [[HellaSwag]] / [[TruthfulQA]] / [[WinoGrande]] / [[GSM8K]] — original 6 benchmarks.
- [[MATHLevel5]] / [[MMLUPro]] / [[GPQA]] / [[MuSR]] / [[BigBenchHard]] / [[IFEval]] — June 2024 replacements.
- [[BenchmarkCorrelation]] — Galambosi 2024 correlation analysis was done on these benchmarks.
- [[BenchmarkAggregation]] / [[MeanWinRate]] — the aggregation-method choice.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names the Open LLM Leaderboard as the **canonical multi-benchmark aggregator** in its survey of generative-LLM evaluation methods. The chapter's framing:

> *"A great example of a leaderboard that contains the most common benchmarks is HuggingFace's Open LLM Leaderboard ... It includes HellaSwag, MMLU, TruthfulQA, GSM8k, and two more."* — Ch 12

Ch 12 also surfaces the **leaderboard-overfit risk** as a downside of leaderboard-driven model selection — consistent with Ch 4's [[BenchmarkSaturation]] framing and the chapter's invocation of [[GoodhartsLaw|Goodhart's Law]] (*"When a measure becomes a target, it ceases to be a good measure"*).
