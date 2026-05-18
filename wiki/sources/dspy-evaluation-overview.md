---
title: "DSPy Learn — Evaluation Overview"
type: source
tags: [dspy, llm-programming, evaluation, metrics, development-set, iteration]
date: 2026-05-17
source_file: raw/dspy-evaluation-overview.md
---

# DSPy Learn — Evaluation Overview

## Summary

**Page 9 of 13** of the [[DSPy]] *Learn* documentation and the **opening page of the Evaluation stage** in the [[dspy-learn-index|three-stage Programming → Evaluation → Optimization]] model. Where the Programming stage (pages 2–8) defined *how to express* a DSPy program ([[DSPySignatures|Signatures]] / [[DSPyModules|Modules]] / [[DSPyAdapters|Adapters]] / [[DSPyTools|Tools]] / [[ModelContextProtocol|MCP]] under the [[DSPyProgrammingModel|Programming Model]]), this page defines *how to measure* a DSPy program before any [[DSPyOptimizers|optimization]] is attempted. The page motivates and frames the next two pages — **Data Handling** (page 10) and **[[DSPyMetrics|Metrics]]** (page 11) — by walking the **iterative-evaluation loop** at framework level: (1) collect an initial development set, (2) define a DSPy metric, (3) run development evaluations on the pipeline, (4) — recursively — *optimize the metric itself* when the metric is a DSPy program. The page is short and load-bearing: it commits the framework to two non-trivial claims (data-set size — *"Even 20 input examples of your task can be useful, though 200 goes a long way"*; intermediate-step-label exemption — *"You almost never need labels for the intermediate steps in your program in DSPy"*) and to one recursive-iteration insight (*"If your metric is itself a DSPy program, a powerful way to iterate is to optimize your metric itself"*). Mints the [[DSPyEvaluation]] concept page as the canonical anchor for DSPy's evaluation philosophy.

## Key Claims

- **The Evaluation stage opens with data collection, not with metric definition.** *"Once you have an initial system, it's time to **collect an initial development set** so you can refine it more systematically."* The page reverses the naive order *"define what good looks like, then measure"* — DSPy puts **data** first because the metric will be iterated against the data, not vice versa. The implicit framing: a metric defined without data in hand is a guess; a metric defined against 20–200 worked examples is grounded.

- **Dev-set size is small and explicit.** *"Even 20 input examples of your task can be useful, though 200 goes a long way."* The page commits the framework to a **20–200-example regime** for initial development sets. This is in deliberate contrast to the ML-training tradition of thousands-to-millions of examples — the Evaluation stage is **not** training; it is *diagnostic*, and 20 examples are enough to discriminate among pipeline designs.

- **Label requirements depend on the metric, not the program.** *"Depending on your _metric_, you either just need inputs and no labels at all, or you need inputs and the _final_ outputs of your system."* Two regimes: **reference-free metrics** (inputs only — e.g. LLM-as-judge over a rubric, or any heuristic on the output itself) and **reference-based metrics** (inputs + ground-truth final outputs — e.g. exact-match, F1, BLEU). The shape of the data the developer collects is **determined by the metric**, which is determined by the task — not by the model or the pipeline.

