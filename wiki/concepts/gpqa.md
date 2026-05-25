---
title: "GPQA"
type: concept
tags: [benchmark, reasoning, graduate-level, evaluation]
sources: [2605.12357-delta-mem, ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# GPQA

**Graduate-level Google-Proof Q&A** benchmark (Rein et al. 2023). A graduate-level [[MultipleChoiceQuestion|MCQ]] benchmark intentionally designed so that experts can't easily Google the answer. Sample subjects: physics, chemistry, biology — at PhD-prelim difficulty.

## Position

Added to HuggingFace's [[OpenLLMLeaderboard|Open LLM Leaderboard]] in the **June 2024 refresh** alongside [[MATHLevel5]], [[MMLUPro]], [[MuSR]], [[BigBenchHard]], and [[IFEval]]. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "GPQA (Rein et al., 2023): a graduate-level Q&A benchmark. It's both really cool and intimidating to see that in just a couple of years, benchmarks had to change from grade-level questions to graduate-level questions."

Used in [[2605.12357-delta-mem]] as **GPQA-Diamond** (a harder subset) for capability-preservation checks alongside [[ifeval|IFEval]].

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source for Ch 4 framing.
- [[2605.12357-delta-mem]] — uses GPQA-Diamond.
- [[OpenLLMLeaderboard]] — leaderboard adoption.
- [[BenchmarkSaturation]] — why grade-level → graduate-level was needed.
- [[mmlu|MMLU]] / [[MMLUPro]] / [[MuSR]] / [[BigBenchHard]] / [[MATHLevel5]] / [[IFEval]] — June 2024 refresh siblings.
- [[MultipleChoiceQuestion]] — format.
