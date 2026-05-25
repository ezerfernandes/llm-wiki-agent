---
title: "Leo Gao"
type: entity
tags: [person, openai, researcher, alignment]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Leo Gao

[[openai|OpenAI]] researcher. Cited in [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]] as the originator of one of the two leading hypotheses for **why language models hallucinate**.

## The internal-knowledge-mismatch hypothesis

> "The second hypothesis is that hallucination is caused by the mismatch between the model's internal knowledge and the labeler's internal knowledge. This view was first argued by Leo Gao, an OpenAI researcher. During SFT, models are trained to mimic responses written by labelers. If these responses use the knowledge that the labelers have but the model doesn't have, we're effectively teaching the model to hallucinate."

The implication: **the very act of [[SupervisedFinetuning|SFT]] trains models to make things up** — labelers write responses confidently using *their* world knowledge, and the model is trained to mimic that confidence even on questions where it doesn't have the knowledge.

[[JohnSchulman|John Schulman]] (OpenAI co-founder) extended the same view in an April 2023 UC Berkeley talk, adding the bold claim that *LLMs know if they know something*.

## Connections
- [[openai|OpenAI]] — employer.
- [[InternalKnowledgeMismatch]] — the hypothesis Gao proposed.
- [[Hallucination]] — the phenomenon the hypothesis explains.
- [[SupervisedFinetuning]] / [[BehaviorCloning]] — the training mechanic the hypothesis indicts.
- [[JohnSchulman]] — extends Gao's hypothesis.
- [[ai-engineering-ch02-foundation-models]] — primary source.
