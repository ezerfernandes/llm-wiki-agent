---
title: "Reference-Based Judge"
type: concept
tags: [evaluation, llm-as-judge, specialized-judge]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Reference-Based Judge

A **reference-based judge** is a specialized [[LLMAsAJudge|AI judge]] that *"evaluates the generated response with respect to one or more reference responses"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]). Output is either a **similarity score** or a **quality score** relative to the references.

## Two named exemplars (Ch 3)

| Judge | Input | Output |
|---|---|---|
| [[BLEURT]] (Sellam et al. 2020) | (candidate, reference) | Similarity score ≈ [-2.5, 1.0] |
| [[Prometheus2\|Prometheus]] (Kim et al. 2023) | (prompt, generated, reference, rubric) | Quality 1-5 (reference = 5) |

## Position in the specialized-judge taxonomy

Ch 3 enumerates **three kinds of specialized judges**:
1. **[[RewardModel|Reward models]]** — score (prompt, response). Example: [[Cappy]].
2. **Reference-based judges** ← *this page* — score (generated, references). Examples: [[BLEURT]], [[Prometheus2|Prometheus]].
3. **[[PreferenceModel|Preference models]]** — score (prompt, response1, response2). Examples: [[PandaLM]], [[JudgeLM]].

## Score-range warning

Ch 3 footnote on BLEURT: *"The BLEURT score range is confusing. It's approximately between -2.5 and 1.0. This highlights the challenge of criteria ambiguity with AI judges: the score range can be arbitrary."* — a concrete instance of [[EvaluationCriteriaAmbiguity]].

## Why specialized > general for some tasks

> "A small, specialized judge can be more reliable than larger, general-purpose judges for specific judgments."

A specialized reference-based judge is trained on a specific scoring system and can be **smaller and cheaper** than a frontier LM while being **more reliable** on the specific judgment it was trained for.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[BLEURT]] / [[Prometheus2]] — two named exemplars.
- [[RewardModel]] / [[PreferenceModel]] — sibling specialized-judge types.
- [[LLMAsAJudge]] — parent paradigm.
- [[ReferenceData]] / [[ReferenceBasedMetric]] — the data substrate.
- [[EvaluationCriteriaAmbiguity]] — the score-range failure mode.
