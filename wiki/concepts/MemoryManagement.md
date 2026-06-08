---
title: "Memory Management"
type: concept
tags: [agents, memory, short-term-memory, long-term-memory, agentic-design-patterns, vector-store, session-state]
sources: [agentic-design-patterns-ch08-memory-management]
last_updated: 2026-06-07
---

# Memory Management

**Memory management** is the agentic design pattern by which an agent **retains and reuses information from past interactions, observations, and learning experiences** — both within a single conversation and across sessions. It is Chapter 8 of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) and one of the defining characteristics of an [[AgenticAI|agentic system]] catalogued by [[AgenticDesignPattern|the meta-pattern]]. Without it, agents are **stateless** ([[StatelessLLM]]) — unable to maintain conversational context, learn from experience, or personalize — which limits them to one-shot interactions.

## The dual-component model

Gulli's framing (consistent with, but coarser than, [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]'s three-tier model) splits agent memory into two types:

| Type | Substrate | Persistence | Speed | Capacity |
|---|---|---|---|---|
| **[[ShortTermMemory|Short-term (contextual)]]** | The LLM [[ContextWindow|context window]] | Per-session (ephemeral) | Fast | Limited by context length |
| **[[LongTermMemory|Long-term (persistent)]]** | External DB / knowledge graph / [[VectorDatabase|vector DB]] | Cross-session | Slow (retrieval latency) | Effectively unbounded |

- **Short-term / contextual / working memory** holds recent messages, agent replies, tool-usage results, and reflections from the current interaction. *"The advent of models with 'long context' windows simply expands the size of this short-term memory… However, this context is still ephemeral and is lost once the session concludes, and it can be costly and inefficient to process every time."* Management techniques: summarizing older segments ([[ConversationSummaryMemory]]), emphasizing key details, [[FIFOMemory|FIFO]] eviction.
- **Long-term / persistent memory** is queried by [[SemanticSearch|semantic similarity]] (the same substrate as [[rag|RAG]]); when needed, relevant data is retrieved and **integrated back into the short-term context** for immediate use.

## Why it matters in agentic systems

The chapter's *Why*: agentic systems need memory to perform complex, multi-step, time-dependent tasks and provide coherent experiences. Use cases: conversational AI / chatbots (flow + recalled preferences), task-oriented agents (track steps/progress/goals), personalized experiences, learning & improvement ([[LearningAndAdaptation]] — store successful strategies and mistakes), [[rag|RAG]]-based information retrieval, and autonomous systems (robots/self-driving needing maps, routes, learned behaviors).

**Rule of thumb:** implement memory whenever an agent must do more than answer a single question — maintain conversation context, track multi-step progress, personalize via recalled history, or learn/adapt from past successes and failures.

## Three types of long-term memory

Long-term memory subdivides into three human-analogous types:

- **[[SemanticMemory]]** — facts and concepts (user preferences, domain knowledge); managed as a continuously-updated user "profile" (JSON) or a "collection" of factual documents.
- **[[EpisodicMemory]]** — past events/actions; for agents, recalling *how to accomplish a task*, often implemented via few-shot example prompting from past successful trajectories.
- **[[ProceduralMemory]]** — rules / how to perform tasks; the agent's core instructions / system prompt, refinable via [[Reflection|Reflection]] (the agent rewrites its own instructions given current instructions + recent interactions).

## Framework operationalizations

The chapter grounds the pattern in three hands-on implementations:

| Framework | Short-term | Long-term |
|---|---|---|
| **[[GoogleADK|Google ADK]]** | `Session` + `session.state` (key-value scratchpad; `user:`/`app:`/`temp:` prefixes) | `MemoryService` (`add_session_to_memory`, `search_memory`); `InMemoryMemoryService` / `VertexAiRagMemoryService` |
| **[[LangChain]] / [[LangGraph]]** | `ChatMessageHistory`, `ConversationBufferMemory`; LangGraph **checkpointer** (resumable threads) | LangGraph **store** — JSON memories under `(namespace, key)`, `put`/`get`/`search` by similarity |
| **[[VertexAiMemoryBank|Vertex AI Memory Bank]]** | (the agent session) | Managed Agent-Engine service; [[gemini|Gemini]] extracts facts/preferences, consolidates, recalls per user ID |

ADK's discipline: **update state through the event pipeline** (`output_key` or `EventActions.state_delta` via `append_event()`), never by direct `session.state` mutation, so changes are logged, persisted, and timestamped. See [[GoogleADK]] for the full Session / State / Memory treatment.

## Relation to RAG and other memory layers

Long-term memory is *retrieval used inside the agent's own session boundary* — same [[VectorDatabase|vector-store]] / [[SemanticSearch|semantic-search]] substrate as [[rag|RAG]] (the chapter explicitly cross-references the RAG chapter). Concrete external-memory layers in the wiki include [[Mem0]] (extraction-LM + vector store, first-class multi-tenancy) and the LangChain memory family ([[ConversationBufferMemory]], [[ConversationBufferWindowMemory]], [[ConversationSummaryMemory]]). **Do not conflate** with hardware/GPU memory pages such as [[ActivationMemory]], [[MemoryHierarchy]], or [[SharedMemory]] — those concern numerical-computation memory, not agent state.

## Connections
- [[AgenticDesignPatterns]] — Chapter 8 of the book; [[AgenticDesignPattern]] meta-concept.
- [[ShortTermMemory]] / [[LongTermMemory]] — the two components.
- [[SemanticMemory]] / [[EpisodicMemory]] / [[ProceduralMemory]] — the three long-term-memory types.
- [[ContextWindow]] / [[ContextLength]] — short-term substrate.
- [[GoogleADK]] / [[LangChain]] / [[LangGraph]] / [[VertexAiMemoryBank]] / [[crewai|CrewAI]] — framework implementations.
- [[Mem0]] — peer external long-term-memory layer.
- [[VectorDatabase]] / [[SemanticSearch]] / [[rag|RAG]] / [[EmbeddingBasedRetrieval]] — storage + retrieval substrate.
- [[Reflection]] — updates procedural memory.
- [[ConversationHistory]] / [[ConversationBufferMemory]] / [[ConversationSummaryMemory]] / [[FIFOMemory]] — conversation-history strategies.
- [[StatelessLLM]] — the limitation memory overcomes.
- [[LearningAndAdaptation]] — the next pattern (Ch 9), for which memory is a prerequisite.
- [[Agent]] / [[AgenticAI]] — the systems memory serves.
- [[agentic-design-patterns-ch08-memory-management]] — source page.
