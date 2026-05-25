---
title: "WinoGrande"
type: concept
tags: [benchmark, reasoning, pronoun-resolution, mcq, evaluation]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# WinoGrande

Sakaguchi et al. 2019 — a **pronoun-resolution [[MultipleChoiceQuestion|MCQ]] benchmark** requiring commonsense reasoning. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Measuring the ability to solve challenging pronoun resolution problems that are designed to be difficult for language models, requiring sophisticated commonsense reasoning."

Based on the Winograd Schema Challenge (Levesque et al. 2012), scaled up.

## Position

One of the **original 6 benchmarks** on HuggingFace's [[OpenLLMLeaderboard|Open LLM Leaderboard]] (2023). Strongly correlated with [[mmlu|MMLU]] (0.901) and [[ARCC]] (0.886) per the [[BenchmarkCorrelation|Galambosi 2024 correlation table]] — reasoning-tied.

Removed in HuggingFace's June 2024 leaderboard refresh.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[OpenLLMLeaderboard]] — leaderboard that included it.
- [[BenchmarkCorrelation]] — strongly correlated with MMLU / ARC-C.
- [[MultipleChoiceQuestion]] — format.
