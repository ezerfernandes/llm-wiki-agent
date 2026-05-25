---
title: "Short-Term Memory (LLM)"
type: concept
tags: [memory, llm, agents, context]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Short-Term Memory

In [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]'s three-tier memory model, **short-term memory** is the model's **context window** — the working memory that holds information relevant to the current task.

## Defining properties

> *"A model's context can be considered its short-term memory as it doesn't persist across tasks (queries). It's fast to access, but its capacity is limited. Therefore, it's often used to store information that is most important for the current task."*

| Property | Short-term memory |
|---|---|
| Substrate | The context window |
| Persistence | Per-query (does not persist across tasks) |
| Access speed | Fast |
| Capacity | Limited by context length |
| Cost to add | Input-token cost per use |

## Position in the three-tier model

| Tier | Substrate | Persistence |
|---|---|---|
| [[InternalKnowledgeMemory|Internal knowledge]] | Model weights | Permanent (until retraining) |
| **Short-term** | Context window | Per-query |
| [[LongTermMemory]] | External stores (RAG-retrievable) | Cross-session |

## Management strategy: capacity split

> *"A model's short-term capacity is, therefore, determined by how much of the context should be allocated for information retrieved from long-term memory. For example, if 30% of the context is reserved, then the model can use at most 70% of the context limit for short-term memory. When this threshold is reached, the overflow can be moved to long-term memory."*

This is the **context-budget design decision** every long-conversation agent must make: short-term holds the immediate conversation, long-term holds the persistent knowledge, and the partition between them is a hyperparameter.

## Connections

- [[ContextWindow]] / [[ContextLength]] — the substrate of short-term memory.
- [[LongTermMemory]] / [[InternalKnowledgeMemory]] — sibling memory tiers.
- [[FIFOMemory]] / [[SummarizationMemory]] / [[ReflectionMemory]] — management strategies.
- [[Agent]] — the agent system that benefits.
- [[rag]] — long-term memory is RAG-retrievable.
- [[ai-engineering-ch06-rag-agents]] — primary source.
