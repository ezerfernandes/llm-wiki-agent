---
title: "Scoring Rubric"
type: concept
tags: [evaluation, methodology, scoring, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Scoring Rubric

The **per-criterion scoring schema** with worked examples. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "For each criterion, choose a scoring system: would it be binary (0 and 1), from 1 to 5, between 0 and 1, or something else? … Which scoring system to use depends on your data and your needs."

## Common scoring systems

| System | Example use |
|---|---|
| **Binary (0/1)** | factual consistency (yes/no) |
| **Ternary (-1/0/1)** | contradiction / neutral / entailment ([[TextualEntailment]]) |
| **1–5 discrete** | typical AI-judge scale (also [[MLflow]] default) |
| **0–1 continuous** | confidence-like; common in [[LLMAsAJudge]] |
| **Point system** | MCQ where harder questions are worth more |

Ch 3's [[LLMAsAJudge]] section warned: *"Language models are generally better with text than with numbers."* Classification > numerical; discrete > continuous; wider discrete ranges → worse. Keep this in mind when designing.

## Build the rubric with examples

> "On this scoring system, create a rubric with examples. What does a response with a score of 1 look like and why does it deserve a 1? Validate your rubric with humans: yourself, coworkers, friends, etc."

Validation iteration: if humans struggle to apply your rubric, it's too ambiguous — refine.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[EvaluationGuideline]] — parent document.
- [[EvaluationPipeline]] — parent process.
- [[LLMAsAJudge]] — the dominant scoring agent.
- [[TextualEntailment]] — example use of a ternary scoring system.
- [[EvaluationCriteriaAmbiguity]] — what rubrics defend against.
