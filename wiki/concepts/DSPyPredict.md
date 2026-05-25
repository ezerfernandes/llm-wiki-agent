---
title: "DSPy Predict"
type: concept
tags: [dspy, llm-programming, modules, primitive, framework, async]
sources: [dspy-modules, dspy-signatures, dspy-language-models, dspy-async-tutorial]
last_updated: 2026-05-24
---

# DSPy Predict

**`dspy.Predict`** is the **minimal primitive [[DSPyModules|Module]]** in [[DSPy]] — *"the most fundamental module"* — and the **substrate every other built-in Module is built on top of**. [[dspy-modules|The Modules page]] makes this explicit:

> "Internally, all other DSPy modules are built using `dspy.Predict`."

This concept page records the primitive itself; [[dspy-modules|the Modules page]] (page 5 of 13) is the canonical source.

## What it does

`dspy.Predict` is the **identity-strategy** Module: it takes a [[DSPySignatures|Signature]] and **does not modify it**. Where [[ChainOfThought|`dspy.ChainOfThought`]] expands a `'question -> answer'` signature into `'question -> reasoning, answer'`, `dspy.Predict` keeps it as `'question -> answer'`. The page's three-step pattern is the canonical usage:

```python
# 1) Declare with a signature.
classify = dspy.Predict('sentence -> sentiment: bool')

# 2) Call with input argument(s).
response = classify(sentence="it's a charming and often affecting journey.")

# 3) Access the output.
print(response.sentiment)   # True
```

Per [[dspy-modules|the Modules page]]: *"`dspy.Predict`: Basic predictor. Does not modify the signature. Handles the key forms of learning (i.e., storing the instructions and demonstrations and updates to the LM)."*

## Why it is more than a thin LM wrapper

The page's most consequential disclosure about `dspy.Predict` is that it is the **learnable-parameter store**. Three things live in a `dspy.Predict` instance:

1. **The instructions string.** What the framework will inject as the system / task prompt under the chosen [[DSPyAdapters|Adapter]].
2. **The demonstrations.** Few-shot exemplars (`Example` objects) the [[DSPyOptimizers|Optimizer]] can bootstrap, swap, or order during search.
3. **LM-weight updates.** For finetuning-style optimizers ([[BootstrapFinetune]]), the Predict instance carries the bound weights or the reference to them.

This is why [[DSPyOptimizers|Optimizers]] read against `named_predictors()` (the walk that finds every `dspy.Predict` in a program) rather than against `named_parameters()` in the strict sense — `dspy.Predict` is the **atomic unit of optimization** in DSPy.

## Per-call configuration

Generation knobs can be passed at the declare step as defaults, or at the call step via a `config={...}` kwarg that overrides for that call:

```python
predict = dspy.Predict("question -> answer", temperature=0.7)        # default
predict(question="What is 1 + 52?", config={"rollout_id": 5,
                                            "temperature": 1.0})     # per-call override
```

This is the channel by which generation parameters flow from a Module to the bound [[DSPyLM|`dspy.LM`]] without forcing a `dspy.context` swap — and it composes the same way for **every** Module subclass since they all route their final LM call through an internal `dspy.Predict`.

## The "primitive" claim

The taxonomic structure of [[DSPyModules|the Modules page]] is that every other built-in Module is a `dspy.Predict` wrapped in a strategy-specific **signature expansion**:

| Module | What it adds over `dspy.Predict` |
|---|---|
| [[ChainOfThought\|`dspy.ChainOfThought`]] | Expands signature with a `reasoning` field before the output. |
| [[DSPyProgramOfThought\|`dspy.ProgramOfThought`]] | Adds code-generation and code-execution slots; final answer is the execution result. |
| [[react\|`dspy.ReAct`]] | Adds tool-call slots; loops through tool dispatches until the LM signals completion. |
| [[DSPyMultiChainComparison\|`dspy.MultiChainComparison`]] | Runs N `ChainOfThought` calls (each itself a Predict+expansion) and adds a final comparison Predict. |
| [[DSPyRecursiveLanguageModel\|`dspy.RLM`]] | Adds recursive sub-LLM-call orchestration in a sandboxed Python REPL. |

This is a **strong claim**: every prompting technique DSPy ships is decomposable to a Predict plus a signature-level expansion. The page asserts it but does not prove it; the wiki carries the claim as the page's headline structural commitment.

## Async surface — `acall()`

`dspy.Predict` exposes `acall()` as the async counterpart to `__call__`:

```python
predict = dspy.Predict("question -> answer")
output  = await predict.acall(question="why did a chicken cross the kitchen?")
```

Because every other built-in [[DSPyModules|Module]] is built over `dspy.Predict`, **the async surface propagates automatically** — `dspy.ChainOfThought(...).acall(...)`, `dspy.ReAct(...).acall(...)`, etc. are all available without per-Module implementation. See [[DSPyAsync]] for the framework-wide pattern and [[dspy-async-tutorial]] for the canonical receipt.

