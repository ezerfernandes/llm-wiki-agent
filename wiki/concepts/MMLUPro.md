---
title: "MMLU-Pro"
type: concept
tags: [benchmark, evaluation, mmlu, mcq]
sources: [ai-engineering-ch03-evaluation-methodology, ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# MMLU-Pro

The **2024 successor to [[mmlu|MMLU]]** (Wang et al. 2024). Created because most leading foundation models had saturated MMLU. Adds harder questions, more distractors, and broader subject coverage.

## Position

Added to HuggingFace's [[OpenLLMLeaderboard|Open LLM Leaderboard]] in the **June 2024 refresh**, directly replacing [[mmlu|MMLU]]. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "MMLU was replaced by MMLU-PRO (Wang et al., 2024)."

## The broader pattern

MMLU-Pro is part of the **benchmark-arms-race** pattern Huyen documents in Chs 3-4:
- [[GLUE]] (2018) → [[SuperGLUE]] (2019)
- [[NaturalInstructions]] (2021) → Super-NaturalInstructions (2022)
- [[mmlu|MMLU]] (2020) → **MMLU-Pro** (2024)
- [[GSM8K]] → [[MATHLevel5]] (June 2024)
- Grade-level Q&A → [[GPQA|graduate-level Q&A]]

Each successor is harder than the last. [[BenchmarkSaturation|Benchmark saturation]] forces these refreshes.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — Ch 4 source.
- [[ai-engineering-ch03-evaluation-methodology]] — Ch 3 introduces the saturation context.
- [[mmlu|MMLU]] — predecessor.
- [[OpenLLMLeaderboard]] — leaderboard adoption.
- [[BenchmarkSaturation]] — why this exists.
- [[MultipleChoiceQuestion]] — format.
