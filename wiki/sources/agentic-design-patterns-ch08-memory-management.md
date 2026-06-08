---
title: "Chapter 8 — Memory Management (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, memory, short-term-memory, long-term-memory, session-state, vector-store]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 8 of [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Gulli) is the **Memory Management** pattern: how agents retain and reuse information across turns and sessions. It establishes the dual-component model — **short-term (contextual) memory** living in the LLM [[ContextWindow|context window]], and **long-term (persistent) memory** living in external databases, knowledge graphs, or [[VectorDatabase|vector databases]] queried by [[SemanticSearch|semantic search]] — and grounds it in three hands-on framework implementations: [[GoogleADK|Google ADK]] (Session / State / MemoryService), [[LangChain]]/[[LangGraph]] (`ConversationBufferMemory`, stores, namespaces), and [[VertexAiMemoryBank|Vertex AI Memory Bank]]. It also names the three human-analogous types of long-term memory — **semantic, episodic, procedural**. (Agentic Design Patterns, PDF pp 132–153.)

## Key Claims
- **Memory is dual-component.** Agent memory is categorized into **short-term (contextual) memory** — recent messages, tool results, and reflections within the LLM's [[ContextWindow|context window]], ephemeral and lost when the session ends — and **long-term (persistent) memory** — a repository in external databases / [[VectorDatabase|vector databases]] retrieved by [[SemanticSearch|semantic similarity]] and integrated back into the short-term context.
- **Long context only enlarges short-term memory; it does not replace long-term memory.** "The advent of models with 'long context' windows simply expands the size of this short-term memory… However, this context is still ephemeral and is lost once the session concludes, and it can be costly and inefficient to process every time."
- **Google ADK structures context as Session / State / Memory.** A `Session` is one chat thread (its `events` log + `state` scratchpad); `session.state` is a key-value dictionary for the active chat; `MemoryService` is the searchable long-term store. SessionService and MemoryService each offer in-memory (testing), database, and cloud-backed (Vertex AI) implementations.
- **ADK state must be updated via the event pipeline, not by direct mutation.** Use `output_key` (auto-saves the agent's final text reply) or `EventActions.state_delta` appended via `session_service.append_event()`. State key prefixes scope persistence: `user:` (per-user across sessions), `app:` (shared across all users), `temp:` (current turn only, not persisted), no-prefix (session-specific). Direct mutation of `session.state` is "strongly discouraged."
- **ADK MemoryService exposes `add_session_to_memory` and `search_memory`.** Defined by the `BaseMemoryService` interface; implementations are `InMemoryMemoryService` (testing) and `VertexAiRagMemoryService` (production, backed by Vertex AI [[rag|RAG]] for scalable, persistent, semantic search).
- **LangChain/LangGraph split memory into short-term (thread-scoped, checkpointed) and long-term (cross-session, namespaced stores).** LangChain's `ChatMessageHistory` (manual) and `ConversationBufferMemory` (automated into chains via `memory_key`/`return_messages`) handle conversation history; LangGraph persists short-term memory via a **checkpointer** (resumable threads) and saves long-term memories as JSON documents in a **store**, organized by `(namespace, key)` and retrievable by `store.put` / `store.get` / `store.search` (similarity).
- **Long-term memory has three human-analogous types.** [[SemanticMemory|Semantic]] (facts/concepts — user "profile" or document "collection"); [[EpisodicMemory|episodic]] (past experiences/actions — often few-shot example prompting from successful past trajectories); [[ProceduralMemory|procedural]] (rules / how to perform tasks — the agent's system prompt, refinable via [[Reflection|Reflection]] that rewrites its own instructions).
- **Vertex AI Memory Bank is a managed long-term-memory service.** Part of the [[GoogleCloudVertexAI|Vertex AI]] Agent Engine, it uses [[gemini|Gemini]] models to asynchronously analyze conversation histories, extract key facts and user preferences, store them scoped by user ID, and intelligently consolidate/resolve contradictions; new sessions recall via full recall or embedding similarity search. Integrates with [[GoogleADK|ADK]] out-of-the-box and with [[LangGraph]]/[[crewai|CrewAI]] via API.
- **Rule of thumb:** implement memory management whenever an agent must do more than answer a single question — maintain conversational context, track multi-step task progress, personalize via recalled preferences, or learn from past successes/failures.

## Key Quotes
> "In agent systems, memory refers to an agent's ability to retain and utilize information from past interactions, observations, and learning experiences." — chapter definition of agent memory

> "Short-Term Memory (Contextual Memory): Similar to working memory, this holds information currently being processed or recently accessed. For agents using large language models (LLMs), short-term memory primarily exists within the context window." — the two-type taxonomy

> "Session and State can be conceptualized as short-term memory for a single chat session, whereas the Long-Term Knowledge managed by the MemoryService functions as a persistent and searchable repository." — ADK's mapping of its primitives onto the memory taxonomy

> "Procedural Memory: Remembering Rules… It's common for agents to modify their own prompts to adapt and improve. An effective technique is 'Reflection,' where an agent is prompted with its current instructions and recent interactions, then asked to refine its own instructions." — procedural memory + self-improvement

> "Memory Bank, a managed service in the Vertex AI Agent Engine, provides agents with persistent, long-term memory. The service uses Gemini models to asynchronously analyze conversation histories to extract key facts and user preferences." — Vertex AI Memory Bank

## Connections
- [[MemoryManagement]] — the chapter's named pattern (primary concept page).
- [[AgenticDesignPatterns]] — Chapter 8 of the book; [[AntonioGulli]], [[google|Google]].
- [[AgenticDesignPattern]] — the meta-concept; memory is one of the defining agent characteristics.
- [[ShortTermMemory]] / [[LongTermMemory]] — the dual-component model this chapter operationalizes per-framework.
- [[ContextWindow]] / [[ContextLength]] — substrate of short-term memory; long context enlarges but does not replace it.
- [[SemanticMemory]] / [[EpisodicMemory]] / [[ProceduralMemory]] — the three types of long-term memory.
- [[GoogleADK]] — Session / State / MemoryService primitives (`output_key`, `EventActions.state_delta`, `add_session_to_memory`, `search_memory`).
- [[LangChain]] — `ChatMessageHistory`, `ConversationBufferMemory`.
- [[LangGraph]] — checkpointer (short-term) + namespaced store (long-term, `InMemoryStore` / `put` / `get` / `search`).
- [[VertexAiMemoryBank]] — managed long-term-memory service; [[GoogleCloudVertexAI|Vertex AI]], [[gemini|Gemini]].
- [[crewai|CrewAI]] — Memory Bank also integrates with CrewAI via API.
- [[Mem0]] — peer external-memory layer (extraction-LM + vector store); same long-term-memory tier.
- [[VectorDatabase]] / [[SemanticSearch]] / [[rag|RAG]] — long-term-memory storage and retrieval substrate (the chapter cross-references Ch 14 on RAG).
- [[Reflection]] — the self-improvement technique used to update procedural memory.
- [[ConversationHistory]] / [[ConversationBufferMemory]] / [[ConversationSummaryMemory]] — conversation-history operationalizations.
- [[StatelessLLM]] — the statelessness memory management overcomes.
- [[LearningAndAdaptation]] — the next pattern (Ch 9); memory is its prerequisite.

## Contradictions
- None found. The chapter is consistent with the wiki's existing three-tier memory model ([[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]: internal-knowledge / short-term / long-term). Gulli's two-type framing (short / long) collapses Huyen's internal-knowledge tier into the model weights and focuses on the contextual vs. persistent split; the two are complementary, not conflicting. The wiki's [[ConversationBufferMemory]] / [[ConversationSummaryMemory]] pages already document the LangChain memory family this chapter re-summarizes.
