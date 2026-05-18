---
title: "DSPy Learn — Optimizers"
type: source
tags: [dspy, llm-programming, optimization, optimizers, bootstrap, mipro, gepa, bootstrap-finetune, copro, simba, knnfewshot, ensemble, bettertogether, teleprompters]
date: 2026-05-17
source_file: raw/dspy-optimizers.md
---

# DSPy Learn — Optimizers

## Summary

**Page 13 of 13** of the [[DSPy]] *Learn* documentation and the **closing page** of the [[dspy-learn-index|three-stage Programming → Evaluation → Optimization]] model. Where [[dspy-optimization-overview|the Optimization Overview]] (page 12) shipped the **workflow-level** contract (three inputs — *program + metric + training set*; one output — *optimized program*; 30/300 training-set sizing; inverted 20/80 train/val split; four iteration axes), **this page ships the catalog** — the concrete per-optimizer list `dspy.<OptimizerName>` callable surface enumerates: `LabeledFewShot` / [[BootstrapFewShot|`BootstrapFewShot`]] / [[BootstrapFewShotWithRandomSearch|`BootstrapFewShotWithRandomSearch`]] / `KNNFewShot` / `COPRO` / [[MIPROv2|`MIPROv2`]] / `SIMBA` / [[GEPA|`GEPA`]] / [[BootstrapFinetune|`BootstrapFinetune`]] / `Ensemble` / `BetterTogether`. The page also names the historical rename — *"Formerly called teleprompters. We are making an official name update."* — and reveals the **composability** claim: optimizers can be chained (`dspy.MIPROv2` then `dspy.BootstrapFinetune`, then top-k extraction into `dspy.Ensemble`) — the **structural essence** of `dspy.BetterTogether`. The page closes the DSPy *Learn* corpus at 13/13 and **resolves every long-standing forward reference** the prior twelve pages carried — [[DSPyOptimizers]], [[BootstrapFewShot]], [[BootstrapFewShotWithRandomSearch]], [[MIPROv2]], [[BootstrapFinetune]], [[GEPA]] (the only optimizer named on page 12, carved out from the 20/80 split rule). Mints the canonical concept page [[DSPyOptimizers]] (sibling to [[DSPyOptimization]] — workflow vs catalog, mirroring the [[DSPyEvaluation]] / [[DSPyMetrics]] precedent) plus three load-bearing per-optimizer concept pages — [[BootstrapFewShot]], [[MIPROv2]], [[GEPA]] — and folds the minor variants ([[BootstrapFewShotWithRandomSearch]] / [[BootstrapFinetune]] / `KNNFewShot` / `COPRO` / `SIMBA` / `Ensemble` / `BetterTogether` / `LabeledFewShot`) into the [[DSPyOptimizers]] catalog table.

## Key Claims

- **DSPy ships a concrete optimizer catalog accessible as `dspy.<OptimizerName>`.** *"Optimizers can be accessed as `dspy.<OptimizerName>` (e.g., `dspy.MIPROv2`, `dspy.BootstrapFewShot`)."* The framework's optimization surface is a small, named set of classes — not a single `dspy.optimize(...)` function — exposing the decision *"which algorithm matches my data and budget?"* to the developer rather than auto-selecting. Eleven optimizers ship in the framework as of this page, grouped into five families: **Automatic Few-Shot Learning** (`LabeledFewShot`, `BootstrapFewShot`, `BootstrapFewShotWithRandomSearch`, `KNNFewShot`), **Automatic Instruction Optimization** (`COPRO`, `MIPROv2`, `SIMBA`, `GEPA`), **Automatic Finetuning** (`BootstrapFinetune`), **Program Transformations** (`Ensemble`), and **Meta-Optimizers** (`BetterTogether`).

- **"Teleprompters" is the framework's prior name for "optimizers".** *"Formerly called teleprompters. We are making an official name update, which will be reflected throughout the library and documentation."* The page records the **lexical migration in progress** — variables named `teleprompter` still appear in the canonical worked example (*"teleprompter = dspy.BootstrapFewShotWithRandomSearch(...)"*) even as the docs adopt the new term. The wiki carries both names but anchors on **optimizer** as the canonical noun. This is the **first explicit rename disclosure** in the [[dspy-learn-index|Learn corpus]] — a reminder that DSPy's surface vocabulary is younger than its mechanism vocabulary.

