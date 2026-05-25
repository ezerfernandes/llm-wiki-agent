---
title: "Per-Component Evaluation"
type: concept
tags: [evaluation, methodology, pipeline, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Per-Component Evaluation

Evaluating **each component of a pipeline independently** in addition to end-to-end. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "You should evaluate the end-to-end output and each component's intermediate output independently."

## The worked example

A resume-employer extractor:
1. Extract all text from the PDF.
2. Extract the current employer from the extracted text.

If the system fails to extract the right employer, it could be either step. *"If you don't evaluate each component independently, you don't know exactly where your system fails."*

| Component | Eval method |
|---|---|
| PDF → text | Similarity between extracted text and ground-truth text |
| Text → employer | Accuracy given the correctly extracted text |

## Why it matters

- **Debugging** — pinpoints which component fails.
- **A/B testing** — swap one component without re-evaluating the whole system.
- **[[Hallucination|Hallucination]] localization** — was it the retriever or the generator that hallucinated?
- **Cost** — fix the cheap component first.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[TurnBasedEvaluation]] / [[TaskBasedEvaluation]] — sibling evaluation granularities.
- [[EvaluationPipeline]] — parent process.
- [[rag|RAG]] — the canonical multi-component AI system needing this.
