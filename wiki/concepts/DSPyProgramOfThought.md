---
title: "DSPy ProgramOfThought"
type: concept
tags: [dspy, llm-programming, modules, program-of-thought, code-generation]
sources: [dspy-modules, dspy-tutorial-program-of-thought]
last_updated: 2026-05-24
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

The underlying execution engine — surfaced as a public primitive in [[dspy-tutorial-program-of-thought|the ProgramOfThought tutorial]] — is [[LocalSandbox|`dspy.LocalSandbox`]]: `sandbox = dspy.LocalSandbox(); sandbox.execute("value = 2*5 + 4\nvalue") == 14`. PoT is structurally to `dspy.LocalSandbox` what [[chainofthought|`dspy.ChainOfThought`]] is to [[DSPyPredict|`dspy.Predict`]] — a thin wrapper that orchestrates the underlying primitive plus signature expansion.

The tutorial also reveals a previously-undocumented constructor kwarg: **`dspy.ProgramOfThought(GenerateAnswer, max_iters=3)`** — caps the number of code-generation retries when execution fails. The default is not disclosed; only the override is in the receipt.

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

## Canonical receipt: CoT-fails-then-PoT-succeeds on `12! / sum-of-primes(1..30)`

[[dspy-tutorial-program-of-thought|The ProgramOfThought tutorial]] is the wiki's **canonical printed receipt** of the CoT-vs-PoT swap. Same `BasicGenerateAnswer(question -> answer)` Signature, same LM ([[Llama3|Llama-3-70b-Instruct]]), constructor name is the only change:

| Module | Result | Comment |
|---|---|---|
| `dspy.ChainOfThought(BasicGenerateAnswer)` | `'3,710,009'` | Wrong. CoT identifies `12! = 479,001,600` and prime sum `129` correctly but fails the final division. |
| `dspy.ProgramOfThought(BasicGenerateAnswer)` | `'3713190.697674419'` | Correct. Generated Python defines `is_prime`, `factorial`, and divides via the Python runtime. |

This is the **first wiki receipt of a CoT arithmetic failure caught and contrasted with PoT on the same prompt** — concrete demo of the *built-in sound critic* claim above.

The tutorial also walks a `MultiHopSearchWithPoT` `dspy.Module` (composing `dspy.ChainOfThought` for query generation with `dspy.ProgramOfThought(GenerateAnswer, max_iters=3)` for the final answer over [[ColBERTv2]]-retrieved Wikipedia context) on the word problem *"square of (atomic number of the metal in the gift from France to the US in the late 19th century) + (sum of digits in the first 10 primes)"* → `2025` (= 43² where 43 = 29 + 14). **First wiki receipt of a multi-hop RAG pipeline whose final answer module is `dspy.ProgramOfThought` instead of `dspy.ChainOfThought`.**

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-tutorial-program-of-thought]] — **canonical end-to-end PoT receipt**: bare `dspy.ProgramOfThought(BasicGenerateAnswer)` corrects a [[chainofthought|`dspy.ChainOfThought`]] arithmetic failure on `12!/sum-of-primes(1..30)`, then a `MultiHopSearchWithPoT` `dspy.Module` composes `dspy.ProgramOfThought(GenerateAnswer, max_iters=3)` over [[ColBERTv2]]-retrieved Wikipedia context; first wiki receipt of [[LocalSandbox|`dspy.LocalSandbox`]] as the underlying executor.
- [[dspy-async-tutorial]] — names `dspy.ProgramOfThought` in the async-surface taxonomy as one of the built-in Modules whose `acall()` form follows the universal `forward → aforward` mirror; async execution of generated code routes through the same `dspy.LocalSandbox` primitive.

## Connections

- [[DSPyModules]] — the parent abstraction.
- [[dspy-modules]] — canonical source (Module-taxonomy entry).
- [[dspy-tutorial-program-of-thought]] — canonical end-to-end PoT tutorial; CoT-vs-PoT printed receipt; `MultiHopSearchWithPoT` composition; `max_iters=3` kwarg.
- [[LocalSandbox]] — the public code-execution primitive `dspy.ProgramOfThought` wraps; `sandbox.execute(expr)` is the underlying call.
- [[DSPySignatures]] — the I/O contract the Module honors.
- [[DSPyPredict]] — the minimal primitive `dspy.ProgramOfThought` is built on top of.
- [[ChainOfThought]] — sibling Module; the *prose-reasoning* counterpart to PoT.
- [[DSPyProgrammingModel]] — names the CoT ↔ PoT swap as a canonical portability example.
- [[LLMModuloFramework]] — code execution is a sound critic in the Kambhampati-et-al. generate-test-critique framing.
- [[ProgramOfThought]] — the underlying research-paper technique (Chen et al. 2022 — *"Program of Thoughts Prompting"*). Forward reference; stub.
- [[DSPyPrediction]] — the return object after the code is executed and the answer field is filled.