## Position in the call stack

`dspy.Predict` is the layer **above** the [[DSPyAdapters|Adapter]] and **below** every strategy-Module:

```
[strategy Module (ChainOfThought / ReAct / ProgramOfThought / ...)]
   ↓ expands signature, then delegates to
dspy.Predict
   ↓ hands signature + inputs to
Adapter
   ↓ which formats messages and calls
dspy.LM
```

Calling `dspy.Predict(signature)(inputs)` skips the strategy expansion — it is the **bare-bones LM call** mediated by a Signature, an Adapter, and the configured LM.

## Why this matters

- **One primitive, seven strategies.** DSPy's claim that *all* prompting techniques decompose to `dspy.Predict` + signature expansion is what makes the framework **uniform**. There is no per-strategy LM-call path; there is one path, called with seven different expanded Signatures.
- **The atomic unit of optimization.** [[DSPyOptimizers|Optimizers]] tune `dspy.Predict` instances. Knowing the program is *just* a tree of `dspy.Predict`s with control flow around them is what makes `named_predictors()` a sufficient API for prompt search.
- **The "no-op" Module is meaningful.** Unlike a no-op identity-function in NN-land, a no-op DSPy module is **already learnable** — its instructions, demonstrations, and LM-weight reference are state worth optimizing.
- **The "start simple" recommendation lands here.** [[dspy-programming-overview|The Programming Overview's]] *start simple, then grow* discipline suggests starting with [[ChainOfThought|`dspy.ChainOfThought`]] (because it's almost always a quality upgrade over `dspy.Predict`), but `dspy.Predict` is the literal floor — when even CoT is too much, drop to Predict.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-ai-text-game-tutorial]] — uses `dspy.Predict` (alongside `dspy.ChainOfThought`) as the entry-level primitive composed inside a `dspy.Module` subclass; smallest receipt of *signature → Predict → output*.
- [[dspy-conversation-history]] — `dspy.Predict('question, history: dspy.History -> answer')` shows the `dspy.History` special-input plumbing through the bare Predict path with no strategy layer.
- [[dspy-email-extraction-tutorial]] — four `dspy.Predict` instances composed sequentially inside one `dspy.Module`; each is the atomic optimization unit later tuned by `MIPROv2`.
- [[dspy-streaming-tutorial]] — wraps `dspy.Predict` in `dspy.streamify(...)` and emits `StreamListener` events keyed by Predict output-field names, exercising the *Predict is the wire-format funnel* property.
- [[dspy-saving-tutorial]] — saves and reloads a `dspy.Predict` instance: makes the *Predict carries instructions + demonstrations + LM-weight reference* claim concrete by persisting exactly those three things.
- [[dspy-async-tutorial]] — canonical receipt of `predict.acall(...)`; demonstrates the async surface is rooted in `dspy.Predict` and propagates automatically to every higher-level Module.
- [[dspy-tutorial-gepa-facility-support-analyzer]] — three-Predict-instance pipeline whose instructions are jointly optimized by `dspy.GEPA`; shows `named_predictors()` enumerating Predict instances as the unit of search.
- [[dspy-tutorial-classification-finetuning]] — `dspy.BootstrapFinetune` mutates the LM-weight reference inside a `dspy.Predict`; the canonical receipt for *Predict as atomic unit of weight optimization*.

## Connections

- [[DSPyModules]] — the parent abstraction; `dspy.Predict` is the minimal primitive Module.
- [[dspy-modules]] — canonical source.
- [[DSPySignatures]] — every `dspy.Predict` is declared with a Signature; Signature is the I/O contract Predict honors.
- [[DSPy]] — the framework; `dspy.Predict` is its substrate prompting primitive.
- [[ChainOfThought]] / [[react|ReAct]] / [[DSPyProgramOfThought]] / [[DSPyMultiChainComparison]] / [[DSPyRecursiveLanguageModel]] — all built on top of `dspy.Predict` plus a signature expansion.
- [[DSPyAdapters]] — `dspy.Predict` hands its expanded Signature to the Adapter for formatting / parsing. Forward reference.
- [[DSPyLM]] — `dspy.Predict` calls the configured `dspy.LM` via the Adapter.
- [[DSPyOptimizers]] — read `named_predictors()` to enumerate `dspy.Predict` instances and tune their instructions / demonstrations / weights.
- [[DSPyPrediction]] — the return-object every `dspy.Predict` call produces.
- [[BootstrapFinetune]] — the weight-tuning optimizer that updates `dspy.Predict`'s LM-weight reference.
- [[DSPyProgrammingModel]] — `dspy.Predict` is the minimal embodiment of the *module-logic* concern.
- [[DSPyAsync]] — `dspy.Predict.acall(...)` is the root async entry; every other Module's async surface inherits from this one. Cross-link.
- [[dspy-async-tutorial]] — canonical source confirming `acall` is universal on built-in modules, rooted in `dspy.Predict`.
