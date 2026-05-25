---
title: "DSPy Tutorial — Managing Conversation History"
type: source
tags: [dspy, tutorial, conversation-history, chatbot, signatures, few-shot]
date: 2026-05-22
source_file: raw/dspy-conversation-history.md
---

## Summary

The [[DSPy]] **Managing Conversation History** tutorial ([dspy.ai/tutorials/conversation_history](https://dspy.ai/tutorials/conversation_history/)) is the canonical source for **how [[DSPy]] supports multi-turn conversational applications** — chatbots, dialogue agents, and any LM program where the model must condition on prior turns. The tutorial's load-bearing disclosure: ***DSPy does not automate conversation-history management.*** Automatic management is **not** built into [[DSPyModules|`dspy.Module`]] — the developer owns the history-instance lifecycle. DSPy supplies one primitive — the [[DSPyHistory|`dspy.History`]] [[DSPySignatures|Signature]] field type, with a `messages: list[dict[str, Any]]` attribute — and the developer threads it through two essential procedures: (1) include a `dspy.History` field in the Signature; (2) maintain a history instance at runtime, appending each conversation turn with all relevant input + output field data. The tutorial also discloses one structural property of [[DSPyHistory|`dspy.History`]] under [[BootstrapFewShot|few-shot]] demonstration: when a [[DSPyHistory|history-bearing]] [[DSPyExample|`dspy.Example`]] is added to a [[DSPyPredict|`dspy.Predict`]]'s `.demos`, the history is rendered **as a single turn with the history serialized as JSON** rather than expanded into multiple conversational turns — *"compatibility with the OpenAI standard format"*.

This tutorial is the **first wiki-corpus page to scope DSPy at the chatbot / multi-turn application layer**. Every prior [[DSPy]] page in the corpus has anchored to single-shot / pipeline-shaped programs (RAG, classification, agent harnesses with [[react|ReAct]] tools, [[CoSTORM|Co-STORM]] mind-map collaborative discourse, [[ArchEHRQA2025|ArchEHR-QA]] essentiality classification, [[MedVAL|MedVAL]] clinical-text validation). The Conversation History tutorial is the **chatbot-shaped counterpart** — the LM program is invoked repeatedly inside a `while True:` loop and the input-output pair from turn $t-1$ flows into turn $t$ as a [[DSPyHistory|history]] entry on the input side.

## Key Claims

- **DSPy does not automate conversation-history management.** *"Currently, DSPy does not provide such functionality out of the box, meaning users are required to manage the conversation history on their own"* — automatic management is not built into [[DSPyModules|`dspy.Module`]]. The developer owns the lifecycle of the history instance: construction, per-turn append, and re-injection on the next call.

- **`dspy.History` is the [[DSPySignatures|Signature]] field type for conversation history.** *"`dspy.History` ... contains a `messages: list[dict[str, Any]]` attribute"* — the same DSPy-special-type slot that [[DSPySignatures|Signatures]] expose for [[DSPyImage|`dspy.Image`]]. Each entry in `messages` is a dict of input and output field names → values for one prior turn. The dict shape mirrors the [[DSPySignatures|Signature]]'s I/O surface — the developer constructs each entry as `{"question": question, **outputs}` where `outputs` is the prior turn's [[DSPyPrediction|`dspy.Prediction`]].

- **Two essential procedures** apply to every conversation-history use case: (i) **include a `dspy.History` field in your Signature** — declared with `history: dspy.History = dspy.InputField()` alongside the task's other typed input fields; (ii) **maintain a history instance at runtime, appending each conversation turn** with all relevant input + output field data. The runtime pattern is `history.messages.append({"question": question, **outputs})` inside the conversation loop.

- **The canonical chatbot loop is a `while True:` with `predict(question=..., history=history)`.** The tutorial's first code receipt — a five-line interactive chatbot over `gpt-4o-mini` — demonstrates the **stateless-LM-call + stateful-history-instance** decomposition: the LM call itself doesn't know about prior turns (it sees them via the `history` input field), and the history instance lives in Python — neither DSPy nor the LM owns its persistence.

- **History in [[BootstrapFewShot|few-shot]] demonstrations is rendered as a single turn with JSON-serialized history**, **not** expanded into multiple conversational turns. *"DSPy renders the history as a single message in the few-shot examples to maintain compatibility with the OpenAI standard format"* — a [[DSPyExample|`dspy.Example`]] that carries a `history=dspy.History(messages=[...])` field is rendered as one user turn whose system / user content includes the history serialized as JSON inside a dedicated history section, rather than expanding the prior turns into separate `role=user` / `role=assistant` entries. This preserves the standard OpenAI `messages=[...]` shape under [[BootstrapFewShot|few-shot]] / [[BootstrapFewShotWithRandomSearch|BFRS]] / [[MIPROv2|MIPRO]] optimization where demos are part of the prompt envelope.

## Key Quotes

> *"DSPy provides `dspy.History` utility to help manage conversation history."* — opening line; positions [[DSPyHistory|`dspy.History`]] as **utility**, not framework-managed state.

> *"Currently, DSPy does not provide such functionality out of the box, meaning users are required to manage the conversation history on their own."* — load-bearing scope disclosure. The same posture as [[DSPyData|`dspy.Example`]]-level data handling ([[dspy-data|page 10]]): DSPy adds **exactly one** typed primitive at the conversation-history layer; lifecycle management is plain Python.

> *"Two important things need to be done in order to manage conversation history: 1. Include a `dspy.History` field in your `Signature`. 2. Maintain the conversation history in your code, and append the new conversation turn to the history with all related input fields and output field information."* — the canonical two-procedure recipe.

> *"DSPy renders the history as a single message in the few-shot examples to maintain compatibility with the OpenAI standard format."* — the structural disclosure for the [[BootstrapFewShot|few-shot]] / [[BootstrapFewShotWithRandomSearch|BFRS]] / [[MIPROv2|MIPRO]] interaction. Without this rendering choice, every history-bearing demo would balloon the prompt envelope by a factor of the conversation depth and break the OpenAI `messages=[...]` standard format that downstream provider routers (the [[LiteLLM]] layer underneath [[DSPyLM|`dspy.LM`]]) assume.

## Code Receipts

### Receipt 1 — Chatbot loop

```python
import dspy
import os

os.environ["OPENAI_API_KEY"] = "{your_openai_api_key}"

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

class QA(dspy.Signature):
    question: str = dspy.InputField()
    history: dspy.History = dspy.InputField()
    answer: str = dspy.OutputField()

predict = dspy.Predict(QA)
history = dspy.History(messages=[])

while True:
    question = input("Type your question, end conversation by typing 'finish': ")
    if question == "finish":
        break
    outputs = predict(question=question, history=history)
    print(f"\n{outputs.answer}\n")
    history.messages.append({"question": question, **outputs})

dspy.inspect_history()
```

Structural notes: (i) [[DSPyConfigure|`dspy.configure(lm=...)`]] is global — the same [[DSPyLM|`dspy.LM`]] instance services every turn; (ii) the `history.messages.append({"question": question, **outputs})` step is the **developer's responsibility** — DSPy does **not** automatically capture per-turn I/O into the history instance even though the [[DSPyLM|`dspy.LM`]] history (`lm.history`) layer captures every wire-level request/response separately; (iii) `dspy.inspect_history()` at the end shows the rendered prompts — useful for verifying the `[[ ## history ## ]]` field rendering the [[DSPyAdapters|`dspy.ChatAdapter`]] produces.

### Receipt 2 — Few-shot demo with history

```python
import dspy

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

class QA(dspy.Signature):
    question: str = dspy.InputField()
    history: dspy.History = dspy.InputField()
    answer: str = dspy.OutputField()

predict = dspy.Predict(QA)
history = dspy.History(messages=[])

predict.demos.append(
    dspy.Example(
        question="What is the capital of France?",
        history=dspy.History(
            messages=[{"question": "What is the capital of Germany?", "answer": "The capital of Germany is Berlin."}]
        ),
        answer="The capital of France is Paris.",
    )
)

predict(question="What is the capital of America?", history=dspy.History(messages=[]))
dspy.inspect_history()
```

Structural notes: (i) [[DSPyExample|`dspy.Example`]] carries a `history` field exactly the same way it carries any other [[DSPySignatures|Signature]]-typed field — [[DSPyHistory|`dspy.History`]] is a **first-class field type**, not a wrapper around `messages=[...]`; (ii) the `.demos.append(...)` mechanism is the same one [[BootstrapFewShot|`BootstrapFewShot`]] uses internally — manual demo construction is the no-optimizer baseline, [[BootstrapFewShot]] is the automated version; (iii) the runtime call `predict(question=..., history=dspy.History(messages=[]))` deliberately uses an **empty** history at inference even though the demo carries a populated one — demonstrating that demo-history and inference-history are independent fields, not a single shared conversation context.

## Connections

- **[[DSPy]]** — entity. The conversation-history tutorial extends the [[DSPy]] framework page with the chatbot-shaped application slice. Every prior DSPy ingest scoped single-shot or pipeline-shaped programs; this is the first to scope **multi-turn application state**.
- **[[DSPyHistory]]** — concept (newly minted). The `dspy.History` [[DSPySignatures|Signature]] field type with a `messages: list[dict[str, Any]]` attribute. The DSPy-special-type slot adjacent to [[DSPyImage|`dspy.Image`]] in [[dspy-signatures|the Signatures page]]'s five-tier type system.
- **[[ConversationHistory]]** — concept (newly minted). The general LM-application concept the [[DSPyHistory|DSPy primitive]] operationalizes.
- **[[DSPySignatures]]** — concept. [[DSPyHistory|`dspy.History`]] is the third DSPy-special-type the [[DSPySignatures|Signatures]] type-system page enumerates (after the basic Python / `typing` composites / pydantic models / dot-notation nested types tiers, alongside [[DSPyImage|`dspy.Image`]] in tier five).
- **[[DSPyModules]]** — concept. The tutorial's scope disclosure — *"DSPy does not provide such functionality out of the box"* — locates the gap precisely: [[DSPyModules|`dspy.Module`]] does not auto-manage conversation state. Multi-turn application state is plain Python around the [[DSPyModules|Module]], not inside it.
- **[[DSPyExample]]** — concept. The demo-with-history receipt demonstrates that [[DSPyHistory|`dspy.History`]] composes as a [[DSPyExample|`dspy.Example`]] field exactly the same way every other [[DSPySignatures|Signature]]-typed field does — `dspy.Example(question=..., history=..., answer=...)`.
- **[[DSPyPredict]]** — concept. The minimal-primitive that the chatbot loop drives. The tutorial uses bare [[DSPyPredict|`dspy.Predict`]] rather than [[ChainOfThought|`dspy.ChainOfThought`]] — the [[DSPyHistory|history-bearing]] pattern doesn't require [[ChainOfThought|CoT]].
- **[[DSPyAdapters]]** — concept. The [[DSPyAdapters|`dspy.ChatAdapter`]] is the layer that renders the [[DSPyHistory|history]] field into the LM's wire format — both as the conversation-history block at inference and as the JSON-serialized history in [[BootstrapFewShot|few-shot]] demos.
- **[[BootstrapFewShot]]** — concept. The few-shot-rendering disclosure scopes how [[DSPyHistory|`dspy.History`]] interacts with the [[BootstrapFewShot|automatic few-shot]] optimizer family. The single-turn JSON-serialized rendering keeps prompt envelopes bounded under demo budgets.
- **[[MIPROv2]]**, **[[BootstrapFewShotWithRandomSearch]]** — concepts. The same prompt-envelope discipline carries to instruction-and-demo optimizers — a history-bearing demo costs roughly the same prompt budget as a non-history demo.
- **[[chainofthought]]** — concept. The tutorial uses bare [[DSPyPredict|`dspy.Predict`]], not [[ChainOfThought|`dspy.ChainOfThought`]] — the pattern is module-agnostic; any [[DSPyModules|Module]] that accepts an arbitrary input [[DSPySignatures|Signature]] field accepts a `history: dspy.History` field.
- **[[LLMAsAJudge]]** — concept. Indirect connection: the [[DSPyEvaluation|metric]] for a conversational application is typically [[LLMAsAJudge|LLM-as-judge]] on the final answer with the history as context (the [[DSPyMetrics|metric]] inherits the history-field plumbing).
- **[[RAGChatbot]]** — concept. The wiki's prior chatbot reference (from [[2408.15232-co-storm|Co-STORM]]) — Co-STORM proposes a more elaborate chatbot architecture; the DSPy conversation-history tutorial provides the **building-block primitive** that any DSPy-implemented chatbot (including a RAG chatbot) would use to thread state across turns.
- **[[gpt-4o]]** — entity. The tutorial uses `openai/gpt-4o-mini` — the smaller [[gpt-4o]] family variant — as the demo LM.
- **[[LiteLLM]]** — entity. The `dspy.LM("openai/gpt-4o-mini")` model string is the [[LiteLLM]] convention the [[DSPyLM|`dspy.LM`]] client inherits; the OpenAI-standard-format `messages=[...]` shape the few-shot rendering preserves is the wire format [[LiteLLM]] expects.
- **[[ModelContextProtocol]]** — concept. Indirect: a [[ModelContextProtocol|MCP]]-tool-using chatbot threads conversation history through the same [[DSPyHistory|`dspy.History`]] field; the MCP integration ([[dspy-mcp]]) is orthogonal to the conversation-history layer.

## Contradictions

None with existing wiki content. The tutorial **complements** every prior DSPy page rather than contradicting any of them:

- [[DSPyData|Data handling page]] commits to *"DSPy adds exactly one class on the data layer"* — the conversation-history tutorial mirrors this discipline at the conversation-state layer (*"DSPy adds exactly one [[DSPySignatures|Signature]]-typed primitive at the conversation-history layer; lifecycle management is plain Python"*).
- [[DSPyModules|Modules page]]'s *"DSPy is just Python code that uses modules in any control flow you like"* commitment is **strengthened** by the chatbot-loop receipt — the conversation loop is plain Python around a [[DSPyPredict|`dspy.Predict`]], not a framework-provided abstraction.
- The few-shot-rendering disclosure is **new information** not contradicted by [[dspy-optimizers|the Optimizers page]] — the catalog of optimizers is silent on history-bearing demos; this tutorial supplies the missing structural detail.

## Scope Limits

The tutorial is deliberately narrow. **Out of scope** (the tutorial does not address):

- **History trimming / windowing** — no built-in mechanism for capping `messages` length; the developer owns truncation policy. The wiki's [[2604.27707-agentic-memory-is-a-memo|agentic-memory-is-a-memo]] paper argues that *"agentic memory"* is **lookup, not memory**, with a provable Ω(k²) generalization gap — this tutorial's `dspy.History` is the most literal instance of *lookup* memory in the [[DSPy]] framework, and inherits the limitation.
- **Persistence** — no built-in serialization of `dspy.History` to disk / DB. The developer pickles / JSON-dumps `history.messages` if persistence is needed.
- **Multi-user concurrency** — no built-in per-session history isolation. Each user / session needs its own `dspy.History` instance; threading discipline is the developer's responsibility.
- **System-prompt-vs-history demarcation** — the tutorial doesn't disclose what the [[DSPyAdapters|`dspy.ChatAdapter`]] renders the history field into at the wire level (system message + structured `[[ ## history ## ]]` block, or interleaved `role=user`/`role=assistant` messages). The disclosure that *few-shot demos* render history as JSON-in-a-single-turn implies that **inference-time** rendering also uses a JSON-style structured block within a single user message rather than expanding to multi-turn — but this is inference from the few-shot disclosure, not directly stated.
- **Token-budget-aware history compression** — no built-in summarize-then-truncate. The `messages` list grows unboundedly unless the developer trims.
- **Tool-use trajectories as history** — [[react|`dspy.ReAct`]] internally tracks a `trajectory` of think-act-observe steps; the relationship between [[react|ReAct's]] `trajectory` and [[DSPyHistory|`dspy.History`]] is not addressed. (Inference: they are orthogonal — `trajectory` is a single-call internal log inside one [[react|ReAct]] [[DSPyPredict|Predict]] invocation; `history` is the cross-call inter-turn log.)

These scope limits define the **expansion surface** for future wiki ingests of related DSPy tutorials (Stop-Words, Streaming, Saving and Loading) that may resolve some of them.

## Position in the DSPy Application Stack

The Conversation History tutorial is the **first tutorial-anchored** DSPy page in the wiki — every prior DSPy ingest has been a *Learn*-section reference page or a paper. This shifts the [[DSPy]] entity's footprint from **framework documentation + research-paper applications** to also include **how-to-build-X tutorials**.

The application slice the tutorial occupies — **multi-turn chatbot state management** — sits between two prior wiki anchors:

| Layer | DSPy primitive | Wiki anchor |
|---|---|---|
| Single LM call | [[DSPyPredict|`dspy.Predict`]] | [[dspy-modules]] |
| Single LM-program call | [[DSPyModules|`dspy.Module`]] subclass | [[dspy-modules]] |
| **Multi-turn conversation** | [[DSPyHistory|`dspy.History`]] in a Signature + Python loop | **this tutorial** |
| Multi-agent collaborative discourse | Custom multi-Module orchestration | [[2408.15232-co-storm|Co-STORM]] |
| Long-horizon RL'd agentic system | [[grpo|GRPO]] / [[GEPA]] over a [[CompoundAISystem|compound system]] | [[2407.10930-better-together]] / [[2507.19457-gepa]] |

The tutorial fills the missing **single-agent multi-turn** rung between the single-call rung and the multi-agent rung — completing the DSPy application-stack ladder from one LM call up to a collaborative-discourse mind-map system.