- **Three axes of what an optimizer tunes.** *"Different optimizers in DSPy will tune your program's quality by **synthesizing good few-shot examples** for every module, like `dspy.BootstrapRS`, **proposing and intelligently exploring better natural-language instructions** for every prompt, like `dspy.MIPROv2` and `dspy.GEPA`, and **building datasets for your modules and using them to finetune the LM weights** in your system, like `dspy.BootstrapFinetune`."* Three orthogonal *what's being tuned* axes — **demonstrations** (the few-shot examples in each prompt) / **instructions** (the natural-language task description in each prompt) / **LM weights** (the underlying model's parameters via fine-tuning) — and each optimizer occupies a position in this 3-axis space. `MIPROv2` is the only optimizer that tunes **both** demonstrations and instructions in the same run; `BootstrapFinetune` is the only one that tunes weights; `LabeledFewShot` is the cheapest (tunes only demonstrations, doesn't even bootstrap them).

- **`MIPROv2` is the framework's reference example of how optimizers work** — and it ships a **three-stage algorithm**: (1) **bootstrapping stage** — runs the program many times on training inputs, collects input/output traces per module, filters traces by the metric to keep only those on highly-scored trajectories; (2) **grounded proposal stage** — previews the program's code, data, and traces, drafts many candidate instructions per prompt; (3) **discrete search stage** — samples training mini-batches, proposes instructions+traces combinations, evaluates candidate programs, updates a **surrogate model** ([[BayesianOptimization|Bayesian Optimization]]) that improves proposals over time. The three-stage decomposition is the **structural template** for *"how a non-trivial DSPy optimizer works"* — the page generalizes from it implicitly: every DSPy optimizer is some combination of (a) collect traces, (b) propose candidates, (c) search the candidate space against the metric.

- **Optimizers are composable.** *"You can run `dspy.MIPROv2` and use the produced program as an input to `dspy.MIPROv2` again or, say, to `dspy.BootstrapFinetune` to get better results. This is partly the essence of `dspy.BetterTogether`."* The Optimization stage's output (an optimized program) is **structurally identical** to its input (a `dspy.Module` subclass), so the same optimizer or a different one can consume it. The page records two compositional patterns: **sequential composition** (run optimizer A, then optimizer B on A's output) which `BetterTogether` formalizes for the prompt→weight→prompt sequence, and **ensemble composition** (run an optimizer, extract top-k candidate programs, wrap them in `dspy.Ensemble` for inference-time voting). Both patterns scale DSPy's *unique* **pre-inference-time compute** axis (the optimizer's budget) on top of the conventional **inference-time compute** axis (ensembles, voting, [[bestofn|best-of-N]]).

