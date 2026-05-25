---
title: "Code Readability"
type: concept
tags: [evaluation, code-generation, qualitative]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Code Readability

The **qualitative dimension** of generated code that resists exact metrics. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "If the generated code runs but nobody can understand it, it will be challenging to maintain the code or incorporate it into a system. There's no obvious way to evaluate code readability exactly, so you might have to rely on subjective evaluation, such as using AI judges."

## Why it matters beyond functional correctness

[[FunctionalCorrectness|Functional correctness]] tells you the code works. Readability tells you whether your team can maintain it. A correct-but-unreadable solution is a long-term liability.

## How to evaluate it

- **[[LLMAsAJudge|AI judges]]** — prompt a model to score readability on a rubric (variable naming, structure, comments, idiomatic style).
- **Static heuristics** — line length, complexity metrics, comment ratio (proxies, not direct measures).
- **Human review** — most reliable, least scalable.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[FunctionalCorrectness]] / [[ExactEvaluation]] — the "code works" dimension.
- [[BIRDSQLEfficiency]] — sibling beyond-functional-correctness eval dimension for SQL.
- [[DomainSpecificCapability]] — parent eval bucket.
- [[LLMAsAJudge]] — the dominant evaluator for this dimension.
