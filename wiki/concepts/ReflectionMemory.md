---
title: "Reflection-Based Memory"
type: concept
tags: [memory, llm, agents, reflection]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Reflection-Based Memory

**Reflection-based memory** is the most-sophisticated LLM-agent memory-management strategy named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]: **after each action, the agent reflects on the new information and decides what to do with it**. Liu et al. (2023) is Huyen's canonical citation.

## The two-step reflection

> *"After each action, the agent is asked to do two things:*
> 1. *Reflect on the information that has just been generated.*
> 2. *Determine if this new information should be inserted into the memory, should merge with the existing memory, or should replace some other information, especially if the other information is outdated and contradicts new information."*

## Three operations on the memory

| Operation | When |
|---|---|
| **Insert** | New, non-overlapping information |
| **Merge** | Related to existing memory, can be combined |
| **Replace** | Contradicts existing memory; the new is canonical |

## How contradictions are handled

Reflection-based memory is the **only** of the three Ch 6 strategies that handles **contradictions** explicitly:

> *"When encountering contradicting pieces of information, some people opt to keep the newer ones. Some people ask AI models to judge which one to keep. How to handle contradiction depends on the use case. Having contradictions can cause an agent to be confused but can also help it draw from different perspectives."*

The contradiction policy is itself a hyperparameter — *prefer newer* is a sensible default for fact updates; *keep both* makes sense for opinion-rich content where multiple perspectives are signal, not noise.

## Position relative to other strategies

| Strategy | Mechanism |
|---|---|
| [[FIFOMemory]] | Drop oldest |
| [[SummarizationMemory]] (Bae et al. 2022) | Compress + retain missed facts |
| **Reflection** (Liu et al. 2023) | Per-action LM-decided add/merge/replace |

## Cost trade-off

Reflection-based memory is the **most expensive** of the three — every action triggers a reflection LM call. It is justified for high-stakes agents where memory errors are costly (medical/legal/financial assistants), less justified for ephemeral assistants where FIFO is fine.

## Connections

- [[ShortTermMemory]] — the substrate.
- [[FIFOMemory]] / [[SummarizationMemory]] — sibling strategies.
- [[reflexion|Reflexion]] / [[react|ReAct]] — the broader reflection family this strategy belongs to.
- [[SelfCritique]] — the underlying mechanism.
- [[Agent]] — the system reflection-based memory serves.
- [[Hallucination]] — what memory contradictions can drive without explicit handling.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch07-advanced-text-generation]] — Ch 7 does NOT cover reflection memory; covers the simpler two predecessors only.

## Position relative to Hands-On LLMs Ch 7

Ch 7 of *Hands-On LLMs* covers three [[LangChain]] memory classes — [[ConversationBufferMemory]] (no eviction), [[ConversationBufferWindowMemory]] (FIFO eviction), [[ConversationSummaryMemory]] (summarization). It does **not** cover reflection-based memory, even though LangChain ships `ConversationKGMemory` (knowledge-graph extraction over the conversation) and `VectorStoreRetrieverMemory` (vector-similarity retrieval over past turns) as partial implementations of the reflection-style strategy. The gap: Ch 7 is pedagogical-first and covers the three monotonically-more-sophisticated baseline strategies. Liu et al. 2023's reflection mechanism remains a wiki-side concept anchored to Huyen Ch 6.
