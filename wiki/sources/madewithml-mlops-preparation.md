---
title: "Made With ML — Data Preparation"
type: source
tags: [mlops, made-with-ml, data-preparation, splitting]
date: 2026-05-15
source_file: raw/madewithml/mlops-preparation.md
---

## Summary
The data-preparation lesson covers ingesting a CSV dataset into a [[pandas]] DataFrame and splitting it into stratified train/val/test partitions for a multiclass text-classification task. It uses `pd.read_csv` to load the Made-With-ML dataset, then applies `sklearn.model_selection.train_test_split` with `stratify=df.tag` and a fixed `random_state=1234` for reproducibility. A separate holdout CSV serves as the immutable test set so model comparisons remain stable as training data grows.

## Key Claims
- Data may live in many formats (CSV, JSON, Parquet) and locations (DBs, files); CSV → DataFrame via `read_csv` is the entry point for this course.
- Train/val/test splits serve distinct roles: train optimizes weights, val tunes hyperparameters, test gives a final unbiased generalization estimate.
- A separate, frozen holdout test set is preferred over re-splitting the full dataset every time so model comparisons stay valid as data grows.
- Stratified splitting is necessary for multiclass tasks with class imbalance — pass `stratify=df.tag` to `train_test_split`.
- Validation class counts must be rescaled by `α = (1 − N_test) / N_test` to compare distributions against the larger train split.
- Splits should be representative, shuffle-safe (unless time-series where shuffles cause leaks), and class-balanced.
- The example dataset has 310 NLP, 285 CV, 106 other, and 63 MLOps samples — a mild imbalance that does not require resampling.

## Key Quotes
> "Over time, our training data may grow and our test splits will look different every time. This will make it difficult to compare models against other models and against each other."

> "Avoid random shuffles if your task can suffer from data leaks (ex. time-series)."

## Connections
- [[MadeWithML]] — parent course.
- [[GokuMohandas]] — author.
- [[Anyscale]] — publisher.
- [[pandas]] — DataFrame library used for ingestion.
- [[scikitlearn]] — provides `train_test_split` and `stratify`.
- [[DataFrame]] — pandas core data structure.
- [[MLOps]] — broader context.
- [[StratifiedSampling]] — splitting strategy for class-imbalanced data.
- [[DataSplitting]] — the lesson's central technique.
- [[HoldoutDataset]] — frozen test set pattern.
- [[ClassImbalance]] — addressed by stratification.
- [[CSVFormat]] — input file format.
- [[Reproducibility]] — `random_state=1234` for deterministic splits.
- [[DataLeakage]] — risk avoided by proper split ordering.

## Contradictions
- None identified.
