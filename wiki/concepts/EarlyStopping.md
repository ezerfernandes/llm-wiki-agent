---
title: "Early Stopping"
type: concept
tags: [regularization, training]
sources: [d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Early Stopping

Halting training when validation loss stops improving for a *patience* window, preventing overfitting and saving compute. Standard companion to [[Adam]] and [[LearningRateScheduler]] in [[FineTuning]] runs; relies on a meaningful [[DataSplitting]] of [[HoldoutDataset]] data.

## Why it works in deep learning

[[d2l-multilayer-perceptrons]] §Early Stopping: deep networks fit *cleanly-labeled* examples first and only later interpolate noisy / mislabeled examples (Rolnick et al. 2017). Cutting off training before the second phase yields better generalization in the presence of label noise (Garg et al. 2021). When labels are clean and the task is *realizable*, early stopping helps less.

## Patience criterion

Track validation error after each epoch; stop when it has not decreased by more than $\epsilon$ for $N_\text{patience}$ epochs. Restore the best-checkpoint weights.

## Practical wins beyond regularization

For multi-day GPU training runs, well-tuned early stopping saves substantial wall-clock + cloud cost — [[d2l-multilayer-perceptrons]] flags this as a primary benefit even when regularization gains are marginal.

## Connections

- [[d2l-multilayer-perceptrons]] — §Early Stopping (canonical reference).
- [[Regularization]] / [[WeightDecay]] / [[Dropout]] — companion regularizers in deep learning.
- [[Overfitting]] / [[Generalization]] — what early stopping mitigates.
- [[HoldoutDataset]] / [[CrossValidation]] — the validation infrastructure required.
- [[Checkpoint]] / [[ModelCheckpoint]] — best-weights restoration.
