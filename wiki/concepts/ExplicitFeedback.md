---
title: "Explicit Feedback"
type: concept
tags: [recommender-systems, data]
sources: [d2l-recommender-systems, d2l-introduction]
last_updated: 2026-05-16
---

# Explicit Feedback

User preference signals **proactively provided by the user** — star ratings, thumbs up/down, written reviews. Canonical examples: IMDb 1–10 stars, Netflix 1–5 stars, YouTube thumbs.

## Defining traits

- **High-quality** — the user directly states a preference; little inference required.
- **Scarce** — collection requires user effort; *"many users may be reluctant to rate products"* ([[d2l-recommender-systems]]).
- **Censored / biased** — users preferentially rate items they feel strongly about, producing a bimodal one-star / five-star distribution (flagged on [[RecommenderSystems]] as a pathology from [[d2l-introduction]]).
- **Numeric / ordinal** — supports regression framings (predict the star rating) and the [[RMSE]] evaluation metric.

## Canonical datasets

- **[[MovieLens]]** — 1–5 stars; D2L's running benchmark.
- **Netflix Prize** dataset — 1–5 stars on ~480k users × 17k movies.
- **Yahoo! Music**, **Book-Crossing** — historical academic benchmarks.

## Modeling consequences

- **Rating prediction is the natural framing** — MSE / [[RMSE]] on observed entries. [[MatrixFactorization]] and [[AutoRec]] are designed for this regime.
- **Side information (timestamps, demographics) is helpful but not required** when explicit ratings carry strong signal.
- **Unobserved entries are treated as missing-at-random** by default — usually false in practice but tolerable for the rating-prediction task.

## Connections
- [[ImplicitFeedback]] — sibling category (more abundant, noisier).
- [[MatrixFactorization]], [[AutoRec]] — canonical explicit-feedback models.
- [[RMSE]] — explicit-feedback evaluation metric.
- [[MovieLens]] — canonical dataset.
- [[RecommenderSystems]] — parent application.
- [[d2l-recommender-systems]], [[d2l-introduction]] — sources.
