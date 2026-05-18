---
title: "DSPy Learn — Optimization Overview"
type: source
tags: [dspy, llm-programming, optimization, optimizers, training-set, validation-set, gepa, iteration]
date: 2026-05-17
source_file: raw/dspy-optimization-overview.md
---

# DSPy Learn — Optimization Overview

## Summary

**Page 12 of 13** of the [[DSPy]] *Learn* documentation and the **opening page of the Optimization stage** in the [[dspy-learn-index|three-stage Programming → Evaluation → Optimization]] model. Where the Programming stage (pages 2–8) defined *how to express* a DSPy program ([[DSPySignatures|Signatures]] / [[DSPyModules|Modules]] / [[DSPyAdapters|Adapters]] / [[DSPyTools|Tools]] / [[ModelContextProtocol|MCP]] under the [[DSPyProgrammingModel|Programming Model]]) and the Evaluation stage (pages 9–11) defined *how to measure* one ([[DSPyEvaluation]] / [[DSPyData]] / [[DSPyExample]] / [[DSPyMetrics]] / [[DSPyEvaluate]]), **this page defines *how to improve* one** — the framework-level framing of what a [[DSPyOptimizers|DSPy Optimizer]] is and what inputs it consumes. The page is short and load-bearing in the same way [[dspy-evaluation-overview|the Evaluation Overview]] was: it doesn't ship a per-optimizer recipe (that lands on page 13), it ships the *workflow-level contract* — *"Once you have a system and a way to evaluate it, you can use DSPy optimizers to tune the prompts or weights in your program."* The page commits the framework to four non-trivial positions: (1) **the optimizer's three inputs are a program, a metric, and a training set** — DSPy's structural answer to *"what does it mean to optimize an LLM pipeline?"*; (2) **training-set size scales from 30 to 300+** — *"You can often get substantial value out of 30 examples, but aim for at least 300 examples"*; (3) **the conventional ML train/val split is inverted** — *"For most prompt optimizers, we recommend allocating 20% of your data for training and 80% for validation, contrary to typical deep learning conventions"* because *"prompt optimizers tend to overfit on small training sets"*; with one named exception — **GEPA reverts to the standard ML convention** (maximize training, keep validation sufficient for downstream-distribution representation); (4) **iterative development is key** — *"DSPy gives you the pieces to do that incrementally"* — across data, program structure, metric, **and** optimizer-choice axes. Mints [[DSPyOptimization]] as the canonical concept page for the optimization **workflow** (the *fourth artifact* of the [[DSPyProgrammingModel|Programming Model]]); deliberately defers the **catalog** of specific optimizers ([[BootstrapFewShot]], [[MIPROv2]], [[BootstrapFinetune]], [[GEPA]], etc.) to page 13 ([[DSPyOptimizers|Optimizers]]).

## Key Claims

- **An optimizer's job is to tune prompts or weights against a metric.** *"Once you have a system and a way to evaluate it, you can use DSPy optimizers to tune the prompts or weights in your program."* This is the canonical one-sentence definition of the [[DSPyOptimizers|Optimization stage]]. Two design choices are baked in: (a) **prompts and weights are equally first-class** — DSPy is a **both-axes** optimization framework (the third portability claim of [[DSPyProgrammingModel|the Programming Model]]); (b) **the program is fixed during optimization** — the optimizer searches over instructions / demonstrations / weights, not over module composition (the developer changes the program; the optimizer changes its parameters).

- **The optimizer's three inputs are program + metric + training set.** This is the **interface contract** the Optimization stage consumes from the prior two stages: the **program** comes from the [[DSPyProgrammingModel|Programming stage]] (a `dspy.Module` subclass with sub-Modules registered as `self.*` attributes for `named_predictors()` / `named_parameters()` walking); the **metric** comes from the [[DSPyEvaluation|Evaluation stage]] (a `(example, pred, trace=None) -> score` callable per [[DSPyMetrics]]); the **training set** is a `list[dspy.Example]` per [[DSPyData]]. The optimizer's output is **an optimized program** — same Python class, same `forward(...)`, refined parameters.

