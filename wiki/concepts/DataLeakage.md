---
title: "Data Leakage"
type: concept
tags: [data, evaluation, pitfalls]
sources: [mechanics-of-ml]
last_updated: 2026-06-04
---

# Data Leakage

When information from outside the training set (test labels, future data, target-derived features) inadvertently enters training, inflating offline metrics and collapsing in production. Prevented via disciplined [[DataSplitting]], time-aware folds, and careful [[FeatureEngineering]] inside a [[FeatureStore]] boundary.

## From *The Mechanics of Machine Learning*

[[mechanics-of-ml|Parr & Howard]] define it crisply — "a general term for the use of features that directly or indirectly hint at the target variable" — and surface three concrete forms: (1) **target-derived features** like [[TargetEncoding|target encoding]], which must be fit on training data only ("transformations of validation and test sets can only use data derived from the training set"); (2) **future leakage** from randomly splitting time-series data, which lets a model "train on data from the future" (hence time-based [[TrainValTestSplit|splitting]] for the bulldozer dataset); and (3) the subtle case of **setting denoising bounds after peeking at the data** — fitting your filters to the noise. Filling missing values or encoding categories using val/test statistics is the same mistake.
