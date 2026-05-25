---
title: "ConversationHistory"
type: concept
tags: [llm, chatbot, conversation, state, dialogue]
sources: [dspy-conversation-history, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

# Conversation History

**Conversation history** is the **inter-turn state** of a multi-turn LM application — the sequence of prior `(input, output)` pairs the model must condition on to maintain coherence across turns. In chatbots, dialogue agents, and any LM program where a turn at time $t$ depends on turns $1..t-1$, conversation history is the **primary state variable** the application threads through every LM call.

## The structural problem

A bare LM call is **stateless** — the model sees only what is in the current prompt envelope. Multi-turn coherence therefore requires the **application** (not the LM, not the framework) to:

1. **Capture** each turn's relevant input and output fields.
2. **Persist** them across calls (in-memory at minimum; pickled / DB-backed for longer-lived sessions).
3. **Re-inject** the relevant history into the next call's prompt envelope.

This is a state-management problem the application owns. The LM-programming framework can supply (a) a typed primitive for the history, (b) wire-format rendering of that primitive, and (c) compatibility with the framework's other layers (demos, optimizers, evaluators). It cannot supply the lifecycle — when to construct a history, when to append, when to truncate, when to persist, when to discard — because those are application-policy decisions, not framework-substrate ones.

## DSPy's operationalization

[[DSPy]] supplies exactly one typed primitive at this layer: [[DSPyHistory|`dspy.History`]] — a [[DSPySignatures|Signature]] field type with a `messages: list[dict[str, Any]]` attribute. The application:

- declares `history: dspy.History = dspy.InputField()` on the [[DSPySignatures|Signature]];
- instantiates `history = dspy.History(messages=[])` at session start;
- threads `predict(..., history=history)` through every turn;
- appends `history.messages.append({"input_field": value, **outputs})` after each turn.

DSPy does **not** supply: history trimming, persistence, multi-session isolation, or token-budget-aware compression. Per the [[dspy-conversation-history|tutorial]]: *"DSPy does not provide such functionality out of the box, meaning users are required to manage the conversation history on their own."*

Full primitive detail on the [[DSPyHistory]] concept page.

## Few-shot rendering: a structural choice

When conversation history appears in [[BootstrapFewShot|few-shot]] demonstrations, two rendering strategies are conceivable:

| Strategy | Rendering | Trade-off |
|---|---|---|
| **Expanded** | Each prior turn becomes a separate `role=user` / `role=assistant` pair in the demo. | Faithful to the conversational structure; **balloons prompt envelopes** by a factor of conversation depth; breaks the OpenAI standard format that downstream provider routers expect. |
| **Single-turn JSON** | The entire `messages` list is serialized as JSON inside a single demo turn. | Compact prompt envelopes; preserves the OpenAI `messages=[...]` standard format; **loses the conversational role-cue structure** the LM might condition on. |

**DSPy chooses single-turn JSON.** Per the tutorial: *"DSPy renders the history as a single message in the few-shot examples to maintain compatibility with the OpenAI standard format."* The trade-off is consciously made: the prompt-budget and provider-compatibility wins outweigh the loss of role-cue structure, particularly because [[BootstrapFewShot|few-shot]] / [[BootstrapFewShotWithRandomSearch|BFRS]] / [[MIPROv2|MIPRO]] optimizers explore many demo combinations and an expanded rendering would compound the budget cost.

This is a load-bearing structural choice — every history-bearing DSPy demo, optimized or hand-written, inherits it.

## Related primitives in the LM-programming landscape

- **OpenAI `messages=[...]`** — the **wire-level** conversation format every modern provider speaks. Pairs of `{"role": ..., "content": ...}` dicts; the format both [[LiteLLM]] and [[DSPyAdapters|`dspy.ChatAdapter`]] target.
- **[[react|ReAct]] `trajectory`** — an **intra-call** log of think-act-observe steps inside a single tool-using LM invocation. Different layer — `trajectory` is for one [[DSPyPredict|Predict]] call's internal scratchpad; conversation history is for **inter-call** application state.
- **[[DSPyLM|`dspy.LM.history`]]** — the [[DSPyLM|`dspy.LM`]] client's per-call wire-level telemetry log. Different layer — for inspection and [[DSPyOptimizers|Optimizer]] replay, not for conditioning future calls.
- **System prompts** — static instructions distinct from turn-specific history. The [[DSPyAdapters|Adapter]] separates them; the conversation-history field is **input data** not framework configuration.
- **[[CoSTORM|Co-STORM]] mind map** — a more elaborate **graph-shaped** conversation-state representation for collaborative discourse (multi-expert + moderator). The flat-list `dspy.History` is the simpler counterpart for single-agent chatbots.

## The agentic-memory tension

[[2604.27707-agentic-memory-is-a-memo|Wang et al. (2026, CUHK/Zhejiang)]] argue that *"agentic memory"* in LM systems is **lookup, not memory** — with a provable Ω(k²) generalization gap and a persistent prompt-injection compromise vulnerability. Conversation history as implemented in [[DSPyHistory|`dspy.History`]] is the most literal instance of *lookup* memory in [[DSPy]]: a flat append-only list re-fed verbatim into the prompt at each turn, with no compression, summarization, retrieval, or selective recall.

Under the [[2604.27707-agentic-memory-is-a-memo|agentic-memory-is-a-memo]] critique:
- The Ω(k²) generalization gap applies — a `k`-turn history grows the prompt envelope linearly but the implicit cross-turn dependency graph grows quadratically.
- The prompt-injection vulnerability applies — every prior turn's content is replayed verbatim, so a malicious turn can persistently steer future turns.

Both limitations are **inherent to the lookup-memory framing**, not specific to [[DSPyHistory|`dspy.History`]]. Resolving them requires moving from lookup memory to a more structured representation — a [[CoSTORMMindMap|mind map]] (Co-STORM), a retrieval-augmented memory ([[rag|RAG]] over prior turns), or a summarization-then-trim policy. Each is an **application-level** policy the developer implements around the `dspy.History` primitive.

## Pedagogical position

Conversation history is the **chatbot rung** of the LM-application complexity ladder:

| Rung | State shape | Wiki anchor |
|---|---|---|
| 1. Single LM call | Stateless | [[DSPyPredict]] |
| 2. Single LM-program call | Module-local state | [[DSPyModules]] |
| 3. **Multi-turn conversation** | Flat append-only history | **this concept** + [[DSPyHistory]] |
| 4. Tool-using agent | Per-call trajectory | [[react]] |
| 5. Multi-agent collaborative discourse | Graph (mind map) | [[CoSTORM]] |
| 6. Long-horizon RL'd compound system | [[CompoundAISystem]] $\langle \Pi, \Theta \rangle$ | [[2407.10930-better-together]] / [[2507.19457-gepa]] |

Rung 3 is the **building block** for rung 5 — a Co-STORM expert agent threads conversation history through its own internal LM calls before contributing to the cross-agent mind map.

## LangChain's three-class operationalization (Ch 7)

Where [[DSPy]] supplies the single `dspy.History` primitive and leaves lifecycle policy to the application, [[LangChain]] (per [[hands-on-llm-ch07-advanced-text-generation|*Hands-On LLMs* Ch 7]]) supplies **three pre-built lifecycle policies** as memory classes:

| LangChain class | Lifecycle policy | Token cost | Information loss |
|---|---|---|---|
| **`ConversationBufferMemory`** | Append-only; nothing dropped | Linear in conversation length | None within context window |
| **`ConversationBufferWindowMemory(k=2)`** | [[FIFOMemory|FIFO eviction]] beyond last `k` turns | Bounded (k turns) | Anything older than last `k` turns dropped |
| **`ConversationSummaryMemory`** | Running LLM-summary replaces history | Bounded (one summary) but +1 LLM call per turn | Specifics lost to gist; quality depends on summarizer |

This is the **framework-policies-built-in** end of the spectrum vs the **framework-provides-primitive-only** end ([[DSPy]]'s [[DSPyHistory|`dspy.History`]]). Both shapes are defensible:
- LangChain's defaults make chat applications easy to bootstrap; the trade-off is **opaque defaults** — *"under the hood, LangChain saves it as an interaction between you (indicated with Human) and the LLM (indicated with AI)"* — which the developer didn't choose.
- DSPy's plain list makes lifecycle explicit at the application layer; the trade-off is **boilerplate** — *"users are required to manage the conversation history on their own"*.

The wiki's two operationalizations of rung 3 (chatbot) are LangChain's class-per-policy and DSPy's primitive-plus-application-policy — Ch 7 + [[dspy-conversation-history]] is the right cross-reference.

## Stateless-LLM framing (Ch 7)

Ch 7's framing of the underlying problem is sharper than [[dspy-conversation-history]]'s: *"When we are using LLMs out of the box, they will not remember what was being said in a conversation. You can share your name in one prompt but it will have forgotten it by the next prompt. ... these models are stateless — they have no memory of any previous conversation!"* The chapter demonstrates statelessness with a two-call probe:

1. *"Hi! My name is Maarten. What is 1 + 1?"* — answered correctly with name acknowledgment.
2. *"What is my name?"* — *"I'm sorry, but as a language model, I don't have the ability to know personal information about individuals."*

This is the **canonical probe for testing whether a chatbot has memory at all** — the "identity-retention test." Ch 7 runs the same probe across all three memory types (`ConversationBufferMemory` passes; `ConversationBufferWindowMemory(k=2)` passes for name but fails for age that was stated alongside; `ConversationSummaryMemory` passes via the summary's *"Human, identified as Maarten"* note).
