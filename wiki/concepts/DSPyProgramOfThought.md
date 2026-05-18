---
title: "DSPy ProgramOfThought"
type: concept
tags: [dspy, llm-programming, modules, program-of-thought, code-generation]
sources: [dspy-modules]
last_updated: 2026-05-17
---

# DSPy ProgramOfThought

**`dspy.ProgramOfThought`** is a [[DSPyModules|DSPy built-in Module]] whose prompting strategy is to **have the LM emit code and let the code's execution result determine the final answer**. From [[dspy-modules|the Modules page]]:

> "`dspy.ProgramOfThought`: Teaches the LM to output code, whose execution results will dictate the response."

It is the code-execution counterpart to [[ChainOfThought|`dspy.ChainOfThought`]]: where CoT routes the LM's intermediate reasoning through *prose*, ProgramOfThought routes it through *executable code* — typically Python — and lets the runtime adjudicate. The technique it implements is the Program-of-Thought prompting pattern (Chen et al. 2022; *"Program of Thoughts Prompting"*), generalized over an arbitrary [[DSPySignatures|Signature]] in the DSPy framing.

## Mechanism

Like every other Module, `dspy.ProgramOfThought` is a wrapper over [[DSPyPredict|`dspy.Predict`]] that **expands the user's [[DSPySignatures|signature]] under the hood**. Where `dspy.ChainOfThought` injects a `reasoning` field, `dspy.ProgramOfThought` injects code-generation and code-execution slots: the LM is asked to produce a Python snippet, the snippet is executed, and the execution result is folded back into the prediction before the user's declared output field is returned.

The usage pattern is identical to every other Module:

```python
pot = dspy.ProgramOfThought("question -> answer")
pot(question="What is the sum of the first 100 prime numbers?")
```

## Position relative to other modules

| Module | How the LM reasons |
|---|---|
| [[DSPyPredict\|`dspy.Predict`]] | One shot — straight to the answer. |
| [[ChainOfThought\|`dspy.ChainOfThought`]] | Prose chain-of-thought before the answer. |
| **`dspy.ProgramOfThought`** | **Code** — written, then executed — before the answer. |
| [[react\|`dspy.ReAct`]] | Tool calls in a loop until completion. |

`dspy.ProgramOfThought` is the right Module when:

- The task has a **computable** ground truth (arithmetic, string transformations, list operations, lookups) where a Python snippet is more reliable than a hand-rolled chain of arithmetic-in-prose.
- The user wants the framework to **adjudicate** the LM's reasoning step rather than trust the LM's own self-report. Code execution is a built-in sound critic in the [[LLMModuloFramework|LLM-Modulo]] sense.

[[dspy-programming-overview|The Programming Overview]] explicitly names the `dspy.ChainOfThought` ↔ `dspy.ProgramOfThought` swap as one of the *swap-one-module-for-another-without-modifying-the-signature* portability claims — moving from CoT to PoT requires changing the constructor name only.

## Why this matters

- **Generalizes Program-of-Thought to any signature.** The underlying technique appears in research papers as a prompt-template recipe; DSPy turns it into a Module class that works for any user-declared [[DSPySignatures|Signature]].
- **Built-in sound critic.** Code execution is a deterministic, sound verifier in a way that LLM-prose reasoning is not. For domains where the answer is computable, `dspy.ProgramOfThought` shifts the verification burden from the LM to the Python runtime.
- **One-character source-code swap from CoT.** The portability claim becomes operational: a program that uses `dspy.ChainOfThought('question -> answer: float')` for math can be re-pointed at `dspy.ProgramOfThought` with no other change.

## Connections

- [[DSPyModules]] — the parent abstraction.
- [[dspy-modules]] — canonical source.
- [[DSPySignatures]] — the I/O contract the Module honors.
- [[DSPyPredict]] — the minimal primitive `dspy.ProgramOfThought` is built on top of.
- [[ChainOfThought]] — sibling Module; the *prose-reasoning* counterpart to PoT.
- [[DSPyProgrammingModel]] — names the CoT ↔ PoT swap as a canonical portability example.
- [[LLMModuloFramework]] — code execution is a sound critic in the Kambhampati-et-al. generate-test-critique framing.
- [[ProgramOfThought]] — the underlying research-paper technique (Chen et al. 2022 — *"Program of Thoughts Prompting"*). Forward reference; stub.
- [[DSPyPrediction]] — the return object after the code is executed and the answer field is filled.
