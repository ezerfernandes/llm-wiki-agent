---
title: "DSPy Tutorial — Tracking DSPy Optimizers with MLflow"
type: source
tags: [dspy, tutorial, mlflow, autologging, experiment-tracking, optimization, miprov2, observability, gsm8k]
date: 2026-05-24
source_file: raw/dspy-optimizer-tracking-tutorial.md
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/optimizer_tracking/` that wires **[[MLflow]] autologging** into a [[MIPROv2|`dspy.MIPROv2`]] optimization run end-to-end. The first wiki-corpus source whose **central subject** is **tracking the optimization process itself** — every prior MLflow-mentioning DSPy ingest ([[dspy-custom-module]], [[dspy-tutorial-rag-as-agent]], [[dspy-entity-extraction-tutorial]]) treated `mlflow.dspy.autolog()` as a one-line side-channel; this tutorial canonicalizes the **three optimization-aware autolog kwargs** (`log_compiles` / `log_evals` / `log_traces_from_compile`), the **parent/child run hierarchy** MLflow imposes on a MIPROv2 search, and the **model-loading round-trip** from MLflow artifact store back into a `dspy.Module` instance via `program.load(...)`.

## Key Claims

- **MLflow ≥ 2.21.1 is the minimum supported version** for the DSPy autologging surface described here — earlier versions lack the optimization-aware tracking hooks. The wiki's prior canonical receipt ([[dspy-custom-module]]) called for `mlflow>=3.0.0`; this tutorial's 2.21.1 floor confirms the DSPy autolog surface predates the MLflow 3.0 line and is supported across the 2.x and 3.x lines alike.
- **The DSPy autologging API exposes three optimization-aware kwargs**: `mlflow.dspy.autolog(log_compiles=True, log_evals=True, log_traces_from_compile=True)` — three independent toggles for the three artifact families MLflow can capture from a compile() call.
- **`log_compiles=True` tracks the optimization workflow itself** — the optimizer's config (number of few-shot examples, number of candidates, `auto` preset), every intermediate program version produced during the search, and the metric-progression curve.
- **`log_evals=True` tracks evaluation results** — both the optimizer's internal mini-batch evaluations during the discrete-search stage and any standalone `dspy.Evaluate` calls.
- **`log_traces_from_compile=True` captures execution traces during compilation** — every LM call made during the optimizer's bootstrap and grounded-proposal stages, with prompts and responses.
- **Server expected to be running at `http://localhost:5000`** — the tutorial recommends launching MLflow via `mlflow server --backend-store-uri sqlite:///mydb.sqlite` and asserts *"It is highly recommended to use SQL store when using MLflow tracing"* (in-memory or file-based stores lose the trace tree).
- **Optimization runs nest as parent/child runs**: the parent run represents the **overall optimization process** (config + final optimized program + metric progression curve + training data); each child run represents **one intermediate program version** produced during MIPROv2's discrete-search stage (parameters + artifacts + execution traces for that specific candidate).
- **Optimized programs can be loaded back via `mlflow.artifacts.download_artifacts(...)` + `program.load(model_path)`** — round-trips the optimizer output through the MLflow artifact store rather than the plain-JSON `program.save(path)` route used in earlier tutorials.
- **Memory caveat**: *"For large datasets, consider setting `log_traces_from_compile=False` to avoid memory issues"* — the per-call trace capture grows linearly with optimizer trials × bootstrap demos × dataset size, and can exceed memory budgets on long runs.
- **Working example uses `dspy.ChainOfThought("question -> answer")` on [[GSM8K]] with `dspy.MIPROv2(metric=gsm8k_metric, auto="light")`** — first wiki-corpus DSPy receipt of MIPROv2 on GSM8K via DSPy's in-framework `dspy.datasets.gsm8k.GSM8K` loader and its built-in `gsm8k_metric`.
- **Programmatic run-data access via `mlflow.get_run(run_id)`** — the tutorial's troubleshooting note surfaces the standard MLflow API for retrieving captured runs after the fact, independent of the UI.

## Key Quotes

> "MLflow's built-in integration for DSPy provides traceability and debuggability for your DSPy optimization experience. It allows you to understand the intermediate trials during the optimization, store the optimized program and its results, and provides observability into your program execution." — opening framing

> "Through the autologging capability, MLflow tracks the following information: **Optimizer Parameters** (Number of few-shot examples, Number of candidates, Other configuration settings); **Program States** (Initial instructions and few-shot examples, Optimized instructions and few-shot examples, Intermediate instructions and few-shot examples during optimization); **Datasets** (Training data used, Evaluation data used); **Performance Progression** (Overall metric progression, Performance at each evaluation step); **Traces** (Program execution traces, Model responses, Intermediate prompts)." — autolog scope

> "It is highly recommended to use SQL store when using MLflow tracing" — backend-store guidance

> "The parent run represents your overall optimization process, while the child runs show each intermediate version of your program that was created during optimization." — run hierarchy

