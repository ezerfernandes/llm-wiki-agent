---
title: "Procedural Memory"
type: concept
tags: [memory, long-term-memory, agents, system-prompt, reflection, agentic-design-patterns]
sources: [agentic-design-patterns-ch08-memory-management]
last_updated: 2026-06-07
---

# Procedural Memory

**Procedural memory** is one of the three human-analogous types of **long-term memory** named in Chapter 8 ([[MemoryManagement|Memory Management]]) of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli). It is the agent's memory of **how to perform tasks — rules and behaviors** — *"Remembering Rules."*

## Definition

> *"Procedural Memory: Remembering Rules: This is the memory of how to perform tasks — the agent's core instructions and behaviors, often contained in its system prompt. It's common for agents to modify their own prompts to adapt and improve. An effective technique is 'Reflection,' where an agent is prompted with its current instructions and recent interactions, then asked to refine its own instructions."* — Ch 8

Where [[SemanticMemory|semantic memory]] holds *facts* and [[EpisodicMemory|episodic memory]] holds *experiences*, procedural memory holds the agent's **operating rules** — most concretely, **its system prompt / core instructions**.

## Self-improvement via Reflection

The chapter's distinguishing claim is that procedural memory is **mutable and self-refining**: agents commonly *modify their own prompts to adapt and improve*. The named technique is **[[Reflection|Reflection]]** — the agent is prompted with (1) its current instructions and (2) recent interactions, and asked to **rewrite its own instructions**. The chapter's pseudo-code stores procedural memory in a [[LangGraph]] `BaseStore`:

- An `update_instructions(state, store)` node fetches the current instructions (`store.search(namespace)`), prompts the LLM to reflect on the conversation and emit `new_instructions`, then writes them back via `store.put(("agent_instructions",), "agent_a", {"instructions": new_instructions})`.
- A `call_model(state, store)` node retrieves the latest instructions (`store.get(namespace, key="agent_a")`) and uses them to format the prompt for the next response.

This closes a [[FeedbackLoop|feedback loop]] in which the agent's behavior is itself a learned, updatable artifact — a form of [[LearningAndAdaptation|learning and adaptation]].

## Framework operationalization

Procedural memory lives in the **long-term** tier (an external [[VectorDatabase|store]] / database), updated and retrieved per session. [[LangGraph]] persists it as namespaced JSON in a store; [[GoogleADK|Google ADK]] exposes a searchable `MemoryService`; [[VertexAiMemoryBank|Vertex AI Memory Bank]] consolidates persisted memories per user.

## Why it matters

Procedural memory is what lets an agent **change how it operates**, not just what it knows — refining its own instructions from experience is the mechanism by which an agent improves its behavior over time.

## Connections
- [[MemoryManagement]] — the parent agentic design pattern (Ch 8).
- [[LongTermMemory]] — the tier procedural memory belongs to.
- [[SemanticMemory]] / [[EpisodicMemory]] — the sibling long-term-memory types.
- [[Reflection]] — the technique by which an agent rewrites its own instructions.
- [[FeedbackLoop]] / [[LearningAndAdaptation]] — self-improvement framing (Ch 9).
- [[LangGraph]] — `BaseStore` `update_instructions` / `call_model` pseudo-code.
- [[GoogleADK]] / [[VertexAiMemoryBank]] — framework implementations.
- [[VectorDatabase]] / [[SemanticSearch]] — storage + retrieval substrate.
- [[AgenticDesignPatterns]] — the book; [[AntonioGulli]] author.
- [[agentic-design-patterns-ch08-memory-management]] — source page.
