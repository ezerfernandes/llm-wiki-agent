---
title: "Superficial Imitation"
type: concept
tags: [synthetic-data, distillation, llm-failure-mode]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Superficial Imitation

**The failure mode where a student model trained on a teacher's outputs mimics the teacher's *style* without inheriting its *capability*.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], the phenomenon was diagnosed by Gudibande et al. (2023) — *"[[FalsePromiseOfImitatingLLMs|The False Promise of Imitating Proprietary LLMs]]"*.

## The Berkeley finding

> "The imitation models are good at mimicking the style of the teacher models but might struggle with factual accuracy and generalization to tasks outside the training data."

So output **looks** like the teacher's — formatting, hedging, tone, length — but the **substance** doesn't match.

## The hallucination trap

> "Imitation can force the student model to hallucinate. Imagine if the teacher model is capable of answering complex math questions, so its responses to those questions are solutions. Training a student model on these solutions effectively teaches it to produce answers that look like solutions, even if the student model isn't capable of solving these questions."

The student learns to **emit solution-shaped outputs without being able to solve the problems** — a structural cause of [[Hallucination|hallucination]].

The same mechanism applies to human annotation: if a labeler uses knowledge the model doesn't have, they're effectively teaching the model to hallucinate (Ch 8 footnote).

## The recommendation

Gudibande et al.: **for improvement in reasoning capabilities, focus on improving the base model**, not on imitation. Imitation is good for style transfer; it's bad for capability transfer.

## Implications for distillation

This is the chapter's strongest warning against naive [[knowledgedistillation|distillation]]:

- Distillation works well when the student already has the underlying capability — it's just learning to *express* it in the teacher's style.
- Distillation fails when the student lacks the capability — it learns to fake it.

## Connections

- [[knowledgedistillation]] — the practice this limit constrains.
- [[FalsePromiseOfImitatingLLMs]] — the source paper.
- [[ModelCollapse]] — sibling limit on AI-generated data; about recursive degradation.
- [[Hallucination]] — the failure mode imitation creates.
- [[InternalKnowledgeMismatch]] — the structurally identical mechanism in human-annotated SFT (Ch 2 framing).
- [[DataSynthesis]] / [[AIPoweredDataSynthesis]] — the practice that hits this limit.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
