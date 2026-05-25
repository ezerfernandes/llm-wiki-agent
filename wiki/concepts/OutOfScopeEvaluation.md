---
title: "Out-of-Scope Evaluation"
type: concept
tags: [evaluation, methodology, ai-engineering, safety]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Out-of-Scope Evaluation

An **evaluation set of inputs your application isn't supposed to engage with**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "You might want an out-of-scope evaluation set, inputs your application isn't supposed to engage with, to make sure that your application handles them appropriately."

## Why it matters

- **Safety** — refuse to give legal/medical/financial advice if your app isn't supposed to.
- **Brand safety** — customer support chatbot shouldn't opine on upcoming elections.
- **Cost** — refuse calls that don't fit your business model.
- **Confidence boundary** — explicit handling of "I don't know."

## Designing the set

> "When creating the evaluation guideline, it's important to define not only what the application should do, but also what it shouldn't do. For example, if you build a customer support chatbot, should this chatbot answer questions unrelated to your product, such as about an upcoming election? If not, you need to define what inputs are out of the scope of your application, how to detect them, and how your application should respond to them."

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[EvaluationGuideline]] — parent document.
- [[EvaluationPipeline]] / [[DataSlicing]] — where this set lives.
- [[Guardrail]] / [[Safety]] — adjacent concerns.
