---
title: "Summarization-Based Memory"
type: concept
tags: [memory, llm, agents, summarization]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Summarization-Based Memory

**Summarization-based memory** is the LLM-agent memory-management strategy in which **conversation history is compressed into running summaries** to reduce context footprint while preserving information. Cited by [[ai-engineering-ch06-rag-agents|Huyen Ch 6]] as the next-step refinement over [[FIFOMemory|FIFO eviction]] — *"one way to remove redundancy is by using a summary of the conversation."*

## Bae et al. 2022 — the canonical receipt

Huyen credits Bae et al. (2022) with the most refined variant: instead of just *summarizing then discarding*, they **join the summary with key information the summary missed**.

The mechanism:

1. Generate a summary of the memory.
2. Train a classifier: for each `(sentence in memory, sentence in summary)` pair, decide whether **only one**, **both**, or **neither** should be added to the new memory.
3. The new memory is the union of summary content and original-but-summary-missed content.

## Why this beats naive summarization

Naive summarization loses **named entities** and **specific facts** that didn't survive the summarizer's compression. Bae et al.'s classifier explicitly recovers them. The combination — summary for context + retained facts for specifics — is the structurally right shape for conversational memory.

## Position relative to other strategies

| Strategy | Cost | Information preservation |
|---|---|---|
| [[FIFOMemory]] | Free | Worst — purpose-statements drop |
| **Summarization** | Per-update LM call | Good — but loses facts the summarizer misses |
| Bae et al. summarization + classifier | Higher | Better — recovers missed facts |
| [[ReflectionMemory]] (Liu et al. 2023) | Highest | Best — agent decides per-action |

## Connections

- [[ShortTermMemory]] — the substrate.
- [[FIFOMemory]] / [[ReflectionMemory]] — sibling strategies.
- [[NamedEntityRecognition]] — the related-but-distinct technique often paired with summarization.
- [[LongTermMemory]] — where summarized content can be persisted.
- [[Agent]] — the system summarization-based memory serves.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch07-advanced-text-generation]] — runnable LangChain operationalization via `ConversationSummaryMemory`.

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

Ch 7 of *Hands-On LLMs* gives summarization-based memory its canonical [[LangChain]] operationalization as **`ConversationSummaryMemory`**:

```python
from langchain.memory import ConversationSummaryMemory

summary_prompt = PromptTemplate(input_variables=["new_lines", "summary"], template="""<s><|user|>Summarize the conversations and update with the new lines.
Current summary: {summary}
new lines of conversation: {new_lines}
New summary:<|end|>
<|assistant|>""")

memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", prompt=summary_prompt)
```

**Three operational points Ch 7 codifies**:

1. **Two LLM calls per turn** — *"there are two calls: the user prompt + the summarization prompt."* The summarization prompt takes the current summary + new conversation lines and produces an updated summary.
2. **The summarization LLM can be different from the user LLM**: *"Although we use the same LLM for both summarizing and user prompting, you could use a smaller LLM for the summarization task to speed up computation."* This is the operational answer to the cost trade-off Huyen Ch 6 named.
3. **The trade-off is not free** — *"This summarization helps keep the chat history relatively small without using too many tokens during inference. However, since the original question was not explicitly saved in the chat history, the model needed to infer it based on the context. This is a disadvantage if specific information needs to be stored in the chat history."* Ch 7 demonstrates this directly: after summarization, the model can **infer** what the first question was (*"what's 1 + 1?"*) but the verbatim form is gone — only the gist survives.

Ch 7's framing of the trade-off (Table 7-1):
- **Pros**: Captures the full history; enables long conversations; reduces tokens needed.
- **Cons**: An additional call is necessary for each interaction; quality is reliant on the LLM's summarization capabilities.

This is the **naive summarization** end of the spectrum — Bae et al. 2022's refinement (summary + classifier-recovered specifics) sits one step further in capability and cost. Ch 7 does **not** cover Bae et al.'s refinement; LangChain has `ConversationSummaryBufferMemory` (summary + recent-buffer hybrid) as a partial answer but Ch 7 doesn't include it either.
