---
title: "Factuality"
type: concept
tags: [evaluation, factuality, hallucination]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Factuality

The property of generated outputs being **true / consistent with reality or with a given context**. Within evaluation, the operationalization is **[[FactualConsistency|factual consistency]]** — see that page for the methodological deep dive ([[LocalFactualConsistency|local]] vs [[GlobalFactualConsistency|global]] settings; [[SelfCheckGPT]], [[SAFEEvaluator|SAFE]], [[TextualEntailment|NLI]], [[TruthfulQA]] / [[GPTJudge]] benchmarks).

[[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] treats factuality as a sub-area of [[Safety|safety]] technically — *"factual inconsistency can cause harm too, so it's technically under safety"* — but gives it its own section due to scope.

## Why it dominates GenAI evaluation

Hallucinations are desirable for creative tasks but catastrophic for factual tasks. Customer support, legal advice, medical Q&A, search, and RAG all depend on factuality.

## Connections

- [[FactualConsistency]] — the operational concept (read this for detail).
- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Hallucination]] — the failure mode factuality metrics detect.
- [[Safety]] — parent category (in Ch 4's taxonomy).
- [[TruthfulQA]] / [[GPTJudge]] / [[SAFEEvaluator]] / [[SelfCheckGPT]] / [[TextualEntailment]] / [[DeBERTaV3FactConsistency]] — the evaluation toolkit.
