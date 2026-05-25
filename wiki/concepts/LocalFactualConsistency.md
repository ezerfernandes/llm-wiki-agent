---
title: "Local Factual Consistency"
type: concept
tags: [evaluation, factuality, hallucination, rag]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Local Factual Consistency

One of two settings for [[FactualConsistency|factual consistency]] per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]. **The output is evaluated against a given context.** *"The output is considered factually consistent if it's supported by the given context."*

## Use cases

- **Summarization** — summary should be consistent with the original document.
- **Customer-support chatbots** — responses should be consistent with company policies/docs.
- **Business analysis** — extracted insights should be consistent with the underlying data.
- **[[rag|RAG]] systems** — generated answers should be consistent with retrieved context. Local factual consistency *is* the standard RAG evaluation metric.

## Why it's the easier setting

Verifying against an explicit context is much easier than verifying against open knowledge — the ground truth is right there. This makes [[TextualEntailment|textual entailment]] / NLI classifiers a viable cheap evaluator: feed (context, output) pairs into a model like [[DeBERTaV3FactConsistency|DeBERTa-v3-base-mnli-fever-anli]] and read the entailment/contradiction/neutral output.

## Contrast with global

[[GlobalFactualConsistency|Global factual consistency]] requires the evaluator to *first* identify reliable facts before checking the output — local skips that step.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[FactualConsistency]] — parent concept.
- [[GlobalFactualConsistency]] — sibling setting.
- [[rag|RAG]] — the dominant local-factual-consistency-evaluated system class.
- [[TextualEntailment]] / [[DeBERTaV3FactConsistency]] — cheap evaluator for this setting.
