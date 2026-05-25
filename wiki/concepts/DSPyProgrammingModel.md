---
title: "DSPy Programming Model"
type: concept
tags: [dspy, llm-programming, framework, separation-of-concerns]
sources: [dspy-programming-overview, dspy-learn-index]
last_updated: 2026-05-24
---

# DSPy Programming Model

The **DSPy Programming Model** is the design philosophy that defines how a developer *writes* a [[DSPy]] program — distinct from the [[dspy-learn-index|three-stage Programming → Evaluation → Optimization workflow]] of the *Learn* documentation, which is about *when* each kind of work happens. The Programming Model is **what**: it is the answer to *"how should an LLM pipeline be expressed in code?"*

The model rests on two load-bearing claims, both stated in [[dspy-programming-overview|the Programming Overview]] (page 2 of 13 of the *Learn* section):

1. **Writing code, not strings.** *"DSPy is a bet on writing code instead of strings."* An LLM pipeline is a **program** — typed inputs, typed outputs, composed control flow — not a string template that happens to be passed to a model. The string is an implementation detail the framework generates from the program.

2. **Separation of concerns.** Conventional prompts entangle four orthogonal concerns into one opaque string. DSPy factors them out as four named, separable artifacts.

## The four-concerns decomposition

[[dspy-programming-overview|The Programming Overview]] explicitly maps each concern a "conventional prompt" encodes to a named DSPy abstraction:

| Conventional-prompt concern | What it does (per the Overview) | DSPy artifact |
|---|---|---|
| **Signature** | "asks the LM to take some inputs and produce some outputs of certain types" | [[DSPySignatures\|Signatures]] |
| **Adapter** | "formats the inputs in certain ways and requests outputs in a form it can parse accurately" | [[DSPyAdapters\|Adapters]] |
| **Module logic** | "asks the LM to apply certain strategies like 'thinking step by step' or using tools" | [[DSPyModules\|Modules]] |
| **Manual optimization** | "relies on substantial trial-and-error to discover the right way to ask each LM to do this" | [[DSPyOptimizers\|Optimizers]] |

The decomposition is the **load-bearing claim** of the Programming Model: a conventional prompt couples all four into a single, non-portable string; DSPy's API gives each one a name and a contract.

## Portability claims (the consequence of separation)

[[dspy-programming-overview|The Programming Overview]] commits to three concrete portability claims that the four-concerns decomposition is supposed to underwrite:

- **Swap the LM (or its adapter)** without changing the rest of the program — re-target across providers / models / formats.
- **Swap one module for another** (e.g. `dspy.ChainOfThought` ↔ `dspy.ProgramOfThought`) without modifying the [[DSPySignatures|signature]] — the Signature is the **stable interface**; the Module is the **swappable strategy**.
- **Run prompt-optimization *or* weight fine-tuning** against the same program — the [[DSPyOptimizers|Optimization stage]] picks up either lever without forcing a program rewrite.

The first two of these are *consequences* of separation-of-concerns; the third is what licenses DSPy's both-axes (prompt + weights) optimizer story already recorded on [[DSPy]] and [[dspy-learn-index]].

## "Start simple, then grow"

[[dspy-programming-overview|The Programming Overview]] couples the four-concerns decomposition with an empirical, iteration-first discipline for *how* a developer should approach a new task:

1. **Define the task** — what are the inputs and outputs?
2. **Define the initial pipeline** — start with the smallest viable program ("perhaps with just a single `dspy.ChainOfThought` module") and **add complexity incrementally based on observations**. Decompose into multiple steps, add [[DSPyTools|tools]], or open up agentic tool use only when observation justifies it.
3. **Craft and try a handful of examples** — record both easy and hard cases for later [[DSPyMetrics|evaluation]] and [[DSPyOptimizers|optimization]].

This is the **opposite** of starting from a maximalist prompt and trimming back. The Programming Model is best read in conjunction with this discipline: separation-of-concerns is the *static* picture; "start simple, then grow" is the *dynamic* picture.

## Why it matters: contrast with the surrounding wiki

