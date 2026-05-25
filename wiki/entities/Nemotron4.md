---
title: "Nemotron-4"
type: entity
tags: [model, nvidia, llm, synthetic-data]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Nemotron-4

[[NVIDIA|NVIDIA]]'s **340-billion-parameter** dense LLM family, notable for being one of the most synthetic-data-heavy post-training pipelines documented. The instruction-tuned variant **Nemotron-4-340B-Instruct** was trained with ~98% synthetic data during instruction + preference finetuning (NVIDIA 2024).

## What makes Nemotron-4 a Ch 8 case study

Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], Nemotron-4 demonstrates **three** non-obvious things about synthetic data:

1. **Massive synthetic-data finetuning works.** 98% synthetic post-training data produced a competitive model.
2. **Reverse-direction distillation works.** The teacher was [[Mixtral8x7B|Mixtral-8x7B-Instruct-v0.1]] (~56B params, MoE) and the student was 340B params dense — and **the student exceeded the teacher**. This contradicts the conventional "teacher > student" framing of [[knowledgedistillation|distillation]].
3. **First-position-bias mitigation in preference judging.** NVIDIA judged each pairwise comparison twice with response order swapped; kept only triples where both judgments agreed. The chapter's canonical example of [[FirstPositionBias|first-position-bias]] handling for synthetic preference data.

## The chapter's caveat

> "Comparing the parameter count of a mixture-of-experts model like Mixtral to that of a dense model like Nemotron-4 isn't fair, but the point that the teacher model (Mixtral) is smaller than the student model (Nemotron-4) still holds."

## Connections

- [[NVIDIA]] — the lab.
- [[Mixtral8x7B]] — the teacher model.
- [[knowledgedistillation]] — the operation Nemotron-4 reframes.
- [[AIPoweredDataSynthesis]] / [[DataSynthesis]] — the synthesis-heavy training regime.
- [[FirstPositionBias]] — the preference-judging bias Nemotron-4 mitigated.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
