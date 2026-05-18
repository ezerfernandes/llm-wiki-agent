---
title: "Made With ML — Moving from Notebooks to Scripts"
type: source
tags: [mlops, made-with-ml, scripting, software-engineering]
date: 2026-05-15
source_file: raw/madewithml/mlops-scripting.md
---

## Summary
Made With ML lesson on graduating a project from Jupyter notebooks to organized Python scripts. Argues notebooks are stateful and non-linear and therefore poor substrate for production code, then shows a canonical module layout (`config.py`, `data.py`, `train.py`, `tune.py`, `evaluate.py`, `predict.py`, `serve.py`, `models.py`, `utils.py`). Covers wrapping notebook cells in workload functions, isolating shared config and utilities to avoid circular imports, and initializing Ray inside the script that actually needs it.

## Key Claims
- Notebooks are problematic for production because they have hidden global state, non-linear execution order, and resist standard testing tooling.
- Scripts are stateless and linear, which makes them composable, testable, and the precondition for CLI-driven workflows.
- The script organization should be intuitive — if you cannot decide which file a function belongs in, the file names are wrong.
- Free-floating cells in a notebook (e.g. `ScalingConfig` setup) must be wrapped in named workload functions like `train_model(experiment_name, dataset_loc, ...)` so they can be invoked from a CLI.
- `config.py` should hold only cross-workload configuration (e.g. MLflow tracking URI); workload-specific config like `ScalingConfig` stays with the workload.
- `utils.py` holds shared components (e.g. `set_seeds`) to prevent circular dependencies between domain scripts.
- Ray should be initialized inside the entrypoint (`if __name__ == "__main__"`) only for scripts that actually need it, not globally.

## Key Quotes
> "Scripts, on the other hand, are stateless and we have to explicitly pass variables to functions and classes." — on why scripts beat notebooks for production

## Connections
- [[MadeWithML]] — source course
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher
- [[Ray]] — distributed runtime initialization
- [[MLflow]] — referenced in config
- [[Jupyter]] — notebook environment being replaced
- [[VSCode]] — recommended editor
- [[MLOps]] — discipline
- [[CodeOrganization]] — primary topic
- [[NotebookToScript]] — workflow concept
- [[WorkloadFunction]] — pattern for CLI-invokable units
- [[ReproducibilityInML]] — motivation
- [[Typer]] — CLI app referenced for `app()` entry

## Contradictions
- None identified.
