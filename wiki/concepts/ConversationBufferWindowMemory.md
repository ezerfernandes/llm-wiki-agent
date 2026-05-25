---
title: "ConversationBufferWindowMemory"
type: concept
tags: [langchain, memory, llm, agents, chains, fifo]
sources: [hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# ConversationBufferWindowMemory

**`langchain.memory.ConversationBufferWindowMemory`** is [[LangChain]]'s **last-`k`-turns** memory class: it retains only the most recent `k` user/AI interaction pairs and drops everything older. This is the [[LangChain]] operationalization of [[FIFOMemory|FIFO eviction]] — the canonical name [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] uses for the same policy.

## Worked example

```python
from langchain.memory import ConversationBufferWindowMemory
memory = ConversationBufferWindowMemory(k=2, memory_key="chat_history")
llm_chain = LLMChain(prompt=prompt, llm=llm, memory=memory)
```

With `k=2`, only the last two `(Human, AI)` pairs are appended to the prompt's `{chat_history}` placeholder.

## The Ch 7 demonstration of the failure mode

Ch 7's worked example surfaces the trade-off Huyen Ch 6 warns about. The user shares **name + age** in turn 1:

```
Turn 1: "Hi! My name is Maarten and I am 33 years old. What is 1 + 1?"
Turn 2: <follow-up>
Turn 3: <follow-up>
Turn 4: "What is my age?"  → forgotten (turn 1 has fallen out of the k=2 window)
```

Ch 7's point: *"the window is too small to remember the age, which was only mentioned in the first turn."* The name survives because the user repeats it later; the age does not.

## Pros / Cons (Ch 7 Table 7-1)

| Pros | Cons |
|---|---|
| No information loss over the last k interactions | Only captures the last k interactions |
| Bounded token cost regardless of conversation length | No compression of the last k interactions |

## Position relative to other memory types

- **Operationalizes [[FIFOMemory|FIFO eviction]]** — drops oldest first. This is the same policy [[openai|OpenAI's]] API silently applies when conversations exceed context, exposed as a tunable `k`.
- **Pre-summarization end of the spectrum** — no LM call per turn (unlike [[ConversationSummaryMemory]]) but no compression either.
- **The failure mode Huyen Ch 6 names** — *"assumes that the early messages are less relevant to the current discussion ... this assumption can be fatally wrong"* — is the exact failure mode Ch 7 illustrates with the forgotten-age example.

## Connections

- [[LangChain]] — the framework.
- [[ConversationBufferMemory]] — the no-eviction variant.
- [[ConversationSummaryMemory]] — the compression variant.
- [[FIFOMemory]] — the abstract policy this class implements.
- [[ConversationHistory]] / [[ShortTermMemory]] — the substrate.
- [[StatelessLLM]] — the LLM property memory works around.
- [[ContextLength]] — the constraint motivating windowed memory.
- [[hands-on-llm-ch07-advanced-text-generation]] — primary source.

## From Hands-On LLMs Ch 7

The second of Ch 7's three memory types. The chapter frames `k` as a **direct dial on the memory-vs-token-cost trade-off**: small `k` is cheap but forgetful, large `k` approaches `ConversationBufferMemory`. Unlike `ConversationSummaryMemory`, no extra LM call is required — eviction is purely string-level. *"Although this is a simple solution to limit the amount of tokens that need to be processed, it doesn't capture information from earlier interactions."*
