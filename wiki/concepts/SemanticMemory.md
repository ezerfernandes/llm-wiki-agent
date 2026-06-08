---
title: "Semantic Memory"
type: concept
tags: [memory, long-term-memory, agents, agentic-design-patterns]
sources: [agentic-design-patterns-ch08-memory-management]
last_updated: 2026-06-07
---

# Semantic Memory

**Semantic memory** is one of the three human-analogous types of **long-term memory** named in Chapter 8 ([[MemoryManagement|Memory Management]]) of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli). It is the agent's memory of **facts and concepts** — *"Remembering Facts."*

## Definition

> *"Semantic Memory: Remembering Facts: This involves retaining specific facts and concepts, such as user preferences or domain knowledge. It is used to ground an agent's responses, leading to more personalized and relevant interactions."* — Ch 8

Semantic memory holds the timeless, context-independent knowledge an agent draws on — user preferences, profile attributes, and domain facts — as distinct from the *experiences* held in [[EpisodicMemory|episodic memory]] or the *rules* held in [[ProceduralMemory|procedural memory]].

## How it is managed

The chapter names two concrete storage shapes for semantic memory:

- **A continuously-updated user "profile"** — a single JSON document that accumulates and revises what the agent knows about a user.
- **A "collection" of individual factual documents** — many discrete fact records, retrieved by [[SemanticSearch|semantic similarity]] when relevant.

Both shapes live in the **long-term** tier — an external [[VectorDatabase|vector store]] / database, not the [[ContextWindow|context window]] — and relevant facts are retrieved and **integrated back into the short-term context** at query time (the same retrieval substrate as [[rag|RAG]]).

## Framework operationalization

In [[LangGraph]], semantic facts are saved as JSON documents in a **store**, organized under a `(namespace, key)` and retrieved by `store.put` / `store.get` / `store.search` (vector similarity). [[VertexAiMemoryBank|Vertex AI Memory Bank]] populates semantic memory automatically — [[gemini|Gemini]] asynchronously extracts key facts and user preferences from conversation histories, scoped by user ID. In [[GoogleADK|Google ADK]] the searchable long-term store is the `MemoryService`.

## Why it matters

Semantic memory is what makes an agent **personalized and grounded** rather than generic: recalling that a user prefers short answers, speaks a particular language, or works in a particular domain lets the agent tailor every response. It is the factual backbone of the [[MemoryManagement|memory management]] pattern.

## Connections
- [[MemoryManagement]] — the parent agentic design pattern (Ch 8).
- [[LongTermMemory]] — the tier semantic memory belongs to.
- [[EpisodicMemory]] / [[ProceduralMemory]] — the sibling long-term-memory types.
- [[VectorDatabase]] / [[SemanticSearch]] / [[rag|RAG]] — storage + retrieval substrate.
- [[GoogleADK]] / [[LangGraph]] / [[VertexAiMemoryBank]] — framework implementations.
- [[gemini|Gemini]] — extracts facts/preferences in Vertex AI Memory Bank.
- [[Mem0]] — peer external long-term-memory layer that stores extracted facts.
- [[AgenticDesignPatterns]] — the book; [[AntonioGulli]] author.
- [[agentic-design-patterns-ch08-memory-management]] — source page.