- **Training-set size is small but not as small as the dev set.** *"You can often get substantial value out of 30 examples, but aim for at least 300 examples."* This is a deliberate **expansion** from [[DSPyEvaluation|the Evaluation stage's]] 20–200-example dev-set regime: the dev set is *diagnostic* (small is fine); the training set is what an optimizer **searches over**, and search benefits from more data. The page commits the framework to a **30-example floor** (substantial value possible) and a **300-example target** (aim for at least). The order-of-magnitude gap between 30 and 300 mirrors [[dspy-evaluation-overview|the Evaluation Overview's]] 20–200 gap — DSPy's *"start simple, then grow"* discipline restated at the training-set layer.

- **The conventional train/val split is inverted for prompt optimizers.** *"For most prompt optimizers, we recommend allocating 20% of your data for training and 80% for validation, contrary to typical deep learning conventions. This is because prompt optimizers tend to overfit on small training sets."* This is the **most consequential single claim** on the page — it tells the developer to **use less training data** than they would in conventional ML. The rationale is *overfitting on small training sets* — a small training set in prompt optimization is easy to memorize because the search space (instructions + demonstrations) is small enough that the optimizer can find configurations that perfectly fit 80% of the data and fail on the rest. The 20/80 split is **non-obvious** to developers coming from deep learning where 80/20 (or 70/15/15 train/val/test) is standard. The page records this as a **recommendation**, not a hard rule — *"for most prompt optimizers"*.

- **GEPA is the named exception that reverts to the standard split.** *"However, the GEPA optimizer follows standard ML practice — maximizing the training set size while keeping the validation set sufficiently sized to represent the downstream task distribution."* This is the page's **first named-optimizer carve-out** — the only specific optimizer mentioned on this page is **[[GEPA]]**, and it is mentioned precisely because it **violates** the framework-level recommendation. The mechanism is left for page 13 ([[DSPyOptimizers|Optimizers]]) to detail, but the workflow-level commitment is clear: GEPA's robustness to training-set size lets it use the conventional ML split. The page does not enumerate which-optimizer-uses-which-split for non-GEPA optimizers — that's deferred to page 13.

- **Iteration spans four axes, not just optimizer-choice.** *"Iterative development is key. DSPy gives you the pieces to do that incrementally."* The page names four iteration axes — **data, program structure, metric, and optimizer** — and frames the developer's reaction to disappointing optimization results as a return to any of them. Six diagnostic questions structure the iteration:

  - *Is your task well-defined?* — return to [[DSPyProgrammingModel|Programming]] (re-design the [[DSPySignatures|Signature]]).
  - *Have you collected enough data?* — expand the training set (return to [[DSPyData]]).
  - *Is your metric appropriate?* — return to [[DSPyMetrics]] (re-define the scoring function).
  - *Are you using the most sophisticated optimizer that fits your needs?* — try a different optimizer from page 13.
  - *Could DSPy Assertions or other advanced features help?* — escape hatch to [[DSPyAssertions|DSPy Assertions]] (forward reference).
  - *Is your program structured optimally — e.g. should you decompose, or simplify?* — return to [[DSPyProgrammingModel|Programming]] (re-decompose the [[DSPyModules|Module]] graph).

  Three of the six questions point **back into the Programming and Evaluation stages**, not forward into the optimizer catalog. The Optimization stage is **not a black-box terminus** — the developer is expected to bounce back when results disappoint.

- **DSPy locates optimization inside an emerging paradigm.** *"This is an emerging paradigm for optimizing LM programs, and the community is here to help."* The page **frames the field**: optimizing LM programs (as opposed to fine-tuning a model end-to-end) is not yet a settled discipline. The page is cautious — it doesn't promise the optimizers will always work — and points developers to the Discord community for support. This is the **first explicit acknowledgment** in the [[dspy-learn-index|Learn corpus]] that DSPy is operating at a research frontier rather than reciting an established methodology.

- **The page deliberately defers the optimizer catalog to page 13.** The Overview names exactly **one** specific optimizer ([[GEPA]]) and only as a carve-out from the 20/80 split rule. It does **not** enumerate `BootstrapFewShot`, `BootstrapFewShotWithRandomSearch`, `MIPROv2`, `BootstrapFinetune`, or the per-optimizer decision rubric — those land on page 13 ([[DSPyOptimizers|Optimizers]]). The scope split mirrors the [[dspy-evaluation-overview|Evaluation Overview]] → [[dspy-metrics|Metrics]] split: the Overview frames the workflow; the sibling page provides the catalog.

