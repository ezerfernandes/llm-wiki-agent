---
title: "JudgeLM"
type: concept
tags: [evaluation, llm-as-judge, preference-model]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# JudgeLM

**JudgeLM** (Zhu et al. 2023) is an open-source [[PreferenceModel|preference model]] — a specialized [[LLMAsAJudge|AI judge]] for comparative evaluation. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]], JudgeLM is one of two named exemplars of preference models in the *"specialized judges"* section, alongside [[PandaLM]] (Wang et al. 2023).

## Position

JudgeLM and PandaLM are siblings: both are pairwise preference judges trained for the (prompt, response_1, response_2) → winner task. They differ in training data, base model, and output format details, but share the same role in the specialized-judge taxonomy.

## Why preference models matter for AI evaluation

Ch 3's broader argument: preference data is **expensive to collect** ([[LMSYS]]: 3-5 minutes per comparison; [[ThomasScialom]]: ≈$3.50 per comparison). A reliable preference model lets you synthesize comparison data on demand — accelerating [[rlhf|RLHF]] / [[DPO|DPO]] data pipelines and enabling auto-graded leaderboards like [[AlpacaEval]].

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[PreferenceModel]] — parent category.
- [[PandaLM]] — sibling preference model.
- [[RewardModel]] / [[ReferenceBasedJudge]] / [[LLMAsAJudge]] — broader judge taxonomy.
- [[ComparativeEvaluation]] — the methodology.
- [[ComparisonData]] — what JudgeLM can synthesize.
