---
title: "Close-Ended Task"
type: concept
tags: [evaluation, classification, multiple-choice]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Close-Ended Task

A task whose outputs are picked from a **fixed option set** — classification or [[MultipleChoiceQuestion|multiple-choice]] questions. The opposite of *open-ended* tasks where outputs are free-form text.

## Why close-ended dominates benchmarks

Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Close-ended outputs are easier to verify and reproduce. … In April 2024, 75% of the tasks in Eleuther's lm-evaluation-harness are multiple-choice."

[[AGIEval]]'s authors *"explained that they excluded open-ended tasks on purpose to avoid inconsistent assessment."*

## Why FM use cases are often close-ended

Even though FMs are open-ended generators, many production use cases are close-ended:
- Intent classification
- Sentiment analysis
- Next-action prediction
- Content moderation

> "It's much easier to evaluate classification tasks than open-ended tasks."

This is partly why these use cases dominate enterprise adoption (per [[EvaluationDrivenDevelopment|evaluation-driven development]]).

## Metrics

- **Accuracy** — fraction correct.
- **Point system** for harder questions or multi-correct options.
- **Classification metrics** — F1, precision, recall (when option set is shared across questions, e.g. POSITIVE/NEGATIVE/NEUTRAL).
- **Random baseline** — for 4-option MCQ, random = 25%; above that suggests model is doing better than chance (typically).

## The fragility caveat

[[MultipleChoiceQuestion|MCQ]] outputs are surprisingly prompt-fragile. Alzahrani et al. 2024: adding an extra space or appending *"Choices:"* can cause the model to flip its answer.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[MultipleChoiceQuestion]] — the dominant close-ended format.
- [[DomainSpecificCapability]] — where close-ended evaluation lives.
- [[ExactEvaluation]] / [[ExactMatch]] — parent evaluation family.
- [[mmlu|MMLU]] / [[AGIEval]] / [[ARCC]] — canonical MCQ benchmarks.
