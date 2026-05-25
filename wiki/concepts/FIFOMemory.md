---
title: "FIFO Memory Management"
type: concept
tags: [memory, llm, agents, strategy]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# FIFO Memory Management

**FIFO (First In, First Out)** is the **simplest** memory-management strategy for LLM agents and chat applications: the oldest messages in [[ShortTermMemory|short-term memory]] are evicted first when the context fills up. Per [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]]:

> *"As a conversation gets longer, API providers like OpenAI might start removing the beginning of the conversation. Frameworks like LangChain might allow the retention of N last messages or N last tokens."*

## Why it's a popular default

- **Trivial to implement** — drop oldest message; no LM call needed.
- **Constant cost** — no per-step summarization or reflection overhead.
- **Predictable behavior** — easy to reason about what the model sees.

## The failure mode

> *"In a long conversation, this strategy assumes that the early messages are less relevant to the current discussion. However, this assumption can be fatally wrong. In some conversations, the earliest messages might carry the most information, especially when the early messages state the purpose of the conversation."*

Worked example: a user opens a coding session with *"Help me debug my Python script that calculates compound interest with a 3% annual rate"* and then continues with 50 messages of error trace pasting. FIFO eviction drops the initial purpose statement — the model loses the *what we're building* anchor.

## Why usage-based eviction is harder

Huyen's footnote: *"Usage-based strategies, such as removing the least frequently used information, is more challenging, since you'll need a way to know when a model uses a given piece of information."*

LLMs don't expose attention-attribution by default, so *"which past messages contributed to this response"* is a hard signal to capture.

## Position relative to better strategies

| Strategy | Trade-off |
|---|---|
| **FIFO** | Cheap; loses purpose-stating messages |
| [[SummarizationMemory]] (Bae et al. 2022) | Costlier; preserves key information; may lose nuance |
| [[ReflectionMemory]] (Liu et al. 2023) | Most expensive; agent decides per-action what to keep |

## Connections

- [[ShortTermMemory]] — the substrate FIFO manages.
- [[SummarizationMemory]] / [[ReflectionMemory]] — more sophisticated alternatives.
- [[LongTermMemory]] — where FIFO-evicted content can be moved instead of deleted.
- [[LangChain]] / [[openai|OpenAI]] — frameworks that implement FIFO defaults.
- [[Agent]] — the system FIFO serves.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch07-advanced-text-generation]] — operationalizes FIFO as [[LangChain]]'s `ConversationBufferWindowMemory(k=2)`.

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

Ch 7 of *Hands-On LLMs* gives FIFO eviction its canonical [[LangChain]] operationalization as **`ConversationBufferWindowMemory(k=2)`**:

```python
from langchain.memory import ConversationBufferWindowMemory
memory = ConversationBufferWindowMemory(k=2, memory_key="chat_history")
```

The `k` parameter is the **window size** — only the last `k` user/AI turns are retained; everything older is dropped on the floor. Ch 7's worked example demonstrates the failure mode Huyen warns about: the user states their **name and age** in turn 1; after two more turns the model knows the name (it appeared in turn 1 which is no longer in the k=2 window, BUT the model also reads it from a later turn where it was repeated) but **forgets the age** which was only mentioned in turn 1.

**Ch 7's framing of the trade-off** (Table 7-1):
- **Pro**: *"No information loss over the last k interactions."*
- **Con**: *"Only captures the last k interactions; no compression of the last k interactions."*

Ch 7's `ConversationBufferWindowMemory` is the concrete LangChain answer to Huyen Ch 6's *"Frameworks like LangChain might allow the retention of N last messages or N last tokens."* — the same FIFO eviction policy, exposed as a tunable `k` parameter.
