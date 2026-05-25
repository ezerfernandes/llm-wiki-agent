---
title: "Experiment Tracking"
type: concept
tags: [mlops, reproducibility, mlflow, dspy, optimization, autologging]
sources: [dspy-optimizer-tracking-tutorial]
last_updated: 2026-05-24
---

# Experiment Tracking

Systematic logging of model training runs — hyperparameters, metrics, code version, dataset version, artifacts — via tools like [[MLflow]], Weights & Biases, or Comet. Enables reproducibility, comparison, and audit; requires [[Determinism]] and integrates with [[DVC]] and [[CICD]].

## Experiment tracking for LM-program optimization — the [[DSPy]] / [[MLflow]] receipt

The [[dspy-optimizer-tracking-tutorial|DSPy Optimizer Tracking tutorial]] is the wiki's canonical source for **what experiment tracking means in the LM-program-optimization regime** — a setting that doesn't fit the classical ML-training mold cleanly because the *"experiment"* is a [[MIPROv2|MIPROv2]]-style discrete search over instructions and demonstrations rather than a gradient-descent training loop. Three structural adaptations make MLflow apply to the DSPy regime:

| Classical-ML axis | DSPy / LM-program adaptation |
|---|---|
| **Hyperparameters** | Optimizer config (`auto` preset, `max_bootstrapped_demos`, `max_labeled_demos`, `num_threads`, metric name) |
| **Training-loss curve** | Metric-progression curve across optimizer trials (each trial is a `(instruction, demo-set)` candidate, not a gradient step) |
| **Model checkpoints** | Intermediate program versions (each one a JSON snapshot of instructions + few-shot demos) — one per child run in the MLflow parent/child run tree |
| **Inference traces** | Per-LM-call traces during compile() (prompts, responses, timing) — enabled by `log_traces_from_compile=True` |
| **Final model artifact** | The optimized [[DSPyModules|`dspy.Module`]] subclass — a JSON file with the final instructions + demos, loadable via `program.load(model_path)` |

The DSPy-specific autologging API exposes three optimization-aware kwargs — `mlflow.dspy.autolog(log_compiles=True, log_evals=True, log_traces_from_compile=True)` — that toggle the three artifact families (workflow / evaluations / traces) independently. The **parent/child run hierarchy** (parent = overall `compile()`; child = each intermediate program version) is the optimization-stage analogue of nested runs in classical ML hyperparameter sweeps.

## Connections

- [[MLflow]] — the canonical experiment-tracking tool for DSPy work; the autologging hook (`mlflow.dspy.autolog()`) is documented across [[dspy-custom-module]] (inference-time), [[dspy-tutorial-rag-as-agent]] ([[react|ReAct]] trajectories), [[dspy-entity-extraction-tutorial]] (`mlflow.dspy.log_model()` for the registry), and [[dspy-optimizer-tracking-tutorial]] (the three optimization-aware kwargs).
- [[dspy-optimizer-tracking-tutorial]] — canonical wiki source for **optimization-stage experiment tracking** in the DSPy regime.
- [[DSPyOptimization]] — the workflow stage experiment tracking instruments in the DSPy setting.
- [[DSPyOptimizers]] — the catalog; experiment tracking applies cross-optimizer.
- [[MIPROv2]] — the worked example whose discrete-search trajectory the parent/child run tree exposes.
- [[Monitoring]] — adjacent MLOps surface; tracking is the offline-experiment cousin of online monitoring.
- [[Observability]] — the broader category experiment tracking is one slice of.
- [[Determinism]] — prerequisite for reproducibility; tracking captures inputs/outputs but only reproduces the run when the underlying LM calls are deterministic (often via temperature=0 + fixed seeds, both fragile guarantees with hosted LMs).
- [[DVC]] — data-version pendant to model-tracking systems.
- [[CICD]] — the broader pipeline tracking integrates into.
- [[MLOps]] — the umbrella discipline.
- [[Reproducibility]] — the property tracking supports but does not by itself guarantee.
