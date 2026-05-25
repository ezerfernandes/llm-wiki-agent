---
title: "The False Promise of Imitating Proprietary LLMs"
type: concept
tags: [paper, distillation, llm-failure-mode]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# The False Promise of Imitating Proprietary LLMs

**Gudibande et al. (2023, UC Berkeley) — the paper that diagnosed [[SuperficialImitation|superficial imitation]] in [[knowledgedistillation|distillation]].** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], this is the foundational critique of "just distill GPT-4" as a shortcut to a strong open model.

## The core claim

> "The perceived performance achieved by mimicking might be superficial. This research shows that the imitation models are good at mimicking the style of the teacher models but might struggle with factual accuracy and generalization to tasks outside the training data."

## The hallucination trap

> "Imitation can force the student model to hallucinate. Imagine if the teacher model is capable of answering complex math questions, so its responses to those questions are solutions. Training a student model on these solutions effectively teaches it to produce answers that look like solutions, even if the student model isn't capable of solving these questions."

So distillation transfers **shape** but not **substance**. When the shape demands substance the student doesn't have, the student fabricates.

## The recommendation

> "For improvement in reasoning capabilities, we need to focus on improving the quality of the base models."

This positions distillation as a **style-transfer tool**, not a capability-acquisition tool — a sharp reframe of how the operation was being marketed in 2023.

## Relationship to [[InternalKnowledgeMismatch]]

The mechanism is structurally identical to Schulman's [[InternalKnowledgeMismatch|internal-knowledge-mismatch]] hypothesis from Ch 2: if the labeler (human or teacher model) uses knowledge the student doesn't have, the student is taught to hallucinate.

## Where Ch 8 places this paper

Among the **four limits of AI-generated data** alongside quality control, [[ModelCollapse|model collapse]], and obscure [[DataLineage|data lineage]].

## Connections

- [[SuperficialImitation]] — the named phenomenon.
- [[knowledgedistillation]] — the practice it critiques.
- [[Hallucination]] — the failure mode it diagnoses.
- [[InternalKnowledgeMismatch]] — the structurally identical human-annotator failure mode.
- [[ModelCollapse]] — sibling AI-data-generation limit.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
