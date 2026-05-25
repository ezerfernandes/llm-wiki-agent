---
title: "DSPy Majority"
type: concept
tags: [dspy, llm-programming, modules, voting, function-style, ensembling]
sources: [dspy-modules]
last_updated: 2026-05-24
---

# DSPy Majority

**`dspy.majority`** is a [[DSPy]] **function-style aggregator** that *"can do basic voting to return the most popular response from a set of predictions"* ([[dspy-modules|the Modules page]]). It is the cheapest possible ensembling primitive — a pure-Python vote over a collection of [[DSPyPrediction|`Prediction`]] objects, with no LM call of its own.

## Mechanism

The page singles out `dspy.majority` as a **function-style** module — *"we also have some function-style modules"* — distinguishing it from the seven `dspy.Module` subclasses. The operational difference:

| Convention | Built-in Modules ([[DSPyPredict|`dspy.Predict`]], [[ChainOfThought|`dspy.ChainOfThought`]], …) | **`dspy.majority`** |
|---|---|---|
| Declared with a [[DSPySignatures|Signature]]? | Yes. | **No** — operates on a set of existing `Prediction`s. |
| Called with input arguments? | Yes — by name. | **No** — called with a collection. |
| Issues an LM call? | Yes. | **No** — pure Python. |
| Returns a `Prediction`? | Yes. | Yes (the winning `Prediction`). |

Typical usage in a multi-sample pipeline:

```python
predictions = [classify(sentence=s) for _ in range(N)]
final = dspy.majority(predictions)
```

The aggregation rule is **syntactic equality** of the output field(s): whichever `Prediction` value appears most often in the collection wins. Ties are broken implementation-defined (the page does not specify).

## Position in the ensembling taxonomy

| Aggregator | Decision rule | LM cost |
|---|---|---|
| **`dspy.majority`** | **Vote** (syntactic equality). | Zero. |
| [[DSPyMultiChainComparison\|`dspy.MultiChainComparison`]] | Compare (LM reads N candidates and picks the best). | One extra LM call. |
| Custom Module in `forward()` | Whatever the user writes. | Whatever the user writes. |

The `dspy.majority` / `dspy.MultiChainComparison` split is the page's clearest example of a **cost-versus-expressiveness tradeoff** in DSPy: voting is free but cannot reconcile semantically-equivalent-but-syntactically-different outputs (*"5"* vs *"five"*); comparison costs one LM call but can.

## Why this matters

- **Free ensembling.** When the output is a closed-set classification or a structured value with stable serialization, `dspy.majority` over N samples is a strictly-positive reliability lever at zero LM cost. The classic *self-consistency* recipe in research papers maps to `dspy.majority` over N `dspy.ChainOfThought(...)` calls.
- **The page's only non-`dspy.Module` building block.** `dspy.majority` is a useful **anomaly** in the taxonomy — it breaks the *Signature → Module → Prediction* shape every other building block honors. Flagged as such on [[dspy-modules]].
- **Composes inside `forward()`.** Use inside a `class MyProgram(dspy.Module)` is straightforward: run a Module N times in a loop, collect the predictions, call `dspy.majority(...)`, return.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-rag-tutorial]] — names `dspy.majority` in the *further-improvements menu* closing the 61.1% [[SemanticF1]] receipt as the **inference-time-scaling ensembling axis**: sample N reasoning paths from the optimized [[chainofthought|`dspy.ChainOfThought`]] RAG program, vote with `dspy.majority`, no extra LM call.

## Connections

- [[DSPyModules]] — the parent abstraction; `dspy.majority` is the function-style outlier.
- [[dspy-modules]] — canonical source.
- [[DSPyPrediction]] — the type `dspy.majority` operates on (collection → single winner).
- [[DSPyMultiChainComparison]] — sibling aggregator; the LM-comparison-not-syntactic-vote counterpart.
- [[ChainOfThought]] — the typical input source — N CoT samples then a majority vote = research-paper *self-consistency*.
- [[SelfConsistency]] — the underlying technique. Forward reference; stub.
- [[DSPySignatures]] — `dspy.majority` is one of the few framework primitives that **does not** take a Signature.
