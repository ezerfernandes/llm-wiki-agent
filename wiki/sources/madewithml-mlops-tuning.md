---
title: "Made With ML — Hyperparameter Tuning"
type: source
tags: [mlops, made-with-ml, hyperparameter-tuning, ray-tune]
date: 2026-05-15
source_file: raw/madewithml/mlops-tuning.md
---

## Summary
The tuning lesson runs hyperparameter optimization on the fine-tuned [[SciBERT]] classifier using [[RayTune]] with the [[HyperOpt]] search algorithm and the [[ASHA]] (`AsyncHyperBandScheduler`) for aggressive early stopping. Four hyperparameters are searched — `dropout_p` (uniform 0.3-0.9), `lr` (loguniform 1e-5 to 5e-4), `lr_factor` (uniform 0.1-0.9), and `lr_patience` (uniform 1-10). Runs are concurrency-limited and logged to MLflow via the same `MLflowLoggerCallback` from the previous lesson. The best trial reaches F1=0.947 on the holdout set.

## Key Claims
- Not every hyperparameter must be tuned — it's acceptable to fix some (e.g. `lower=True` for text preprocessing) and tune a small, influential subset first.
- [[RayTune]] is chosen for its simplicity and integration with HyperOpt, Optuna, and Bayesian search algorithms.
- Tuning configuration requires three pieces: a stopping criterion, a search algorithm (next-parameter chooser), and a search space (parameter distributions).
- Seeding the search with `points_to_evaluate=initial_params` guarantees at least one reasonable baseline trial.
- `ConcurrencyLimiter(search_alg, max_concurrent=2)` caps simultaneous trials based on available compute.
- [[ASHA]] is an aggressive early-stopping scheduler that prunes unpromising trials; `grace_period` ensures every trial runs at least a few epochs before being killed.
- A `TuneConfig(metric="val_loss", mode="min", search_alg, scheduler, num_samples=num_runs)` glues the pieces together for the `Tuner`.
- The best trial's hyperparameters were `{dropout_p: 0.5, lr: 1e-4, lr_factor: 0.8, lr_patience: 3.0}` and produced test F1=0.947, precision=0.949, recall=0.948.

## Key Quotes
> "Just because something is a hyperparameter doesn't mean we need to tune it... You can initially just tune a small, yet influential, subset of hyperparameters that you believe will yield great results."

> "It's a good idea to start with some initial parameter values that you think might be reasonable. This can help speed up the tuning process and also guarantee at least one experiment that will perform decently well."

## Connections
- [[MadeWithML]] — parent course.
- [[GokuMohandas]] — author.
- [[Anyscale]] — publisher.
- [[Ray]] — distributed runtime.
- [[RayTune]] — hyperparameter tuning framework.
- [[RayTrain]] — the trainer being tuned (`TorchTrainer`).
- [[HyperOpt]] — search-algorithm backend used.
- [[Optuna]] — alternative tuner referenced.
- [[ASHA]] — `AsyncHyperBandScheduler` for early stopping.
- [[HyperparameterTuning]] — the lesson's core concept.
- [[BayesianOptimization]] — alternative search-algorithm family.
- [[EarlyStopping]] — pattern implemented by ASHA.
- [[SearchSpace]] — uniform / loguniform distributions over params.
- [[MLflow]] — tracking backend reused from the previous lesson.
- [[SciBERT]] — model being tuned.
- [[bert]] — base architecture family.
- [[transformer]] — underlying neural architecture.
- [[LearningRateScheduling]] — `lr_factor` and `lr_patience` parameters.
- [[DropoutRegularization]] — `dropout_p` parameter.
- [[F1Score]] — evaluation metric.
- [[MLOps]] — surrounding discipline.

## Contradictions
- None identified.
