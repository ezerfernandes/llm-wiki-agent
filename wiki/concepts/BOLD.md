---
title: "BOLD"
type: concept
tags: [benchmark, safety, bias, evaluation]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# BOLD

**Bias in Open-ended Language generation Dataset** (Dhamala et al. 2021). One of the two canonical [[Safety|safety]] benchmarks named in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] (alongside [[RealToxicityPrompts]]).

Measures bias in open-ended generation across demographic axes (profession, gender, race, religion, political ideology). Generates continuations to neutral or demographically-marked prompts and scores them for sentiment and bias.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Safety]] — what it measures.
- [[RealToxicityPrompts]] — sibling.
- [[GenerationCapability]] — parent eval bucket.