> "One of the most powerful features is the Traces tab, which provides a step-by-step view of your program's execution. Here you can understand exactly how your DSPy program processes inputs and generates outputs." — Traces tab as the canonical optimizer-debugging surface

> "If traces aren't appearing, ensure `log_traces_from_compile=True`" — troubleshooting

> "For large datasets, consider setting `log_traces_from_compile=False` to avoid memory issues" — memory-budget caveat

## The four-step setup recipe

The tutorial codifies a **four-step setup** that other DSPy ingests now refer back to:

```bash
# 1. Install
pip install mlflow>=2.21.1
```

```bash
# 2. Launch tracking server (sqlite backend; recommended over the file backend)
mlflow server --backend-store-uri sqlite:///mydb.sqlite
```

```python
# 3. Enable autologging (three optimization-aware kwargs)
import mlflow
import dspy

mlflow.dspy.autolog(
    log_compiles=True,
    log_evals=True,
    log_traces_from_compile=True,
)
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("DSPy-Optimization")
```

```python
# 4. Run optimization — tracking is automatic from this point
import dspy
from dspy.datasets.gsm8k import GSM8K, gsm8k_metric

lm = dspy.LM(model="openai/gpt-4o")
dspy.configure(lm=lm)

gsm8k = GSM8K()
trainset, devset = gsm8k.train, gsm8k.dev

program = dspy.ChainOfThought("question -> answer")

teleprompter = dspy.teleprompt.MIPROv2(metric=gsm8k_metric, auto="light")
optimized_program = teleprompter.compile(program, trainset=trainset)
```

The step-4 receipt is **the wiki's first MIPROv2 receipt on [[GSM8K]]** via DSPy's in-framework dataset loader + built-in `gsm8k_metric`, and the **first MIPROv2 receipt using `gpt-4o` as the task LM** (every prior MIPROv2 receipt in the corpus used `gpt-4o-mini` or a Llama student). The tutorial reports no headline accuracy number — its scope is the tracking surface, not the optimization gain.

## The three autolog kwargs

| Kwarg | What gets captured | Cost axis |
|---|---|---|
| `log_compiles=True` | Optimizer config, intermediate program versions (instructions + few-shot demos per attempt), metric-progression curve, training data | Lightweight — one row per optimizer trial |
| `log_evals=True` | Per-step evaluation metric values (during compile() and during standalone `dspy.Evaluate`) | Moderate — one row per evaluation |
| `log_traces_from_compile=True` | Per-LM-call trace tree (prompts, responses, timing) for every call inside the optimizer's bootstrap / proposal / search stages | **Heavy** — linear in (trials × demos × dataset size); tutorial recommends disabling for large datasets |

The three kwargs are **independent toggles** — disabling `log_traces_from_compile` still preserves the program-version progression and metric curve, just not the LM-call-level granularity.

## Parent/child run hierarchy

MIPROv2's three-stage algorithm ([[MIPROv2|bootstrapping → grounded proposal → discrete search]]) produces many intermediate program versions during the discrete-search stage — one per (instruction, demo-set) candidate the [[BayesianOptimization|Bayesian surrogate]] samples. MLflow's autolog hook materializes this structure as a **two-level run tree**:

| Level | Represents | Stored artifacts |
|---|---|---|
| **Parent run** | The overall `teleprompter.compile(program, trainset=trainset)` call | Optimizer config (`auto`, `metric` name, kwargs), final optimized program JSON (with signature + instructions + demos), training data snapshot, metric progression across trials |
| **Child run** | One intermediate program version produced during discrete search | Per-attempt parameters (which instruction / demo-set combination was tested), the intermediate program's JSON, the Traces tab (step-by-step LM-call tree for that attempt's evaluation runs) |

This structure makes the run UI the **canonical introspection surface for MIPROv2's search trajectory** — clicking through child runs is how you see *which instructions the proposer drafted* and *which demo combinations got selected* over the course of the search. The structure is **specific to optimization runs** — inference-time `mlflow.dspy.autolog()` use ([[dspy-custom-module]], [[dspy-tutorial-rag-as-agent]]) produces a single trace tree per `__call__`, not a parent/child run pair.

## Model-loading round-trip

The tutorial demonstrates loading the optimized program back from the MLflow artifact store into a `dspy.Module` instance:

```python
model_path = mlflow.artifacts.download_artifacts("mlflow-artifacts:/path/to/best_model.json")
program.load(model_path)
```

This is the **second documented load path** for optimized DSPy programs in the wiki — the first being the plain-text JSON `program.save(path)` / `program.load(path)` round-trip ([[dspy-optimizers|Optimizers page]], [[dspy-entity-extraction-tutorial]], [[dspy-tutorial-rag-as-agent]]). Both ultimately call `program.load(...)` against a JSON file; the MLflow path adds **provenance** (the artifact is stored against a tracked run with the optimizer config + metric progression that produced it) at the cost of a running tracking server.

## Connections

