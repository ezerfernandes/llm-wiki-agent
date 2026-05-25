---
title: "Evaluation Guideline"
type: concept
tags: [evaluation, methodology, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Evaluation Guideline

The **unambiguous rubric document** that defines what "good" means for an application. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Creating a clear evaluation guideline is the most important step of the evaluation pipeline. An ambiguous guideline leads to ambiguous scores that can be misleading. If you don't know what bad responses look like, you won't be able to catch them."

## What it must define

1. **What the application should do.**
2. **What the application should not do.** Out-of-scope inputs, refusal cases, escalation rules.
3. **What good and bad responses look like.** Concrete examples.
4. **The scoring rubric** for each criterion (see [[ScoringRubric]]).

## The LinkedIn case

LinkedIn's deployed AI surfaced *"creating an evaluation guideline"* as the **first hurdle** in one-year-deployed AI generative apps:

> "A correct response is not always a good response. For example, for their AI-powered Job Assessment application, the response 'You are a terrible fit' might be correct but not helpful, thus making it a bad response. A good response should explain the gap between this job's requirements and the candidate's background, and what the candidate can do to close this gap."

## Iteration

> "If humans find it hard to follow the rubric, you need to refine it to make it unambiguous. This process can require a lot of back and forth, but it's necessary. A clear guideline is the backbone of a reliable evaluation pipeline."

## Reusable for training

> "This guideline can also be reused later for training data annotation, as discussed in Chapter 8."

Single source of truth for both evaluation and supervised finetuning.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[EvaluationPipeline]] — parent process.
- [[ScoringRubric]] — what to build on top.
- [[LinkedIn]] — case study.
- [[OutOfScopeEvaluation]] — what the guideline must address.
