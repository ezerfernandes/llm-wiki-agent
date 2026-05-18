---
title: "DSPy Learn — Adapters"
type: source
tags: [dspy, llm-programming, adapters, formatting, parsing, structured-output]
date: 2026-05-17
source_file: raw/dspy-adapters.md
---

## Summary

**Page 6 of 13** of the [[DSPy]] *Learn* documentation. **Defines** the **third** of the four orthogonal artifacts [[DSPyProgrammingModel|the Programming Model]] factors out of a conventional prompt — the **Adapter**: *"the bridge between `dspy.Predict` and the actual Language Model (LM)"*. Adapters translate between [[DSPy]]'s structured `dspy.Predict` module and the underlying [[DSPyLM|LM]] — converting [[DSPySignatures|Signatures]] into system messages, formatting inputs (including [[DSPyTools|Tool]] / `dspy.Image` / `dspy.History` types) into multi-turn messages, and parsing the LM's textual response back into a typed [[DSPyPrediction|`dspy.Prediction`]]. The page documents two built-in adapters in detail — **`dspy.ChatAdapter`** (the default; uses `[[ ## field_name ## ]]` delimiters and universal-compatibility framing) and **`dspy.JSONAdapter`** (uses the LM's native `response_format` structured-output channel) — plus two further adapters named only (`dspy.XMLAdapter`, `dspy.TwoStepAdapter`) and the custom-adapter escape hatch. **Resolves the long-standing forward reference [[DSPyAdapters]]** carried by every prior DSPy ingest since the corpus opened.

## Key Claims

- **An Adapter is the bridge between `dspy.Predict` and the LM.** The page's opening sentence is load-bearing: *"Adapters function as the bridge between `dspy.Predict` and the actual Language Model (LM)."* This is the most concrete description in the *Learn* corpus of what the Adapter axis of [[DSPyProgrammingModel|the Programming Model]] actually does at the wire level.

- **Three responsibilities.** The Adapter is responsible for **three** tasks the rest of DSPy cannot do generically:
  1. Converting a [[DSPySignatures|Signature]] into a system message defining the task.
  2. Formatting input data per request structures (multi-turn messages, role assignments, demo injection).
  3. Parsing LM responses into structured outputs — concretely a [[DSPyPrediction|`dspy.Prediction`]] instance.

  The Adapter also handles **conversation history**, **function calls**, and converting DSPy-special types ([[DSPyTools|`Tool`]], `dspy.Image`, `dspy.History`) into prompt messages.

- **`ChatAdapter` is the default.** *"When no adapter is specified, DSPy defaults to `ChatAdapter`."* Two configuration channels mirror the [[DSPyLM|LM]] bind modes — `dspy.configure(adapter=...)` (global) and `with dspy.context(adapter=...)` (block-local).

- **Six-step processing flow.** The page's canonical end-to-end flow:
  1. User invokes a DSPy module with inputs.
  2. Inner `dspy.Predict` calls `Adapter.format()`.
  3. Adapter converts signature, inputs, and demonstrations into multi-turn messages.
  4. Language model generates response.
  5. `Adapter.parse()` transforms the response into structured outputs.
  6. Caller receives parsed results.

  Two introspection hooks: `adapter.format(signature, demos, inputs)` returns the full multi-turn message list; `adapter.format_system_message(signature)` returns only the system message.

- **`ChatAdapter` — universal-compatibility default.** *"Universal compatibility: Works with all language models."* Uses field-delimiter markers `[[ ## field_name ## ]]` to delineate sections of the prompt and response. For non-primitive types (pydantic models, `list[...]`, `dict[...]`), the JSON schema is included in the system instructions, then field values are emitted inside the delimiters. **Includes automatic fallback to `JSONAdapter` on failure**. Trade-off: *"more boilerplate output tokens compared to other adapters"* — higher token count may increase latency.

- **`JSONAdapter` — native structured-output channel.** Prompts LMs to return JSON with all output fields. *"Effective for models that support structured output via the `response_format` parameter."* Advantages: *"Minimal boilerplate in the LM response results in faster responses."* Trade-off: *"Requires models supporting the `response_format` parameter; incompatible with smaller open-source models lacking this capability."* This is the **first concrete model-capability boundary** the [[dspy-learn-index|Learn corpus]] surfaces: a model that does not implement `response_format` is incompatible with `JSONAdapter`, and the user must fall back to `ChatAdapter`.

- **Two named-only adapters: `XMLAdapter` and `TwoStepAdapter`.** The page references both in the API reference sidebar but provides no implementation details, use cases, or guidance within the main content. They cover XML-formatted I/O and two-step extract-then-format workflows respectively (recovered from the API surface, not the prose).

- **Custom adapters are supported.** *"Custom adapter development remains possible for specialized requirements."* The framework's `Adapter` base class can be subclassed; `format()` / `parse()` overridden — though the page does not work an example.

- **Worked example: same `NewsQA` signature, two adapters.** The page demonstrates **the same** typed [[DSPySignatures|Signature]] (`NewsQA` with a `list[ScienceNews]` output of a pydantic `BaseModel`) under **both** `ChatAdapter` and `JSONAdapter`, with `dspy.inspect_history()` showing the difference in wire format. The example is the page's most explicit *"swap the adapter without touching the signature"* demonstration — the concrete payoff of [[DSPyProgrammingModel|the Programming Model's]] separation-of-concerns claim **at the Adapter axis**.

