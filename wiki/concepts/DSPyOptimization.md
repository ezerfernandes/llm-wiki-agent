---
title: "DSPy Optimization"
type: concept
tags: [dspy, llm-programming, optimization, training-set, validation-set, gepa, iteration, workflow]
sources: [dspy-optimization-overview, dspy-optimizers, dspy-learn-index, dspy-evaluation-overview, dspy-metrics, dspy-data]
last_updated: 2026-05-17
---

# DSPy Optimization

**DSPy Optimization** is the **third and final stage** of [[DSPy]]'s three-stage [[dspy-learn-index|Programming → Evaluation → Optimization]] workflow — the *automated-search discipline* that turns a runnable, measurable DSPy program (the outputs of the Programming and Evaluation stages) into a **program whose dev-set metric is higher than the hand-written baseline**.

The canonical source is the [[dspy-optimization-overview|Optimization Overview]] (page 12 of 13 of the *Learn* section). The stage's load-bearing definition — *"Once you have a system and a way to evaluate it, you can use DSPy optimizers to tune the prompts or weights in your program"* — places Optimization **downstream** of both Programming and Evaluation and makes the quality of the program, metric, and training set load-bearing for the entire stage.

This concept page captures the **workflow-level** picture of optimization in DSPy — what an optimizer *is for*, what it consumes, what it produces, and how the developer iterates around it. The **catalog-level** enumeration of specific optimization algorithms ([[BootstrapFewShot]], [[BootstrapFewShotWithRandomSearch]], [[MIPROv2]], [[BootstrapFinetune]], [[GEPA]], etc.) lives on the sibling concept page [[DSPyOptimizers]] (forward reference; minted by page 13). The split mirrors the [[DSPyEvaluation]] / [[DSPyMetrics]] precedent — one page anchors the workflow, the sibling page anchors the per-algorithm machinery.

## What an optimizer takes and produces

[[dspy-optimization-overview|The Optimization Overview]] commits the framework to a **three-input, one-output** contract:

| Slot | What it is | Source | Notes |
|---|---|---|---|
| **Program** (input) | A [[DSPyModules\|`dspy.Module`]] subclass — typed [[DSPySignatures\|Signatures]] + composed sub-Modules + LM wiring | [[DSPyProgrammingModel\|Programming stage]] | The optimizer searches over the program's *parameters* (instructions, demonstrations, LM weights), **not** its structure. |
| **Metric** (input) | A `(example, pred, trace=None) -> float \| int \| bool` callable | [[DSPyEvaluation\|Evaluation stage]] ([[DSPyMetrics]]) | The **only signal the optimizer climbs**. The dual-purpose `trace` argument is what makes bootstrap-based optimizers possible — `trace is None` returns continuous scores for evaluation passes; `trace is not None` returns strict booleans for demo selection. |
| **Training set** (input) | A `list[dspy.Example]` of 30–300+ examples | [[DSPyEvaluation\|Evaluation stage]] ([[DSPyData]] / [[DSPyExample]]) | Larger than the dev set (20–200); some optimizers also consume a separate validation set. |
| **Optimized program** (output) | Same [[DSPyModules\|`dspy.Module`]] subclass, refined parameters | The optimizer | The optimized program is **the same Python class** as the input — same `forward(...)`, same sub-Modules, same Signatures; the optimizer mutates instructions / demonstrations / weight references. |

The contract is what makes the [[dspy-learn-index|three-stage model]] composable: the Programming stage's *output* (the program) and the Evaluation stage's *output* (the metric + dev/training set) compose into the Optimization stage's *input*, and the Optimization stage's *output* (the optimized program) can be re-evaluated under the same metric or returned to the Programming stage for structural revision.

## Training-set sizing — the 30/300 floor and ceiling

[[dspy-optimization-overview|The Optimization Overview]] commits the framework to an explicit **training-set-size regime**:

> *"You can often get substantial value out of 30 examples, but aim for at least 300 examples."*

