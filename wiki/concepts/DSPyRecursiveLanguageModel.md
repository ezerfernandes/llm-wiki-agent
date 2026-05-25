---
title: "DSPy Recursive Language Model"
type: concept
tags: [dspy, llm-programming, modules, recursion, context-overflow, sandbox]
sources: [dspy-modules]
last_updated: 2026-05-24
---

# DSPy Recursive Language Model

**`dspy.RLM`** — the **Recursive Language Model** — is a [[DSPyModules|DSPy built-in Module]] designed for cases where **the context is too large to fit in a single prompt**. From [[dspy-modules|the Modules page]]:

> "`dspy.RLM`: A Recursive Language Model that explores large contexts through a sandboxed Python REPL with recursive sub-LLM calls. Use when context is too large to fit in the prompt effectively."

It is DSPy's structural answer to the **context-overflow** problem — distinct from the retrieval-augmented-generation answer ([[ChainOfThought|`dspy.ChainOfThought`]] over a `'context, question -> response'` signature with an external `search(...)` callable) and distinct from the *summarize-then-answer* answer.

## Mechanism

The two load-bearing pieces of the strategy are:

1. **A sandboxed Python REPL.** The Module gives the LM a Python execution environment to *explore* the context — slice it, search it, summarize chunks of it, run computations on it. The sandbox is the boundary that contains the LM's side effects.

2. **Recursive sub-LLM calls.** Within the REPL, the LM can invoke sub-LMs on sub-contexts — a recursion the framework orchestrates rather than the user. The recursion terminates when a sub-call produces an output that satisfies the outer Signature.

This is structurally different from the [[DSPyModules|other built-in Modules]] in two ways:

- **Recursion as a first-class control structure.** No other built-in Module recurses; `dspy.MultiChainComparison` and `dspy.ReAct` loop but do not call sub-LMs on sub-contexts.
- **Execution-environment-as-strategy.** No other built-in Module ships with a sandboxed runtime; `dspy.ProgramOfThought` executes code but for *answer adjudication*, not for *context exploration*.

## When to use it

[[dspy-modules|The Modules page]] is precise about the use case: *"when context is too large to fit in the prompt effectively."* This distinguishes `dspy.RLM` from:

| Strategy | Use when |
|---|---|
| **RAG** ([[ChainOfThought\|`dspy.ChainOfThought`]] over `'context, question -> response'` with `search(...)`) | The relevant facts are a **small subset** of a corpus you can retrieve from. |
| **Map-reduce-style summarization** | The full context is needed but can be **summarized losslessly** to fit the budget. |
| **`dspy.RLM`** | The context is **too large to fit** even after retrieval, and an LM-driven recursive exploration is the right way to find what matters. |

## Position in the module taxonomy

| Module | Strategic primitive | Context budget |
|---|---|---|
| [[DSPyPredict\|`dspy.Predict`]] | Direct call | One prompt. |
| [[ChainOfThought\|`dspy.ChainOfThought`]] | Reasoning prose | One prompt. |
| [[DSPyProgramOfThought\|`dspy.ProgramOfThought`]] | Code execution | One prompt + code runtime. |
| [[react\|`dspy.ReAct`]] | Tool calls in a loop | One prompt + external tools. |
| [[DSPyMultiChainComparison\|`dspy.MultiChainComparison`]] | N CoT + final comparison | N+1 prompts. |
| **`dspy.RLM`** | **Recursive sub-LLM calls in a sandboxed REPL** | **Larger than one prompt; unbounded by recursion depth.** |

## Why this matters

- **Carries recursion as a built-in.** Most LLM frameworks treat context-overflow as a model-side problem (bigger windows, retrieval, hierarchical summarization); DSPy makes recursion a first-class Module. The user writes `dspy.RLM('massive_context, question -> answer')`; the framework handles the recursive decomposition.
- **Sandbox as a sound critic.** The Python REPL is a deterministic execution boundary in the same [[LLMModuloFramework|LLM-Modulo]] sense `dspy.ProgramOfThought` exploits — but applied to **context exploration** rather than to **answer adjudication**.
- **Composes with the other Modules.** `dspy.RLM` returns a `dspy.Prediction(...)` honoring the user-declared Signature, so it slots into any `class MyProgram(dspy.Module)` `forward()` body that another Module would.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-async-tutorial]] — names `dspy.RLM` in the async-surface taxonomy as one of the built-in Modules whose `acall()` form follows the universal `forward → aforward` mirror; no standalone end-to-end RLM receipt yet in the wiki corpus.

## Connections

- [[DSPyModules]] — the parent abstraction.
- [[dspy-modules]] — canonical source.
- [[DSPySignatures]] — the user-declared Signature `dspy.RLM` honors.
- [[DSPyPredict]] — the recursive sub-LLM calls each ultimately decompose to a Predict at the leaves.
- [[DSPyProgramOfThought]] — sibling Module that also uses code execution, but for answer adjudication rather than context exploration.
- [[react|ReAct]] — sibling Module that also loops, but over external tool calls rather than recursive sub-LLM calls.
- [[DSPyPrediction]] — the return object.
- [[LongContext]] — the underlying NLP problem `dspy.RLM` is designed for. Forward reference; stub.
- [[RetrievalAugmentedGeneration]] — the alternative strategy for cases where the relevant facts are a retrievable subset.
- [[LLMModuloFramework]] — the sandboxed Python REPL is a sound execution boundary in the Kambhampati-et-al. generate-test framing.
