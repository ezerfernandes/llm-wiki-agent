---
title: "DSPy Evaluate"
type: concept
tags: [dspy, llm-programming, evaluation, metrics, parallel-evaluation, utility]
sources: [dspy-metrics]
last_updated: 2026-05-24
---

# DSPy Evaluate

**`dspy.Evaluate`** (imported as `from dspy.evaluate import Evaluate`) is DSPy's **built-in dev-set-evaluation utility** — a reusable harness that runs a [[DSPyMetrics|metric]] over a [[DSPyData|dataset]] under a [[DSPyModules|program]] with parallelism, progress display, and tabular result rendering. Introduced by [[dspy-metrics|the Metrics page]] (page 11 of 13 of the *Learn* section).

Where [[DSPyMetrics]] defines the **`(example, pred, trace) -> score`** contract, `dspy.Evaluate` defines **how to apply that contract** over a `list[dspy.Example]`. The two concepts are siblings minted by the same ingest: a metric is a function; `Evaluate` is the harness that calls the function.

## The minimal usage

```python
from dspy.evaluate import Evaluate

# Set up the evaluator, which can be re-used in your code.
evaluator = Evaluate(devset=YOUR_DEVSET, num_threads=1, display_progress=True, display_table=5)

# Launch evaluation.
evaluator(YOUR_PROGRAM, metric=YOUR_METRIC)
```

The pattern is **two-phase**: construct the evaluator with the dev set and ergonomic kwargs **once**; call it with `(program, metric)` pairs **multiple times**. This is the dev-set-comparison primitive — the same `evaluator` compares multiple candidate programs against the same dev set with the same metric.

## The two-line raw equivalent

[[dspy-metrics|The Metrics page]] shows what `Evaluate` is doing under the hood:

```python
scores = []
for x in devset:
    pred = program(**x.inputs())
    score = metric(x, pred)
    scores.append(score)
```

Three things happen per example:

1. **`x.inputs()`** — call the [[DSPyExample|`Example.inputs()`]] partition accessor (from [[dspy-data|page 10]]) to get only the input fields, returned as a new `Example`.
2. **`program(**x.inputs())`** — splat the input fields as kwargs into the program's `forward()`. The program returns a [[DSPyPrediction|`dspy.Prediction`]].
3. **`metric(x, pred)`** — call the [[DSPyMetrics|metric]] with the original example (carrying any reference labels) and the predicted output. Trace is **not passed** — `Evaluate` runs metrics in the `trace is None` evaluation regime.

`Evaluate` is a **thread-parallel wrapper** around that loop with display ergonomics. `Evaluate` exists because the raw loop is sequential, has no progress feedback, and doesn't display sample inputs/outputs — useful properties when iterating on a metric or comparing pipeline designs.

## Constructor kwargs

[[dspy-metrics|The Metrics page]] names four constructor kwargs:

| Kwarg | Type | Purpose |
|---|---|---|
| `devset` | `list[dspy.Example]` | The held-out development set (per [[dspy-data\|page 10]]: a plain Python list of [[DSPyExample\|`dspy.Example`]] with `with_inputs(...)` tags) |
| `num_threads` | `int` | Parallelism — `num_threads=1` is the sequential baseline; higher values use a thread pool |
| `display_progress` | `bool` | TQDM-style progress bar |
| `display_table` | `int` | Show a tabular sample of the first N rows (inputs, outputs, scores) |

The constructor binds these once; the call-time arguments are the **program** and the **metric**.

## What `Evaluate` returns and prints

The page is light on the return-value contract; the operational signal `Evaluate` produces is **the aggregated score** (a percentage or float, depending on metric return type — `True`/`False` are summed as `1.0`/`0.0`) plus, when `display_table > 0`, a tabular display of sample inputs / outputs / scores. This is **the qualitative-diagnostic surface** [[dspy-evaluation-overview|the Evaluation Overview]] names — *"Look at the outputs and the metric scores. This will probably allow you to spot any major issues, and it will define a baseline for your next steps."*

## How `Evaluate` fits in the four-step loop