## Key Quotes

> "Adapters function as the bridge between `dspy.Predict` and the actual Language Model (LM)." — opening definition

> "When no adapter is specified, DSPy defaults to `ChatAdapter`." — the default adapter

> "Universal compatibility: Works with all language models." — `ChatAdapter`'s headline property

> "Effective for models that support structured output via the `response_format` parameter." — `JSONAdapter`'s scoping condition

> "Minimal boilerplate in the LM response results in faster responses." — the latency motivation for `JSONAdapter`

## Code Examples

The default adapter is implicit:

```python
import dspy

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

predict = dspy.Predict("question -> answer")
result = predict(question="What is the capital of France?")
```

…and equivalent to the explicit form:

```python
import dspy

dspy.configure(
    lm=dspy.LM("openai/gpt-4o-mini"),
    adapter=dspy.ChatAdapter(),  # This is the default value
)

predict = dspy.Predict("question -> answer")
result = predict(question="What is the capital of France?")
```

Introspecting the formatted messages:

```python
signature = dspy.Signature("question -> answer")
inputs = {"question": "What is 2+2?"}
demos = [{"question": "What is 1+1?", "answer": "2"}]

adapter = dspy.ChatAdapter()
print(adapter.format(signature, demos, inputs))
```

Or just the system message:

```python
import dspy

signature = dspy.Signature("question -> answer")
system_message = dspy.ChatAdapter().format_system_message(signature)
print(system_message)
```

The page's worked **same-signature, different-adapter** example with a non-primitive `list[ScienceNews]` output:

```python
import dspy
import pydantic

dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"), adapter=dspy.ChatAdapter())  # or dspy.JSONAdapter()


class ScienceNews(pydantic.BaseModel):
    text: str
    scientists_involved: list[str]


class NewsQA(dspy.Signature):
    """Get news about the given science field"""

    science_field: str = dspy.InputField()
    year: int = dspy.InputField()
    num_of_outputs: int = dspy.InputField()
    news: list[ScienceNews] = dspy.OutputField(desc="science news")

predict = dspy.Predict(NewsQA)
predict(science_field="Computer Theory", year=2022, num_of_outputs=1)
dspy.inspect_history()
```

Switching `adapter=dspy.ChatAdapter()` → `adapter=dspy.JSONAdapter()` is the **only** change; the Signature, the Module, the LM, and the call site are unchanged.

## Connections

