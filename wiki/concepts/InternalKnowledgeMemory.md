---
title: "Internal Knowledge Memory"
type: concept
tags: [memory, llm, weights]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Internal Knowledge Memory

In [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]'s three-tier memory model, **internal knowledge** is the knowledge **stored in the model's weights** — the substrate of everything the model knows without external help. Huyen makes the load-bearing observation that **the model itself is a memory mechanism**:

> *"The model itself is a memory mechanism, as it retains the knowledge from the data it was trained on. This knowledge is its internal knowledge. A model's internal knowledge doesn't change unless the model itself is updated. The model can access this knowledge in all queries."*

## Defining properties

| Property | Internal knowledge |
|---|---|
| Substrate | Model weights |
| Persistence | Permanent (until retraining / [[FineTuning|finetuning]]) |
| Access speed | Immediate (no retrieval) |
| Capacity | Bounded by parameter count |
| Mutability | Requires training / finetuning to change |

## Human analogy

> *"How to breathe is your internal knowledge. You typically don't forget how to breathe unless you're in serious trouble."*

Information essential for *all* tasks should be incorporated into internal knowledge via training or finetuning. Information rarely needed should reside in [[LongTermMemory|long-term memory]]. Information immediately context-specific belongs in [[ShortTermMemory|short-term memory]].

## Position in the wiki

The wiki already records the *root cause* of why internal knowledge is unreliable — [[InternalKnowledgeMismatch]] (Schulman 2023) and [[SelfDelusion]] (Ortega et al., DeepMind 2021) — under [[Hallucination]]. Internal-knowledge memory is the **mechanism** these phenomena fail in.

## Connections

- [[ShortTermMemory]] / [[LongTermMemory]] — sibling memory tiers.
- [[FineTuning]] — the operation that mutates internal knowledge.
- [[InternalKnowledgeMismatch]] — the failure mode.
- [[Hallucination]] — the consequence of internal-knowledge failures.
- [[FoundationModel]] / [[ParametricMemory]] — adjacent abstractions.
- [[Agent]] — the system internal knowledge powers.
- [[ai-engineering-ch06-rag-agents]] — primary source.
