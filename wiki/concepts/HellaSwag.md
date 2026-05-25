---
title: "HellaSwag"
type: concept
tags: [benchmark, commonsense, mcq, evaluation]
sources: [ai-engineering-ch04-evaluate-ai-systems, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# HellaSwag

Zellers et al. 2019 — a **commonsense [[MultipleChoiceQuestion|MCQ]] benchmark** that tests the ability to predict the completion of a sentence or scene. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Measuring the ability to predict the completion of a sentence or a scene in a story or video. The goal is to test common sense and understanding of everyday activities."

## Position

One of the **original 6 benchmarks** on HuggingFace's [[OpenLLMLeaderboard|Open LLM Leaderboard]] (2023). Moderately correlated with most other benchmarks per the [[BenchmarkCorrelation|Galambosi 2024 correlation table]] — commonsense is partially independent of pure reasoning.

Removed in HuggingFace's June 2024 leaderboard refresh — saturated.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[OpenLLMLeaderboard]] — leaderboard that included it.
- [[BenchmarkCorrelation]] — independence story.
- [[MultipleChoiceQuestion]] — format.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names HellaSwag (Zellers et al. 2019) in **Table 12-1** as one of six canonical public benchmarks for evaluating generative LLMs (alongside [[MMLU]], [[GLUE]], [[TruthfulQA]], [[GSM8K]], [[HumanEval]]) and as one of the six aggregated by the [[OpenLLMLeaderboard|Open LLM Leaderboard]]. Description: *"common-sense inference; multiple choice."*