`dspy.Evaluate` is the **Step 3** operationalization of [[DSPyEvaluation|the Evaluation stage's four-step iterative loop]]:

| Step | Action | Tool |
|---|---|---|
| 1 | Collect dev set | [[DSPyData]] / [[DSPyExample]] |
| 2 | Define metric | [[DSPyMetrics]] |
| **3** | **Run development evaluations on pipeline designs** | **`dspy.Evaluate`** |
| 4 | (Recursive) Optimize the metric itself | [[DSPyOptimizers]] |

`Evaluate` is the **harness Step 3 uses** to produce both deliverables of that step: the **baseline score** (the numeric output) and the **qualitative diagnostic** (the `display_table` rendering).

## Reusability across the development cycle

The page's emphasis that the evaluator *"can be re-used in your code"* is structurally important. The same `Evaluate` instance is used in three places in a typical DSPy project:

- **Initial baseline.** Construct the evaluator, call it on the unoptimized program — record the baseline score.
- **Optimization-iteration comparison.** After each [[DSPyOptimizers|Optimizer]] run, call the same evaluator on the optimized program to compare against the baseline.
- **Metric-iteration comparison.** When the metric itself is iterated (Step 4 of the recursive loop), call the evaluator with the **new metric** against the **same program** to spot scoring drift.

This is the **dev-set-as-fixed-reference** discipline `Evaluate`'s reuse pattern operationalizes.

## Relationship to internal Optimizer evaluation

[[DSPyOptimizers|DSPy Optimizers]] use **the same metric contract** `dspy.Evaluate` does — they call `metric(example, pred, trace)` over candidates against the same dev set. The user-facing `Evaluate` is therefore **structurally identical** to the optimizer's internal evaluation pass; the difference is purpose:

- **User-facing `dspy.Evaluate`** — *"is my current program any good against this metric?"* — runs once per program version.
- **Optimizer-internal evaluation** — *"is this candidate program better than the previous candidate?"* — runs once per candidate inside the search loop.

Both **always call metrics with `trace=None`** — the `trace is not None` regime is reserved for the Optimizer's **bootstrap phase**, which is a different sub-routine from its evaluation pass.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-tutorial-math]] — simplest end-to-end receipt: `dspy.Evaluate(devset=dataset.dev, metric=dataset.metric, num_threads=24, display_progress=True, display_table=5)` against the [[MATH-benchmark|MATH]] algebra subset; same evaluator instance scores baseline and post-MIPROv2 program.
- [[dspy-rag-tutorial]] — canonical multi-stage `dspy.Evaluate(devset=..., metric=SemanticF1(), num_threads=24, ...)` walk from 42% [[SemanticF1]] baseline to optimized RAG; the [[SemanticF1]] metric is itself a [[DSPyModules|`dspy.Module`]].
- [[dspy-entity-extraction-tutorial]] — `evaluate_correctness = dspy.Evaluate(devset=..., metric=extraction_correctness_metric, ...)` with a custom exact-list-match metric over CoNLL-2003 PER spans; demonstrates the *"baseline → optimize → re-evaluate"* reuse pattern.
- [[dspy-multihop-search-tutorial]] — `dspy.Evaluate(devset=devset, metric=top5_recall, num_threads=16, ...)` over [[HoVer]] 3-hop; shows `Evaluate` running the same dual-mode metric the [[MIPROv2|MIPROv2]] optimizer climbs internally.
- [[dspy-tool-use-tutorial]] — `dspy.Evaluate(devset=devset, metric=metric, num_threads=24, display_progress=True, display_table=0)` paired with [[SIMBA|`dspy.SIMBA`]] over [[ToolHop]]; `display_table=0` because trajectories are too wide to render.
- [[dspy-tutorial-classification-finetuning]] — `dspy.Evaluate(devset=devset, metric=metric, display_progress=True, display_table=5, num_threads=16)` brackets a [[BootstrapFinetune|`dspy.BootstrapFinetune`]] run on Banking77 (66% → 87%); evaluator is reused before and after weight-tuning.
- [[dspy-tutorial-games]] — `dspy.Evaluate(devset=devset, metric=metric, display_progress=True, ...)` with `metric = lambda x, y, trace=None: y.success` over [[AlfWorld]]; the simplest possible metric callable feeding `Evaluate`.
- [[dspy-observability-tutorial]] — meta-receipt: documents the `on_evaluate_start` / `on_evaluate_end` [[MLflow]] callback hooks that attach to `dspy.Evaluate` runs for tracing and lifecycle observability.

## Connections

- [[DSPy]] — the framework `dspy.Evaluate` is a built-in utility of.
- [[dspy-metrics]] — the canonical source for this concept (page 11 of 13 of the *Learn* section); mints this page alongside [[DSPyMetrics]].
- [[DSPyMetrics]] — the **sibling concept**; the function-signature contract `dspy.Evaluate` calls. A metric is the *what to measure*; `Evaluate` is the *how to apply the measurement*.
- [[DSPyEvaluation]] — the parent concept (the Evaluation stage); `dspy.Evaluate` is the harness that operationalizes Step 3 (*"run development evaluations on the pipeline"*).
- [[dspy-evaluation-overview]] — page 9 of 13; the four-step loop within which Step 3 lives.
- [[dspy-data]] — page 10 of 13; defines the `list[dspy.Example]` dev-set shape `Evaluate` consumes via its `devset=` kwarg and the [[DSPyExample|`Example.inputs()`]] accessor `Evaluate` uses to extract input fields.
- [[DSPyExample]] — the dev-set element type; `Evaluate`'s `devset=` kwarg expects `list[DSPyExample]`.
- [[DSPyPrediction]] — the program-output type the metric receives; what `program(**x.inputs())` returns.
- [[DSPyModules]] — `Evaluate` runs a [[DSPyModules|`dspy.Module`]] over the dev set; the program-side argument is any callable that returns a [[DSPyPrediction|`Prediction`]].
- [[DSPyOptimizers]] — **forward reference to page 13 of 13**; uses the same metric contract internally. `Evaluate`'s dev-set-comparison role is the user-facing analog of the Optimizer's per-candidate evaluation.
- [[OfflineEvaluation]] — the regime `Evaluate` operates in; held-out dev set, not live traffic.
- [[ModelEvaluation]] — the general wiki concept; `Evaluate` is the DSPy-specific operational utility.
