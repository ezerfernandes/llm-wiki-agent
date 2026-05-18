---
title: "DSPy Signatures"
type: concept
tags: [dspy, llm-programming, signatures, typed-io, declarative-spec, framework]
sources: [dspy-signatures, dspy-programming-overview, dspy-language-models, dspy-learn-index]
last_updated: 2026-05-17
---

# DSPy Signatures

**A DSPy Signature is a *declarative specification of input/output behavior of a DSPy module*** — the typed-interface artifact that defines *what* an LM call's inputs and outputs are, **without** specifying *how* the LM should be prompted to produce them. Signatures are the first and most user-facing of the four orthogonal axes [[DSPyProgrammingModel|the DSPy Programming Model]] factors out of a conventional prompt (alongside [[DSPyAdapters|Adapters]], [[DSPyModules|Modules]], and [[DSPyOptimizers|Optimizers]]) — and the **stable interface** the other three artifacts compose against. This concept page records the abstraction itself; [[dspy-signatures|the Signatures page]] (page 4 of 13 of the DSPy *Learn* documentation) is the canonical source.

## What a Signature *is*

The page's one-line definition is load-bearing:

> "A signature is a declarative specification of input/output behavior of a DSPy module. Signatures enable you to communicate *what* needs to happen rather than *how* to prompt the model."

Three properties are non-obvious:

1. **It's runtime, not documentation.** Unlike a Python function signature, a `dspy.Signature` is a **program object** the framework reads at run time — to build messages, parse responses into typed outputs, and (later) drive [[DSPyOptimizers|Optimizer]] search.
2. **Field *names* are semantic.** *"A `question` differs fundamentally from an `answer`."* The names of the input and output fields appear in the prompt the framework generates; they are not decorative. The page's discipline is *"field names should be semantically meaningful but kept simple initially."*
3. **It's the *stable interface*.** The Signature is the artifact that survives [[DSPyModules|Module]] swaps (`dspy.Predict` → `dspy.ChainOfThought` → `dspy.ReAct`), [[DSPyAdapters|Adapter]] swaps, and [[DSPyLM|LM]] swaps. The other three axes change around the Signature; the Signature itself does not.

## Two surface forms — equivalent in mechanism, different in capacity

### Inline (string) form

A short Python string `"<inputs> -> <outputs>"`, optionally with `: type` annotations:

```python
dspy.Predict('sentence -> sentiment: bool')                       # bool output
dspy.Predict('document -> summary')                                # str default
dspy.Predict('context: list[str], question: str -> answer: str')  # RAG QA
dspy.Predict('question, choices: list[str] -> reasoning: str, selection: int')
```

