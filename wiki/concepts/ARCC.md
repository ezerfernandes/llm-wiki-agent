---
title: "ARC-C"
type: concept
tags: [benchmark, reasoning, science, mcq, evaluation]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# ARC-C

**AI2 Reasoning Challenge — Challenge set** (Clark et al. 2018). [[AllenAI|AI2]]'s grade-school-level science MCQ benchmark, restricted to the harder ("challenge") subset that simple retrieval baselines couldn't solve. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Measuring the ability to solve complex, grade school-level science questions."

## Position

One of the **original 6 benchmarks** on HuggingFace's [[OpenLLMLeaderboard|Open LLM Leaderboard]] (2023). Strongly correlated with [[mmlu|MMLU]] (0.867) and [[WinoGrande]] (0.886) per the [[BenchmarkCorrelation|Galambosi 2024 correlation table]] — all three are reasoning-focused.

Replaced/de-emphasized in HuggingFace's June 2024 leaderboard refresh as it had saturated.

## Format

[[MultipleChoiceQuestion|MCQ]] with 4 options.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[OpenLLMLeaderboard]] — leaderboard that included it.
- [[BenchmarkCorrelation]] — strongly correlated with MMLU/WinoGrande.
- [[MultipleChoiceQuestion]] — format.
- [[DomainSpecificCapability]] — science-reasoning bucket.