The progression aligns with — but is **larger than** — [[DSPyEvaluation|the Evaluation stage's]] 20–200-example dev-set regime:

| Set | Size | Source | Purpose |
|---|---|---|---|
| **Dev set** | 20–200 examples | [[dspy-evaluation-overview]] | Diagnostic — establish baseline + qualitative failure-mode discovery |
| **Training set** | 30–300+ examples | [[dspy-optimization-overview]] | The optimizer's search-objective sample |
| **Test set** | held-out | [[dspy-data]] | Final assessment after the loop closes |

The order-of-magnitude gap between *"substantial value at 30"* and *"aim for at least 300"* mirrors [[dspy-evaluation-overview|the Evaluation Overview's]] 20–200 gap — DSPy's [[DSPyProgrammingModel|*"start simple, then grow"*]] discipline restated at the training-set layer. The 30-example floor lets a developer **try optimization early**; the 300-example target marks the *"goes a long way"* point for serious optimization work.

## The inverted 20/80 train/validation split

The page's **most non-obvious single recommendation**:

> *"For most prompt optimizers, we recommend allocating 20% of your data for training and 80% for validation, contrary to typical deep learning conventions. This is because prompt optimizers tend to overfit on small training sets."*

The conventional ML convention is 80/20 (or 70/15/15 train/val/test) — DSPy **inverts** this for most prompt optimizers because the prompt-optimization search space (instructions + demonstrations) is small enough that an optimizer can **memorize** a small training set and **generalize poorly**. A large validation set is the **overfitting defense** — the optimizer must produce a candidate that satisfies *80% of the data*, not just *the few examples it directly searched over*.

The 20/80 split is therefore not a general DSPy rule — it is a **DSPy-specific defense against a DSPy-specific failure mode**, applicable to prompt-tuning optimizers but not to weight-tuning ones, and explicitly carved out for [[GEPA]] (see below).

## The GEPA carve-out — the only named exception

[[dspy-optimization-overview|The Optimization Overview]] names **exactly one** specific optimizer — **[[GEPA]]** — and only to disclose that it **does not** follow the framework-level 20/80 recommendation:

> *"However, the GEPA optimizer follows standard ML practice — maximizing the training set size while keeping the validation set sufficiently sized to represent the downstream task distribution."*

The implication — left implicit by the page — is that GEPA's algorithm is **more robust** to overfitting on small training sets than the other prompt optimizers, and therefore benefits from the conventional ML split (large train, small val). The mechanism is deferred to page 13 ([[DSPyOptimizers|Optimizers]]); the wiki carries [[GEPA]] as a forward reference until that page lands.

The carve-out is structurally important: it tells the developer that the **20/80 split is not a universal DSPy rule** but a per-optimizer recommendation that depends on the specific algorithm's data-budget contract. Reading the page-13 per-optimizer documentation is therefore **load-bearing** before applying the 20/80 split mechanically.

## The four iteration axes

The Optimization stage is **not a black-box terminus** — when results are disappointing, the developer is expected to revise. [[dspy-optimization-overview|The Optimization Overview]] names four iteration axes via six diagnostic questions:

| Axis | Diagnostic question | Stage it points back into |
|---|---|---|
| **Data** | *Have you collected enough data?* | [[DSPyEvaluation\|Evaluation]] ([[DSPyData]] / [[DSPyExample]]) |
| **Program structure** | *Is your task well-defined? Is your program structured optimally — should you decompose, or simplify?* | [[DSPyProgrammingModel\|Programming]] |
| **Metric** | *Is your metric appropriate?* | [[DSPyEvaluation\|Evaluation]] ([[DSPyMetrics]]) |
| **Optimizer** | *Are you using the most sophisticated optimizer that fits your needs? Could DSPy Assertions or other advanced features help?* | Optimization (page 13 [[DSPyOptimizers]]) + [[DSPyAssertions]] (forward reference) |

**Three of the four axes point *back* into prior stages.** Only one stays inside the Optimization stage. The structural message: optimization is not the *last* step — it is the step that **most often forces a return to earlier stages**, because optimizer failure is usually evidence of a poorly-defined task, an inadequate metric, or insufficient data, not of a bad optimizer choice.

This makes the [[dspy-learn-index|three-stage model]] a **closed feedback loop**, not a strictly forward sequence: every stage can revise every prior stage, and the Optimization stage is the most aggressive at forcing revisions.

## The fourth artifact of the Programming Model

[[DSPyProgrammingModel|The DSPy Programming Model]] (page 2) named four orthogonal concerns a "conventional prompt" entangles:

| Concern | DSPy artifact | Operationalized by |
|---|---|---|
| **Signature** (typed I/O) | [[DSPySignatures\|Signatures]] | [[dspy-signatures]] (page 4) |
| **Adapter** (formatting/parsing) | [[DSPyAdapters\|Adapters]] | [[dspy-adapters]] (page 6) |
| **Module logic** (strategy) | [[DSPyModules\|Modules]] | [[dspy-modules]] (page 5) |
| **Manual optimization** (replaced by automation) | **Optimizers** | **This page (workflow) + page 13 (catalog)** |

The Optimization stage **is** the operationalization of the fourth concern. The Programming Model's commitment — *"DSPy is a bet on writing code instead of strings"* — would be incomplete without the automated-search layer that replaces the *"substantial trial-and-error to discover the right way to ask each LM to do this"* that conventional prompt engineering relies on.

With [[dspy-optimization-overview|this page]] ingested, the **four-artifact picture is structurally complete at the workflow level**: every concern named on the Programming Model has a corresponding source page and concept anchor. The remaining sibling ingest (page 13) will fill in the per-optimizer catalog.

## Position in the three-stage model

| Stage | What it produces | What it consumes |
|---|---|---|
| **1. Programming** | A runnable program (a [[DSPyModules\|`dspy.Module`]] subclass) | A task definition |
| **2. Evaluation** | A metric + dev set + **baseline score** | The runnable program |
| **3. Optimization** | An **optimized program** (refined parameters; higher metric than baseline) | The runnable program + the metric + a training set (30–300+ examples) + (some optimizers) a validation set |

The Optimization stage is the **third and final** stage by ordering, but **first under disappointment** — when the optimized program doesn't beat the baseline by a meaningful margin, the developer returns to the prior two stages along the four iteration axes above.

## Why the Optimization stage is **not** a black box

DSPy explicitly resists the framing of optimization as a one-shot improvement procedure. Three commitments distinguish DSPy Optimization from generic ML hyperparameter optimization:

- **Iteration spans four axes, not just hyperparameters.** The developer revises data, program structure, metric, and optimizer-choice together, not just the optimizer's hyperparameters. This is fundamentally different from a scikit-learn-style `GridSearchCV` where the program structure and metric are fixed.

- **The metric is itself iterable.** [[dspy-evaluation-overview|The Evaluation Overview's]] Step-4 recursive-metric-optimization claim — *"a powerful way to iterate is to optimize your metric itself"* — applies fully here. The optimizer's input metric can itself be optimized by an optimizer; the *"metric of the metric"* is easier to define than the original metric because the metric's output is bounded and scalar.

- **The three-stage model is a loop, not a pipeline.** The Optimization stage's failure is **evidence about the prior stages**, not just about the optimizer. *"Iterative development is key"* commits the framework to revising freely across all four axes.

## Where DSPy Optimization sits in the wiki's optimization landscape

- **vs. [[HyperparameterOptimization]] (the general concept).** Hyperparameter Optimization is *"search over the model's hyperparameters to maximize validation performance"* — a general ML notion. DSPy Optimization is the **DSPy-specific operationalization**: the hyperparameters are instructions / demonstrations / LM weights; the model is a `dspy.Module`; the validation set discipline inverts (20/80 instead of 80/20 for most optimizers). The DSPy version is **narrower** (specific to programs over LMs) and **richer** (commits to the four-iteration-axis discipline).

- **vs. [[PromptEngineering]] (manual prompt iteration).** DSPy Optimization is the **automated alternative** to hand-tuning prompts. [[dspy-programming-overview|The Programming Overview]] names this counter-position explicitly: *"manual optimization relies on substantial trial-and-error to discover the right way to ask each LM to do this"* — DSPy's optimizers replace that trial-and-error with metric-driven search.

- **vs. [[FineTuning]] (weight tuning at the LM layer).** DSPy Optimization spans **both** prompt tuning **and** weight tuning — *"tune the prompts or weights in your program"*. `BootstrapFinetune` (forward reference) bridges DSPy into the weight-tuning regime; the other prompt-only optimizers stay above the LM's parameters.

- **vs. [[GradientDescent]] (the canonical ML optimization algorithm).** DSPy prompt optimizers **do not** use gradients (no gradients are available over a string-valued search space). The optimizer family lives in the **search / sampling / bootstrapping** branch of the optimization tree; weight-tuning optimizers (`BootstrapFinetune`) bridge to gradient-based fine-tuning via the underlying LM provider's API.

- **vs. [[LLMModuloFramework|LLM-Modulo]] (Kambhampati et al.).** DSPy's Optimizer is precisely the **search procedure** layer of the Generate-Test-Critique loop — the [[DSPyMetrics|metric]] is the critic, the [[DSPyModules|program]] is the generator, the Optimizer is the search procedure over candidate generators. The mapping is clean.

- **vs. [[2604.25850-agentic-harness-engineering|Agentic Harness Engineering]] (Lee et al.).** The harness-engineering counter-position names *"DSPy-style instruction tuning"* explicitly as something the load-bearing axes are *not*. The page's emphasis on *iterating across four axes* (data / program / metric / optimizer) is **partial common ground** — AHE would say *the optimizer should also evolve the harness's tools and middleware*; DSPy doesn't make that claim. The frameworks are orthogonal: AHE iterates the harness; DSPy iterates the prompts and demonstrations inside the harness.

## Forward references — now resolved

[[dspy-optimization-overview|The Optimization Overview]] motivated the closing page of the *Learn* section. **All forward references this concept page originally carried are now resolved by [[dspy-optimizers|page 13]]** (ingested 2026-05-17):

- **[[DSPyOptimizers]]** — the **catalog-level sibling** of this page (workflow vs catalog, mirroring the [[DSPyEvaluation]] / [[DSPyMetrics]] split). Now minted by [[dspy-optimizers]]; expands the per-optimizer catalog into the eleven `dspy.<OptimizerName>` callables grouped into five families.
- **[[BootstrapFewShot]]** — the canonical 10-example demonstration-tuning optimizer. Now minted.
- **[[BootstrapFewShotWithRandomSearch]]** — the random-search-augmented 50+-example optimizer; the canonical worked-example in the general optimizer API. Now minted.
- **[[MIPROv2]]** — the framework's reference optimizer; three-stage Bayesian-search-driven joint instruction+demonstration tuner. Now minted.
- **[[BootstrapFinetune]]** — the only weight-tuning optimizer; bridges DSPy into [[FineTuning]]. Now minted.
- **[[GEPA]]** — the reflection-based instruction optimizer; the framework's named carve-out from this page's inverted 20/80 train/val split recommendation. Now minted.

The only remaining DSPy-related forward reference is **[[DSPyAssertions]]** (no scheduled ingest yet) — the advanced feature this page's diagnostic-questions list mentions as an escape hatch when optimization alone doesn't suffice; the wiki carries it as a forward reference for a possible later ingest.

## Connections

- [[DSPy]] — the framework whose third stage this concept operationalizes.
- [[dspy-optimization-overview]] — the canonical source for this concept (Optimization Overview, page 12 of 13 of the *Learn* section). Mints this page.
- [[dspy-learn-index]] — the three-stage Programming → Evaluation → Optimization workflow inside which this stage sits as the third stage.
- [[DSPyOptimizers]] — **forward reference to page 13 of 13**; will expand the optimizer catalog. Owned by a sibling ingest. The split between [[DSPyOptimization]] (this page — workflow) and [[DSPyOptimizers]] (catalog) mirrors the [[DSPyEvaluation]] / [[DSPyMetrics]] split — one page anchors the workflow, the sibling page anchors the per-algorithm machinery.
- [[DSPyProgrammingModel]] — the design philosophy from page 2; **the fourth of its four orthogonal artifacts is the optimizer**, and this page is the workflow-level operationalization of that artifact.
- [[DSPyEvaluation]] — the prior stage; this stage consumes the metric and dev/training set the Evaluation stage produces.
- [[DSPyMetrics]] — the canonical metric contract; the metric is one of the optimizer's three inputs. The dual-purpose `trace` argument is what makes bootstrap-based optimizers (e.g. `BootstrapFewShotWithRandomSearch`, forward reference) possible.
- [[DSPyEvaluate]] — the dev-set-evaluation harness whose **`trace=None`** call mode this stage's metric uses during evaluation passes (vs the **`trace=[...]`** mode used during bootstrap demo selection).
- [[DSPyData]] — the dataset-layer discipline; the training set this stage uses is a `list[dspy.Example]` per [[DSPyData]].
- [[DSPyExample]] — the per-datapoint primitive the training set is composed of.
- [[DSPyModules]] — the program this stage optimizes is a `dspy.Module` subclass; the sub-Modules registered as `self.*` attributes are what the optimizer's `named_predictors()` / `named_parameters()` walks enumerate.
- [[DSPyPredict]] — the minimal primitive Module the optimizer's parameter walk bottoms out on; the *"all other DSPy modules are built using `dspy.Predict`"* claim from page 5 is what makes the optimizer's enumeration tractable — every learnable parameter site is a `Predict` instance.
- [[DSPyPrediction]] — the typed return object every Module call produces; the metric consumes a [[DSPyPrediction|`Prediction`]] from the program against an [[DSPyExample|`Example`]] from the training set.
- [[DSPySignatures]] — the stable interface the optimizer **does not** modify; the optimizer searches over instructions / demonstrations / weights, leaving the Signature unchanged. The Signature's role as *"stable interface"* in [[DSPyProgrammingModel|the Programming Model]] is **vindicated** by the optimizer's behavior.
- [[DSPyAdapters]] — the wire-format layer the optimizer **does not** modify; the optimized prompts produced by the optimizer compose through the same Adapter as the unoptimized ones.
- [[DSPyLM]] — the LM client the program (and the metric, if it is an AI-feedback DSPy program) routes through; optimization can target the LM's *weights* (when fine-tuning is available — `BootstrapFinetune`) or just its *prompts* (every other optimizer).
- [[LiteLLM]] — the upstream provider-abstraction layer [[DSPyLM|`dspy.LM`]] routes through; relevant to weight-tuning optimizers (`BootstrapFinetune`) where provider-specific fine-tuning APIs are reached through LiteLLM.
- [[GEPA]] — the only specific optimizer named on [[dspy-optimization-overview|the Optimization Overview]]; carved out from the 20/80 split recommendation as following standard ML practice. **Forward reference**; full mechanism deferred to page 13.
- [[BootstrapFewShot]] / [[BootstrapFewShotWithRandomSearch]] / [[MIPROv2]] / [[BootstrapFinetune]] — the optimizer catalog page 13 will introduce; **forward references**.
- [[DSPyAssertions]] — advanced feature named in the diagnostic-questions list as an escape hatch when optimization alone doesn't suffice; **forward reference**.
- [[HyperparameterOptimization]] — the general ML concept this DSPy-specific concept specializes; an [[DSPyOptimizers|Optimizer]] is structurally a search over the program's *prompt-and-weight hyperparameters*.
- [[ModelEvaluation]] — the general concept the metric this stage consumes specializes.
- [[OfflineEvaluation]] — the regime this stage operates in (DSPy is pre-deployment; the optimizer climbs an offline dev/validation set, not live traffic).
- [[OverFitting]] — the failure mode the inverted 20/80 split defends against — *"prompt optimizers tend to overfit on small training sets"*.
- [[FineTuning]] — the weight-tuning regime that `BootstrapFinetune` (forward reference) operates in; the *"or weights"* half of *"tune the prompts or weights"*.
- [[GradientDescent]] — the optimization paradigm DSPy prompt optimizers **do not** use (no gradients available over a string-valued search space).
- [[PromptOptimization]] — the general concept DSPy's *"most prompt optimizers"* recommendation specializes; the 20/80 split is a DSPy-specific recommendation for the prompt-optimization sub-family.
- [[PromptEngineering]] — the manual discipline DSPy automates; the Optimization stage is the **automated alternative** to hand-tuning instructions and few-shot demonstrations.
- [[ChainOfThought]] — the default *start-simple* module from the Programming stage; an optimizer typically improves a [[ChainOfThought|`dspy.ChainOfThought`]]-based program before structural revision is considered.
- [[llmasjudge|LLM-as-judge]] — when the metric is an AI-feedback program ([[dspy-metrics|page 11]]), the optimizer's recursive *"metric of the metric"* loop ([[DSPyEvaluation|Step 4]] of the four-step Evaluation loop) is what makes the judge itself optimizable.
- [[LLMModuloFramework]] — DSPy's [[DSPyOptimizers|Optimizer]] is the **search procedure** layer of Kambhampati et al.'s generate-test-critique loop; the [[DSPyMetrics|metric]] is the *critic*, the [[DSPyModules|program]] is the *generator*, the Optimizer is what does the search.
- [[2604.25850-agentic-harness-engineering]] — the harness-engineering counter-position; this concept's emphasis on *iterating across four axes* (data / program / metric / optimizer) is **partial common ground**, but DSPy does not iterate over the harness layer (tools / middleware / memory) the way AHE does.
