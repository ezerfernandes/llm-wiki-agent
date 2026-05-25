---
title: "ConversationSummaryMemory"
type: concept
tags: [langchain, memory, llm, agents, chains, summarization]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# ConversationSummaryMemory

**`langchain.memory.ConversationSummaryMemory`** is [[LangChain]]'s **running-summary** memory class: instead of retaining raw turn-by-turn history (like [[ConversationBufferMemory]]) or windowed history (like [[ConversationBufferWindowMemory]]), it maintains a **single rolling summary** of the conversation, **updated each turn by an LLM call**. The [[LangChain]] operationalization of [[SummarizationMemory|summarization-based memory]] (Huyen Ch 6's vocabulary; Bae et al. 2022 is the canonical research citation).

## Worked example

```python
from langchain.memory import ConversationSummaryMemory

summary_prompt_template = """<s><|user|>Summarize the conversations and update with the new lines.
Current summary: {summary}
new lines of conversation: {new_lines}
New summary:<|end|>
<|assistant|>"""
summary_prompt = PromptTemplate(input_variables=["new_lines", "summary"], template=summary_prompt_template)

memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", prompt=summary_prompt)
llm_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)
```

Each turn triggers **two LM calls**: one to answer the user, one to update the running summary.

## The "two LLMs" optimization

Ch 7 explicitly notes that the summarization LLM **does not have to be the same model** as the user-facing LLM:

> *"This summarization process is enabled by another LLM that is given the conversation history as input and asked to create a concise summary. A nice advantage of using an external LLM is that we are not confined to using the same LLM during conversation. Although we use the same LLM for both summarizing and user prompting, you could use a smaller LLM for the summarization task to speed up computation."* — Ch 7

This is the operational answer to the cost criticism Huyen Ch 6 levels at summarization memory.

## Pros / Cons (Ch 7 Table 7-1)

| Pros | Cons |
|---|---|
| Captures the full history | An additional LM call is necessary for each interaction |
| Enables long conversations | Quality is reliant on the LLM's summarization capabilities |
| Reduces tokens needed to capture full history | Specific verbatim information may be lost (model must *infer* it from the summary) |

## The trade-off Ch 7 codifies

> *"This summarization helps keep the chat history relatively small without using too many tokens during inference. However, since the original question was not explicitly saved in the chat history, the model needed to infer it based on the context. This is a disadvantage if specific information needs to be stored in the chat history."* — Ch 7

Ch 7 demonstrates this directly: after summarization, the model can **infer** *"what was the first question?"* (the gist survives) but the verbatim form is gone.

## Position relative to other memory types

- **Most expensive per turn** of the three Ch 7 memory classes — two LM calls vs one.
- **Most compact in tokens** — the running summary stays bounded regardless of conversation length.
- **Lossy by design** — sits one step behind [[ReflectionMemory|reflection-based memory]] (Liu et al. 2023) in Huyen Ch 6's three-tier taxonomy.
- Ch 7's framing: *"Where ConversationBufferMemory is instant but hogs tokens, ConversationSummaryMemory is slow but frees up tokens to use."*

## Connections

- [[LangChain]] — the framework.
- [[ConversationBufferMemory]] / [[ConversationBufferWindowMemory]] — sibling memory classes.
- [[SummarizationMemory]] — the abstract concept this class operationalizes.
- [[ReflectionMemory]] — the next-step-up strategy (not provided by Ch 7).
- [[ConversationHistory]] / [[ShortTermMemory]] — the substrate.
- [[StatelessLLM]] — the LLM property memory works around.
- [[PromptTemplate]] — the summary prompt is itself a PromptTemplate.
- [[ContextLength]] — the constraint summarization-memory addresses by compression.
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

Ch 7's third and most sophisticated memory type. The chapter frames it as the **compression-vs-cost** answer to the [[ConversationBufferMemory]] / [[ConversationBufferWindowMemory]] tension: instead of choosing between *keeping everything* and *dropping oldest*, you *re-encode everything more compactly*. Ch 7 stops here — LangChain also provides `ConversationSummaryBufferMemory` (hybrid: summary of old + verbatim recent) which is not covered.
