---
title: "Number of Epochs"
type: concept
tags: [training, hyperparameters, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Number of Epochs

A training hyperparameter: **the number of complete passes through the training dataset**. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "An epoch is a pass over the training data. The number of epochs determines how many times each training example is trained on."

## Rule of thumb (Ch 7)

- **Millions of examples** (pre-training-scale) → **1–2 epochs** sufficient.
- **Thousands of examples** (typical finetuning) → **4–10 epochs** may still improve performance.
- **Hundreds of examples** (few-shot finetuning) → **more epochs** can help but watch for [[Overfitting|overfitting]].

The intuition: smaller datasets need more passes because each example needs more "drilling" for the model to internalize the pattern.

## How to diagnose the right number

Ch 7's heuristic uses the **gap between training loss and validation loss**:

- **Both training loss and validation loss still decreasing** → train for more epochs.
- **Training loss decreasing, validation loss increasing** → [[Overfitting|overfitting]]; reduce epochs (or add regularization, or get more data).
- **Both plateaued** → adding epochs won't help; need a different lever.

## Interaction with [[BatchSize|batch size]]

Number of epochs and batch size combine to give the **total number of gradient updates** = `(num_examples / batch_size) × num_epochs`. Different combinations giving the same total update count don't necessarily produce the same model quality — empirically, batch size and epochs each matter.

## Connections

- [[Overfitting]] — the failure mode that bounds epoch count from above.
- [[BatchSize]] — the orthogonal axis of training extent.
- [[LearningRate]] / [[LearningRateScheduler]] — the per-update step size.
- [[HyperparameterTuning]] — the broader discipline.
- [[ValidationLoss]] / [[TrainingLoss]] — the diagnostic signals.
- [[ai-engineering-ch07-finetuning]] — primary source.
