---
title: "Episodic Memory"
type: concept
tags: [memory, long-term-memory, agents, few-shot, agentic-design-patterns]
sources: [agentic-design-patterns-ch08-memory-management]
last_updated: 2026-06-07
---

# Episodic Memory

**Episodic memory** is one of the three human-analogous types of **long-term memory** named in Chapter 8 ([[MemoryManagement|Memory Management]]) of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli). It is the agent's memory of **past events, experiences, and actions** — *"Remembering Experiences."*

## Definition

> *"Episodic Memory: Remembering Experiences: This involves recalling past events or actions. For AI agents, episodic memory is often used to remember how to accomplish a task. In practice, it's frequently implemented through few-shot example prompting, where an agent learns from past successful interaction sequences to perform tasks correctly."* — Ch 8

Where [[SemanticMemory|semantic memory]] holds *facts*, episodic memory holds *experiences* — specific past interaction sequences (trajectories) and how a task was accomplished.

## How it is implemented

The chapter's canonical implementation is **[[FewShotLearning|few-shot example prompting]]**: past **successful trajectories** are stored and, when a similar task arises, retrieved and injected into the prompt as worked examples. The agent thereby *"learns from past successful interaction sequences to perform tasks correctly"* — a form of in-context learning grounded in the agent's own history rather than a static example set. This connects directly to [[LearningAndAdaptation|learning and adaptation]] (Ch 9): storing successful strategies (and mistakes) is how an agent improves over time.

## Framework operationalization

Episodic experiences live in the **long-term** tier — retrieved by [[SemanticSearch|semantic similarity]] from an external store, then integrated back into the [[ContextWindow|context window]] as few-shot examples. In [[LangGraph]] they are saved as JSON documents in a `(namespace, key)` **store**; in [[GoogleADK|Google ADK]] via the `MemoryService`; [[VertexAiMemoryBank|Vertex AI Memory Bank]] recalls relevant past memories per user via full recall or embedding similarity.

## Why it matters

Episodic memory turns an agent's accumulated experience into **reusable competence** — it is the bridge between merely answering and actually *learning how* to perform multi-step tasks from what worked before.

## Connections
- [[MemoryManagement]] — the parent agentic design pattern (Ch 8).
- [[LongTermMemory]] — the tier episodic memory belongs to.
- [[SemanticMemory]] / [[ProceduralMemory]] — the sibling long-term-memory types.
- [[FewShotLearning]] / [[InContextLearning]] — the typical implementation mechanism.
- [[LearningAndAdaptation]] — Ch 9; episodic memory of successes/failures is its substrate.
- [[VectorDatabase]] / [[SemanticSearch]] / [[rag|RAG]] — storage + retrieval substrate.
- [[GoogleADK]] / [[LangGraph]] / [[VertexAiMemoryBank]] — framework implementations.
- [[Mem0]] — peer external long-term-memory layer.
- [[AgenticDesignPatterns]] — the book; [[AntonioGulli]] author.
- [[agentic-design-patterns-ch08-memory-management]] — source page.