- [[MLflow]] — the entity. This tutorial is the canonical wiki source for the **optimizer-aware autologging kwargs** (`log_compiles` / `log_evals` / `log_traces_from_compile`); the [[dspy-custom-module|DSPy Custom Module tutorial]] supplied the bare `mlflow.dspy.autolog()` recipe and the [[dspy-tutorial-rag-as-agent|RAG-as-Agent tutorial]] confirmed it traces [[react|ReAct]] trajectories — this tutorial completes the picture at the optimization-stage layer.
- [[MIPROv2]] — the optimizer used in the worked example; the tutorial is the wiki's canonical source for *what MIPROv2's internal trial structure looks like when surfaced through an external tracking system*. The parent/child run mapping makes MIPROv2's [[BayesianOptimization|Bayesian-surrogate]] discrete-search trajectory directly inspectable.
- [[DSPyOptimization]] — the workflow stage this tutorial instruments.
- [[DSPyOptimizers]] — the catalog. Tracking is a cross-cutting concern across every optimizer that has a compile() loop; the three autolog kwargs are optimizer-agnostic.
- [[ExperimentTracking]] — the general concept this tutorial operationalizes for DSPy.
- [[GSM8K]] — the dataset used in the worked example; first wiki-corpus MIPROv2 receipt on GSM8K.
- [[chainofthought|ChainOfThought]] — the entire program in the worked example, mirroring [[dspy-tutorial-math]]'s *one-line-program* shape.
- [[BayesianOptimization]] — the search algorithm whose trajectory MLflow's parent/child run tree exposes.
- [[Databricks]] — MLflow's parent organization; this tutorial is the third [[Databricks]] touchpoint on the DSPy line after [[MateiZaharia|Matei Zaharia]]'s authorship of [[2406.11695-mipro|MIPRO]] / [[2507.19457-gepa|GEPA]] and the MLflow gateway role in [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]].
- [[DSPy]] — the framework.
- [[dspy-custom-module]] — prior wiki source for the bare `mlflow.dspy.autolog()` recipe; this tutorial is its optimization-aware sibling.
- [[dspy-tutorial-rag-as-agent]] — prior wiki source confirming `mlflow.dspy.autolog()` traces [[react|ReAct]] trajectories during inference.
- [[dspy-entity-extraction-tutorial]] — prior wiki source touching `mlflow.dspy.log_model(...)` for production-shaped MLflow registry use.
- [[DSPyModules]] — the program input/output type.
- [[DSPyPredict]] — the parameter site MIPROv2 mutates (instructions + demos) and MLflow captures per intermediate program version.
- [[Observability]] — the umbrella concept the tutorial frames its contribution as ("provides observability into your program execution").
- [[Monitoring]] — adjacent MLOps surface; tracking is the offline-experiment cousin of online monitoring.
- [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]] — names MLflow AI Gateway as a canonical [[ModelGateway]] solution; this tutorial documents the same MLflow platform's experiment-tracking surface.

## Contradictions

- **MLflow version floor**: the [[dspy-custom-module|DSPy Custom Module tutorial]] called for `mlflow>=3.0.0`; this tutorial calls for `mlflow>=2.21.1`. Resolution: both work — the DSPy autolog surface predates MLflow 3.0 and is supported on both lines. The 3.0.0 floor in [[dspy-custom-module]] is the more conservative recommendation (likely picking the version current at that tutorial's writing); 2.21.1 is the actual minimum supported version.

## Scope-limit gaps

- **No headline accuracy gain reported** — the tutorial demonstrates the tracking surface, not the optimization outcome. The wiki's MIPROv2 receipt on a single-line-CoT-on-math program is [[dspy-tutorial-math]] (MATH algebra 74→88.57); GSM8K with this exact recipe is uninstrumented in the corpus.
- **No discussion of multi-run aggregation** — MIPROv2's `auto="light"/medium/heavy"` presets produce vastly different child-run counts; the tutorial doesn't compare. The MLflow UI's metric-progression chart aggregates per parent run but the cross-parent-run comparison surface is undocumented here.
- **No mention of the MLflow Model Registry** — the artifact-download path stops at `mlflow.artifacts.download_artifacts(...)`, not the registered-model API. The [[dspy-entity-extraction-tutorial|Entity Extraction tutorial]] uses `mlflow.dspy.log_model(...)` (which targets the registry); the two artifact paths are not reconciled.
- **No GEPA tracking receipt** — [[GEPA]] has a different optimizer trajectory (LM-reflection rather than Bayesian search); whether `log_compiles=True` captures GEPA's reflection traces in the same parent/child shape is not addressed.
- **No cost tracking** — `lm.history`-based cost reporting ([[dspy-entity-extraction-tutorial]]) is not integrated into the MLflow surface here.
- **No `dspy.Evaluate` standalone example** — `log_evals=True` is documented as covering both compile-time and standalone evaluations, but only the compile-time path is exercised.
- **Memory-budget caveat is qualitative** — no thresholds, no benchmarks for *when* `log_traces_from_compile=False` becomes necessary.
