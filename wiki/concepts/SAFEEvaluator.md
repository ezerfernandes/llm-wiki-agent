---
title: "SAFE — Search-Augmented Factuality Evaluator"
type: concept
tags: [evaluation, factuality, hallucination, retrieval, deepmind]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# SAFE — Search-Augmented Factuality Evaluator

**Knowledge-augmented [[FactualConsistency|factual-consistency]] verification** introduced by [[googledeepmind|Google DeepMind]] (Wei et al. 2024, *"Long-Form Factuality in Large Language Models"*). One of three advanced factual-consistency methods discussed in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]].

## The four-step pipeline

1. **Decompose** the response into individual statements via an AI model.
2. **Revise** each statement to be self-contained. *"The 'it' in the statement 'It opened in the 20th century' should be changed to the original subject."*
3. **Generate fact-checking queries** for each statement → send to a Google Search API.
4. **Verify** consistency between the statement and the search results via AI.

## Position

The **global** counterpart to [[SelfCheckGPT|SelfCheckGPT's]] reference-free self-disagreement check — SAFE uses *external* search evidence as the ground truth rather than relying on internal self-consistency. Particularly suited for [[GlobalFactualConsistency|global factual consistency]] where no context is provided.

## Trade-offs

- **External-knowledge access.** Requires a search API.
- **Latency.** Each fact-check needs at least one search round-trip.
- **Per-statement granularity.** Useful for long-form outputs where some claims are right and some wrong.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[googledeepmind|Google DeepMind]] — authoring organization.
- [[FactualConsistency]] / [[GlobalFactualConsistency]] — what it measures.
- [[SelfCheckGPT]] — sibling advanced method (no external search).
- [[rag|RAG]] — conceptually adjacent (both use retrieval as a grounding signal).
