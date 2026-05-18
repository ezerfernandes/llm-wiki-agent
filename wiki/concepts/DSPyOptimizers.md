---
title: "DSPy Optimizers"
type: concept
tags: [dspy, llm-programming, optimization, optimizers, bootstrap, mipro, gepa, bootstrap-finetune, copro, simba, knnfewshot, labeledfewshot, ensemble, bettertogether, teleprompters, catalog]
sources: [dspy-optimizers, dspy-optimization-overview, dspy-learn-index]
last_updated: 2026-05-17
---

# DSPy Optimizers

**DSPy Optimizers** are the **catalog of concrete algorithms** that operationalize the [[DSPyOptimization|Optimization stage]] of [[DSPy]]'s [[dspy-learn-index|three-stage Programming → Evaluation → Optimization]] workflow. Each optimizer is a callable surfaced under the `dspy.<OptimizerName>` namespace ([[BootstrapFewShot|`dspy.BootstrapFewShot`]], [[MIPROv2|`dspy.MIPROv2`]], [[GEPA|`dspy.GEPA`]], [[BootstrapFinetune|`dspy.BootstrapFinetune`]], etc.) implementing the same `Optimizer(metric=..., **config).compile(program, trainset=...) -> optimized_program` interface, but with different **search strategies**, **data-budget contracts**, and **what-it-tunes** axes.

The canonical source is [[dspy-optimizers|the Optimizers page]] (page 13 of 13 of the *Learn* section). This concept page is the **catalog-level sibling** of [[DSPyOptimization]] (which captures the *workflow*) — the split mirrors the [[DSPyEvaluation]] (workflow) / [[DSPyMetrics]] (catalog) precedent. The framework's prior name for the family is **"teleprompters"** — *"Formerly called teleprompters. We are making an official name update."* — and the canonical worked-example local-variable name `teleprompter` is still the *de-facto* idiomatic name in the framework's documentation.

## The three orthogonal what's-being-tuned axes

[[dspy-optimizers|The Optimizers page]] commits the framework to **three orthogonal axes** of what an optimizer can tune:

