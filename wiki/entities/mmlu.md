---
title: "MMLU"
type: entity
tags: [benchmark, exam, knowledge]
sources: [2312.11805-gemini, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# MMLU

**Massive Multitask Language Understanding** (Hendrycks et al., 2021) — a 57-subject multiple-choice exam benchmark spanning law, biology, history, mathematics, and more. The defacto knowledge-and-reasoning benchmark for LLMs since 2020. Human-expert performance: 89.8%.

[[Gemini]] Ultra is the **first model to exceed the human-expert threshold** ([[2312.11805-gemini]]), scoring 90.04% with Chain-of-Thought @ 32 samples and uncertainty-routed consensus selection.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] of *Hands-On LLMs* names MMLU as one of the six canonical public benchmarks for evaluating generative LLMs (alongside [[GLUE]], [[TruthfulQA]], [[GSM8K]], [[HellaSwag]], [[HumanEval]]) and one of the six aggregated by the [[OpenLLMLeaderboard|Open LLM Leaderboard]]. Description in Ch 12 Table 12-1: *"57 tasks: classification, QA, sentiment."* See the [[mmlu|concept page]] for the broader [[BenchmarkSaturation]] thread.
