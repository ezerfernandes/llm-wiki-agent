---
title: "Behavior Cloning"
type: concept
tags: [post-training, sft, imitation-learning]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Behavior Cloning

The **SFT paradigm** under one name. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "You demonstrate how the model should behave, and the model clones this behavior."

Equivalent to [[SupervisedFinetuning|supervised finetuning]] on [[DemonstrationData|demonstration data]] — same operation, different framing emphasis. The term *behavior cloning* comes from **imitation learning** in robotics/RL: an agent learns a policy by mimicking demonstrations from an expert (typically a human teacher).

## What it produces

- A model that **defaults to the kind of response demonstrated** in the training set.
- For LLMs: a model that responds with answers (rather than completions, follow-up questions, or context-addition) because answers are what labelers demonstrate.

## Trade-offs

- **+** Conceptually simple; just supervised next-token-prediction loss on the response tokens.
- **+** Quality bounded by labeler quality — easy to reason about.
- **−** Cannot exceed labeler quality on the demonstrated distribution.
- **−** **Teaches the model to mimic responses requiring knowledge the labelers have but the model doesn't have** — see [[InternalKnowledgeMismatch]]. Ch 2 cites this as one of the two leading hypotheses for why language models hallucinate.

## Why preference finetuning follows

After behavior cloning, the model knows *what kind* of response to produce, but not *which version* among many plausible responses is best. [[PreferenceFinetuning|Preference finetuning]] (RLHF/DPO/RLAIF) addresses this by **learning from comparisons** rather than from positive demonstrations alone.

## Connections
- [[SupervisedFinetuning]] — same operation, formal name.
- [[DemonstrationData]] — the data format.
- [[PreferenceFinetuning]] — the stage that picks up where behavior cloning stops.
- [[InternalKnowledgeMismatch]] — the hallucination hypothesis tied to behavior cloning's mechanics.
- [[ai-engineering-ch02-foundation-models]] — primary source.