| Axis | Mechanism | Representative optimizers |
|---|---|---|
| **Demonstrations** (few-shot examples in each prompt) | Bootstrap traces of program behavior; filter by metric; install passing traces as `demos` on each [[DSPyPredict\|`dspy.Predict`]] | [[BootstrapFewShot]], [[BootstrapFewShotWithRandomSearch]], `KNNFewShot`, `LabeledFewShot`, [[MIPROv2]] (also tunes instructions) |
| **Instructions** (natural-language task description in each prompt) | Propose candidate instructions; explore via coordinate ascent / [[BayesianOptimization\|Bayesian Optimization]] / LM-reflection over program trajectories | `COPRO`, [[MIPROv2]], `SIMBA`, [[GEPA]] |
| **LM weights** (the underlying model's parameters) | Distill a prompt-based program into a fine-tuned model via metric-validated bootstrapped traces | [[BootstrapFinetune]] |

The page's canonical summary: *"Different optimizers in DSPy will tune your program's quality by synthesizing good few-shot examples for every module, like `dspy.BootstrapRS`, proposing and intelligently exploring better natural-language instructions for every prompt, like `dspy.MIPROv2` and `dspy.GEPA`, and building datasets for your modules and using them to finetune the LM weights in your system, like `dspy.BootstrapFinetune`."* Three axes; eleven optimizers; only [[MIPROv2]] tunes more than one axis in the same run (instructions **and** demonstrations); only [[BootstrapFinetune]] tunes weights.

## The five families

The page groups the eleven optimizers into five families. The grouping is taxonomic, not orthogonal — `MIPROv2` is *both* a few-shot and an instruction optimizer, but the page lists it under *Automatic Instruction Optimization* because instruction generation is its distinctive contribution.

| Family | Optimizers |
|---|---|
| **Automatic Few-Shot Learning** | `LabeledFewShot`, [[BootstrapFewShot]], [[BootstrapFewShotWithRandomSearch]], `KNNFewShot` |
| **Automatic Instruction Optimization** | `COPRO`, [[MIPROv2]], `SIMBA`, [[GEPA]] |
| **Automatic Finetuning** | [[BootstrapFinetune]] |
| **Program Transformations** | `Ensemble` |
| **Meta-Optimizers** | `BetterTogether` |

## The full catalog table

| # | Optimizer | Family | What it tunes | Mechanism | Key parameters |
|---|---|---|---|---|---|
| 1 | `LabeledFewShot` | Few-Shot | Demonstrations | Random selection from labeled `trainset` (no bootstrapping, no metric validation) | `k`, `trainset` |
| 2 | [[BootstrapFewShot\|`BootstrapFewShot`]] | Few-Shot | Demonstrations (bootstrapped + labeled) | A `teacher` module (defaults to your program) generates demos for each program stage; the metric filters them — only metric-passing demos enter the compiled prompt | `max_labeled_demos`, `max_bootstrapped_demos`, optional `teacher` (a different DSPy program) |
| 3 | [[BootstrapFewShotWithRandomSearch\|`BootstrapFewShotWithRandomSearch`]] | Few-Shot | Demonstrations | `BootstrapFewShot` repeated with random search over generated demos; best program selected over candidates (uncompiled + `LabeledFewShot` + `BootstrapFewShot`-unshuffled + N randomized `BootstrapFewShot`) | `max_labeled_demos`, `max_bootstrapped_demos`, `num_candidate_programs`, `num_threads` |
| 4 | `KNNFewShot` | Few-Shot | Per-example demonstrations | [[KNearestNeighbors\|k-NN]] finds nearest training examples to the input; those become the trainset for `BootstrapFewShot` | k, embeddings |
| 5 | `COPRO` | Instruction | Instructions | Generates and refines new instructions per step; **coordinate ascent / hill-climbing** using metric + `trainset` | `depth` (refinement iterations) |
| 6 | [[MIPROv2\|`MIPROv2`]] | Instruction | **Instructions + demonstrations** | Three-stage: bootstrapping → grounded proposal → discrete search via [[BayesianOptimization\|Bayesian Optimization]] | `auto="light"/"medium"/"heavy"`, `metric`, `num_threads`, `max_bootstrapped_demos`, `max_labeled_demos` |
| 7 | `SIMBA` | Instruction | Instructions (self-reflective) | Stochastic mini-batch sampling on high-variability examples; LM introspectively analyzes failures and generates self-reflective improvement rules or adds successful demos | (not detailed on page) |
| 8 | [[GEPA\|`GEPA`]] | Instruction | Instructions (reflection-based) | LM reflects on program trajectory (*"what worked, what didn't"*) and proposes prompts addressing the gaps; can leverage domain-specific textual feedback | (not detailed on page; tutorials linked) |
| 9 | [[BootstrapFinetune\|`BootstrapFinetune`]] | Finetuning | LM weights | Distills a prompt-based DSPy program into weight updates; output is a program with the same steps, each conducted by a fine-tuned model | `metric`, `num_threads` |
| 10 | `Ensemble` | Program Transformation | Composition | Wraps a set of DSPy programs (full set or random subset) into one | (not detailed on page) |
| 11 | `BetterTogether` | Meta-Optimizer | Sequence of optimizers | Configurable prompt-and-weight optimization sequence (e.g. prompt → weight → prompt) | (not detailed on page) |

## The general API

Every optimizer in the catalog implements the same two-step lifecycle:

```python
import dspy

# 1. Construct with metric + config
config = dict(max_bootstrapped_demos=4, max_labeled_demos=4, num_candidate_programs=10, num_threads=4)
teleprompter = dspy.BootstrapFewShotWithRandomSearch(metric=YOUR_METRIC_HERE, **config)

# 2. Compile against (program, trainset) -> optimized program of same class
optimized_program = teleprompter.compile(YOUR_PROGRAM_HERE, trainset=YOUR_TRAINSET_HERE)
```

The variable name `teleprompter` is a legacy holdover from the pre-rename era and remains idiomatic in the framework's documentation. The optimizer's output is a [[DSPyModules|`dspy.Module`]] subclass of the **same class** as the input — same `forward(...)`, same sub-Modules, same [[DSPySignatures|Signatures]] — with refined instructions, demonstrations, or weight references.

## The five-rule getting-started rubric

[[dspy-optimizers|The page]] ships a concrete decision rubric tying optimizer choice to dataset size and compute budget:

| Data budget / goal | Recommended optimizer | Rationale |
|---|---|---|
| **~10 examples** | [[BootstrapFewShot]] | Smallest data budget; metric-validated bootstrapped demos suffice. |
| **50+ examples** | [[BootstrapFewShotWithRandomSearch]] | Enough data to search over multiple bootstrap seeds. |
| **Want 0-shot prompts** | [[MIPROv2]] configured for 0-shot | Instruction optimization without demonstrations in the final prompt. |
| **40+ trials + 200+ examples** | [[MIPROv2]] (full) | Bayesian search benefits from larger trial budget; 200+ examples avoid overfitting. |
| **Used 7B+ LM, want a small efficient model** | [[BootstrapFinetune]] | Distill prompt-based behavior into a smaller fine-tuned model. |

The rubric **operationalizes** [[DSPyOptimization|the workflow-level page's]] *"are you using the most sophisticated optimizer that fits your needs?"* diagnostic question into a concrete (data, compute) → optimizer map. **Five named optimizers are absent** from the rubric — [[GEPA]], `SIMBA`, `COPRO`, `KNNFewShot`, `Ensemble`, `BetterTogether`, `LabeledFewShot` — those are *expert paths* left for the user to discover via the catalog.

## The canonical three-stage decomposition (via `MIPROv2`)

[[dspy-optimizers|The page]] uses [[MIPROv2|`dspy.MIPROv2`]] as its **reference example** of how a non-trivial DSPy optimizer works. The three-stage decomposition is a **structural template** the rest of the catalog can be read against:

1. **Bootstrapping stage.** Run the program many times on training inputs; collect input/output traces per module; **filter** traces by the metric — only traces appearing in highly-scored trajectories survive.

2. **Grounded proposal stage.** Preview the program's **code**, **data**, and **traces**; draft **many candidate instructions** per prompt. This is where DSPy's *"writing code instead of strings"* discipline pays off — the optimizer's proposer can inspect the actual Python program, not just a string prompt.

3. **Discrete search stage.** Sample training mini-batches; propose **(instructions, traces)** combinations; evaluate candidate programs on the mini-batch; update a **surrogate model** ([[BayesianOptimization|Bayesian Optimization]]) that improves proposals over time.

The template generalizes implicitly: every non-trivial DSPy optimizer is some combination of **(a) collect traces, (b) propose candidates, (c) search the candidate space against the metric** — with different optimizers occupying different positions in this 3-step space.

| Optimizer | Step (a) collect | Step (b) propose | Step (c) search |
|---|---|---|---|
| `LabeledFewShot` | — (uses labels directly) | — | — (random selection) |
| [[BootstrapFewShot]] | Bootstrap traces, filter by metric | — | — (deterministic install) |
| [[BootstrapFewShotWithRandomSearch]] | Bootstrap traces, filter by metric | — | Random search over N candidates |
| `KNNFewShot` | Bootstrap traces (per-input) | — | k-NN over input embeddings |
| `COPRO` | — | Generate + refine instructions | Coordinate ascent |
| [[MIPROv2]] | Bootstrap traces, filter by metric | Grounded proposal from code+data+traces | Bayesian optimization |
| `SIMBA` | Bootstrap traces on high-variability examples | LM introspection / self-reflection | Mini-batch stochastic search |
| [[GEPA]] | Collect trajectories | LM reflection on what worked / didn't | Reflection-driven; supports domain feedback |
| [[BootstrapFinetune]] | Bootstrap traces, filter by metric | — | Fine-tune target LM on filtered traces |

## Composability: the structural payoff

[[dspy-optimizers|The page]] commits the framework to a **composability** claim:

> *"You can run `dspy.MIPROv2` and use the produced program as an input to `dspy.MIPROv2` again or, say, to `dspy.BootstrapFinetune` to get better results. This is partly the essence of `dspy.BetterTogether`."*

Two compositional patterns the page operationalizes:

- **Sequential composition.** An optimized program is structurally identical to its input — a [[DSPyModules|`dspy.Module`]] subclass — so the same optimizer or a different one can consume it. This makes *"run optimizer A, then run optimizer B on A's output"* a one-line operation. **`BetterTogether`** formalizes this for the prompt→weight→prompt sequence; *"empirically, this approach often outperforms either strategy alone."*

- **Ensemble composition.** After an optimizer run, extract the top-k candidate programs and wrap them in `dspy.Ensemble`. The ensemble votes at inference time. This scales DSPy's **pre-inference-time compute** (the optimizer's budget) and **inference-time compute** (the ensemble's vote) **together** — structurally novel relative to conventional ML where the *training-time vs inference-time compute* axis is rarely scalable in both directions from a single artifact.

The composability claim is **structurally novel** relative to conventional ML hyperparameter optimization. A `sklearn.GridSearchCV` doesn't typically consume another `GridSearchCV`'s output as input — the output is a fitted estimator, not a configurable pipeline. DSPy optimizers preserve the program's structure as their output type, so they compose like ordinary Python functions over a single algebraic type (`dspy.Module -> dspy.Module`).

## Cost: cents to tens of dollars

[[dspy-optimizers|The page]] names a concrete operating-cost ballpark:

> *"A typical simple optimization run costs on the order of $2 USD and takes around ten minutes ... Optimizer runs can cost as little as a few cents or up to tens of dollars, depending on your LM, dataset, and configuration."*

DSPy's first explicit operating-cost disclosure in the *Learn* corpus. This anchors the **research-frontier framing** from [[DSPyOptimization|page 12]] (*"this is an emerging paradigm"*) at the wallet level — optimization is a **finite budget**, not free, and the budget scales with LM cost × dataset size × candidate count.

## Three worked end-to-end receipts

[[dspy-optimizers|The page]] ships three worked optimization receipts that anchor the abstract decision rubric to concrete metric improvements:

| Receipt | Setup | Metric | Improvement (DSPy 2.5.29, informal) |
|---|---|---|---|
| **`dspy.ReAct` + [[MIPROv2\|`MIPROv2(auto="light")`]] on HotPotQA** | [[react\|`dspy.ReAct`]] with Wikipedia search via `dspy.ColBERTv2`; GPT-4o-mini; 500 train examples | `dspy.evaluate.answer_exact_match` | **24% → 51%** |
| **`RAG(dspy.Module)` + [[MIPROv2\|`MIPROv2(auto="medium")`]] on StackExchange** | [[ChainOfThought\|`dspy.ChainOfThought`]]-based RAG; `max_bootstrapped_demos=2`, `max_labeled_demos=2` | `dspy.SemanticF1()` (an [[llmasjudge\|LLM-as-judge]] DSPy module) | **53% → 61%** |
| **Banking77 classification + [[BootstrapFinetune\|`BootstrapFinetune`]] on `gpt-4o-mini-2024-07-18`** | `Literal[tuple(CLASSES)]`-typed [[DSPySignatures\|Signature]]; 2000 examples; `set_lm(...)` per-Module LM binding | `lambda x, y, trace=None: x.label == y.label` | **66% → 87%** |

Three deliberate coverage points: **agent + prompt-only**, **RAG + AI-feedback metric**, **classification + weight-tuning**. The middle receipt is the **only place in the corpus** that an LLM-as-judge metric (`SemanticF1()`) drives an optimizer — exercising the recursive-metric-optimization claim from [[DSPyMetrics|Step 4 of the four-step Evaluation loop]] in practice.

## Save / load: the inspectability commitment

```python
optimized_program.save(YOUR_SAVE_PATH)

loaded_program = YOUR_PROGRAM_CLASS()
loaded_program.load(path=YOUR_SAVE_PATH)
```

The saved file is **plain-text JSON** containing all parameters and steps. A developer can `cat` it and see exactly which instructions and demonstrations the optimizer chose. This is consistent with DSPy's *"writing code instead of strings"* discipline ([[DSPyProgrammingModel|the Programming Model]]) — the optimizer's output is not a separate artifact (a `*.pt` weight file, a fine-tuned model handle) but a **refined version of the same program** the developer wrote. [[BootstrapFinetune|`BootstrapFinetune`]] is the exception — it produces a fine-tuned model handle, which is the LM provider's artifact, but the surrounding DSPy program is still serialized as JSON.

## Position in the wiki's optimization landscape

- **vs. [[DSPyOptimization]] (the workflow-level sibling).** The two pages are **complementary** — [[DSPyOptimization]] captures the *three-input contract* (program + metric + training set → optimized program), the *30/300 training-set regime*, the *inverted 20/80 train/val split*, the *[[GEPA]] carve-out*, and the *four iteration axes*. **This page** is the catalog of concrete algorithms that operationalize the workflow. The split mirrors [[DSPyEvaluation]] / [[DSPyMetrics]] — one anchors the discipline, the sibling anchors the per-algorithm machinery.

- **vs. [[HyperparameterOptimization]] (the general concept).** Hyperparameter Optimization is *"search over the model's hyperparameters to maximize validation performance"* — a general ML notion. DSPy Optimizers are the **DSPy-specific operationalization** — the hyperparameters are *instructions / demonstrations / LM weights*; the model is a [[DSPyModules|`dspy.Module`]]; the validation set discipline inverts (20/80 instead of 80/20 for most optimizers). The DSPy version is **narrower** (specific to LM programs) and **richer** (commits to a five-family taxonomy and a getting-started rubric).

- **vs. [[BayesianOptimization]] (the surrogate-model search procedure).** Bayesian Optimization is the **search algorithm** [[MIPROv2|`MIPROv2`]]'s discrete-search stage uses. It is one strategy in the catalog's *Step (c) search* slot — others use coordinate ascent (`COPRO`), random search (`BootstrapFewShotWithRandomSearch`), k-NN ranking (`KNNFewShot`), stochastic mini-batch sampling (`SIMBA`), or LM reflection ([[GEPA]]).

- **vs. [[FineTuning]] (the weight-tuning regime).** [[BootstrapFinetune]] is DSPy's bridge into [[FineTuning]] — the only optimizer in the catalog that targets the LM's weights rather than its prompts. The rest of the catalog stays above the LM's parameters, treating the LM as a fixed function whose prompts are the only mutable surface.

- **vs. [[PromptEngineering]] (manual prompt iteration).** DSPy Optimizers are the **automated alternative** to hand-tuning prompts. [[dspy-programming-overview|The Programming Overview]] names this counter-position explicitly: *"manual optimization relies on substantial trial-and-error to discover the right way to ask each LM to do this"*. This catalog is **the list of automated alternatives** the framework ships.

- **vs. [[bestofn|best-of-N]] (an inference-time compute paradigm).** The `Ensemble` + top-k-extraction pattern operationalizes inference-time compute on top of the optimizer's pre-inference-time compute. DSPy can scale **both axes** from a single optimizer run — extract the top-5 candidate programs, wrap them in `Ensemble`, vote at inference time. This is **structurally distinct** from [[bestofn|best-of-N]] alone, which scales inference-time compute but not pre-inference-time compute.

- **vs. [[LLMModuloFramework|LLM-Modulo]] (Kambhampati et al.).** Every optimizer in this catalog is a different **search procedure** layer of the generate-test-critique loop — the [[DSPyMetrics|metric]] is the critic, the [[DSPyModules|program]] is the generator, the optimizer is the search procedure. The catalog is a taxonomy of search-procedure strategies for the generate-test loop.

## The optimizer's three-input contract (recap)

From [[DSPyOptimization|the workflow page]]:

| Slot | What it is | Source |
|---|---|---|
| **Program** (input) | A [[DSPyModules\|`dspy.Module`]] subclass | [[DSPyProgrammingModel\|Programming stage]] |
| **Metric** (input) | A `(example, pred, trace=None) -> float \| int \| bool` callable | [[DSPyEvaluation\|Evaluation stage]] ([[DSPyMetrics]]) |
| **Training set** (input) | A `list[dspy.Example]` of 30–300+ examples | [[DSPyEvaluation\|Evaluation stage]] ([[DSPyData]] / [[DSPyExample]]) |
| **Optimized program** (output) | Same [[DSPyModules\|`dspy.Module`]] subclass; refined parameters | This catalog's optimizers |

Every optimizer in this catalog consumes this contract identically. The differences are in the **search strategy** over the program's parameters, not in the interface.

## Connections

- [[DSPy]] — the framework whose third-stage catalog this concept page anchors.
- [[dspy-optimizers]] — the canonical source for this concept (Optimizers, page 13 of 13). Mints this page.
- [[DSPyOptimization]] — the workflow-level sibling; this catalog's *what* to that page's *why and how*.
- [[dspy-optimization-overview]] — the workflow-level source (page 12); names [[GEPA]] as its single carved-out optimizer and defers the rest of the catalog to this page.
- [[dspy-learn-index]] — the three-stage Programming → Evaluation → Optimization workflow this catalog closes (page 13 of 13).
- [[BootstrapFewShot]] — the canonical 10-example optimizer; metric-validated bootstrapped demos.
- [[BootstrapFewShotWithRandomSearch]] — the canonical 50+-example optimizer; random search over `BootstrapFewShot` candidates.
- [[MIPROv2]] — the framework's reference optimizer; three-stage Bayesian-search-driven instruction+demonstration tuner.
- [[GEPA]] — the reflection-based prompt optimizer; the named carve-out from the 20/80 train/val split on [[dspy-optimization-overview|page 12]].
- [[BootstrapFinetune]] — the only weight-tuning optimizer; bridges DSPy into [[FineTuning]].
- [[DSPyProgrammingModel]] — the *fourth artifact* of the four-concerns decomposition; this catalog is its catalog-level operationalization.
- [[DSPyEvaluation]] — the connective stage; produces the metric + training set every optimizer in this catalog consumes.
- [[DSPyMetrics]] — the metric contract; the **dual-purpose `trace` argument** is what makes bootstrap-based optimizers ([[BootstrapFewShot]] / [[BootstrapFewShotWithRandomSearch]] / `KNNFewShot` / [[MIPROv2]] / [[BootstrapFinetune]]) possible.
- [[DSPyData]] / [[DSPyExample]] — the training-set primitive every `.compile(program, trainset=...)` call consumes.
- [[DSPyModules]] — the program input and output type of every optimizer in this catalog.
- [[DSPyPredict]] — the minimal Module primitive every learnable parameter site bottoms out on; the optimizer's mutations target a Predict's `signature` (instructions) and `demos` (demonstrations) attributes.
- [[DSPyPrediction]] — the typed return object every Module call produces; the metric consumes a Prediction.
- [[DSPyLM]] — the LM client; [[BootstrapFinetune]] is the only optimizer that targets the LM's **weights** rather than its prompts.
- [[DSPySignatures]] — the stable interface the optimizer **does not** modify.
- [[DSPyAdapters]] — the wire-format layer the optimizer **does not** modify.
- [[ChainOfThought]] — the canonical starting Module used in the RAG worked receipt.
- [[react|ReAct]] — the tool-using agent used in the HotPotQA worked receipt.
- [[BayesianOptimization]] — the surrogate-model search procedure [[MIPROv2]]'s discrete-search stage uses.
- [[KNearestNeighbors]] — the algorithm `KNNFewShot` uses to pick per-input demonstrations.
- [[FineTuning]] — the weight-tuning regime [[BootstrapFinetune]] operates in.
- [[HyperparameterOptimization]] — the general ML concept this catalog specializes for LM programs.
- [[PromptOptimization]] — the general activity DSPy's prompt-tuning optimizers (`MIPROv2` / [[GEPA]] / `COPRO` / `SIMBA` / `BootstrapFewShot*`) operationalize.
- [[PromptEngineering]] — the manual discipline this catalog automates.
- [[bestofn|best-of-N]] — the inference-time compute axis the `Ensemble` + top-k-extraction pattern operationalizes alongside DSPy's pre-inference-time compute.
- [[llmasjudge]] — the AI-feedback metric pattern; `dspy.SemanticF1()` in the RAG worked receipt is an LLM-as-judge metric optimizing an optimization run.
- [[LLMModuloFramework]] — every optimizer in this catalog is a different *search procedure* in Kambhampati et al.'s generate-test-critique loop.
- [[OverFitting]] — the failure mode the [[DSPyOptimization|workflow page's]] inverted 20/80 train/val split defends against; relevant to every prompt optimizer in this catalog except [[GEPA]] (carved out).
