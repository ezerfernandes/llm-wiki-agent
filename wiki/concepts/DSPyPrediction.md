---
title: "DSPy Prediction"
type: concept
tags: [dspy, llm-programming, modules, typed-output, telemetry]
sources: [dspy-modules, dspy-signatures, dspy-email-extraction-tutorial]
last_updated: 2026-05-24
---

# DSPy Prediction

**`dspy.Prediction`** is the **typed return object** every [[DSPyModules|DSPy Module]] call produces. It is the framework's wire-frame for *"this is what the LM (and the surrounding strategy) computed for the user's declared [[DSPySignatures|Signature]]."* This concept page records the abstraction; [[dspy-modules|the Modules page]] is the canonical source.

## Shape

A `dspy.Prediction(...)` instance has three load-bearing properties:

1. **Output fields as attributes.** Every output field declared on the calling Module's Signature is accessible as an attribute on the Prediction. For a signature `'question -> answer: float'` the Prediction exposes `.answer`. For multi-output signatures like `'question, choices: list[str] -> reasoning: str, selection: int'` the Prediction exposes both `.reasoning` and `.selection`.

2. **Module-injected fields.** Strategy Modules that **expand the user's signature under the hood** (per [[dspy-signatures]]'s *modules-expand-signatures* mechanism) surface those expanded fields on the Prediction. The most common case:

   ```python
   classify = dspy.ChainOfThought('question -> answer')
   response = classify(question="What's something great about the ColBERT retrieval model?")
   print(response.reasoning)   # injected by ChainOfThought
   print(response.answer)      # declared by the user
   ```

   The page's worked example makes this explicit: *"The `dspy.ChainOfThought` module will generally inject a `reasoning` before the output field(s) of your signature."*

3. **`get_lm_usage()` telemetry method.** From DSPy 2.6.16, every Prediction carries the LM-call provenance that produced it (when `dspy.configure(track_usage=True)` is set).

## The repr

`Prediction` instances pretty-print as a labeled tuple of their fields. The page's math example:

```
Prediction(
    reasoning='When two dice are tossed, each die has 6 faces, resulting in a total of 6 x 6 = 36 possible outcomes. ...',
    answer=0.0277776
)
```

This is the user-facing surface for *"here is what the Module computed"* — both the expanded-signature `reasoning` slot and the user-declared `answer` slot are visible in one object.

## Returning a Prediction from a user Module

Composing a multi-Module program means **constructing** Predictions explicitly inside `forward()`. The page's multi-hop search example:

```python
return dspy.Prediction(notes=notes, titles=list(set(titles)))
```

This is what preserves the *Module returns a typed Prediction* contract for user-defined `class MyProgram(dspy.Module)` subclasses — they have the same return-type interface as every built-in Module, so they compose interchangeably.

## LM-usage tracking

The Prediction is the **container** for the framework's cost-accounting telemetry. From DSPy 2.6.16:

```python
dspy.configure(lm=dspy.LM('openai/gpt-4o-mini', cache=False), track_usage=True)
output = program(question="What is the capital of France?")
print(output.get_lm_usage())
# {'openai/gpt-4o-mini': {'prompt_tokens': 260, 'completion_tokens': 61, 'total_tokens': 321, ...}}
```

Three properties:

| Property | Mechanism |
|---|---|
| **Per-model aggregation.** | Return is `{provider/model: {token-counts-and-details}}`. Multi-LM programs (via `dspy.context(lm=...)`) get separate keys. |
| **Sub-call rollup.** | A `MyProgram.forward()` that calls `self.predict1` and `self.predict2` produces **one** combined dict on the outer Prediction. |
| **Cache-aware.** | *"Cached responses won't count toward usage statistics"* — a second call returning a cached response shows `{}`. The cache discipline is inherited from [[LiteLLM]] through [[DSPyLM]]. |

The dict's full schema (per the page's example): `{prompt_tokens, completion_tokens, total_tokens, completion_tokens_details: {accepted_prediction_tokens, audio_tokens, reasoning_tokens, rejected_prediction_tokens, text_tokens}, prompt_tokens_details: {audio_tokens, cached_tokens, text_tokens, image_tokens}}` — the provider's full per-call breakdown, surfaced unchanged.

## Why this matters