## Key Quotes

> "Once you have a system and a way to evaluate it, you can use DSPy optimizers to tune the prompts or weights in your program." — the canonical one-sentence definition of the Optimization stage.

> "Now that you have some data and a metric, you're ready to optimize the program you built. You can iterate fast by trying out different optimizers." — the workflow framing — *data + metric + iterate over optimizers*.

> "You can often get substantial value out of 30 examples, but aim for at least 300 examples." — the explicit 30–300 training-set-size regime.

> "For most prompt optimizers, we recommend allocating 20% of your data for training and 80% for validation, contrary to typical deep learning conventions. This is because prompt optimizers tend to overfit on small training sets." — the inverted-split recommendation and its rationale.

> "However, the GEPA optimizer follows standard ML practice — maximizing the training set size while keeping the validation set sufficiently sized to represent the downstream task distribution." — the named carve-out from the 20/80 split rule.

> "Iterative development is key. DSPy gives you the pieces to do that incrementally." — the iterate-across-four-axes commitment (data / program / metric / optimizer).

> "This is an emerging paradigm for optimizing LM programs, and the community is here to help." — the field-framing disclosure; DSPy operates at a research frontier.

## The Optimization-stage interface contract

| Input | Type | Source | Documented on |
|---|---|---|---|
| **Program** | [[DSPyModules\|`dspy.Module`]] subclass with sub-Modules as `self.*` attributes | [[DSPyProgrammingModel\|Programming stage]] | [[dspy-modules]] (page 5) |
| **Metric** | `(example, pred, trace=None) -> float \| int \| bool` callable | [[DSPyEvaluation\|Evaluation stage]] | [[dspy-metrics]] (page 11) |
| **Training set** | `list[dspy.Example]` (30–300+ examples) | [[DSPyEvaluation\|Evaluation stage]] | [[dspy-data]] (page 10) |
| **Validation set** *(some optimizers)* | `list[dspy.Example]` (80% of data for most prompt optimizers; smaller for [[GEPA]]) | [[DSPyEvaluation\|Evaluation stage]] | [[dspy-data]] (page 10) |
| **Output: optimized program** | Same `dspy.Module` subclass; refined instructions / demonstrations / LM-weight references | The optimizer | [[dspy-optimizers]] (page 13, forward reference) |

The contract is what makes the [[dspy-learn-index|three-stage model]] composable: the Programming stage's *output* is the Optimization stage's *input* (program), the Evaluation stage's *output* is the Optimization stage's *input* (metric + training set), and the Optimization stage's *output* is a refined program that can be re-evaluated (potentially with the same metric and a held-out test set) or returned to Programming for structural revision.

## The four iteration axes

The page commits the framework to **four iteration axes** the developer may revise when optimization results are disappointing:

| Axis | What to revise | Stage it belongs to |
|---|---|---|
| **Data** | Training-set size, sourcing, label quality | [[DSPyEvaluation\|Evaluation]] ([[DSPyData]]) |
| **Program structure** | [[DSPyModules\|Module]] decomposition, [[DSPySignatures\|Signature]] design, control flow | [[DSPyProgrammingModel\|Programming]] |
| **Metric** | Scoring rule, AI-feedback rubric, deterministic gates | [[DSPyEvaluation\|Evaluation]] ([[DSPyMetrics]]) |
| **Optimizer** | Choose a different algorithm from the page-13 catalog | Optimization |

Only the fourth axis stays inside the Optimization stage. Three of four point back to prior stages — **the Optimization stage is open under revision from the prior two**.

## The 30/300 training-set-size scaling

The page's training-set guidance forms a clear scaling progression with the dev-set guidance from [[dspy-evaluation-overview|the Evaluation Overview]]:

| Set | Size | Source | Purpose |
|---|---|---|---|
| **Dev set** | 20–200 examples | [[dspy-evaluation-overview]] (page 9) | Diagnostic — establish baseline + qualitative failure-mode discovery |
| **Training set** | 30–300+ examples | This page (page 12) | The optimizer's search-objective sample |
| **Validation set** (80% of data) | 4× training (for most optimizers) | This page | Selection signal during optimization (overfitting defense) |
| **Test set** | held-out | [[dspy-data]] (page 10) | Final assessment after the loop closes |

