---
title: "ConversationBufferMemory"
type: concept
tags: [langchain, memory, llm, agents, chains]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# ConversationBufferMemory

**`langchain.memory.ConversationBufferMemory`** is [[LangChain]]'s **simplest memory class**: it stores the **full conversation history verbatim** and appends it (as `"Human: ...\nAI: ..."` pairs) to every prompt via a designated `memory_key` variable (typically `chat_history`). The first of the three memory types treated in [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]].

## Worked example

```python
from langchain import PromptTemplate, LLMChain
from langchain.memory import ConversationBufferMemory

template = """<s><|user|>Current conversation:{chat_history}

{input_prompt}<|end|>
<|assistant|>"""
prompt = PromptTemplate(template=template, input_variables=["input_prompt", "chat_history"])
memory = ConversationBufferMemory(memory_key="chat_history")
llm_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)
```

After `llm_chain.invoke({"input_prompt": "Hi! My name is Maarten. What is 1 + 1?"})` the memory holds:
```
Human: Hi! My name is Maarten. What is 1 + 1?
AI: The answer to 1 + 1 is 2.
```
A follow-up `llm_chain.invoke({"input_prompt": "What is my name?"})` correctly returns *"Maarten"* because the prior turn is in the prompt — the [[StatelessLLM|statelessness]] of the underlying LLM has been masked by application-side memory.

## Pros / Cons (Ch 7 Table 7-1)

| Pros | Cons |
|---|---|
| Easiest implementation | Slower generation as more tokens are needed |
| Ensures no information loss within context window | Only suitable for large-context LLMs |
| Large-context LLMs not needed unless chat history is large | Larger chat histories make information retrieval difficult (model has to find the relevant fact in a long buffer) |

## Position relative to other memory types

- **No eviction** — sits at the opposite end of [[FIFOMemory|FIFO eviction]] (which `ConversationBufferWindowMemory` operationalizes).
- **No compression** — sits at the opposite end of [[SummarizationMemory|summarization]] (which `ConversationSummaryMemory` operationalizes).
- Ch 7's framing: *"Where ConversationBufferMemory is instant but hogs tokens, ConversationSummaryMemory is slow but frees up tokens to use."*

## Connections

- [[LangChain]] — the framework providing this memory class.
- [[ConversationBufferWindowMemory]] — the windowed-FIFO variant.
- [[ConversationSummaryMemory]] — the summarization variant.
- [[ConversationHistory]] — the underlying concept.
- [[StatelessLLM]] — the LLM property that motivates memory.
- [[FIFOMemory]] / [[SummarizationMemory]] / [[ReflectionMemory]] — [[ai-engineering-ch06-rag-agents|Huyen Ch 6]]'s broader taxonomy.
- [[ContextLength]] / [[ContextWindow]] — what eventually bounds this strategy.
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

Ch 7's first memory type. *"By extending the chain with memory, the LLM was able to use the chat history to find the name we gave it previously. LangChain saves it internally as `Human: ... AI: ...` interaction pairs."* The chapter introduces it as the **baseline-and-simplest** option — the conceptual starting point against which the windowed and summarized variants are then compared. The chapter is candid about the trade-off: the buffer is **instant** (no extra LM call) but **token-hungry** — long conversations eventually hit the context-length ceiling.
