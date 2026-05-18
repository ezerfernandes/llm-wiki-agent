---
title: "DSPy Learn — Programming Overview"
type: source
tags: [dspy, documentation, framework, llm-programming]
date: 2026-05-17
source_file: raw/dspy-programming-overview.md
---

# DSPy Learn — Programming Overview

Page 2 of 13 in the [[DSPy]] *Learn* documentation ([dspy.ai/learn/programming/overview/](https://dspy.ai/learn/programming/overview/)), and the opening page of the **Programming** stage from [[dspy-learn-index|the Learn index's]] three-stage model (Programming → Evaluation → Optimization). Where the [[dspy-learn-index|index page]] only sketched the three-stage pipeline, this page operationalizes the *Programming* stage as **(1) define your task → (2) define your initial pipeline → (3) craft a handful of examples**, and articulates the framework-level thesis that makes the whole approach coherent: **DSPy is a bet on *writing code instead of strings***. The page also names the four concerns DSPy factors out of "conventional prompts" — *signature*, *adapter*, *module*, *optimization* — and is the canonical anchor for DSPy's *separation-of-concerns* design philosophy.

## Summary

The Programming Overview frames DSPy's first stage as three nested sub-steps the developer iterates on: defining the task's input/output (chatbot? code assistant? translator? citation-aware report generator?), choosing an initial pipeline (single module vs decomposed steps; pure LM vs tool-augmented vs agentic; "start simple, perhaps with just a single `dspy.ChainOfThought` module, then add complexity incrementally based on observations"), and collecting a handful of input examples for later evaluation and optimization. The page's load-bearing claim is that conventional prompting **couples** system architecture with four incidental concerns — signatures, adapters, modules, manual optimization — that are **not portable** across LMs, objectives, or pipelines. DSPy **separates** these concerns and **automates** the lower-level ones, yielding shorter, more portable code: swap an LM, an adapter, or a module without touching the rest of the program, and run the same program through prompt-optimization or weight fine-tuning when ready.

## Key Claims

- **The DSPy thesis: "writing code instead of strings."** DSPy is positioned as the *programming* alternative to prompt-as-string development. *"DSPy is a bet on writing code instead of strings. In other words, building the right control flow is crucial."* This is the framework-level claim that justifies every concrete design choice downstream (typed [[DSPySignatures|Signatures]], composable [[DSPyModules|Modules]], programmatic [[DSPyOptimizers|Optimizers]]).

- **The Programming stage is three nested sub-steps.** (1) **Define your task** — what are the inputs and outputs? Is it a chatbot, code assistant, translator, snippet-highlighter, citation-aware report generator? (2) **Define your initial pipeline** — single module or multi-step decomposition? Pure LM or [[DSPyTools|tool]]-augmented (retrieval, calculator, calendar API)? Fixed workflow or open-ended agentic tool use? (3) **Craft and try a handful of examples** — record both easy and hard cases for later evaluation and optimization.

- **"Start simple."** The page's explicit advice is to begin with the smallest viable program — *"perhaps with just a single `dspy.ChainOfThought` module"* — and **add complexity incrementally based on observations**. This is the empirical, iteration-first stance that justifies DSPy's emphasis on swappable modules.

- **Conventional prompts are coupled and non-portable.** "Conventional prompts couple your fundamental system architecture with incidental choices not portable to new LMs, objectives, or pipelines." The page identifies the *four concerns* a conventional prompt entangles:
  - a **signature** — "asks the LM to take some inputs and produce some outputs of certain types"
  - an **adapter** — "formats the inputs in certain ways and requests outputs in a form it can parse accurately"
  - a **module's logic** — "asks the LM to apply certain strategies like 'thinking step by step' or using tools"
  - a **manual optimization** — "relies on substantial trial-and-error to discover the right way to ask each LM to do this"

  These four match exactly the abstractions DSPy provides as named, separable artifacts: [[DSPySignatures|Signatures]] / [[DSPyAdapters|Adapters]] / [[DSPyModules|Modules]] / [[DSPyOptimizers|Optimizers]]. This is the page that **defines the mapping** between the conventional-prompt-engineering vocabulary and DSPy's API surface.

- **Separation of concerns enables portability via swap-without-rewrite.** Three concrete portability claims:
  - **Swap the LM (or its adapter) without changing the rest of your logic.** Re-target a program from one provider/model to another without touching pipeline code.
  - **Swap one module for another (e.g. `dspy.ChainOfThought` → `dspy.ProgramOfThought`) without modifying your signatures.** The Signature is the stable interface; module choice is the swappable strategy.
  - **Run prompt-optimization *or* weight fine-tuning against the same program.** The Optimization stage operates on whichever lever is available without requiring a program rewrite. This is the wire-frame claim behind DSPy's both-axes (prompt + weights) optimizer story already noted in [[dspy-learn-index]].

- **DSPy *automates the lower-level concerns until you need to consider them*.** The framework's default is to hide adapter/format/optimization detail from the developer; surfacing them is an opt-in escape hatch, not a forced burden. This is the principle that lets DSPy programs stay short.

## Key Quotes

> "DSPy is a bet on *writing code instead of strings*. In other words, building the right control flow is crucial." — the framework-level thesis

> "Start by **defining your task**. What are the inputs to your system and what should your system produce as output?" — Programming sub-step 1

> "Next, **define your initial pipeline**. Can your DSPy program just be a single module or do you need to break it down into a few steps?" — Programming sub-step 2

> "Think about these but start simple, perhaps with just a single `dspy.ChainOfThought` module, then add complexity incrementally based on observations." — the start-simple-then-grow discipline

> "As you do this, **craft and try a handful of examples** of the inputs to your program. … Record interesting (both easy and hard) examples you try. This will be useful when you are doing evaluation and optimization later." — Programming sub-step 3 and the forward-link to the Evaluation and Optimization stages

> "Conventional prompts couple your fundamental system architecture with incidental choices not portable to new LMs, objectives, or pipelines." — the load-bearing critique of prompt-engineering-as-string

> "A conventional prompt asks the LM to take some inputs and produce some outputs of certain types (a *signature*), formats the inputs in certain ways and requests outputs in a form it can parse accurately (an *adapter*), asks the LM to apply certain strategies like 'thinking step by step' or using tools (a *module*'s logic), and relies on substantial trial-and-error to discover the right way to ask each LM to do this (a form of manual *optimization*)." — the four-concerns decomposition that defines DSPy's API surface

> "DSPy separates these concerns and automates the lower-level ones until you need to consider them. This allow you to write much shorter code, with much higher portability." — the separation-of-concerns claim

> "If you write a program using DSPy modules, you can swap the LM or its adapter without changing the rest of your logic. Or you can exchange one *module*, like `dspy.ChainOfThought`, with another, like `dspy.ProgramOfThought`, without modifying your signatures. When you're ready to use optimizers, the same program can have its prompts optimized or its LM weights fine-tuned." — three concrete portability claims

## Connections

- [[DSPy]] — the framework whose Programming stage this page documents. The page is the canonical anchor for DSPy's *writing-code-instead-of-strings* thesis and *separation-of-concerns* philosophy; both are now reflected on the entity page.
- [[dspy-learn-index]] — the parent Learn index page (page 1 of 13). The Programming Overview operationalizes the *Programming* stage that the index page only sketches.
- [[DSPyProgrammingModel]] — concept page minted by this ingest; captures the **separation-of-concerns philosophy** (Signatures / Adapters / Modules / Optimizers as the four orthogonal axes that conventional prompts entangle) and the **start-simple-then-grow** discipline.
- [[DSPySignatures]] — one of the four concerns this page names; the typed input → output spec. Forward reference to the dedicated *Signatures* sub-page (page 4 of 13).
- [[DSPyAdapters]] — the formatting / parsing layer this page names as the "adapter" concern. Forward reference to *Adapters* (page 6 of 13).
- [[DSPyModules]] — the strategy-logic layer; the page names `dspy.ChainOfThought` and `dspy.ProgramOfThought` as two interchangeable instances. Forward reference to *Modules* (page 5 of 13).
- [[DSPyTools]] — the page's "calculator or calendar API" example. Forward reference to *Tools* (page 7 of 13).
- [[DSPyOptimizers]] — the "manual optimization" concern automated by DSPy. Forward reference to *Optimizers* (page 13 of 13).
- [[LanguageModel]] — the "swap the LM" claim is the integration story covered in the next ingest (*Language Models*, page 3 of 13).
- [[ChainOfThought|chain-of-thought]] — named explicitly as the recommended "start simple" module (`dspy.ChainOfThought`).
- [[PromptEngineering]] — the discipline DSPy positions itself **against** by name on this page. Conventional prompts are "coupled" and rely on "trial-and-error"; DSPy automates the same lever. Forward reference (page not yet minted).
- [[2604.25850-agentic-harness-engineering]] — the harness-engineering paper's critique of "DSPy-style instruction tuning" lands precisely on what this page describes; this page makes the target of that critique explicit.

## Contradictions

- **Coupling-vs-decoupling, in mild tension with [[2604.25850-agentic-harness-engineering]].** The Programming Overview's central claim is that *the four conventional-prompt concerns* — signature, adapter, module logic, manual optimization — are the right axes to decouple. The harness-engineering paper argues the load-bearing component is not the prompt at all, but the surrounding tools / middleware / memory machinery. The two positions are not strictly contradictory (DSPy decouples the **prompt-level** axes; AHE makes the orthogonal claim about the **harness-level** axes), but they place very different weight on which decoupling matters. This is a refinement of the wiki's existing DSPy-vs-AHE framing already recorded on [[DSPy]] and [[2604.25850-agentic-harness-engineering]] — no new disagreement, but the Programming Overview is the first DSPy page to *name* the four prompt-level concerns at issue.
- No direct factual contradictions with existing wiki content.