- **Optimizer choice has a concrete decision rubric tied to dataset size and compute budget.** The page ships a five-rule getting-started flowchart: **10 examples → `BootstrapFewShot`**, **50+ examples → `BootstrapFewShotWithRandomSearch`**, **want 0-shot prompts → `MIPROv2` configured for 0-shot**, **40+ trials and 200+ examples → `MIPROv2`** (full configuration), **want an efficient small-LM program after success with a large LM → `BootstrapFinetune`** (the only weight-tuner). The rubric **operationalizes** [[dspy-optimization-overview|page 12's]] *"are you using the most sophisticated optimizer that fits your needs?"* diagnostic question into a concrete map from (data, compute) → optimizer. Notably, the rubric does **not** include `GEPA`, `SIMBA`, `COPRO`, `KNNFewShot`, `Ensemble`, `BetterTogether`, or `LabeledFewShot` — those are "expert paths" left for the user to discover via the catalog.

- **Cost is on the order of cents to tens of dollars per run.** *"A typical simple optimization run costs on the order of $2 USD and takes around ten minutes ... Optimizer runs can cost as little as a few cents or up to tens of dollars, depending on your LM, dataset, and configuration."* The framework names a concrete cost ballpark — DSPy's first explicit operating-cost disclosure in the *Learn* corpus. This anchors the **research-frontier framing** from [[dspy-optimization-overview|page 12]] (*"this is an emerging paradigm"*) at the wallet level — optimization is a **finite budget**, not free.

- **Three worked end-to-end optimization receipts** demonstrate the framework's coverage:
  - **`dspy.ReAct` + `dspy.MIPROv2(auto="light")` on `HotPotQA`** — 500 train examples, `dspy.evaluate.answer_exact_match` metric, GPT-4o-mini LM; **24% → 51%** on DSPy 2.5.29 (informal). Demonstrates **prompt-only optimization of a tool-using agent** ([[react|`dspy.ReAct`]] + Wikipedia search via `dspy.ColBERTv2`).
  - **`RAG(dspy.Module)` + `dspy.MIPROv2(metric=dspy.SemanticF1(), auto="medium")`** — a [[ChainOfThought|`dspy.ChainOfThought`]]-based RAG module, `max_bootstrapped_demos=2`, `max_labeled_demos=2`; **53% → 61%** on a StackExchange subset. Demonstrates **AI-feedback-metric-driven optimization** ([[DSPyMetrics|`dspy.SemanticF1`]] is itself a DSPy module — the recursive-metric-optimization claim from [[DSPyMetrics|Step 4 of the four-step Evaluation loop]] surfaces in practice).
  - **Banking77 classification + `dspy.BootstrapFinetune` on `gpt-4o-mini-2024-07-18`** — 2000 examples, `Literal[tuple(CLASSES)]`-typed output ([[DSPySignatures|Signature]] specialization), `set_lm(...)` to fix the per-Module LM, simple `lambda x, y, trace=None: x.label == y.label` metric; **66% → 87%** on DSPy 2.5.29. Demonstrates **weight-tuning** — the only `BootstrapFinetune` worked example in the corpus, and the *only place in the entire 13-page Learn series* that `dspy.LM.set_lm(...)` and OpenAI fine-tuning are exercised.

- **`save()` / `load()` produce plain-text JSON.** *"The resulting file is in plain-text JSON format. It contains all the parameters and steps in the source program. You can always read it and see what the optimizer generated."* The optimizer's output is **inspectable**, not opaque — a developer can read the JSON and see exactly which instructions and demonstrations the optimizer chose. This is consistent with DSPy's *"writing code instead of strings"* discipline — the optimizer doesn't ship a black-box artifact; it ships a refined version of the same program structure the developer wrote.

## Key Quotes

> "A DSPy optimizer is an algorithm that can tune the parameters of a DSPy program (i.e., the prompts and/or the LM weights) to maximize the metrics you specify, like accuracy."

> "Formerly called teleprompters. We are making an official name update, which will be reflected throughout the library and documentation."

> "Different optimizers in DSPy will tune your program's quality by **synthesizing good few-shot examples** for every module, like `dspy.BootstrapRS`, **proposing and intelligently exploring better natural-language instructions** for every prompt, like `dspy.MIPROv2` and `dspy.GEPA`, and **building datasets for your modules and using them to finetune the LM weights** in your system, like `dspy.BootstrapFinetune`." — the three orthogonal what's-being-tuned axes.

> "Take the `dspy.MIPROv2` optimizer as an example. First, MIPRO starts with the **bootstrapping stage**. ... Second, MIPRO enters its **grounded proposal stage**. ... Third, MIPRO launches the **discrete search stage**." — the canonical three-stage decomposition of a non-trivial DSPy optimizer.

> "One thing that makes DSPy optimizers so powerful is that they can be composed. You can run `dspy.MIPROv2` and use the produced program as an input to `dspy.MIPROv2` again or, say, to `dspy.BootstrapFinetune` to get better results. This is partly the essence of `dspy.BetterTogether`." — the composability claim and the structural definition of `BetterTogether`.

> "If you have **very few examples** (around 10), start with `BootstrapFewShot`. If you have **more data** (50 examples or more), try `BootstrapFewShotWithRandomSearch`. ... If you have been able to use one of these with a large LM (e.g., 7B parameters or above) and need a very **efficient program**, finetune a small LM for your task with `BootstrapFinetune`." — the five-rule data-size-to-optimizer rubric.

> "A typical simple optimization run costs on the order of $2 USD and takes around ten minutes, but be careful when running optimizers with very large LMs or very large datasets. Optimizer runs can cost as little as a few cents or up to tens of dollars."

> "An informal run similar to this on DSPy 2.5.29 raises ReAct's score from 24% to 51%." (HotPotQA + MIPROv2 light) // "It improves the quality of a RAG system over a subset of StackExchange communities from 53% to 61%." // "An informal run similar to this on DSPy 2.5.29 raises GPT-4o-mini's score 66% to 87%." (Banking77 + BootstrapFinetune)

> "The resulting file is in plain-text JSON format. It contains all the parameters and steps in the source program. You can always read it and see what the optimizer generated." — the inspectability commitment.

## The optimizer catalog (full enumeration)

The page documents **eleven** optimizers grouped by family. The table below is the canonical roll-up the wiki carries forward into [[DSPyOptimizers]]:

| Family | Optimizer | What it tunes | Mechanism | Key parameters | Catalog notes |
|---|---|---|---|---|---|
| **Automatic Few-Shot** | `LabeledFewShot` | Demonstrations only | Random selection from labeled `trainset` | `k`, `trainset` | Simplest — no bootstrapping, no metric-driven validation. |
| **Automatic Few-Shot** | [[BootstrapFewShot\|`BootstrapFewShot`]] | Demonstrations only (bootstrapped + labeled) | A `teacher` module (defaults to your program) generates demos for each program stage; metric filters them — only metric-passing demos enter the "compiled" prompt | `max_labeled_demos`, `max_bootstrapped_demos`, `teacher` (optional different DSPy program) | The canonical 10-example starting point. The recommended default for *very few examples*. |
| **Automatic Few-Shot** | [[BootstrapFewShotWithRandomSearch\|`BootstrapFewShotWithRandomSearch`]] | Demonstrations only | `BootstrapFewShot` applied several times with random search over the generated demos; best program selected | `max_labeled_demos`, `max_bootstrapped_demos`, `num_candidate_programs` | The 50+-example default. Evaluates uncompiled + `LabeledFewShot` + `BootstrapFewShot`-unshuffled + N randomized `BootstrapFewShot` candidates. |
| **Automatic Few-Shot** | `KNNFewShot` | Per-example demonstrations | [[KNearestNeighbors\|k-NN]] finds nearest training examples to the input; those become the trainset for `BootstrapFewShot` | k, embeddings | Input-conditioned demo selection — different inputs get different few-shot demos. |
| **Automatic Instruction** | `COPRO` | Instructions only | Generates and refines new instructions per step; **coordinate ascent / hill-climbing** using metric + `trainset` | `depth` (number of refinement iterations) | Instruction-only optimization without Bayesian search. |
| **Automatic Instruction** | [[MIPROv2\|`MIPROv2`]] | **Both** instructions and demonstrations | Three-stage: bootstrapping → grounded proposal → discrete search via [[BayesianOptimization\|Bayesian Optimization]] | `auto="light"/"medium"/"heavy"`, `metric`, `num_threads`, `max_bootstrapped_demos`, `max_labeled_demos` | The reference example of a non-trivial optimizer. The only one that jointly optimizes instructions+demos. |
| **Automatic Instruction** | `SIMBA` | Instructions (self-reflective) | Stochastic mini-batch sampling identifies high-variability examples; LM introspectively analyzes failures and generates self-reflective improvement rules or adds successful demos | (not detailed) | Failure-mode-driven optimization. |
| **Automatic Instruction** | [[GEPA\|`GEPA`]] | Instructions (reflection-based) | LM reflects on the program's trajectory — *"what worked, what didn't"* — and proposes prompts addressing the gaps; can leverage domain-specific textual feedback | (not detailed) | The **only optimizer named on [[dspy-optimization-overview\|page 12]]** — carved out from the 20/80 train/val split (uses conventional ML split). |
| **Automatic Finetuning** | [[BootstrapFinetune\|`BootstrapFinetune`]] | LM weights | Distills a prompt-based DSPy program into weight updates — same program steps, each step run by a fine-tuned model | `metric`, `num_threads` | The only weight-tuner. The post-success efficient-deployment path. |
| **Program Transformations** | `Ensemble` | None — composition | Wraps a set of DSPy programs into one — full set or random subset | (not detailed) | The recipient of *top-k extraction* after an optimizer run; enables inference-time-compute scaling. |
| **Meta-Optimizers** | `BetterTogether` | Composition of optimizers | Sequences prompt-optimization and weight-optimization in configurable orders (e.g. prompt → weight → prompt) | (not detailed) | Empirically often outperforms either strategy alone. Operationalizes the page's *composability* claim. |

## The five-rule getting-started rubric

| If you have… | Use | Why |
|---|---|---|
| **~10 examples** | [[BootstrapFewShot\|`BootstrapFewShot`]] | Smallest data budget; metric-validated bootstrapped demos suffice. |
| **50+ examples** | [[BootstrapFewShotWithRandomSearch\|`BootstrapFewShotWithRandomSearch`]] | Enough data to search over multiple bootstrap seeds. |
| **Need 0-shot prompts** | [[MIPROv2\|`MIPROv2`]] (0-shot mode) | Instruction optimization without demonstrations in the final prompt. |
| **40+ trials + 200+ examples** | [[MIPROv2\|`MIPROv2`]] (full) | Bayesian search benefits from larger trial budget; 200+ examples avoid overfitting. |
| **Used a 7B+ LM and want efficiency** | [[BootstrapFinetune\|`BootstrapFinetune`]] | Distill prompt-based behavior into a smaller fine-tuned model. |

## The general API

Every optimizer shares the same surface:

```python
import dspy

config = dict(max_bootstrapped_demos=4, max_labeled_demos=4, num_candidate_programs=10, num_threads=4)
teleprompter = dspy.BootstrapFewShotWithRandomSearch(metric=YOUR_METRIC_HERE, **config)
optimized_program = teleprompter.compile(YOUR_PROGRAM_HERE, trainset=YOUR_TRAINSET_HERE)
```

Two methods make up the lifecycle:

- **`Optimizer(metric=..., **config)`** — constructor receives the metric (and optimizer-specific hyperparameters).
- **`.compile(program, trainset=...)`** — consumes the program and training set; returns an optimized program of the **same class**.

The variable name `teleprompter` in the canonical example is a legacy holdover from before the rename. The page does not change it — `teleprompter` is still the *de-facto* idiomatic local-variable name in the framework's worked examples.

## Save / load: the inspectability commitment

```python
optimized_program.save(YOUR_SAVE_PATH)

loaded_program = YOUR_PROGRAM_CLASS()
loaded_program.load(path=YOUR_SAVE_PATH)
```

The saved file is plain-text JSON containing all parameters and steps. A developer can `cat` it and see exactly which instructions and demonstrations the optimizer chose. This consistency with the *"writing code instead of strings"* discipline ([[DSPyProgrammingModel|the Programming Model]]) is structurally important — the optimizer's output is not a separate artifact (a `*.pt` weight file, a fine-tuned model handle) but a **refined version of the same program** the developer wrote.

## Closing the *Learn* corpus at 13/13

This page is the **final** of the 13 *Learn* sub-pages opened by [[dspy-learn-index|the Learn index]] on 2026-05-17:

| # | Source | Stage | Concept anchor(s) minted |
|---|---|---|---|
| 1 | [[dspy-learn-index]] | Index | — (the three-stage model is captured on [[DSPy]]) |
| 2 | [[dspy-programming-overview]] | Programming | [[DSPyProgrammingModel]] |
| 3 | [[dspy-language-models]] | Programming | [[DSPyLM]], [[LiteLLM]], [[Ollama]], [[SGLang]], [[TogetherAI]] |
| 4 | [[dspy-signatures]] | Programming | [[DSPySignatures]] |
| 5 | [[dspy-modules]] | Programming | [[DSPyModules]], [[DSPyPredict]], [[DSPyProgramOfThought]], [[DSPyMultiChainComparison]], [[DSPyRecursiveLanguageModel]], [[DSPyMajority]], [[DSPyPrediction]] |
| 6 | [[dspy-adapters]] | Programming | [[DSPyAdapters]] |
| 7 | [[dspy-tools]] | Programming | [[DSPyTools]] |
| 8 | [[dspy-mcp]] | Programming | [[ModelContextProtocol]], [[DSPyMCP]] |
| 9 | [[dspy-evaluation-overview]] | Evaluation | [[DSPyEvaluation]] |
| 10 | [[dspy-data]] | Evaluation | [[DSPyExample]], [[DSPyData]] |
| 11 | [[dspy-metrics]] | Evaluation | [[DSPyMetrics]], [[DSPyEvaluate]] |
| 12 | [[dspy-optimization-overview]] | Optimization | [[DSPyOptimization]] |
| **13** | **[[dspy-optimizers]] (this page)** | **Optimization** | **[[DSPyOptimizers]], [[BootstrapFewShot]], [[MIPROv2]], [[GEPA]], [[BootstrapFinetune]], [[BootstrapFewShotWithRandomSearch]]** |

With this page ingested, **every forward reference carried by the prior twelve DSPy ingests is resolved** at the per-optimizer catalog level. The [[DSPyOptimization]] (workflow) / [[DSPyOptimizers]] (catalog) split mirrors the [[DSPyEvaluation]] (workflow) / [[DSPyMetrics]] (catalog) precedent — one page anchors the **stage's discipline**, the sibling page anchors the **per-algorithm machinery**. The four orthogonal concerns named on [[DSPyProgrammingModel|the Programming Model]] now have **complete coverage** at both the workflow and catalog levels:

| Concern | Workflow anchor | Catalog anchor |
|---|---|---|
| **Signatures** | [[dspy-signatures]] | [[DSPySignatures]] |
| **Modules** | [[dspy-modules]] | [[DSPyModules]] + 6 module pages |
| **Adapters** | [[dspy-adapters]] | [[DSPyAdapters]] |
| **Optimizers** | [[DSPyOptimization]] (workflow) | [[DSPyOptimizers]] (this catalog) |

The fifth, half-stage concern — **Evaluation as the connective stage** between Programming and Optimization — is also complete: [[DSPyEvaluation]] (workflow), [[DSPyMetrics]] / [[DSPyData]] / [[DSPyExample]] / [[DSPyEvaluate]] (catalog).

## Connections

- [[DSPy]] — the framework whose third-stage catalog this page documents.
- [[dspy-learn-index]] — the three-stage Programming → Evaluation → Optimization workflow inside which this page is **the final sub-page**.
- [[dspy-optimization-overview]] — the workflow-level sibling (page 12); the **catalog** this page ships is the *"how"* to that page's *"what"*.
- [[DSPyOptimization]] — the workflow-level concept this page's catalog-level concept [[DSPyOptimizers]] is the sibling of. The split mirrors [[DSPyEvaluation]] / [[DSPyMetrics]].
- [[DSPyOptimizers]] — the canonical concept page minted by this ingest; the per-optimizer catalog.
- [[BootstrapFewShot]] — the canonical 10-example optimizer; the **first metric-driven optimizer** the page introduces.
- [[BootstrapFewShotWithRandomSearch]] — the canonical 50+-example optimizer; the canonical worked-example in the *general API* section.
- [[MIPROv2]] — the framework's **reference optimizer** — the three-stage example, the worked ReAct receipt (24%→51%), the worked RAG receipt (53%→61%), and the joint instruction+demonstration optimizer.
- [[GEPA]] — the only optimizer named on [[dspy-optimization-overview|page 12]]; the **named carve-out** from the 20/80 train/val split. Resolves the forward reference carried by [[DSPyOptimization]].
- [[BootstrapFinetune]] — the only weight-tuning optimizer; the post-success efficient-deployment path; the Banking77 worked receipt (66%→87%). Bridges DSPy into the [[FineTuning]] regime.
- [[DSPyEvaluation]] — the prior stage; this page's optimizers consume the metric + training set produced by the Evaluation stage.
- [[DSPyMetrics]] — the metric contract; every optimizer's first kwarg is `metric=...`. The **dual-purpose `trace` argument** is what enables bootstrap-based optimizers (`BootstrapFewShot` / `BootstrapFewShotWithRandomSearch` / `KNNFewShot` / `MIPROv2`).
- [[DSPyData]] / [[DSPyExample]] — the training-set primitive every `.compile(program, trainset=...)` call consumes.
- [[DSPyModules]] — every optimizer takes a [[DSPyModules|`dspy.Module`]] subclass and returns one of the same class. The `Hop`-style multi-Module composition pattern from [[dspy-modules]] is what the optimizer's `named_predictors()` walk enumerates.
- [[DSPyPredict]] — every learnable parameter site bottoms out on a [[DSPyPredict|`dspy.Predict`]] instance; the optimizer's instruction/demonstration mutations target Predict's `signature` and `demos` attributes.
- [[DSPyLM]] — the LM the optimizer's program calls through; `BootstrapFinetune` is the only optimizer that targets the LM's **weights** rather than its prompts. The Banking77 receipt's `classify.set_lm(lm)` is the only `set_lm(...)` exercise in the corpus.
- [[ChainOfThought]] — the canonical starting Module used in the RAG worked receipt.
- [[react|ReAct]] — the tool-using agent used in the HotPotQA worked receipt.
- [[BayesianOptimization]] — the surrogate-model-based search procedure [[MIPROv2|`MIPROv2`]]'s discrete-search stage uses.
- [[KNearestNeighbors]] — the algorithm `KNNFewShot` uses to pick per-input demonstrations.
- [[FineTuning]] — the weight-tuning regime [[BootstrapFinetune|`BootstrapFinetune`]] operates in. DSPy's *"tune the prompts or weights"* commitment is fully realized by this optimizer's existence.
- [[HyperparameterOptimization]] — the general ML concept the DSPy optimizer family specializes (over a prompt-and-weight search space).
- [[bestofn]] — the inference-time-compute axis the `Ensemble` + top-k-extraction pattern operationalizes. DSPy's *pre-inference-time compute* (the optimizer's budget) **and** *inference-time compute* (the ensemble's vote) can be scaled together.
- [[llmasjudge]] — the `dspy.SemanticF1()` metric in the RAG worked receipt is an LLM-as-judge metric. The recursive-metric-optimization claim from [[DSPyMetrics|Step 4 of the four-step Evaluation loop]] is implicitly exercised: an LLM-as-judge metric scoring an optimization run is a DSPy program scoring another DSPy program.
- [[PromptOptimization]] — the general activity DSPy's prompt-tuning optimizers (`MIPROv2` / `GEPA` / `COPRO` / `SIMBA` / `BootstrapFewShot*`) operationalize.
- [[PromptEngineering]] — the manual discipline DSPy automates. This page is **the catalog of automated alternatives** to hand-tuning prompts.
- [[LLMModuloFramework]] — DSPy's optimizer is the *search procedure* layer of the generate-test-critique loop; the metric is the *critic*, the program is the *generator*, the optimizer is what does the search. Every optimizer in the catalog is a different search strategy.

## Contradictions

- **None.** The page **extends** every prior DSPy ingest by minting the catalog of specific algorithms the prior twelve pages deferred to it. The 20/80 split recommendation from [[dspy-optimization-overview|page 12]] is **operationalized** by this page's per-optimizer family structure — three of the four families are prompt optimizers (where the 20/80 split applies); `BootstrapFinetune` (the weight-tuning family) is implicitly outside the 20/80 recommendation since the rationale (*prompt optimizers tend to overfit on small training sets*) doesn't apply to weight optimizers; [[GEPA|`GEPA`]] is the named exception from page 12 (uses conventional ML split). The page is **fully consistent** with the workflow-level commitments from page 12.

- One **productive new claim** the wiki captures for the first time: **DSPy optimizers are first-class composable units**. The Optimization stage's output is structurally identical to its input — a `dspy.Module` subclass — which makes *"run optimizer A, then run optimizer B on A's output"* a one-line operation. This is **structurally novel** relative to conventional ML hyperparameter optimization, where a `GridSearchCV` doesn't typically consume another `GridSearchCV`'s output as input. The `dspy.BetterTogether` meta-optimizer is what happens when this composability is **formalized as a sequence schedule** (prompt → weight → prompt).