- **Against [[PromptEngineering]].** DSPy positions the Programming Model as the *automated alternative* to manual prompt engineering. The four-concerns decomposition is the *theory of what prompt engineering actually does*; DSPy's claim is that each axis can be programmed and optimized independently rather than tuned by hand as an indivisible string.
- **In tension with [[2604.25850-agentic-harness-engineering|harness engineering]].** Lee et al.'s critique of "DSPy-style instruction tuning" lands at the Programming Model level: they argue the load-bearing axes are *not* the four prompt-level concerns DSPy names, but the surrounding tools / middleware / memory. The two positions are orthogonal in principle — DSPy decouples prompt-level concerns; AHE decouples harness-level concerns — and could be composed in the same system.
- **As candidate-generator substrate for [[LLMModuloFramework|LLM-Modulo]].** Each of DSPy's four artifacts maps cleanly onto Kambhampati et al.'s generate-test loop: [[DSPyModules|Modules]] are candidate generators; [[DSPyMetrics|Metrics]] are critics; [[DSPyOptimizers|Optimizers]] are the search procedure over the generator. The Programming Model is therefore a natural substrate on which an LLM-Modulo pipeline can be expressed.
- **Inside the [[AgenticAI]] DAG framework.** A DSPy program **is** an instance of the [[AgenticAI]] DAG (Modules are nodes; inter-Module dataflow is edges); the Programming Model is the *coding interface* over the [[CompositionalCapacity|compositional substrate]] that framework formalizes.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-rag-tutorial]] — canonical end-to-end "start simple, then grow" receipt: baseline `dspy.ChainOfThought('question -> response')` → RAG with retrieval → optimized program, holding the Signature stable across all three stages.
- [[dspy-ai-text-game-tutorial]] — minimal-surface composition: three Signatures under `dspy.ChainOfThought` modules inside one `dspy.Module` subclass; the smallest worked program that exercises all four concerns at once.
- [[dspy-email-extraction-tutorial]] — composes four Signatures into a single sequential `dspy.Module` pipeline; the canonical multi-stage worked instance of *"writing code, not strings"*.
- [[dspy-customer-service-agent]] — module-swap receipt: lifts a typed-Signature pipeline to a `dspy.ReAct` agent with the Signature unchanged — the *"swap one module for another without modifying the signature"* portability claim made concrete.
- [[dspy-saving-tutorial]] — surfaces the program-as-object stance: state-only save vs whole-program `cloudpickle` save, both of which require the program *be* a typed `dspy.Module` rather than a string template.
- [[dspy-streaming-tutorial]] — orthogonal-composition receipt: token-streaming layer composes over every Module without changing the four-concern interface, proving the layering is more than naming.
- [[dspy-tutorial-program-of-thought]] — drop-in module swap (`dspy.ChainOfThought` → `dspy.ProgramOfThought`) on a fixed Signature; the receipt of the third portability claim.
- [[dspy-tutorial-gepa-aime]] — both-axes optimizer receipt: same program is later compiled by `dspy.GEPA` against a metric, exercising the "run prompt-optimization against the same program" portability claim.
- [[dspy-tutorial-classification-finetuning]] — the *weight-finetune* lever on the same Programming Model: `dspy.BootstrapFinetune` updates LM weights against the program with no architectural change.

## Connections

- [[DSPy]] — the framework this Programming Model defines.
- [[dspy-programming-overview]] — the canonical source for the model (Programming Overview, page 2 of 13).
- [[dspy-learn-index]] — the three-stage Programming → Evaluation → Optimization workflow inside which this Programming Model sits as the "Programming" stage's *how-to*.
- [[DSPySignatures]] — the typed-interface concern. Forward reference.
- [[DSPyAdapters]] — the formatting / parsing concern. Forward reference.
- [[DSPyModules]] — the strategy-logic concern; the swappable layer above a stable Signature. Forward reference.
- [[DSPyOptimizers]] — the automated-search concern; both-axes (prompt + weights). Forward reference.
- [[DSPyTools]] — the "calculator or calendar API" sub-component named on the Programming Overview. Forward reference.
- [[ChainOfThought|chain-of-thought]] — the *recommended "start simple" module* (`dspy.ChainOfThought`).
- [[PromptEngineering]] — the discipline DSPy positions itself against. Forward reference.
- [[2604.25850-agentic-harness-engineering]] — the framework whose critique of "DSPy-style instruction tuning" lands at the Programming Model level.
- [[LLMModuloFramework]] — natural complementary framework; DSPy's four artifacts map onto its generate-test-critique structure.