- **Single uniform return type across the framework.** Every built-in Module, every user-defined `class MyProgram(dspy.Module)`, and the `dspy.majority` aggregator all return a `dspy.Prediction`. This is what makes the *swap-one-module-for-another* portability claim work at the **calling** end — the caller never has to know which Module subclass was used.
- **The visible surface of the *modules-expand-signatures* mechanism.** A user-declared `'document -> summary'` Signature passed to [[ChainOfThought|`dspy.ChainOfThought`]] gives a Prediction with **both** `.summary` and `.reasoning`. The Prediction is where the framework's behind-the-scenes signature expansion **becomes user-visible**.
- **Cost accounting is per-call, not per-program.** A Prediction's `get_lm_usage()` returns the costs of *this particular call's* LM activity, with cache-aware semantics. This is what makes [[DSPyOptimizers|Optimizer]] runs (which call thousands of Predictions across the search) cost-trackable — the Optimizer accumulates per-call totals from per-Prediction reads.
- **The contract user Modules must honor.** A `class MyProgram(dspy.Module)` whose `forward()` returns anything other than a `dspy.Prediction(...)` breaks composition — outer Modules and `dspy.majority` callers cannot read it. This is an implicit contract the framework enforces by convention.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-conversation-history]] — minimal `response.answer` access on a `dspy.Predict` return; the smallest receipt of *output field as attribute*.
- [[dspy-customer-service-agent]] — surfaces `dspy.ReAct`'s expanded Prediction with `.trajectory`, `.reasoning`, and the user-declared output fields side-by-side; canonical *module-injected fields* example.
- [[dspy-tutorial-program-of-thought]] — `dspy.ProgramOfThought`'s Prediction exposes `.reasoning` and the user-declared answer after sandboxed code execution; the wider expansion case beyond `reasoning`.
- [[dspy-email-extraction-tutorial]] — Prediction is the inter-stage carrier in a four-stage sequential pipeline; each intermediate `.field` becomes the next stage's input.
- [[dspy-output-refinement-tutorial]] — `dspy.BestOfN` / `dspy.Refine` consume and re-emit `dspy.Prediction` instances; receipt of the *uniform return type makes wrapping orthogonal* property.
- [[dspy-streaming-tutorial]] — the final yielded value of a streamified module is the same `dspy.Prediction`; the streaming sidecar preserves the typed-return contract.
- [[dspy-llms-txt-generation-tutorial]] — composite `dspy.Module.forward()` constructs and returns a `dspy.Prediction(...)` aggregating outputs of multiple inner Predicts; receipt of the *user-Module honors the Prediction contract* convention.
- [[dspy-custom-module]] — explicit `return dspy.Prediction(notes=notes, titles=titles)` in a multi-hop `forward()`; the canonical *construct-a-Prediction-yourself* receipt for class-form `dspy.Module` subclasses.
- [[dspy-mcp-tutorial]] — Prediction holds a multi-step `dspy.ReAct` trajectory after MCP tool calls; surfaces the `trajectory` injected field on a Prediction whose schema spans an entire tool-augmented session.
- [[dspy-audio-tutorial]] — Prediction carries `dspy.Audio` outputs through the same typed-return interface, demonstrating multi-modal output composes through the same Prediction abstraction as text.

## Connections

- [[DSPyModules]] — every Module call produces a `Prediction`; this is the return-type half of the Module contract.
- [[dspy-modules]] — canonical source.
- [[DSPySignatures]] — the Prediction's attributes correspond to the calling Module's expanded Signature output fields.
- [[DSPyPredict]] / [[ChainOfThought]] / [[DSPyProgramOfThought]] / [[react|ReAct]] / [[DSPyMultiChainComparison]] / [[DSPyRecursiveLanguageModel]] — every built-in Module returns a `Prediction`.
- [[DSPyMajority]] — the function-style aggregator; consumes a collection of `Prediction`s and returns a single one.
- [[DSPyLM]] — the LM client whose call-history (`lm.history`) feeds the per-Prediction `get_lm_usage()` telemetry.
- [[LiteLLM]] — the upstream cache discipline that makes *cached responses don't count* possible.
- [[DSPyOptimizers]] — read per-Prediction `get_lm_usage()` to cost-track the search. Forward reference.
- [[DSPyVersion]] — `track_usage=True` and `get_lm_usage()` require DSPy 2.6.16+. Forward reference; named only.
