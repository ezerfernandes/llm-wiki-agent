---
title: "DSPy MultiChainComparison"
type: concept
tags: [dspy, llm-programming, modules, ensembling, self-consistency]
sources: [dspy-modules]
last_updated: 2026-05-24
---

# DSPy MultiChainComparison

**`dspy.MultiChainComparison`** is a [[DSPyModules|DSPy built-in Module]] that **runs multiple `dspy.ChainOfThought` samples and produces a final prediction by comparing them.** From [[dspy-modules|the Modules page]]:

> "`dspy.MultiChainComparison`: Can compare multiple outputs from `ChainOfThought` to produce a final prediction."

It is the *ensembled chain-of-thought* strategy lifted from research-paper territory into a typed, signature-parameterized Module — the DSPy-side answer to **self-consistency** ([[SelfConsistency|Wang et al. 2022]]) and **majority-of-CoT** prompting patterns, but with **comparison** (not just voting) as the aggregation rule.

## Mechanism

Internally, `dspy.MultiChainComparison` is a composite Module: it runs N independent `dspy.ChainOfThought` calls (typically at higher `temperature` to induce variance) over the same user-declared [[DSPySignatures|Signature]], collects the N `Prediction(reasoning=..., <output>=...)` objects, and then invokes a final [[DSPyPredict|`dspy.Predict`]] whose Signature is *"given these N candidate reasonings-and-answers, decide the best answer."* The result is a single `dspy.Prediction(...)` honoring the user's original Signature.

This puts `dspy.MultiChainComparison` in contrast with the function-style [[DSPyMajority|`dspy.majority`]]:

| Aggregator | Decision rule | Uses an LM call? |
|---|---|---|
| [[DSPyMajority\|`dspy.majority`]] | **Vote** — most-popular response wins. | No — pure Python. |
| **`dspy.MultiChainComparison`** | **Compare** — an LM reads all N candidates and picks the best. | Yes — one additional LM call to compare. |

The comparison-rather-than-vote distinction matters when the N candidate outputs disagree on **how** to express the right answer rather than on **what** the right answer is — `dspy.majority` cannot distinguish *"5"* and *"five"* without normalization; `dspy.MultiChainComparison` can.

## Position relative to other modules

| Module | Aggregates over multiple LM calls? |
|---|---|
| [[DSPyPredict\|`dspy.Predict`]] | No. |
| [[ChainOfThought\|`dspy.ChainOfThought`]] | No — one CoT call. |
| **`dspy.MultiChainComparison`** | **Yes — N CoT calls + 1 comparison call.** |
| [[DSPyMajority\|`dspy.majority`]] | Yes — vote over a set of `Prediction`s. |
| [[react\|`dspy.ReAct`]] | Yes — N tool-call loops, not aggregation. |
| [[DSPyRecursiveLanguageModel\|`dspy.RLM`]] | Yes — recursive sub-LLM calls. |

## Why this matters

- **First-class ensembling.** Self-consistency / majority-of-CoT is a well-known reliability boost for reasoning tasks; DSPy carries it as a built-in Module rather than leaving it as a user-implemented loop.
- **Comparison strictly more expressive than voting.** A vote requires syntactic equality; a comparison can adjudicate on semantic equivalence — at the cost of an extra LM call.
- **Signature-preserving.** Despite calling N+1 LMs internally, `dspy.MultiChainComparison` returns a `Prediction(...)` matching the user's declared Signature — the user-facing API is identical to `dspy.ChainOfThought`. This is another instance of the *swap-one-module-for-another-without-modifying-the-signature* portability claim.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-async-tutorial]] — names `dspy.MultiChainComparison` in the async-surface taxonomy as one of the built-in Modules whose `acall()` form follows the same `forward → aforward` mirror as the other strategy modules; no standalone receipt.

## Connections

- [[DSPyModules]] — the parent abstraction.
- [[dspy-modules]] — canonical source.
- [[DSPySignatures]] — the user-declared Signature `dspy.MultiChainComparison` honors at its outer interface.
- [[ChainOfThought]] — the sub-Module `dspy.MultiChainComparison` runs N times.
- [[DSPyPredict]] — both the underlying primitive each `ChainOfThought` call decomposes to and the final comparison Module.
- [[DSPyMajority]] — sibling aggregator; the function-style vote-not-compare counterpart.
- [[DSPyPrediction]] — the return object.
- [[SelfConsistency]] — the underlying research-paper technique (Wang et al. 2022 — *"Self-Consistency Improves Chain of Thought Reasoning in Language Models"*). Forward reference; stub.
- [[DSPyProgrammingModel]] — instances the *swap-modules-without-touching-signature* portability claim at the aggregation level.