Unannotated fields default to `str`. `"question -> answer"` is **equivalent to** `"question: str -> answer: str"`. Multiple inputs and outputs are comma-separated. The inline form is the **prototyping default** — the form [[dspy-language-models|the Language Models page]] uses in its `dspy.ChainOfThought('question -> answer')` opener and the form the closing sentence of [[dspy-programming-overview|the Programming Overview's]] *start-simple* discipline implies.

A top-level task description can be attached via the `instructions=` kwarg on `dspy.Signature(...)`:

```python
toxicity = dspy.Predict(
    dspy.Signature(
        "comment -> toxic: bool",
        instructions="Mark as 'toxic' if the comment includes insults, harassment, or sarcastic derogatory remarks.",
    )
)
```

### Class-based form

A `dspy.Signature` subclass whose **docstring is the task description**, whose **fields are typed attributes** annotated `dspy.InputField()` or `dspy.OutputField()`, and whose `desc=` kwarg supplies per-field hints:

```python
from typing import Literal

class Emotion(dspy.Signature):
    """Classify emotion."""

    sentence: str = dspy.InputField()
    sentiment: Literal['sadness', 'joy', 'love', 'anger', 'fear', 'surprise'] = dspy.OutputField()
```

The class form is the right choice when *any* of three conditions hold (the page's explicit checklist):

1. **Task nature needs clarification via docstring.**
2. **Input fields need hints** — `dspy.InputField(desc="facts here are assumed to be true")`.
3. **Output fields need constraints** — `dspy.OutputField(desc="Supporting evidence for claims")`.

The two forms are **equivalent in wire-level mechanism** — they produce the same calls to [[DSPyLM|`dspy.LM`]] through the same [[DSPyAdapters|Adapter]] — but the class form carries information the inline form cannot fit on one line.

## The type system

The page enumerates the type tiers `dspy.Signature` understands after each `:`:

| Tier | Examples |
|---|---|
| **Basic Python types** | `str`, `int`, `bool` |
| **`typing` composites** | `list[str]`, `dict[str, int]`, `Optional[float]`, `Union[str, int]` |
| **Custom pydantic models** | `class QueryResult(pydantic.BaseModel): text: str; score: float` → `dspy.Signature("query: str -> result: QueryResult")` |
| **Nested types via dot notation** | `dspy.Signature("query: MyContainer.Query -> score: MyContainer.Score")` |
| **DSPy-special types** | `dspy.Image` (multi-modal input), `dspy.History` (conversational context) |

`dspy.Image` is the multi-modal-input primitive, paired with `dspy.Image.from_url(...)` at call time:

```python
class DogPictureSignature(dspy.Signature):
    """Output the dog breed of the dog in the image."""
    image_1: dspy.Image = dspy.InputField(desc="An image of a dog")
    answer: str = dspy.OutputField(desc="The dog breed of the dog in the image")

classify = dspy.Predict(DogPictureSignature)
classify(image_1=dspy.Image.from_url("https://picsum.photos/id/237/200/300"))
```

`typing.Literal[...]` is the **DSPy-idiomatic closed-set classification** primitive — no separate `Enum` or `Choice` is needed. The `Emotion` example above constrains the LM's output to one of six labels by virtue of the `Literal[...]` annotation alone.

### Type checking is warn-not-fail

Input field values are validated against their type annotations at call time:

```python
class MathSignature(dspy.Signature):
    """Perform a mathematical operation."""
    number: int = dspy.InputField()
    result: str = dspy.OutputField()

predictor = dspy.Predict(MathSignature)
predictor(number="42")  # Warning: Type mismatch for field 'number'
```

The framework **warns, does not exception** — and the warning can be turned off globally via `dspy.configure(warn_on_type_mismatch=False)`. The choice of warning-over-exception preserves DSPy's *prototyping-first* discipline: type mismatches are visible, but they don't block iteration.

## Modules *expand* signatures under the hood

The page's most consequential note for the Programming Model is this:

> "Many DSPy modules expand signatures under the hood. For example, `dspy.ChainOfThought` adds a `reasoning` field."

A user-declared `'document -> summary'` Signature passed to `dspy.ChainOfThought` becomes a `document -> reasoning, summary` Signature at run time. The returned `response` object exposes **both** `response.summary` and `response.reasoning` — the user never declared the `reasoning` field. This is the canonical mechanism by which [[DSPyModules|Modules]] *layer behavior on top of* a Signature without forcing the user to declare the intermediate fields. The same mechanism is how `dspy.ReAct` injects tool-call slots, `dspy.ProgramOfThought` injects code-generation slots, etc.

This is what licenses [[DSPyProgrammingModel|the Programming Model's]] *"swap one module for another without modifying the signature"* portability claim: the user's Signature is the **observation interface**; the Module decides what additional fields to materialize between input and output.

## Worked examples on the page

The Signatures page works through five examples; each is a sharper reading of the abstraction:

| Example | Signature | Module | Point made |
|---|---|---|---|
| **A — Sentiment** | `'sentence -> sentiment: bool'` (inline) | `dspy.Predict` | Inline form with a typed-`bool` output; the simplest possible Signature. |
| **B — Summarization** | `'document -> summary'` (inline) | `dspy.ChainOfThought` | The user-declared signature is **expanded** with a `reasoning` field by the Module. |
| **C — Emotion classification** | `class Emotion(dspy.Signature)` with `Literal[...]` | `dspy.Predict` | Class form + closed-set output via `typing.Literal`. |
| **D — Citation faithfulness** | `class CheckCitationFaithfulness(dspy.Signature)` with `desc=` on inputs and a `dict[str, list[str]]` output | `dspy.ChainOfThought` | Class form with mixed input/output hints, structured-dict output, and `reasoning` expansion — a worked instance of a Signature that *is* a [[DSPyMetrics|metric]]. |
| **E — Multi-modal** | `class DogPictureSignature(dspy.Signature)` with `image_1: dspy.Image` | `dspy.Predict` | The multi-modal input case via `dspy.Image` + `dspy.Image.from_url(...)`. |

The Citation Faithfulness example is the most generalizable: it's the page's first glimpse of a Signature being used as a **verifier** — exactly the role [[DSPyMetrics|Metrics]] and the broader [[LLMModuloFramework|LLM-Modulo]] critique-layer will play in the wiki's downstream framings.

## Position in the DSPy stack

Signatures sit at the **top** of the user-facing API surface — they are the artifact the developer *writes* by hand. Underneath, the call flow is:

```
Signature (user-written)
   ↓ passed to
Module (dspy.Predict / dspy.ChainOfThought / dspy.ReAct / …)
   ↓ formats via
Adapter
   ↓ calls
dspy.LM
   ↓ routes through
LiteLLM
   ↓ to
Provider (OpenAI / Anthropic / Gemini / SGLang / Ollama / …)
```

Each step below the Signature is **swappable without touching the Signature**. This is what makes the *"Signature is the stable interface"* claim true.

## Why this matters

- **Operationalizes the *signature* concern of [[DSPyProgrammingModel|the Programming Model]].** The Programming Overview *names* the four orthogonal artifacts in the abstract; this is the page that turns the first of them into a typed Python API surface. The page is therefore the canonical mooring point for everything DSPy says about typed I/O.
- **Establishes the *prompt-is-derived, not written* discipline.** A DSPy program declares the *interface* (Signature) and the *strategy* (Module); the framework derives the prompt. This is the concrete form of [[dspy-programming-overview|the Programming Overview's]] *"writing code instead of strings"* thesis at the API layer.
- **Names the type system Signatures use.** The five-tier enumeration — basic / `typing` / pydantic / dot-notation / DSPy-special — is the wiki's first record of a structured-output framework's typing surface. This is what makes Signatures *interoperable with the Python ecosystem*: any pydantic model or `typing` construct is a valid Signature field type.
- **`Literal[...]` as the classification primitive.** A small but important detail: closed-set classification in DSPy is *just a `typing.Literal` annotation* — no separate vocabulary. This collapses an entire category of "prompt engineering for classification" into a Python type annotation.
- **Multi-modal via `dspy.Image`.** The page demonstrates that the same Signature/Module/Predict stack scales to multi-modal input without a separate API. This generalizes the *swap the LM* portability claim to *swap the modality*.
- **Modules *expand* signatures.** The `dspy.ChainOfThought`-adds-`reasoning` pattern is the page's most consequential implementation detail. It's the mechanism by which a Module can be *strategically richer* than its Signature suggests — and it's why a swap from `dspy.ChainOfThought` to `dspy.ProgramOfThought` doesn't require declaring intermediate fields the user shouldn't have to know about.

## Connections

- [[DSPy]] — the framework whose typed input/output surface this concept *is*.
- [[dspy-signatures]] — canonical source for the API surface (DSPy *Learn* page 4 of 13).
- [[dspy-programming-overview]] — names the *signature* concern in the abstract as one of the four orthogonal artifacts a conventional prompt entangles; this concept page is the concrete definition that concern points at.
- [[dspy-language-models]] — uses `dspy.ChainOfThought('question -> answer')` in passing; the present page is what that string syntactically and semantically is.
- [[dspy-learn-index]] — parent Learn index page; lists *Signatures* as the third Programming-stage sub-topic.
- [[DSPyProgrammingModel]] — the *separation-of-concerns* design philosophy. The Signature is the first of the four orthogonal artifacts; this concept page is its API-level definition.
- [[DSPyLM]] — the LM-client abstraction sitting below the Signature in the call stack. A Signature is what survives unchanged across `provider/model-name` swaps.
- [[DSPyAdapters]] — the formatting / parsing layer **between** the Signature and `dspy.LM`. Adapters translate a typed Signature into the messages the LM is called with and parse the response back into a typed `Prediction(...)`. Forward reference (page 6 of 13).
- [[DSPyModules]] — the layer that **consumes** Signatures. `dspy.Predict` / `dspy.ChainOfThought` / `dspy.ReAct` all take a Signature as their constructor argument. Forward reference (page 5 of 13).
- [[DSPyPredict]] — the simplest Module; the page's primary worked example. Forward reference.
- [[ChainOfThought]] — `dspy.ChainOfThought` is the page's *signature-expansion* exemplar (adds a `reasoning` field) and the *"start simple"* module from [[dspy-programming-overview|the Programming Overview]].
- [[DSPyMetrics]] — the citation-faithfulness example on the page is a worked instance of a Signature acting as a metric / verifier; natural bridge into the Metrics page. Forward reference.
- [[DSPyOptimizers]] — *"The DSPy compiler will figure out how to build a highly-optimized prompt for your LM … for your signature, on your data, and within your pipeline."* The Signature is what the compiler tunes against. Forward reference (page 13 of 13).
- [[LanguageModel]] — the underlying NLP concept; the Signature is the typed-program-side of the program-↔-LM interface.
- [[PromptEngineering]] — the discipline DSPy positions itself against. A Signature *is* the prompt-engineer's specification, but in a typed, optimizable, swappable form.
- [[Pydantic]] — the Python data-validation library the page demonstrates as a first-class type provider for Signatures. Forward reference.
- [[TypingLiteral]] — Python's `typing.Literal[...]` used as the DSPy-idiomatic closed-set classification primitive. Forward reference.
- [[2604.25850-agentic-harness-engineering]] — counter-positioning paper whose critique of "DSPy-style instruction tuning" lands at the Signature/Adapter/Module/Optimizer level; the present page is the most concrete instance of the prompt-level decoupling claim AHE counter-positions against.
- [[LLMModuloFramework]] — complementary framework. A Signature acting as a verifier (the citation-faithfulness example) is precisely the *critic* role Kambhampati et al.'s framework assigns to external sound checkers.