- [[DSPy]] — the framework whose **third** orthogonal artifact this page defines. Page 6 of 13 of *Learn*.
- [[DSPyAdapters]] — **concept page minted by this ingest.** The canonical wiki anchor for the Adapter abstraction; **resolves the long-standing forward reference** carried by [[DSPy]] / [[DSPyProgrammingModel]] / [[DSPySignatures]] / [[DSPyLM]] / [[DSPyModules]] / [[dspy-learn-index]] / [[dspy-programming-overview]] / [[dspy-language-models]] / [[dspy-signatures]] / [[dspy-modules]] since the corpus opened.
- [[DSPyProgrammingModel]] — names *adapter* as the third of four orthogonal concerns; this page is the API-level definition.
- [[DSPySignatures]] — the **upstream** artifact the Adapter consumes. A Signature is the typed contract; the Adapter is the layer that translates that contract into the LM's wire format and back.
- [[DSPyLM]] — the **downstream** artifact the Adapter calls into. The Adapter formats the Signature into messages the configured `dspy.LM` sends; LM response parsing happens before the [[DSPyPrediction|`Prediction`]] is returned.
- [[DSPyModules]] — every Module's call chain runs through `Adapter.format()` → `dspy.LM` → `Adapter.parse()`. The Module decides *what* to ask the LM; the Adapter decides *how* to encode the ask.
- [[DSPyPredict]] — the inner-most caller of `Adapter.format()` / `Adapter.parse()`; the page's three-task list is framed from `dspy.Predict`'s perspective.
- [[DSPyPrediction]] — the typed output `Adapter.parse()` produces.
- [[DSPyTools]] — Tools are one of the special types the Adapter converts into prompt messages. Forward reference (page 7 of 13).
- [[Pydantic]] — the page's `NewsQA` worked example uses a `pydantic.BaseModel` (`ScienceNews`) as the element type of a `list[...]` output; the Adapter is responsible for emitting the JSON schema (`ChatAdapter`) or invoking the LM's `response_format` (`JSONAdapter`).
- [[LiteLLM]] — the upstream provider-abstraction layer; the `response_format` parameter `JSONAdapter` depends on is plumbed through LiteLLM.
- [[StructuredOutput]] — the broader LM-engineering concept `JSONAdapter` operationalizes. Forward reference.
- [[OpenAIResponseFormat]] — the specific OpenAI parameter `JSONAdapter` consumes. Forward reference; named only.

## Contradictions

None. The Adapters page **extends** every prior DSPy ingest:

- [[dspy-programming-overview]] named *adapter* as one of four concerns; this page **defines** the artifact that concern points at.
- [[dspy-signatures]] showed Signatures are the *stable interface*; this page shows the Adapter is what makes that interface stable under [[DSPyLM|LM]] / format swaps — the same Signature drives both `ChatAdapter` (delimiter-based) and `JSONAdapter` (response-format-based) wire formats.
- [[dspy-modules]] showed Modules are the *swappable strategy*; this page shows the Adapter is **also** swappable, on a separate axis — strategy and wire-format are independently exchangeable.
- [[dspy-language-models]] documented `dspy.LM` as the universal LM client; this page documents the layer that sits **between** [[DSPySignatures|Signatures]] and [[DSPyLM|`dspy.LM`]].

Three productive clarifications of prior ambient framing:

1. **`ChatAdapter` has a `JSONAdapter` fallback.** A small but consequential implementation detail — the default path is not strictly delimiter-based; on parse failure it automatically retries through the JSON channel. This means the *"universal compatibility"* claim is partly upheld by an automatic recovery mechanism rather than being purely a property of the delimiter encoding.

2. **`JSONAdapter` is model-capability-gated.** *"Requires models supporting the `response_format` parameter; incompatible with smaller open-source models lacking this capability."* This is the **first explicit model-capability scoping** in the [[dspy-learn-index|Learn corpus]] — a reminder that DSPy's *"swap the LM"* portability is not unconditional at the wire-format layer.

3. **Adapters handle [[DSPyTools|Tool]] / `Image` / `History` conversion.** The page lists this responsibility explicitly: *"Converting DSPy types (`Tool`, `Image`, etc.) into prompt messages."* This means the [[DSPyTools|Tools]] artifact (page 7) and the multi-modal `dspy.Image` primitive (introduced on [[dspy-signatures]]) both compose through the Adapter — not through a separate sub-system. The Adapter is the **single funnel** through which every DSPy-typed value crosses into the LM's wire format.
