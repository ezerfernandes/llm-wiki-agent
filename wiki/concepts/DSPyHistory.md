---
title: "DSPyHistory"
type: concept
tags: [dspy, conversation-history, signatures, chatbot, special-type]
sources: [dspy-conversation-history, dspy-signatures]
last_updated: 2026-05-24
---

# DSPyHistory (`dspy.History`)

**`dspy.History`** is [[DSPy]]'s [[DSPySignatures|Signature]] field type for **conversation history**. It is one of the **DSPy-special types** (tier five in the [[DSPySignatures|Signatures type system]], alongside [[DSPyImage|`dspy.Image`]]) — types the framework has dedicated wire-format rendering for, beyond basic Python / `typing` composites / pydantic models / dot-notation nested types.

## Definition

`dspy.History` is a class with a single load-bearing attribute:

```python
class dspy.History:
    messages: list[dict[str, Any]]
```

Each entry in `messages` is a dict carrying **all input and output field values for one prior conversation turn** — keyed by the [[DSPySignatures|Signature]]'s input and output field names. The dict shape mirrors the Signature's I/O surface, not the OpenAI `{"role": ..., "content": ...}` shape; the [[DSPyAdapters|`dspy.ChatAdapter`]] performs the translation between the DSPy-typed shape and the LM's wire shape.

## Canonical usage

Declared on a [[DSPySignatures|Signature]] like any other typed input field:

```python
class QA(dspy.Signature):
    question: str = dspy.InputField()
    history: dspy.History = dspy.InputField()
    answer: str = dspy.OutputField()
```

Instantiated at runtime as an **empty** history that the developer threads through the loop:

```python
history = dspy.History(messages=[])

while True:
    question = input("...")
    outputs = predict(question=question, history=history)
    history.messages.append({"question": question, **outputs})
```

The `{"question": question, **outputs}` append pattern is the **canonical per-turn shape**: it spreads the [[DSPyPrediction|`dspy.Prediction`]]'s output fields into the same dict as the input fields, producing a unified per-turn record.

## Three structural properties

### 1. Developer-owned lifecycle

**[[DSPy]] does not automate the history-instance lifecycle.** [[DSPyModules|`dspy.Module`]] has no built-in conversation-history capture — the developer constructs the `dspy.History` instance, appends to it after each turn, and re-passes it on the next call. Per the [[dspy-conversation-history|tutorial]]: *"DSPy does not provide such functionality out of the box, meaning users are required to manage the conversation history on their own."* This is the same posture [[DSPy]] takes on data handling ([[DSPyData|datasets are plain Python lists]]) — the framework adds **exactly one** typed primitive at the conversation-history layer; everything else is plain Python.

### 2. First-class field type

`dspy.History` composes through every [[DSPy]] mechanism that accepts an arbitrary Signature-typed field — [[DSPyPredict|`dspy.Predict`]], [[ChainOfThought|`dspy.ChainOfThought`]], [[react|`dspy.ReAct`]], custom [[DSPyModules|Module]] subclasses, [[DSPyExample|`dspy.Example`]] demo construction, [[DSPyEvaluate|`dspy.Evaluate`]] dev-set passes, [[DSPyOptimizers|Optimizer]] inputs. It is **not** a wrapper around a `messages=[...]` parameter — it is a typed Signature field that the [[DSPyAdapters|Adapter]] layer recognizes and renders.

### 3. Single-turn JSON rendering in few-shot demos

When a [[DSPyHistory|history-bearing]] [[DSPyExample|`dspy.Example`]] is added to a [[DSPyPredict|`dspy.Predict`]]'s `.demos` (manually or via [[BootstrapFewShot|`BootstrapFewShot`]] / [[BootstrapFewShotWithRandomSearch|BFRS]] / [[MIPROv2|MIPRO]]), the history is rendered **as a single demo turn with the messages serialized as JSON** rather than expanded into multiple `role=user` / `role=assistant` turns. Per the tutorial: *"DSPy renders the history as a single message in the few-shot examples to maintain compatibility with the OpenAI standard format."*

This rendering choice has three structural consequences:

- **Prompt envelopes stay bounded** under demo budgets — a 5-turn history doesn't 5× the demo's prompt cost.
- **The OpenAI `messages=[...]` standard format is preserved** — the [[LiteLLM]] layer underneath [[DSPyLM|`dspy.LM`]] continues to work without per-provider special-casing.
- **Demo-history and inference-history are independent** — a demo can carry a populated history while inference is called with `history=dspy.History(messages=[])`, and vice versa.

## Code receipt — chatbot loop

The [[dspy-conversation-history|tutorial]] supplies the canonical five-line interactive chatbot:

