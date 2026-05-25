---
title: "MMLU"
type: concept
tags: [benchmark, mcq, knowledge, reasoning, evaluation]
sources: [ai-engineering-ch03-evaluation-methodology, ai-engineering-ch04-evaluate-ai-systems, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# MMLU

**Massive Multitask Language Understanding** (Hendrycks et al. 2020, [[stanforduniversity|UC Berkeley]] — actually a Berkeley-led collaboration). A [[MultipleChoiceQuestion|MCQ]] benchmark covering **57 subjects** including elementary mathematics, US history, computer science, and law. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Measuring knowledge and reasoning capabilities in 57 subjects, including elementary mathematics, US history, computer science, and law."

## Significance in the FM era

MMLU has been the **single most influential FM benchmark**:

- One of two benchmarks (with [[GSM8K]]) shared between HuggingFace's [[OpenLLMLeaderboard|Open LLM Leaderboard]] and [[stanforduniversity|Stanford]]'s [[HELMLite]].
- One of the **original 6 benchmarks** on HuggingFace's Open LLM Leaderboard.
- The benchmark that Figure 4-7 uses to show the open-vs-proprietary performance gap closing.
- The benchmark that most "model X is the new state-of-the-art" announcements were measured against from 2021-2024.

## Saturated → MMLU-Pro

Per [[BenchmarkSaturation]], MMLU saturated by mid-2024 — frontier models cluster at the ceiling. **HuggingFace replaced it with [[MMLUPro]] in the June 2024 leaderboard refresh.**

## Correlation profile

Per [[BenchmarkCorrelation|Galambosi 2024]]: MMLU correlates strongly with [[ARCC]] (0.867), [[WinoGrande]] (0.901), [[GSM8K]] (0.794). It's the central node of the "reasoning cluster." TruthfulQA is only moderately correlated (~0.55).

## From [[ai-engineering-ch03-evaluation-methodology|AI Engineering Ch 3]]

Ch 3 names MMLU as the canonical example of a benchmark that **saturated and was replaced** ([[mmlu]] → [[MMLUPro]]). Part of the [[BenchmarkSaturation]] thread that motivates Ch 3's overview of evaluation difficulty.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] / [[ai-engineering-ch03-evaluation-methodology]] — primary sources.
- [[MMLUPro]] — 2024 successor.
- [[OpenLLMLeaderboard]] / [[HELMLite]] — leaderboards that use it.
- [[BenchmarkCorrelation]] — correlation analysis showing reasoning-cluster centrality.
- [[BenchmarkSaturation]] — why it was replaced.
- [[MultipleChoiceQuestion]] — format.
- [[DomainSpecificCapability]] — eval bucket.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* names MMLU (Hendrycks et al. 2020) in **Table 12-1** as one of six canonical public benchmarks for evaluating generative LLMs (alongside [[GLUE]], [[TruthfulQA]], [[GSM8K]], [[HellaSwag]], [[HumanEval]]). The chapter's description: *"57 tasks: classification, QA, sentiment."* MMLU is also one of the six aggregated by the [[OpenLLMLeaderboard|Open LLM Leaderboard]] in the chapter's framing.

Ch 12's caveat on public benchmarks: *"overfitting risk; broad coverage that misses specific use cases; some are GPU-heavy (hours to compute)"* — consistent with the wiki's broader [[BenchmarkSaturation]] thread that explains why MMLU was replaced by MMLU-Pro in 2024.
