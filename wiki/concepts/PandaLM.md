---
title: "PandaLM"
type: concept
tags: [evaluation, llm-as-judge, preference-model]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# PandaLM

**PandaLM** (Wang et al. 2023) is an open-source [[PreferenceModel|preference model]] — a specialized [[LLMAsAJudge|AI judge]] that takes `(prompt, response 1, response 2)` and outputs which response is better, *plus a rationale*. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "Figure 3-9 shows an example of how PandaLM works. It not only outputs which response is better but also explains its rationale."

## What makes PandaLM useful

- **Open-source** — can be run locally, no API costs, full transparency.
- **Pairwise-native** — designed specifically for comparative judgments, not general-purpose scoring shoehorned into pairwise.
- **Rationale output** — explanations make the judge's decisions auditable, which is essential when using it to generate [[ComparisonData|comparison data]] for [[rlhf|RLHF]] training.

## Position in the specialized-judge taxonomy

PandaLM is one of two named [[PreferenceModel|preference models]] in Ch 3, alongside [[JudgeLM]] (Zhu et al. 2023). Sits beside [[RewardModel|reward models]] like [[Cappy]] and [[ReferenceBasedJudge|reference-based judges]] like [[BLEURT]] / [[Prometheus2|Prometheus]] in the specialized-judge cluster.

## Caveats

PandaLM inherits the AI-judge biases ([[SelfBiasJudge|self-bias]], [[FirstPositionBias|first-position bias]], [[VerbosityBias|verbosity bias]]). The rationale output can also be **post-hoc rationalization** — the judge picks a winner first and then explains why, rather than reasoning to the choice — a known failure mode of explain-then-score models.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[PreferenceModel]] — parent category.
- [[JudgeLM]] — sibling preference model.
- [[RewardModel]] / [[ReferenceBasedJudge]] / [[LLMAsAJudge]] — broader judge taxonomy.
- [[ComparativeEvaluation]] — the methodology PandaLM can power.
- [[ComparisonData]] — what PandaLM can synthesize.
- [[SelfBiasJudge]] / [[FirstPositionBias]] / [[VerbosityBias]] — inherited biases.
