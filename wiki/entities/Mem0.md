---
title: "Mem0"
type: entity
tags: [framework, memory, agents, long-term-memory, vector-store, python-library]
sources: [dspy-mem0-react-tutorial]
last_updated: 2026-05-24
---

# Mem0

**Mem0** ([mem0.ai](https://mem0.ai/), [github.com/mem0ai/mem0](https://github.com/mem0ai/mem0), `pip install mem0ai`) is an open-source **long-term memory layer for LLM applications**. It exposes a small CRUD-shaped API (`add` / `search` / `get_all` / `update` / `delete`) over a backing **vector store** + **internal extraction LM**: raw text is added with a `user_id` key, an internal LM decides what discrete factual memories to extract, an embedder vectorizes the extracted memories, and the vector index serves nearest-neighbor search at retrieval time.

Across the wiki, Mem0 is one of several candidate **long-term memory** implementations the [[LongTermMemory]] page describes in the abstract — alongside vanilla [[VectorDatabase|vector-DB]]-as-memory and the [[LangChainAgent|LangChain]] [[ConversationBufferMemory|in-process buffer]] / [[ConversationSummaryMemory|summary-memory]] patterns. Its differentiator is the **internal extraction LM**: where a raw vector DB stores whatever text the caller writes, Mem0 stores only what its extraction LM decides is memorable.

## Two-component shape

Every Mem0 instance is configured with two LM-shaped components:

| Component | Purpose | Tutorial default |
|---|---|---|
| `llm` | Internal extraction LM — reads raw input, decides what factual claims to store | `openai/gpt-4o-mini` @ temperature 0.1 |
| `embedder` | Vectorizes stored memories for similarity search | `openai/text-embedding-3-small` |

Low temperature on the extraction LM is the conventional setting — memory storage should be deterministic, not creative. The embedder choice trades dimension count, semantic quality, and cost; the tutorial defaults to OpenAI's small embedding for tutorial simplicity.

## API surface

The `Memory` class exposes the CRUD methods Mem0-enabled agents wrap as tools:

| Method | Purpose |
|---|---|
| `memory.add(content, user_id=...)` | Hand raw text to the extraction LM; store whatever factual memories it extracts |
| `memory.search(query, user_id=..., limit=...)` | Vector-NN-search the per-user memory index |
| `memory.get_all(user_id=...)` | Return all stored memories for a user |
| `memory.update(memory_id, new_content)` | Replace a specific memory in place |
| `memory.delete(memory_id)` | Remove a specific memory |

Every method takes `user_id` (with a `"default_user"` sentinel) — **multi-tenant from the first line of code**. The same instance serves arbitrarily many users; isolation is the `user_id` partition key.

`Memory.from_config(config_dict)` is the canonical constructor: a dict-of-dicts with `llm` and `embedder` sub-blocks (and optionally a backing-store sub-block).

## Integration receipts

### DSPy + Mem0 (this wiki's canonical receipt)

[[dspy-mem0-react-tutorial]] is the **first wiki receipt** of Mem0 integrated with [[DSPy]]: a `dspy.Module` subclass exposes Mem0's CRUD methods as `tools=[...]` to a `dspy.ReAct` Module. The agent's persistence policy is one sentence in the Signature docstring — *"Whenever you answer a user's input, remember to store the information in memory so that you can use it later"*. The integration shape:

```python
import dspy
from mem0 import Memory

config = {
    "llm": {"provider": "openai", "config": {"model": "gpt-4o-mini", "temperature": 0.1}},
    "embedder": {"provider": "openai", "config": {"model": "text-embedding-3-small"}},
}
memory = Memory.from_config(config)

# In the agent class:
self.react = dspy.ReAct(
    signature=MemoryQA,
    tools=[memory_tools.store_memory, memory_tools.search_memories, ...],
    max_iters=6
)
```

Bound methods of a tool class work as DSPy tools — [[DSPy]] introspects `__name__` and docstring as if they were free functions. The `Memory` instance is constructor-injected, shared across all tools.

## Counter-positioning vs other memory patterns

| Pattern | Storage | Decision layer | Per-user isolation | Mutability |
|---|---|---|---|---|
| **[[ConversationBufferMemory]]** (LangChain) | In-process Python list | None — store everything | Per-process | Append-only |
| **[[ConversationBufferWindowMemory]]** (LangChain) | In-process ring buffer | Drop oldest | Per-process | Eviction by recency |
| **[[ConversationSummaryMemory]]** (LangChain) | In-process running summary | Summarization LM | Per-process | Lossy compression |
| **Raw [[VectorDatabase|vector DB]]** | External vector index | None — store whatever | Caller-managed | Append + delete |
| **[[DSPyHistory|`dspy.History`]]** | In-process list of `dict` | None | Per-session | Append-only |
| **Mem0** | External vector index | Internal **extraction LM** | First-class `user_id` partition | Add / search / update / delete |

Mem0's two distinguishing properties are (i) the **internal extraction LM** (decides what to store rather than storing everything) and (ii) **first-class multi-tenancy** (`user_id` on every call rather than caller-managed key namespacing).

## Wiki receipts

- [[dspy-mem0-react-tutorial]] — first wiki receipt. [[DSPy]] [[react|`dspy.ReAct`]] agent with Mem0 CRUD tools, single `"default_user"`, seven-turn personalization demo over food / exercise / hiking preferences plus reminders.

## Connections

- **[[LongTermMemory]]** — concept. Mem0 is a concrete implementation of the [[LongTermMemory|long-term memory]] tier in the [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] three-tier memory model.
- **[[DSPy]]** — entity. Composes with [[DSPy]] via the `tools=[...]` kwarg on [[react|`dspy.ReAct`]]; see [[dspy-mem0-react-tutorial]].
- **[[react|ReAct]]** — concept. The think-act-observe loop the wiki's canonical Mem0 receipt uses to dispatch memory CRUD.
- **[[Agent]]** — concept. Memory layer turns a stateless agent into a personalized one across sessions.
- **[[VectorDatabase]]** — concept. Mem0's storage substrate is a vector store; the embedder config determines the embedding space.
- **[[openai]]** — entity. Default provider for both the extraction LM and the embedder in the wiki's canonical receipt.
- **[[AgenticRAG]]** — concept. Adjacent pattern: agentic RAG retrieves from a document store; a Mem0-enabled agent retrieves from a **personalized memory store**.
- **[[2604.25850-agentic-harness-engineering]]** — paper. The AHE paper positions **long-term memory** as one of the three load-bearing legs of an agent harness (alongside tools and middleware); Mem0 is a concrete instantiation of that leg.