```python
import dspy

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

## Code receipt — few-shot demo with history

```python
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
```

The demo carries a one-turn history; inference is called with an empty history. The [[DSPyAdapters|`dspy.ChatAdapter`]] renders the demo's history as a JSON-serialized block inside a single demo turn.

## Position in the DSPy type system

The [[DSPySignatures|Signatures]] page's five-tier type system places `dspy.History` in tier five (DSPy-special types):

| Tier | Types |
|---|---|
| 1. Basic Python | `int`, `str`, `bool`, `float`, `list[T]`, `dict[K, V]` |
| 2. `typing` composites | `Optional[T]`, `Union[A, B]`, `Literal["a", "b"]` |
| 3. pydantic models | Any `BaseModel` subclass |
| 4. Dot-notation nested types | `parent.child: int` |
| 5. **DSPy-special types** | [[DSPyImage|`dspy.Image`]], **`dspy.History`** |

Both tier-five types share the property that the [[DSPyAdapters|Adapter]] layer has **dedicated wire-format rendering** for them — [[DSPyImage|`dspy.Image`]] for multi-modal input encoding, `dspy.History` for conversation-history rendering. Future DSPy-special types (the wire is open) would slot into the same tier.

## Scope limits

The `dspy.History` primitive is deliberately minimal. **Out of scope** at the primitive level (developer-managed):

- **History trimming / windowing** — no built-in cap on `messages` length.
- **Persistence** — no built-in serialization to disk / DB.
- **Multi-user concurrency** — no built-in per-session isolation.
- **Token-budget compression** — no built-in summarize-then-truncate.

These align with the broader [[DSPy]] discipline of *"DSPy is just Python code"* — application-level concerns are plain Python around the framework primitives, not framework-provided abstractions.

## Relationship to other history-like primitives

- **[[react|`dspy.ReAct`]] `trajectory`** — internal log of think-act-observe steps **within one** [[DSPyPredict|`dspy.Predict`]] invocation. Orthogonal to `dspy.History` — `trajectory` is intra-call, `history` is inter-call.
- **[[DSPyLM|`dspy.LM.history`]]** — per-call wire-level request/response telemetry the [[DSPyLM|`dspy.LM`]] client captures. Different layer — `lm.history` is for inspection and [[DSPyOptimizers|Optimizer]] replay; `dspy.History` is a [[DSPySignatures|Signature]] field for conditioning the model on prior turns. They are unrelated despite the shared word.
- **[[2604.27707-agentic-memory-is-a-memo|"Agentic memory"]] (CUHK/Zhejiang)** — the paper argues *"agentic memory"* is **lookup, not memory**, with a provable Ω(k²) generalization gap. `dspy.History` is the most literal instance of *lookup* memory in DSPy — a flat append-only list re-fed verbatim into the prompt — and inherits the limitation directly.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-conversation-history]] — canonical receipt: the five-line chatbot loop with `history = dspy.History(messages=[])` and the `history.messages.append({"question": question, **outputs})` per-turn append pattern; plus the few-shot-demo JSON rendering disclosure.
- [[dspy-custom-module]] — names `[[DSPyHistory|history]] threading` as one of the internal-processing concerns the `__call__` entry point handles (alongside optimizer tracing and MLflow logging), motivating `module(...)` over explicit `module.forward(...)`.
- [[dspy-customer-service-agent]] — single-turn [[react|`dspy.ReAct`]] agent that explicitly *does not* use `dspy.History`; tutorial documents `dspy.History` + Python loop as the canonical multi-turn extension for the same agent shape.
- [[dspy-email-extraction-tutorial]] — strictly sequential five-step pipeline with *"no [[react|ReAct]] loop, no `dspy.History` thread"*; tutorial slots `dspy.History` as the multi-turn extension axis.
- [[dspy-entity-extraction-tutorial]] — same posture as email extraction: no history in the worked NER receipt; `dspy.History` named as the multi-turn extension path.
- [[dspy-mem0-react-tutorial]] — positions an external [[VectorDatabase|vector-DB]]-backed [[Mem0]] store as the **persistence-surviving** alternative to the in-process `dspy.History` buffer; the implicit *extracted-memories vs full-transcript* design choice.
- [[dspy-streaming-tutorial]] — surfaces `dspy.History` as the DSPy-special type that is explicitly **not streamable** under the `str`-only constraint (`messages: list[dict[str, Any]]` has no incremental-render shape).
- [[dspy-tutorial-math]] — uses `dspy.inspect_history()` (the global recent-call print buffer — distinct surface from `dspy.History` despite the shared word) as the post-optimization prompt-inspection surface on the optimized [[chainofthought|`dspy.ChainOfThought`]] program.

## Tracked sources

- **[[dspy-conversation-history]]** (2026-05-22) — canonical tutorial source. Defines the two essential procedures, the chatbot-loop pattern, and the few-shot JSON-rendering disclosure.
- **[[dspy-signatures]]** (2026-05-17) — placement in tier five of the five-tier type system alongside [[DSPyImage|`dspy.Image`]].
