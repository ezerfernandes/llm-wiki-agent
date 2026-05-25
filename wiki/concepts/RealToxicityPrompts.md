---
title: "RealToxicityPrompts"
type: concept
tags: [benchmark, safety, toxicity, evaluation]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# RealToxicityPrompts

A **safety benchmark** of 100,000 naturally-occurring prompts that elicit toxic outputs from language models (Gehman et al. 2020). One of the two canonical toxicity benchmarks named in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] (alongside [[BOLD]]).

## What's in it

> "RealToxicityPrompts contains 100,000 naturally occurring prompts that are likely to get models to generate toxic outputs."

Sample prompts from Ch 4 (truncated to keep the page family-friendly):

- *"So, I'm starting to think she's full …"*
- *"I'm 99 percent sure it was someone being an …"*

The benchmark scores models on the *toxicity of their continuations* — typically using a toxicity classifier like [[PerspectiveAPI]] as the scorer.

## Position

[[BOLD]] (Dhamala et al. 2021) is the sibling — focuses on bias in open-ended generation rather than toxicity per se.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Safety]] — what it measures.
- [[BOLD]] — sibling toxicity/bias benchmark.
- [[PerspectiveAPI]] — typical scorer used to grade continuations.
- [[GenerationCapability]] — parent eval bucket.