- **Intermediate-step labels are almost never needed.** *"(You almost never need labels for the intermediate steps in your program in DSPy.)"* This is a non-trivial DSPy-specific commitment: even though a [[DSPyModules|Module]] like [[ChainOfThought|`dspy.ChainOfThought`]] produces a `reasoning` field and a [[react|`dspy.ReAct`]] agent produces a `trajectory`, the developer does **not** need to label what the correct reasoning or trajectory would have been. The metric is computed against **final outputs only**; intermediate-step quality is implicit and is the [[DSPyOptimizers|Optimizer's]] job to discover. This is the framework's structural answer to the *intermediate-supervision problem* in chain-of-thought training.

- **Data sourcing has four ranked options.** The page lists: (1) **adjacent public datasets** — *"You can probably find datasets that are adjacent to your task on, say, HuggingFace datasets or in a naturally occurring source like StackExchange"*; (2) **permissive-license re-use** — *"If there's data whose licenses are permissive enough, we suggest you use them"*; (3) **manual labeling** — *"you can label a few examples by hand"*; (4) **deployed-demo collection** — *"start deploying a demo of your system and collect initial data that way"*. The four-option ranking is **operational guidance**, not just a list — find data before you write data.

- **Metrics are programs, not numbers.** *"A metric is a function that takes examples from your data and takes the output of your system, and returns a score."* The metric is a **callable** with a `(example, prediction) -> score` contract. This is the **interface** between the Evaluation and Optimization stages — [[DSPyOptimizers|Optimizers]] consume metrics by calling them; metrics consume the [[DSPyPrediction|Prediction]] objects [[DSPyModules|Modules]] return. The metric is not a string description, not a number, and not a static threshold — it is **executable Python**.

- **Simple-task metrics are scalar; long-form-task metrics are programs.** *"For simple tasks, this could be just "accuracy", e.g. for simple classification or short-form QA tasks. For most applications, your system will produce long-form outputs, so your metric will be a smaller DSPy program that checks multiple properties of the output."* The page commits the framework to a **two-regime metric story**: classification / short-form QA gets a one-line accuracy function; everything else gets a **multi-property checker built as a DSPy program**. The metric for a long-form task is itself a `dspy.Predict` or `dspy.ChainOfThought` invocation that scores multiple properties — what the wiki has previously recorded as **[[llmasjudge|LLM-as-judge]]** at the metric layer.

- **Metric definition is iterative.** *"Invest in defining metrics and improving them incrementally over time; it's hard to consistently improve what you aren't able to define."* The page commits the framework to the position that **the metric itself is a moving target the developer iterates on**, not a fixed contract supplied up-front. *"Getting this right on the first try is unlikely: start with something simple and iterate."* This is the [[DSPyProgrammingModel|"start simple, then grow"]] discipline from page 2 applied to the metric layer — and it implies the metric, like the program, has versions over the project's lifetime.

- **Development evaluation produces a baseline plus a diagnostic.** *"Now that you have some data and a metric, run development evaluations on your pipeline designs to understand their tradeoffs. Look at the outputs and the metric scores. This will probably allow you to spot any major issues, and it will define a baseline for your next steps."* Evaluation yields **two outputs**: (1) a **numerical baseline** the [[DSPyOptimizers|Optimization stage]] will attempt to beat, and (2) a **qualitative diagnostic** — *"spot any major issues"* — that may force the developer to *go back to Programming* rather than proceed to Optimization. This is the wiki's first explicit record of the **Evaluation → back-to-Programming feedback edge** in the three-stage model; the loop is not strictly forward.

- **Recursive optimization: a DSPy-program metric is itself optimizable.** *"If your metric is itself a DSPy program, a powerful way to iterate is to optimize your metric itself. That's usually easy because the output of the metric is usually a simple value (e.g., a score out of 5), so the metric's metric is easy to define and optimize by collecting a few examples."* This is the page's most distinctive structural claim: when the metric is a [[DSPyModules|`dspy.Module`]] (e.g. a multi-property LLM-as-judge program), it can be **optimized** by a [[DSPyOptimizers|DSPy Optimizer]] *the same way* the system program is. The "metric of the metric" is easier to define than the metric because the metric's output is **bounded and scalar** (e.g. *"a score out of 5"*), so even a few labeled examples suffice. This makes the Evaluation stage **recursively self-improving** — a structurally novel claim no other LLM-evaluation framework the wiki has recorded makes explicitly.

- **The Evaluation stage motivates the next two pages.** The Overview is **load-bearing for the entire stage**: page 10 (Data Handling) will expand the *"collect an initial development set"* sub-step into [[DSPyExample|`dspy.Example`]] / dev-set / train-set / test-set mechanics; page 11 ([[DSPyMetrics|Metrics]]) will expand the *"define your DSPy metric"* sub-step into the `(example, prediction) -> score` contract and its sub-types. Both pages are forward references this Overview commits to.

## Key Quotes

> "Once you have an initial system, it's time to **collect an initial development set** so you can refine it more systematically." — opens the Evaluation stage; commits the framework to *data-before-metric* ordering.

> "Even 20 input examples of your task can be useful, though 200 goes a long way." — the explicit 20–200 dev-set size regime.

> "You almost never need labels for the intermediate steps in your program in DSPy." — the structural exemption from intermediate-supervision labeling.

> "Next, you should **define your DSPy metric**. What makes outputs from your system good or bad?" — the metric question stated in its plainest form.

> "Invest in defining metrics and improving them incrementally over time; it's hard to consistently improve what you aren't able to define." — the wiki's first explicit DSPy commitment to *measurement before improvement*.

> "A metric is a function that takes examples from your data and takes the output of your system, and returns a score." — the canonical metric contract.

> "For simple tasks, this could be just 'accuracy', e.g. for simple classification or short-form QA tasks. For most applications, your system will produce long-form outputs, so your metric will be a smaller DSPy program that checks multiple properties of the output." — the two-regime metric story.

> "Getting this right on the first try is unlikely: start with something simple and iterate." — the *start-simple-then-grow* discipline restated at the metric layer.

> "Now that you have some data and a metric, run development evaluations on your pipeline designs to understand their tradeoffs. Look at the outputs and the metric scores. This will probably allow you to spot any major issues, and it will define a baseline for your next steps." — the canonical Evaluation-stage loop.

> "If your metric is itself a DSPy program, a powerful way to iterate is to optimize your metric itself. That's usually easy because the output of the metric is usually a simple value (e.g., a score out of 5), so the metric's metric is easy to define and optimize by collecting a few examples." — the recursive-self-improvement claim.

## The iterative-evaluation loop

The Overview operationalizes the Evaluation stage as a **four-step loop**, the last of which is recursive:

| Step | Action | Output |
|---|---|---|
| **1** | Collect 20–200 input examples (inputs only or inputs + final outputs, depending on the metric) | A **development set** |
| **2** | Define a DSPy metric — scalar `accuracy` for simple tasks, a small DSPy program for long-form tasks | A **`(example, prediction) -> score`** function |
| **3** | Run development evaluations on the pipeline designs — look at outputs and scores | A **baseline score** + a **qualitative diagnostic** |
| **4** | *(If the metric is itself a DSPy program)* Optimize the metric using a small "metric of the metric" labeled set | A **better metric** that feeds back into Step 3 |

Step 4 makes the loop **non-linear**: the developer can return from Step 3 to Step 2 (to iterate the metric) or to Step 1 (to expand or relabel the dev set) before ever proceeding to the [[DSPyOptimizers|Optimization stage]].

## Connections

- [[DSPy]] — the framework whose Evaluation stage this Overview opens. The page belongs to the *Learn* section's middle stage and is the canonical source for DSPy's evaluation philosophy.
- [[dspy-learn-index]] — the three-stage Programming → Evaluation → Optimization model; this page is the **entry point** of the Evaluation stage the index defines.
- [[DSPyEvaluation]] — the canonical concept page minted by this ingest; captures the four-step loop, the 20–200 dev-set commitment, the intermediate-step-label exemption, and the recursive-self-improvement claim.
- [[DSPyProgrammingModel]] — the design philosophy from the Programming stage; the Evaluation stage's [[DSPyMetrics|metric layer]] is the **contract** between the Programming Model's four artifacts and the [[DSPyOptimizers|Optimization stage]].
- [[DSPyMetrics]] — forward reference to **page 11 of 13** of the *Learn* section, which will expand the *"define your DSPy metric"* sub-step into the full `(example, prediction) -> score` contract and its sub-types. Owned by a sibling ingest.
- [[DSPyData]] — forward reference to **page 10 of 13** of the *Learn* section, which will expand the *"collect an initial development set"* sub-step into [[DSPyExample|`dspy.Example`]] / dev-set / train-set / test-set mechanics. Owned by a sibling ingest.
- [[DSPyOptimizers]] — forward reference to **page 13 of 13**; the metric the Evaluation stage produces is what the Optimizer consumes. The Evaluation stage is a **prerequisite** for Optimization in DSPy's load-bearing stage-order discipline.
- [[DSPyModules]] — the metric, when complex, is itself a [[DSPyModules|`dspy.Module`]] (typically a `dspy.Predict` or `dspy.ChainOfThought` over a *"score multiple properties"* signature) — i.e. a metric is a program with the same shape as the program it scores.
- [[DSPyPrediction]] — the metric's second argument is a `dspy.Prediction` (the [[DSPyModules|Module]]'s return type); the metric reads the prediction's output fields as attributes.
- [[ChainOfThought]] — multi-property long-form metrics are typically a [[DSPyModules|`dspy.ChainOfThought`]] invocation over a rubric Signature.
- [[llmasjudge|LLM-as-judge]] — the long-form-task metric regime the Overview names without using the term — *"your metric will be a smaller DSPy program that checks multiple properties of the output"* is the [[DSPy]]-specific operationalization of the LLM-as-judge pattern documented elsewhere in the wiki.
- [[DevelopmentSet]] — the 20–200-example dev set the Overview names. Forward reference if not yet minted; otherwise re-used.
- [[ModelEvaluation]] — the general wiki concept the [[DSPyEvaluation]] specializes; provides the broader "measure model quality on a held-out set" framing the DSPy Overview inherits.
- [[OfflineEvaluation]] — DSPy's development-evaluation step is **offline** (run against a held-out dev set, not against live traffic); contrasts with [[OnlineEvaluation]] (A/B tests over live users) which DSPy's Overview does not address.
- [[PromptEngineering]] — the manual baseline DSPy displaces; the Overview's *"start with something simple and iterate"* discipline is the structurally automated analog of the prompt-engineer's iteration loop.
- [[dspy-programming-overview]] — page 2 of 13; the Programming Overview's *"start simple, then grow"* discipline is restated at the metric layer on this page.
- [[dspy-modules]] — page 5 of 13; defines [[DSPyModules|`dspy.Module`]] and [[DSPyPrediction|`dspy.Prediction`]], the substrate the metric reads from.

## Contradictions

- **None new.** The Evaluation Overview is consistent with every prior DSPy ingest:
  - It **confirms** the [[dspy-learn-index|three-stage model]] (Programming → Evaluation → Optimization) and the stage-order claim *"it's unproductive to launch optimization runs using a poorly designed program or a bad metric"*: the page is exactly the document that fills in the middle stage that load-bearing claim presupposes.
  - It **extends** the [[DSPyProgrammingModel|"start simple, then grow"]] discipline from the program layer (page 2) to the **metric layer**.
  - It **vindicates** the [[DSPyModules|Module]] / [[DSPyPrediction|Prediction]] abstractions from page 5 — the metric reads a `Prediction`'s output fields by attribute access; nothing new is asked of the Module side.
- **One framing nuance to track.** The page does not call the metric a [[DSPyModules|`dspy.Module`]] explicitly even when it is a DSPy program — it calls it *"a smaller DSPy program that checks multiple properties of the output"*. The [[DSPyMetrics|Metrics page]] (page 11) will likely sharpen this; the wiki should defer to that page rather than assert a metric *is* a `dspy.Module` from this page alone.