The page commits the framework to a **non-trivial relationship** between dev set and training set: they can overlap or be distinct collections, but the training set is the larger one (30+ vs 20+) because the optimizer's search benefits from more examples than diagnostic measurement does. The 20/80 split applies to **the optimizer's data**, not to the entire collection — the dev set from the Evaluation stage may stand outside this split as a separate diagnostic resource.

## The GEPA carve-out

The page names exactly one optimizer — **[[GEPA]]** — and only to disclose that it **does not** follow the framework-level 20/80 recommendation. GEPA *"follows standard ML practice — maximizing the training set size while keeping the validation set sufficiently sized to represent the downstream task distribution."* Two implications:

1. **Per-optimizer scope-limits matter at the workflow level.** The recommendation is *"for most prompt optimizers"* — it is **not** a universal DSPy rule. Different optimizers have different data-budget contracts; the developer must read the per-optimizer documentation (page 13) before applying the 20/80 split mechanically.

2. **GEPA is distinguished by training-set robustness.** The page implies — but does not state — that GEPA's algorithm is **more robust** to overfitting on small training sets than the other prompt optimizers. The mechanism is deferred to page 13. The wiki should treat GEPA as a forward reference until [[dspy-optimizers|the Optimizers page]] lands.

## Why the Optimization stage is the **fourth** artifact of the Programming Model

[[DSPyProgrammingModel|The Programming Model]] (page 2) named four orthogonal artifacts a "conventional prompt" entangles: **Signature** (typed I/O), **Adapter** (formatting/parsing), **Module logic** (strategy), and **Manual optimization** (trial-and-error). The first three were operationalized by pages 4–8 — [[DSPySignatures]], [[DSPyAdapters]], [[DSPyModules]] + [[DSPyTools]] + [[DSPyMCP]]. The fourth was carried as the long-standing [[DSPyOptimizers]] forward reference; **this page is where it begins to land**.

The page is the **workflow-level** answer (what an optimizer *is for*); page 13 will be the **catalog-level** answer (which optimizers exist). The structural mapping:

| Programming Model artifact | Operationalized by |
|---|---|
| **Signature** (typed I/O) | [[dspy-signatures]] (page 4) → [[DSPySignatures]] |
| **Adapter** (wire format) | [[dspy-adapters]] (page 6) → [[DSPyAdapters]] |
| **Module logic** (strategy) | [[dspy-modules]] (page 5) → [[DSPyModules]] |
| **Manual optimization** (replaced by automation) | **This page + page 13** → [[DSPyOptimization]] (workflow, this page) + [[DSPyOptimizers]] (catalog, page 13) |

With page 12 ingested, the four-artifact picture is **structurally complete at the workflow level** — every concern named on the Programming Model has a corresponding source page and concept anchor.

## Forward references this page commits to

The page motivates **page 13 ([[DSPyOptimizers|Optimizers]])** by deliberately deferring the catalog — `BootstrapFewShot`, `BootstrapFewShotWithRandomSearch`, `MIPROv2`, `BootstrapFinetune`, [[GEPA]], and others — to that page. It also names **DSPy Assertions** as an advanced feature the developer should consider before declaring optimization complete; the wiki carries this as a forward reference ([[DSPyAssertions]]) for a possible later ingest.

The wiki mints **[[DSPyOptimization]]** as the canonical concept page for the optimization **workflow** (the *fourth artifact* of the Programming Model), and explicitly **does not** mint [[DSPyOptimizers]] — that page is owned by the sibling page-13 ingest. The split between [[DSPyOptimization]] (workflow / concept) and [[DSPyOptimizers]] (catalog / registry) mirrors the [[DSPyEvaluation]] / [[DSPyMetrics]] split established for the Evaluation stage — one page anchors the workflow, the sibling page anchors the per-algorithm machinery.

## Connections

