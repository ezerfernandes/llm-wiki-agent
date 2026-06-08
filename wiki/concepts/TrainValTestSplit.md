---
title: "Train/Val/Test Split"
type: concept
tags: [evaluation, methodology]
sources: [madewithml-splitting, mechanics-of-ml]
last_updated: 2026-06-04
---

# Train/Val/Test Split

Partitioning data into a training set (fit), validation set (tune), and test set (final unbiased estimate). Often combined with [[StratifiedSampling]] to preserve class balance and prevent [[Overfitting]].

## The "testing trilogy" — *The Mechanics of Machine Learning*

[[mechanics-of-ml|Parr & Howard]] call it the **testing trilogy**: train (learn) → validate (tune [[Hyperparameter|hyperparameters]]) → test (final, untouched). The test set is sacred — "the only true measure of model generality comes from computing metrics on a test set that has never previously been run through the model," because "every change made to a model after testing it on a dataset, tailors the model to that dataset." Two regimes: random ~70/15/15 holdout for **time-insensitive** data; **time-based** splitting (sort chronologically, last 15% = test, prior 15% = validation) for time-series, since random splitting "allows the model to train on data from the future." Cautionary stat: 108 of 475 Kaggle bulldozer competitors hit perfect validation via overfitting yet failed the hidden test set. Note [[OutOfBagScore|OOB scores]] are over-optimistic for time-series.
