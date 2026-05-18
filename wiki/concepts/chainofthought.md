---
title: "Chain-of-Thought"
type: concept
tags: [ml-method, prompting]
sources: [2512.04388-conductor, 2604.21590-agenticqwen, dspy-modules, dspy-signatures, dspy-programming-overview]
last_updated: 2026-05-17
---

# Chain-of-Thought

CoT prompting (Wei et al., 2022) elicits step-by-step intermediate reasoning before a final answer. In this corpus it shows up as the substrate the [[2512.04388-conductor|Conductor]] parses workflow lists from, and as a baseline tool-use foundation cited by [[2604.21590-agenticqwen|AgenticQwen]] alongside ReAct.

## DSPy implementation: `dspy.ChainOfThought`

In [[DSPy]], CoT is exposed as the **built-in [[DSPyModules|Module]]** `dspy.ChainOfThought` — *"Teaches the LM to think step-by-step before committing to the signature's response"* ([[dspy-modules]]). It is one of the seven built-in Modules and the one [[dspy-programming-overview|the Programming Overview]] recommends as the *"start simple"* default for any new task.

Three properties make the DSPy framing meaningfully distinct from CoT-as-a-prompt-template:

1. **Generalized over any signature.** `dspy.ChainOfThought('question -> answer')`, `dspy.ChainOfThought('document -> summary')`, and `dspy.ChainOfThought('claim, notes -> query')` are the *same Module class* applied to three different [[DSPySignatures|Signatures]]. There is no per-task CoT prompt to engineer — the framework derives the prompt from the Signature.

2. **Expands the signature with a `reasoning` field.** *"The `dspy.ChainOfThought` module will generally inject a `reasoning` before the output field(s) of your signature"* ([[dspy-modules]]). A user-declared `'question -> answer'` becomes `'question -> reasoning, answer'` on the wire; the returned `dspy.Prediction(...)` exposes **both** `.reasoning` and `.answer`. The user never declared `reasoning` — this is the canonical instance of [[DSPySignatures|the *modules-expand-signatures* mechanism]].

3. **Swap-in upgrade over [[DSPyPredict|`dspy.Predict`]].** *"In many cases, simply swapping `dspy.ChainOfThought` in place of `dspy.Predict` improves quality."* The swap is the constructor name only; the Signature, the LM, the Adapter, the Optimizer all stay the same. This is the operational form of [[DSPyProgrammingModel|the Programming Model's]] *"swap one module for another without modifying the signature"* portability claim at the *prompting-strategy* axis.

### Canonical usage

```python
question = "What's something great about the ColBERT retrieval model?"

classify = dspy.ChainOfThought('question -> answer', temperature=0.7)
response = classify(question=question)
print(response.reasoning)   # injected by the Module
print(response.answer)      # declared by the user
```

### Position in the DSPy module taxonomy

| Module | Signature expansion |
|---|---|
| [[DSPyPredict\|`dspy.Predict`]] | None — identity. |
| **`dspy.ChainOfThought`** | **Adds a `reasoning` field before the output.** |
| [[DSPyProgramOfThought\|`dspy.ProgramOfThought`]] | Code-and-execution slots. |
| [[react\|`dspy.ReAct`]] | Tool-call slots. |
| [[DSPyMultiChainComparison\|`dspy.MultiChainComparison`]] | Runs N `ChainOfThought` and adds a comparison Predict. |

`dspy.ChainOfThought` is the **base case** for two of the more elaborate Modules: `dspy.MultiChainComparison` runs N of them and aggregates; the [[SelfConsistency|self-consistency]] pattern in research papers maps to running N `ChainOfThought` calls and calling [[DSPyMajority|`dspy.majority`]] on the result.

## Connections
- [[react|ReAct]]
- [[grpo|GRPO]]
- [[2512.04388-conductor]]
- [[2604.21590-agenticqwen]]
- [[DSPy]] — framework whose `dspy.ChainOfThought` Module is CoT's typed, signature-parameterized form.
- [[DSPyModules]] — the parent abstraction.
- [[DSPyPredict]] — the minimal primitive `dspy.ChainOfThought` is built on top of.
- [[DSPySignatures]] — the Signature the Module honors and expands.
- [[DSPyProgrammingModel]] — names `dspy.ChainOfThought` as the *start simple, then grow* default starting point.
- [[DSPyMultiChainComparison]] — sibling Module that runs N CoT calls + comparison.
- [[DSPyMajority]] — function-style aggregator commonly paired with N `ChainOfThought` samples (research-paper *self-consistency*).
- [[DSPyPrediction]] — the return object carrying both the `reasoning` slot and the user-declared output.
- [[SelfConsistency]] — N-CoT + majority-vote pattern. Forward reference; stub.