- [[DSPy]] — the framework whose Optimization stage this Overview opens. **Completes the four-artifact picture** (Signatures / Modules / Adapters / Optimizers) at the workflow level, with Evaluation as the connective stage between Programming and Optimization.
- [[dspy-learn-index]] — the three-stage Programming → Evaluation → Optimization model; this page is the **entry point** of the third (Optimization) stage and **page 12 of 13** in the Learn corpus.
- [[DSPyOptimization]] — the canonical concept page minted by this ingest; captures the optimizer's three-input contract, the 30/300 training-set scaling, the inverted 20/80 train/val split, the [[GEPA]] carve-out, the four iteration axes, and the workflow-level position of optimization in the [[DSPyProgrammingModel|Programming Model]].
- [[DSPyOptimizers]] — **forward reference to page 13 of 13**; the catalog page will enumerate `BootstrapFewShot`, `BootstrapFewShotWithRandomSearch`, `MIPROv2`, `BootstrapFinetune`, [[GEPA]], and the per-optimizer decision rubric. Owned by a sibling ingest.
- [[DSPyProgrammingModel]] — the design philosophy from page 2; **the *fourth* of its four orthogonal artifacts is the optimizer**, and this page is where the workflow level of that artifact lands.
- [[DSPyEvaluation]] — the prior stage; this page consumes the metric and dev/training set the Evaluation stage produces. *"Now that you have some data and a metric, you're ready to optimize the program you built"* is the workflow-level transition statement.
- [[dspy-evaluation-overview]] — page 9 of 13; opens the Evaluation stage whose four-step loop produces the metric + dev set this page's optimizer consumes.
- [[dspy-data]] — page 10 of 13; defines [[DSPyExample|`dspy.Example`]] and the `list[dspy.Example]` dataset shape the training set this page describes uses. The page commits the train/dev/test convention; this page commits the within-train-data 20/80 train/validation split.
- [[dspy-metrics]] — page 11 of 13; defines the `(example, pred, trace=None) -> score` callable this page names as one of the optimizer's three inputs. The dual-purpose `trace` argument is what makes a metric usable by bootstrap-based optimizers like `BootstrapFewShotWithRandomSearch` — this page is the workflow-level reason that dual-purpose mechanism exists.
- [[DSPyData]] — the dataset-layer discipline; the training set this page describes is a `list[dspy.Example]` per [[DSPyData]]'s commitment that datasets are plain Python lists.
- [[DSPyExample]] — the per-datapoint primitive the training set is composed of.
- [[DSPyMetrics]] — the metric contract this page's optimizer consumes.
- [[DSPyModules]] — the program this page's optimizer optimizes is a `dspy.Module` subclass; the sub-Modules registered as `self.*` attributes are what the optimizer's `named_predictors()` / `named_parameters()` walks enumerate.
- [[DSPyPrediction]] — the typed return object every Module call produces; the metric consumes a [[DSPyPrediction|`Prediction`]] from the program against an [[DSPyExample|`Example`]] from the training set.
- [[DSPyPredict]] — the minimal primitive Module the optimizer's parameter walk bottoms out on.
- [[DSPyEvaluate]] — the dev-set-evaluation harness whose **`trace=None`** call mode this page's metric uses during evaluation passes (vs the **`trace=[...]`** mode used during bootstrap demo selection).
- [[DSPySignatures]] — the stable interface the optimizer **does not** modify; the optimizer searches over instructions / demonstrations / weights, leaving the Signature unchanged.
- [[DSPyAdapters]] — the wire-format layer the optimizer **does not** modify; the optimized prompts produced by the optimizer compose through the same Adapter as the unoptimized ones.
- [[DSPyLM]] — the LM client the program (and the metric, if it is an AI-feedback DSPy program) routes through; optimization can target the LM's *weights* (when fine-tuning is available — `BootstrapFinetune`) or just its *prompts* (every other optimizer).
- [[GEPA]] — the only specific optimizer named on this page; carved out from the 20/80 split recommendation as following standard ML practice. **Forward reference**; full mechanism deferred to page 13.
- [[BootstrapFewShot]] / [[BootstrapFewShotWithRandomSearch]] / [[MIPROv2]] / [[BootstrapFinetune]] — the optimizer catalog page 13 will introduce; **forward references** this Overview does not enumerate.
- [[DSPyAssertions]] — advanced feature named in the diagnostic-questions list as an escape hatch when optimization alone doesn't suffice; **forward reference** for a possible later ingest.
- [[PromptOptimization]] — the general concept this page's *"most prompt optimizers"* recommendation specializes; the 20/80 split is a DSPy-specific recommendation for the prompt-optimization sub-family.
- [[OverFitting]] — the failure mode the inverted 20/80 split defends against — *"prompt optimizers tend to overfit on small training sets"*.
- [[TrainValTestSplit]] / [[TrainTestSplit]] — the general ML convention this page **inverts** for prompt optimizers; the canonical 80/20 (or 70/15/15) split assumed by deep-learning training does not apply to most DSPy prompt optimization.
- [[CrossValidation]] — the alternative validation scheme not discussed on this page; DSPy uses a fixed validation set rather than k-fold cross-validation.
- [[FineTuning]] — the weight-tuning regime that `BootstrapFinetune` (forward reference) operates in; the *"or weights"* half of *"tune the prompts or weights"*.
- [[HyperparameterOptimization]] — the general framework this DSPy-specific optimization workflow specializes; an [[DSPyOptimizers|Optimizer]] is structurally a search over the program's *prompt-and-weight hyperparameters*.
- [[ModelEvaluation]] — the general concept the metric this page consumes specializes; the optimizer climbs the metric the same way an HPO loop climbs validation accuracy.
- [[GradientDescent]] — the optimization paradigm DSPy prompt optimizers **do not** use (no gradients available over a string-valued search space); the optimizer family lives in the **search / sampling / bootstrapping** branch of the optimization tree, with weight-tuning optimizers (`BootstrapFinetune`) bridging to gradient-based fine-tuning via the underlying LM provider.
- [[PromptEngineering]] — the manual discipline DSPy automates; the Optimization stage is the **automated alternative** to hand-tuning instructions and few-shot demonstrations.
- [[2604.25850-agentic-harness-engineering]] — the harness-engineering counter-position that names *"DSPy-style instruction tuning"* explicitly. The page's emphasis on *iterative development across four axes* (not just optimizer-choice) is **partial common ground** — both frameworks treat optimization as an iterative-search problem over program structure, not just over prompts.
- [[LLMModuloFramework]] — DSPy's [[DSPyOptimizers|Optimizer]] is the **search procedure** layer of Kambhampati et al.'s generate-test-critique loop; the metric is the *critic*, the program is the *generator*, the optimizer is what does the search over candidate generators.
- [[llmasjudge|LLM-as-judge]] — when the metric is an AI-feedback program ([[dspy-metrics|page 11]]), the optimizer's *"metric of the metric"* recursion ([[DSPyEvaluation|Step 4]] of the four-step loop) is operationalized by the same machinery this page describes — the AI-feedback metric is itself a DSPy program with the same three-input optimization contract.

