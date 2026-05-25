---
name: FeatureCrossing
title: "Feature Crossing"
type: concept
tags: [feature-engineering, recommender-systems, ctr-prediction]
sources: [dmls-ch05-feature-engineering]
last_updated: 2026-05-23
---

# Feature Crossing

Combining two or more raw features into a single new feature that models a **nonlinear interaction** between them. Essential for linear/logistic/[[GradientBoosting|tree]] models that can't learn interactions implicitly, and a foundational building block of [[DeepFM]] / [[xDeepFM]] / similar [[CTRPrediction|CTR prediction]] architectures per [[ChipHuyen|Huyen]]'s [[dmls-ch05-feature-engineering|DMLS Ch 5]].

## Why
Linear models compute `w · x + b` — they can only express features additively. If the conversion probability for an ecommerce user depends on the **interaction** of `device_type` and `country` (Android users in Brazil convert differently from iOS users in Brazil), the linear model needs an explicit `device_type × country` crossed feature to learn it.

## How
For categorical features: take the Cartesian product (`{Android, iOS} × {BR, US, IN}` → 6 new categories). For continuous features: bucket via [[Discretization]] first, then cross. The result is typically encoded via [[OneHotEncoding|one-hot]] or — if the cross space is huge — the [[HashingTrick|hashing trick]].

## Trade-offs
- **Combinatorial blowup**: a 100-category × 100-category cross yields 10,000 dimensions; nontrivial regularization required.
- **Overfitting risk**: crossed features memorize training combinations easily.
- **Generalization gap**: a `device × country` cross that appears 50× in training but 0× in test contributes noise.
- **Modern alternative**: deep networks ([[MultiLayerPerceptron]], [[transformer|Transformer]]) learn feature interactions implicitly — though [[DeepFM]]-family models combine explicit crosses with deep blocks to get both signal.

## Connections
- [[FeatureEngineering]] — Ch 5 covers crossing as a core operation.
- [[HashingTrick]] — common downstream encoding for high-cardinality crosses.
- [[Discretization]] — usually needed before crossing continuous features.
- [[CTRPrediction]] — canonical application domain.
- [[DeepFM]] / [[xDeepFM]] — architectures that automate feature crossing.
