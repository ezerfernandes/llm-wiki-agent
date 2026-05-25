---
title: "Long-Term Memory (LLM)"
type: concept
tags: [memory, llm, agents, rag]
sources: [ai-engineering-ch06-rag-agents, dspy-mem0-react-tutorial]
last_updated: 2026-05-24
---

# Long-Term Memory

In [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]'s three-tier memory model, **long-term memory** is the **external data sources** the model accesses via retrieval — typically the same [[VectorDatabase|vector database]] / [[InvertedIndex|inverted-index]] substrate as [[rag|RAG]].

## Defining properties

> *"External data sources that a model can access via retrieval, such as in a RAG system, are a memory mechanism. This can be considered the model's long-term memory, as it can be persisted across tasks. Unlike a model's internal knowledge, information in the long-term memory can be deleted without updating the model."*

| Property | Long-term memory |
|---|---|
| Substrate | External stores (vector DB, SQL DB, file system) |
| Persistence | Cross-task, cross-session |
| Access speed | Slow (retrieval latency) |
| Capacity | Effectively unbounded |
| Mutability | Add / delete without retraining |

## What benefits long-term memory unlocks

Huyen names four benefits an explicit memory system provides:

1. **Information overflow management within a session** — when the agent acquires more information than fits in [[ShortTermMemory|short-term memory]], move it to long-term.
2. **Cross-session persistence** — *"An AI coach is practically useless if every time you want the coach's advice, you have to explain your whole life story."* Long-term memory remembers user preferences and conversation history.
3. **Consistency boost** — *"If you ask me a subjective question twice, like rating a joke between 1 and 5, I'm much more likely to give consistent answers if I remember my previous answer."*
4. **Data structural integrity** — long-term memory can store structured data (Excel sheets, queues, JSON) that text contexts cannot reliably maintain.

## Concrete implementations

The wiki tracks several candidate long-term-memory implementations:

| Implementation | Substrate | Decision layer | Wiki receipt |
|---|---|---|---|
| **[[Mem0]]** | External vector index | **Internal extraction LM** decides what to store | [[dspy-mem0-react-tutorial]] |
| Raw [[VectorDatabase]] | External vector index | None — caller writes whatever | [[ai-engineering-ch06-rag-agents]] |
| [[ConversationBufferMemory]] (LangChain) | In-process list | None — store all turns | LangChain memory family |
| [[ConversationSummaryMemory]] (LangChain) | In-process running summary | Summarization LM | LangChain memory family |
| [[DSPyHistory|`dspy.History`]] | In-process list of dicts | None | [[dspy-conversation-history]] |

The [[Mem0]] integration in [[dspy-mem0-react-tutorial]] is the wiki's **first canonical receipt for an external persistent memory layer wired into a [[DSPy]] [[react|`dspy.ReAct`]] agent** — memory CRUD methods become `tools=[...]`, and the agent's persistence policy is one sentence in the Signature docstring (*"remember to store the information in memory so that you can use it later"*).

## Position relative to RAG

> *"Memory retrieval is similar to RAG retrieval, as long-term memory is an external data source."*

Long-term memory is *RAG used inside the agent's own session boundary* — same retrieval substrate, different orchestration. RAG retrieves *external knowledge* (the company's documents, the codebase, the textbook); long-term memory retrieves *the agent's own past* (its conversation history, its prior reflections, its decisions).

## Connections

- [[ShortTermMemory]] / [[InternalKnowledgeMemory]] — sibling memory tiers.
- [[rag]] — the retrieval mechanism long-term memory shares with RAG.
- [[VectorDatabase]] — common substrate.
- [[FIFOMemory]] / [[SummarizationMemory]] / [[ReflectionMemory]] — the strategies that decide what moves from short- to long-term.
- [[memoryagentbench|MemoryAgentBench]] — adjacent wiki entry.
- [[Agent]] — the system long-term memory serves.
- [[Mem0]] — concrete long-term-memory implementation; first wiki receipt at [[dspy-mem0-react-tutorial]].
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[dspy-mem0-react-tutorial]] — concrete DSPy + [[Mem0]] integration receipt.