## Contradictions

- **None new.** This page **completes** rather than contradicts every prior DSPy ingest:
  - It **fulfills** [[dspy-learn-index|the Learn index's]] forward reference to the Optimization stage — *"use DSPy optimizers to tune the prompts or weights in your program"* — by operationalizing the workflow.
  - It **fulfills** [[DSPyProgrammingModel|the Programming Model's]] *fourth-artifact* commitment from page 2 at the workflow level. The catalog completion lands on page 13.
  - It **vindicates** [[DSPyEvaluation|the Evaluation stage's]] *"the metric is the function the Optimizer maximizes"* commitment by naming the metric explicitly as one of the optimizer's three inputs.
  - It **vindicates** [[DSPyMetrics|the metric contract's]] dual-purpose `trace` argument by naming the optimizer (specifically bootstrap-based optimizers like `BootstrapFewShotWithRandomSearch`) as the consumer of the `trace is not None` regime.
  - It **vindicates** [[DSPyData|the data-handling discipline's]] *"DSPy is a machine learning framework"* commitment — the Optimization stage is the **training** stage of that ML framework.
- **One framing nuance to track.** The page's 30/300 training-set guidance and 20/80 split recommendation are **not universal** — *"for most prompt optimizers"* is the explicit qualifier, with [[GEPA]] as the named carve-out. The wiki should not over-commit on these as DSPy-wide rules; they are recommendations whose applicability depends on the specific optimizer chosen from page 13.
- **One scope-limit to record.** The page does **not** discuss test sets (held-out final evaluation) — only training and validation. The test-set discipline lives implicitly on [[dspy-data|page 10]]'s *"training sets, development sets, and test sets"* trichotomy but is not re-stated here. The wiki should treat test-set use as **assumed** (DSPy is a machine learning framework; test sets are part of the supervised-ML tradition) rather than absent.
