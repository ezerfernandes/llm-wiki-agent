---
title: "DSPy Tutorial — Memory-Enabled ReAct Agents with Mem0"
type: source
tags: [dspy, tutorial, react, agent, memory, mem0, long-term-memory, personalization]
date: 2026-05-24
source_file: raw/dspy-mem0-react-tutorial.md
---

## Summary

The [[DSPy]] **Memory-Enabled ReAct Agents with Mem0** tutorial ([dspy.ai/tutorials/mem0_react_agent](https://dspy.ai/tutorials/mem0_react_agent/)) is the wiki's first receipt for **wiring a persistent external [[LongTermMemory|long-term memory]] layer into a [[react|`dspy.ReAct`]] agent**. The recipe combines two libraries — [[DSPy]]'s [[react|ReAct]] [[DSPyModules|Module]] for the think-act-observe loop and [[Mem0]] (`mem0ai`) for cross-session memory storage / retrieval — into a single `MemoryReActAgent(dspy.Module)` class whose `tools=[...]` list exposes memory CRUD operations (`store_memory`, `search_memories`, `get_all_memories`) plus three higher-level personalization helpers (`set_reminder`, `get_preferences`, `update_preferences`) and a `get_current_time` utility.

The tutorial is the **ninth wiki-corpus [[DSPy]] tutorial** after [[dspy-conversation-history|conversation history]], [[dspy-customer-service-agent|customer-service agent]], [[dspy-custom-module|custom module]], [[dspy-rag-tutorial|RAG tutorial]], [[dspy-tutorial-rag-as-agent|RAG-as-agent]], [[dspy-entity-extraction-tutorial|entity extraction]], [[dspy-tutorial-math|MATH algebra]], and [[dspy-ai-text-game-tutorial|creative text game]]. It fills the **persistent-memory agent rung** the corpus had not yet covered — every prior DSPy tutorial either ran single-turn ([[dspy-customer-service-agent|customer service]], [[dspy-tutorial-math|MATH]], [[dspy-entity-extraction-tutorial|NER]]) or kept conversation state in an in-process [[DSPyHistory|`dspy.History`]] buffer ([[dspy-conversation-history]]). This tutorial is the first DSPy receipt where **memory survives outside the program** — a [[VectorDatabase|vector-DB]]-backed store the agent reads and writes through tool calls.

The tutorial's three load-bearing structural claims:

1. **Memory is a tool, not a Module concern.** The `MemoryReActAgent` is a thin `dspy.Module` whose `forward()` just dispatches to a single `dspy.ReAct(...)` call; all memory behavior lives in the **tool functions** the LM decides to invoke. This is the *agent-via-tools* pattern from [[dspy-customer-service-agent]] applied to the memory subsystem.
2. **The Signature's docstring is the persistence policy.** *"Whenever you answer a user's input, remember to store the information in memory so that you can use it later"* — this one-sentence instruction inside the `MemoryQA` Signature docstring is what makes the agent **proactively write** to memory rather than only reading from it. Without that instruction, the LM would only call memory tools when the user explicitly asked.
3. **Memory tools take a `user_id` argument** — even with the *"default_user"* default, the API shape is **multi-tenant from the first line of code**. Cross-session personalization (Alice's food preferences persisting across turns) and multi-user isolation are the same mechanism: a string key on every `add` / `search` / `get_all` call.

## Key Claims

- **Mem0 is the persistence layer; DSPy is the orchestration layer.** *"This tutorial demonstrates building conversational agents that retain information across interactions by combining DSPy's ReAct framework with Mem0's memory system."* — the division of labor is explicit: [[DSPy]] owns the [[react|ReAct]] loop and the Signature; [[Mem0]] owns the storage, embedding, and similarity-search subsystem. The agent code is the **glue layer** that exposes [[Mem0]]'s `add` / `search` / `get_all` / `update` / `delete` API as DSPy tools.

- **Memory configuration follows the [[Mem0]] two-component shape**: an `llm` block (provider + model + temperature) for memory-extraction decisions (Mem0 internally uses an LM to decide what to store from raw turns), and an `embedder` block (provider + embedding model) for the vector-index over stored memories. The tutorial uses `gpt-4o-mini` for both the extraction LM and the agent LM, and `text-embedding-3-small` as the embedder.

- **Tool-class-as-namespace pattern.** The five Mem0-CRUD tools live as methods on a `MemoryTools` class instance (`store_memory`, `search_memories`, `get_all_memories`, `update_memory`, `delete_memory`). The instance is constructed with the `Memory` object the agent shares. When passed into `dspy.ReAct(tools=[...])`, the bound methods are treated as plain callables — [[DSPy]] introspects `__name__` and docstring as if they were free functions. This is a **mild extension** of the [[dspy-customer-service-agent|customer-service agent's]] *"tools are plain Python functions"* discipline: bound methods work too, because the framework only needs callability + signature.

- **The Signature is two fields**: `user_input: str = dspy.InputField()` → `response: str = dspy.OutputField()`. Identical shape to [[dspy-customer-service-agent]]'s `user_request` → `process_result`. The tool list is what carries the agent's capability; the Signature stays minimal.

- **`max_iters=6` is the per-call ReAct budget.** The agent has six think-act-observe iterations per user turn to decide whether to write, read, or both, and to compose a final `response`. Tight enough to prevent runaway tool-calling, loose enough for a *"What do you know about me so far?"* turn that needs both `get_all_memories` and `search_memories` calls before answering.

- **Higher-level helpers compose CRUD primitives.** `set_reminder`, `get_preferences`, `update_preferences` are not new Mem0 features — they are **opinionated wrappers** that pre-format the content string (`f"REMINDER: ..."`, `f"User preference for {category}: ..."`) before calling `store_memory`, or pre-format the query string (`f"user preferences {category}"`) before calling `search_memories`. The wrappers exist to **bias the LM toward consistent storage / retrieval phrasing** rather than letting it invent the format per turn.

- **The demo conversation script demonstrates personalization across seven turns** with a single `user_id="default_user"`: the agent stores food preferences (turn 1), exercise preferences (turn 2), retrieves food preferences (turn 3), sets a reminder (turn 4), retrieves exercise preferences (turn 5), stores hiking preference (turn 6), and synthesizes everything in a final summary (turn 7). The Alice persona is just a string in the input — the multi-user mechanism is the `user_id` kwarg, not the prose.

## Key Quotes

> *"This tutorial demonstrates building conversational agents that retain information across interactions by combining DSPy's ReAct framework with Mem0's memory system."* — frames the tutorial as the canonical [[DSPy]] + [[Mem0]] receipt.

> *"Whenever you answer a user's input, remember to store the information in memory so that you can use it later."* — the one-sentence instruction inside the `MemoryQA` Signature docstring. Load-bearing: it is what makes the agent **proactively write** to memory rather than only reading on demand.

> *"LM handles creative generation while game logic remains deterministic and controllable."* — this is the *prior* tutorial's framing, but the pattern recurs here: **LM owns the decision of what to remember; Mem0 owns the storage substrate**. The deterministic-substrate / LM-decision-layer split is a recurring DSPy-tutorial architectural pattern.

> *"The combination allows agents to reason through multi-step problems while simultaneously managing contextual information for future interactions, creating more coherent and personalized AI experiences."* — closing thesis: memory + ReAct = personalization.

## Code Receipts

### Receipt 1 — Mem0 configuration

```python
import dspy
from mem0 import Memory
import os

os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4o-mini",
            "temperature": 0.1
        }
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    }
}
```

Two-block config: `llm` for Mem0's internal memory-extraction LM (decides what to store from raw turns), `embedder` for the vector index over stored memories. Low temperature (`0.1`) on the extraction LM — memory storage should be deterministic, not creative.

### Receipt 2 — Mem0 CRUD tools

```python
class MemoryTools:
    """Tools for interacting with the Mem0 memory system."""

    def __init__(self, memory: Memory):
        self.memory = memory

    def store_memory(self, content: str, user_id: str = "default_user") -> str:
        """Store information in memory."""
        try:
            self.memory.add(content, user_id=user_id)
            return f"Stored memory: {content}"
        except Exception as e:
            return f"Error storing memory: {str(e)}"

    def search_memories(self, query: str, user_id: str = "default_user", limit: int = 5) -> str:
        """Search for relevant memories."""
        try:
            results = self.memory.search(query, user_id=user_id, limit=limit)
            if not results:
                return "No relevant memories found."

            memory_text = "Relevant memories found:\n"
            for i, result in enumerate(results["results"]):
                memory_text += f"{i}. {result['memory']}\n"
            return memory_text
        except Exception as e:
            return f"Error searching memories: {str(e)}"

    def get_all_memories(self, user_id: str = "default_user") -> str:
        """Get all memories for a user."""
        # ... (similar pattern)
```

Structural notes: (i) every tool takes `user_id` — multi-tenant from the API surface; (ii) every tool returns a `str` formatted for LM consumption (numbered list, error messages framed as natural-language sentences) — the LM reads tool outputs as observations, so formatting matters; (iii) try/except wraps every Mem0 call — a tool error returns a string the LM can reason over, not a Python exception that would abort the ReAct loop.

### Receipt 3 — Signature

```python
class MemoryQA(dspy.Signature):
    """
    You're a helpful assistant and have access to memory method.
    Whenever you answer a user's input, remember to store the information in memory
    so that you can use it later.
    """
    user_input: str = dspy.InputField()
    response: str = dspy.OutputField()
```

Two-field Signature. The **docstring is the persistence policy** — without the *"remember to store"* sentence, the LM would only read from memory, never write. This is the receipt for *"docstring scopes agent behavior"* from [[dspy-customer-service-agent]] applied to memory persistence.

### Receipt 4 — Agent class

```python
class MemoryReActAgent(dspy.Module):
    """A ReAct agent enhanced with Mem0 memory capabilities."""

    def __init__(self, memory: Memory):
        super().__init__()
        self.memory_tools = MemoryTools(memory)

        self.tools = [
            self.memory_tools.store_memory,
            self.memory_tools.search_memories,
            self.memory_tools.get_all_memories,
            get_current_time,
            self.set_reminder,
            self.get_preferences,
            self.update_preferences,
        ]

        self.react = dspy.ReAct(
            signature=MemoryQA,
            tools=self.tools,
            max_iters=6
        )

    def forward(self, user_input: str):
        return self.react(user_input=user_input)
```

The agent is a **one-line forward** that delegates to `dspy.ReAct`. The `__init__` does all the wiring: instantiate the `MemoryTools` over the shared `Memory` object, assemble the seven-tool list (three Mem0 CRUD + one utility + three preference wrappers), and instantiate `dspy.ReAct` with `max_iters=6`.

### Receipt 5 — Higher-level preference helpers

```python
def set_reminder(self, reminder_text: str, date_time: str = None, user_id: str = "default_user") -> str:
    """Set a reminder for the user."""
    reminder = f"Reminder set for {date_time}: {reminder_text}"
    return self.memory_tools.store_memory(
        f"REMINDER: {reminder}",
        user_id=user_id
    )

def get_preferences(self, category: str = "general", user_id: str = "default_user") -> str:
    """Get user preferences for a specific category."""
    query = f"user preferences {category}"
    return self.memory_tools.search_memories(query=query, user_id=user_id)

def update_preferences(self, category: str, preference: str, user_id: str = "default_user") -> str:
    """Update user preferences."""
    preference_text = f"User preference for {category}: {preference}"
    return self.memory_tools.store_memory(preference_text, user_id=user_id)
```

The three helpers are **format wrappers** over the underlying CRUD primitives. They bias the LM toward consistent storage phrasing (`"REMINDER: ..."`, `"User preference for {category}: ..."`) and consistent retrieval phrasing (`"user preferences {category}"`). The cost: the agent now has seven tools instead of three, increasing the per-turn tool-selection complexity.

### Receipt 6 — Driver

```python
def run_memory_agent_demo():
    lm = dspy.LM(model='openai/gpt-4o-mini')
    dspy.configure(lm=lm)
    memory = Memory.from_config(config)
    agent = MemoryReActAgent(memory)

    conversations = [
        "Hi, I'm Alice and I love Italian food, especially pasta carbonara.",
        "I'm Alice. I prefer to exercise in the morning around 7 AM.",
        "I'm Alice. What do you remember about my food preferences?",
        "I'm Alice. Set a reminder for me to go grocery shopping tomorrow.",
        "I'm Alice. What are my exercise preferences?",
        "I'm Alice. I also enjoy hiking on weekends.",
        "I'm Alice. What do you know about me so far?"
    ]

    for user_input in conversations:
        response = agent(user_input=user_input)
        print(response.response)
        time.sleep(1)
```

The `time.sleep(1)` between turns is a rate-limit guard against the [[openai|OpenAI]] tier. The agent is instantiated once and reused across all turns — memory persistence comes from [[Mem0]]'s backing store, not from the agent object's lifetime.

## Connections

- **[[DSPy]]** — entity. The tutorial extends [[DSPy]] with the canonical memory-enabled agent receipt. Adds to the tutorial-stack table at the *long-term-memory* rung.
- **[[Mem0]]** — entity (newly minted). The persistent-memory layer this tutorial integrates with. First wiki receipt of [[Mem0]].
- **[[react|ReAct]]** — concept. The tutorial is a worked example of [[react|`dspy.ReAct`]] where the tool list is a memory CRUD surface. Direct extension of the [[dspy-customer-service-agent|customer-service agent's]] tool-list-as-action-surface pattern.
- **[[LongTermMemory|Long-Term Memory]]** — concept. The tutorial operationalizes [[LongTermMemory]] as defined in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] — external persistent store the LM reads via retrieval, written across sessions. [[Mem0]] is the concrete implementation; the tutorial is the DSPy wiring receipt.
- **[[DSPyModules]]** — concept. The `MemoryReActAgent(dspy.Module)` pattern: a thin subclass whose `forward` dispatches to a single `dspy.ReAct`. The receipt for *"compose `dspy.ReAct` inside a custom Module"* from [[DSPyModules]].
- **[[DSPyTools]]** — concept. Operationalizes the *"tools are plain Python callables"* discipline for **bound methods** of a tool class — extends the [[dspy-customer-service-agent]] receipt (which used free functions) to method-bound tools sharing a constructor-injected `Memory` instance.
- **[[DSPySignatures]]** — concept. Two-field Signature (`user_input` → `response`) where the **docstring carries the agent's persistence policy**. Same shape as [[dspy-customer-service-agent]]'s `user_request` → `process_result`.
- **[[DSPyProgrammingModel]]** — concept. The tutorial stops at the *Programming* rung — no [[DSPyMetrics|metric]], no [[DSPyEvaluation|eval set]], no [[MIPROv2|optimizer]] run. Like [[dspy-conversation-history]] and [[dspy-ai-text-game-tutorial]], this is one of the deliberately-non-optimized DSPy tutorials.
- **[[Agent]]** — concept. Memory-enabled agent is a canonical agent capability extension; the tutorial demonstrates the minimal wiring.
- **[[AgenticRAG]]** — concept. Adjacent pattern: where [[AgenticRAG]] retrieves from a document store, this agent retrieves from a **personalized memory store**. Both share the *retrieval-as-tool* discipline.
- **[[ConversationBufferMemory]]** — concept. Counter-positioning: the [[LangChainAgent|LangChain]] in-process memory pattern keeps full transcript in a Python buffer; [[Mem0]] keeps **extracted memories** in an external vector store. Mem0's internal extraction LM decides what to keep — buffer-style memory keeps everything.
- **[[ConversationSummaryMemory]]** — concept. Closer comparison: summary memory compresses transcript into running summary; Mem0 extracts discrete factual memories. Both lose information vs full transcript, but Mem0's memories are individually addressable for retrieval.
- **[[LongTermMemory]]** vs **[[ShortTermMemory]]** vs **[[InternalKnowledgeMemory]]** — concepts. [[Mem0]] sits squarely in [[LongTermMemory]]: external, cross-session, mutable without retraining.
- **[[openai]]** — entity. The tutorial uses `gpt-4o-mini` for both the agent LM and the [[Mem0]] internal extraction LM, and `text-embedding-3-small` for the embedder. Both [[OpenAI]] models.
- **[[VectorDatabase|Vector Database]]** — concept. [[Mem0]] uses a vector store under the hood for memory similarity search; the embedder config (`text-embedding-3-small`) is the substrate for the vector index.
- **[[LiteLLM]]** — entity. `dspy.LM("openai/gpt-4o-mini")` routes through [[LiteLLM]] for provider-agnostic LM dispatch.
- **[[2604.25850-agentic-harness-engineering]]** — paper. Strong counter-positioning: the AHE paper argues that **tools + middleware + long-term memory** (not prompt optimization) are the load-bearing layers of an agent harness. This tutorial is a concrete DSPy receipt of an agent built on the *long-term-memory* leg of that triad — DSPy is the orchestration glue, Mem0 is the long-term-memory substrate.
- **[[2407.10930-better-together]]** — paper. The natural optimization extension surface: a [[Mem0]]-enabled agent could be optimized over $\langle \Pi, \Theta \rangle$ — prompts AND the Mem0 extraction LM weights — using the *Better Together* recipe. The tutorial does not pursue this.

## Contradictions

None with existing wiki content. The tutorial **complements** prior memory-related pages:

- The [[LongTermMemory|Long-Term Memory]] page (sourced from [[ai-engineering-ch06-rag-agents]]) defined the *what*; this tutorial supplies the *how* — the concrete API shape ([[Mem0]]) and orchestration shape ([[DSPy]] + [[react|ReAct]] + tool list) that the *AI Engineering* chapter describes only in the abstract.
- The [[dspy-customer-service-agent]] tutorial's *seven-tool ReAct agent* over a typed domain is structurally mirrored here as a *seven-tool ReAct agent* over a memory CRUD + preference-helper surface. Both share the `max_iters=6` budget and the two-field-Signature shape.
- The deliberately-non-optimized scoping mirrors [[dspy-conversation-history]] and [[dspy-ai-text-game-tutorial]] — three of nine DSPy tutorials now deliberately stop at the *Programming* rung, demonstrating Module-composition value without the [[MIPROv2|optimizer]] step.

## Scope Limits

The tutorial is deliberately demonstrative. **Out of scope** (the tutorial does not address):

- **Optimization** — no [[BootstrapFewShot]] / [[MIPROv2]] / [[GEPA]] receipt. The agent is hand-written; no metric, no training set, no optimizer run.
- **Persistent storage backend** — the tutorial uses [[Mem0]]'s default in-memory backend; persistence across process restarts requires configuring a backing store (Qdrant, Chroma, pgvector, etc.). Explicitly listed in the *Advanced Recommendations* section as a follow-on.
- **Multi-user isolation under load** — the API supports `user_id` from the first call, but the tutorial only demonstrates a single `"default_user"`. Multi-tenant production would need user-auth boundaries, per-user rate limiting, and isolation guarantees [[Mem0]]'s default config doesn't supply.
- **Memory expiration / lifecycle** — no TTL on stored memories, no compaction, no archival. Listed as a follow-on (*"Create expiration rules for memory lifecycle management"*).
- **Memory categorization / tagging** — Mem0 internally extracts factual claims but the tutorial doesn't surface a tag schema. The `set_reminder` / `update_preferences` helpers prepend a `"REMINDER:"` / `"User preference for {category}:"` prefix to fake categorical lookup, but this is string-matching, not a real tag index.
- **Conflict resolution** — if the user contradicts a stored memory (*"I'm now vegetarian, scratch the carbonara"*), the agent has no explicit update-vs-add discrimination. The `update_memory(memory_id, new_content)` tool exists but is not in the agent's `tools=[...]` list.
- **Cost accounting** — no `dspy.LM.history` cost tracking, no measurement of the Mem0 internal extraction LM's token cost (which is hidden behind `Memory.add`).
- **Comparison with [[DSPyHistory|`dspy.History`]]** — the tutorial doesn't position [[Mem0]] against [[DSPyHistory|`dspy.History`]] (the [[dspy-conversation-history|conversation-history]] in-process buffer pattern); the design choice between extracted-memories (Mem0) vs full-transcript (`dspy.History`) is left implicit.
- **Tool-failure handling** — every tool wraps Mem0 calls in `try/except` and returns a string error; no retry, no fallback, no escalation. Production memory layers need graceful degradation when the vector store is unreachable.

## Position in the DSPy Application Stack

The Mem0-ReAct tutorial is the **ninth wiki-corpus DSPy tutorial** and the **first whole-system worked example of a memory-enabled agent over an external persistent store**. It slots one rung above [[dspy-customer-service-agent]] on the DSPy application stack:

| Rung | Pattern | Wiki anchor |
|---|---|---|
| 1. Single LM call | [[DSPyPredict|`dspy.Predict`]] | [[dspy-modules]] |
| 2. Single LM-program call | [[DSPyModules|`dspy.Module`]] subclass | [[dspy-modules]] |
| 3. Multi-turn conversation (in-process) | [[DSPyHistory|`dspy.History`]] + Python loop | [[dspy-conversation-history]] |
| 4. Single-agent multi-tool task | [[react|`dspy.ReAct`]] + typed tool list | [[dspy-customer-service-agent]] |
| 5. **Single-agent multi-tool + external memory** | **[[react|`dspy.ReAct`]] + [[Mem0]] CRUD tools** | **this tutorial** |
| 6. Creative-systems Module composition | Three-sub-CoT [[DSPyModules|Module]] | [[dspy-ai-text-game-tutorial]] |
| 7. RAG + optimization | [[react|ReAct]] + [[MIPROv2]] | [[dspy-tutorial-rag-as-agent]] / [[dspy-rag-tutorial]] |
| 8. Symbolic reasoning + optimization | [[chainofthought|CoT]] + [[MIPROv2]] | [[dspy-tutorial-math]] |
| 9. Multi-agent collaborative discourse | Custom multi-Module orchestration | [[2408.15232-co-storm]] |
| 10. Long-horizon RL'd compound system | [[grpo|GRPO]] / [[GEPA]] over $\langle \Pi, \Theta \rangle$ | [[2407.10930-better-together]] / [[2507.19457-gepa]] |

Rung 5 is the **natural composition** of rung 4 (single-agent multi-tool) with [[LongTermMemory|long-term memory]] (rung-2-of-the-three-tier-memory-model from [[ai-engineering-ch06-rag-agents]]) — the agent's action surface gains memory CRUD as a first-class capability. The Alice-persona demo is the **personalization shape** every consumer chatbot eventually needs and that vanilla [[react|`dspy.ReAct`]] cannot supply on its own (without external storage).
