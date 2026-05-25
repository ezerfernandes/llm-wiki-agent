---
title: "Stateless LLM"
type: concept
tags: [llm, memory, agents, statelessness, conversation]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Stateless LLM

**LLMs are stateless.** Each forward pass through an LLM has **no memory** of any previous forward pass — *"they have no memory of any previous conversation."* All memory in LLM-powered applications is **application-side**: the application must explicitly include past turns in the prompt for the model to "remember" them. Named in [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]] as **the structural reason memory abstractions like [[ConversationBufferMemory]] / [[ConversationBufferWindowMemory]] / [[ConversationSummaryMemory]] exist**.

## The Ch 7 demonstration

Ch 7's two-call test that surfaces the property:

```python
# Call 1
basic_chain.invoke({"input_prompt": "Hi! My name is Maarten. What is 1 + 1?"})
# → "The answer to 1 + 1 is 2. ..."

# Call 2 — completely separate forward pass
basic_chain.invoke({"input_prompt": "What is my name?"})
# → "I'm sorry, but as a language model, I don't have the ability to know personal information about individuals."
```

The LLM doesn't know it told Maarten his sum was 2 a few seconds ago — the second call is a **clean forward pass** with no shared state.

Per Ch 7:

> *"When we are using LLMs out of the box, they will not remember what was being said in a conversation. You can share your name in one prompt but it will have forgotten it by the next prompt. ... The reason is that these models are stateless — they have no memory of any previous conversation!"*

## Where state lives in an LLM application

Even though the LLM is stateless, an LLM **application** can be stateful via three mechanisms:

1. **Conversation memory** (the [[LangChain]] memory classes — [[ConversationBufferMemory]], [[ConversationBufferWindowMemory]], [[ConversationSummaryMemory]], etc.) prepend past turns to each new prompt.
2. **Retrieval-augmented generation ([[rag|RAG]])** — fetches context from an external store and injects it into the prompt.
3. **Agent scratchpads** ([[LangChainAgent|`{agent_scratchpad}`]] in ReAct) — accumulate the Thought/Action/Observation trajectory across cycles within a single agent invocation.

In all three cases, **the LLM itself is still stateless**; the application is the stateful entity.

## Why this matters

- **Memory is an application concern, not a model concern.** The memory-type taxonomy (FIFO / summary / reflection) is a design surface over the application's prompt-construction logic.
- **The context window is the only place state can live.** All memory eventually compresses to *what you put in the next prompt*.
- **The trade-offs (tokens vs LM calls vs information loss) are real engineering trade-offs**, not gotchas — they're forced by the underlying statelessness.

## Connections

- [[ConversationBufferMemory]] / [[ConversationBufferWindowMemory]] / [[ConversationSummaryMemory]] — the [[LangChain]] memory classes that work around statelessness.
- [[FIFOMemory]] / [[SummarizationMemory]] / [[ReflectionMemory]] — [[ai-engineering-ch06-rag-agents|Huyen Ch 6's]] broader taxonomy.
- [[ConversationHistory]] — the application-state primitive.
- [[ContextLength]] / [[ContextWindow]] — the constraint that bounds in-context memory.
- [[rag|RAG]] — the retrieval-based answer to statelessness.
- [[Agent]] / [[AgenticAI]] — agent loops also work around statelessness via [[LangChainAgent|scratchpads]].
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

Ch 7 names statelessness directly — *"these models are stateless"* — and uses it as the structural justification for the entire **Memory** section of the chapter. The three Ch 7 memory classes ([[ConversationBufferMemory]] / [[ConversationBufferWindowMemory]] / [[ConversationSummaryMemory]]) are three different operationalizations of *"how do we work around the LLM being stateless?"* The chapter is the wiki's most explicit anchor for the property.
