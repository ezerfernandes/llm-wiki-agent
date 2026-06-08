---
title: "Vertex AI Memory Bank"
type: concept
tags: [memory, long-term-memory, agents, google-cloud, vertex-ai, managed-service, agentic-design-patterns]
sources: [agentic-design-patterns-ch08-memory-management]
last_updated: 2026-06-07
---

# Vertex AI Memory Bank

**Vertex AI Memory Bank** is a **managed long-term-memory service** within the [[GoogleCloudVertexAI|Vertex AI]] **Agent Engine**, presented in Chapter 8 ([[MemoryManagement|Memory Management]]) of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) as the cloud-backed operationalization of [[LongTermMemory|long-term memory]].

## What it is

> *"Memory Bank, a managed service in the Vertex AI Agent Engine, provides agents with persistent, long-term memory. The service uses [[gemini|Gemini]] models to asynchronously analyze conversation histories to extract key facts and user preferences."* — Ch 8

It removes the need to build and operate a memory store yourself: [[gemini|Gemini]] does the extraction, the service does the storage and consolidation, and the agent simply recalls.

## How it works

- **Asynchronous extraction.** [[gemini|Gemini]] models analyze conversation histories *out of band* to extract key facts and user preferences.
- **Persistent, scoped storage.** Extracted information is stored persistently and **organized by a defined scope like user ID** (each memory tagged with a unique `USER_ID` and `APP_NAME`).
- **Intelligent consolidation.** New data is *"intelligently updated to consolidate new data and resolve contradictions"* — Memory Bank actively reconciles conflicting facts rather than blindly appending (cf. [[ReflectionMemory|reflection-based memory]]'s insert/merge/replace policy).
- **Recall on new sessions.** When a new session starts, the agent retrieves relevant memories via either **full data recall** or a **similarity search using embeddings**, maintaining continuity and personalization across sessions.

## Integration

The agent's runner interacts with a `VertexAiMemoryBankService` (initialized first with `project`, `location`, `agent_engine_id`), which handles automatic storage of memories generated during conversations:

```python
from google.adk.memory import VertexAiMemoryBankService
memory_service = VertexAiMemoryBankService(project="PROJECT_ID", location="LOCATION", agent_engine_id=agent_engine_id)
# ...
await memory_service.add_session_to_memory(session)
```

- **[[GoogleADK|Google ADK]]:** *seamless, out-of-the-box* integration via `VertexAiMemoryBankService` (from `google.adk.memory`) — exposing the same `add_session_to_memory` interface as the rest of ADK's `MemoryService` layer.
- **[[LangGraph]] and [[crewai|CrewAI]]:** supported through **direct API calls** ("Online code examples demonstrating these integrations are readily available").

## Where it fits

Memory Bank is the production, cloud-managed answer to the same long-term-memory need that [[GoogleADK|ADK]]'s `VertexAiRagMemoryService`, [[LangGraph]]'s namespaced store, and external layers like [[Mem0]] address — but as a fully managed service where [[gemini|Gemini]] handles fact extraction and consolidation automatically.

## Connections
- [[MemoryManagement]] — the parent agentic design pattern (Ch 8).
- [[LongTermMemory]] — the tier it implements; [[SemanticMemory]] / [[EpisodicMemory]] / [[ProceduralMemory]] the memory types it stores.
- [[GoogleCloudVertexAI]] — the Vertex AI platform / Agent Engine it is part of.
- [[gemini|Gemini]] — the models that extract and consolidate facts.
- [[GoogleADK]] — out-of-the-box integration (`VertexAiMemoryBankService`).
- [[LangGraph]] / [[crewai|CrewAI]] — integrate via direct API calls.
- [[Mem0]] — peer external long-term-memory layer.
- [[VectorDatabase]] / [[SemanticSearch]] / [[rag|RAG]] — embedding-similarity recall substrate.
- [[ReflectionMemory]] — peer mechanism for contradiction resolution in memory.
- [[AgenticDesignPatterns]] — the book; [[AntonioGulli]] author.
- [[agentic-design-patterns-ch08-memory-management]] — source page.
