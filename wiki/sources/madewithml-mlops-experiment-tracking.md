---
title: "Made With ML — Experiment Tracking"
type: source
tags: [mlops, made-with-ml, experiment-tracking, mlflow]
date: 2026-05-15
source_file: raw/madewithml/mlops-experiment-tracking.md
---

## Summary
The experiment-tracking lesson plugs [[MLflow]] into the Ray training workflow via `MLflowLoggerCallback` so that every run's parameters, metrics, artifacts, and checkpoints are logged automatically. The tracking URI points at a local filesystem store (`/tmp/mlflow`) for the course; in production it would be S3 + a managed database (PostgreSQL RDS). After training, `mlflow.search_runs` sorts runs by `val_loss`, the best `run_id` is mapped back to its Ray checkpoint via `Result.from_path`, and `TorchPredictor.from_checkpoint` loads the model for evaluation and inference.

## Key Claims
- Experiment tracking exists to *organize* run components, enable *reproducibility*, and *log* iterative improvements over time/data/ideas/teams.
- [[MLflow]] is chosen because it is fully free, open-source, self-hostable, and used at Microsoft, Facebook, and Databricks; alternatives include Comet ML, Neptune, and Weights & Biases.
- The MLflow logger is wired into Ray via `RunConfig(callbacks=[mlflow_callback], checkpoint_config=...)` — no extra code in the training loop.
- For local development the artifact store and backend store both live on disk; production deployments use remote object storage (S3) and a database backend (PostgreSQL RDS).
- `MLflowLoggerCallback(save_artifact=True)` automatically logs all standard components; direct `mlflow.log_*` calls can still be used for custom logging.
- `mlflow.search_runs(experiment_names=[...], order_by=["metrics.val_loss ASC"])` returns ranked runs as a pandas DataFrame for downstream selection.
- The `mlflow server -h 0.0.0.0 -p 8080 --backend-store-uri /tmp/mlflow/` command launches the web dashboard for plots, params, metrics, and custom visualizations.
- A `get_best_checkpoint(run_id)` helper translates MLflow's artifact URI back into a Ray `Result` to recover the best checkpoint.

## Key Quotes
> "Experiment tracking is the process of managing all the different experiments and their components, such as parameters, metrics, models and other artifacts and it enables us to: Organize all the necessary components of a specific experiment... Reproduce past results (easily) using saved experiments... Log iterative improvements across time, data, ideas, teams, etc."

> "We can run MLFlow on our own servers and databases so there are no storage cost / limitations, making it one of the most popular options and is used by Microsoft, Facebook, Databricks and others."

## Connections
- [[MadeWithML]] — parent course.
- [[GokuMohandas]] — author.
- [[Anyscale]] — publisher.
- [[Ray]] — surrounding runtime.
- [[RayTrain]] — training integration point.
- [[MLflow]] — experiment tracker used throughout.
- [[ExperimentTracking]] — the lesson's central concept.
- [[ModelRegistry]] — MLflow's storage role.
- [[CometML]] — alternative tracker referenced.
- [[Neptune]] — alternative tracker referenced.
- [[WeightsAndBiases]] — alternative tracker referenced.
- [[microsoft]] — listed as an MLflow user.
- [[Facebook]] — listed as an MLflow user.
- [[Databricks]] — listed as an MLflow user (and MLflow originator).
- [[PostgreSQL]] — recommended production backend store.
- [[AmazonS3]] — recommended production artifact store.
- [[Reproducibility]] — primary motivation for tracking.
- [[Checkpoint]] — Ray Train checkpoint loaded via MLflow's artifact URI.
- [[MLOps]] — surrounding discipline.

## Contradictions
- None identified.
