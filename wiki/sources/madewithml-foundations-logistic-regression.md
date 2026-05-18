---
title: "Made With ML — Logistic Regression"
type: source
tags: [foundations, made-with-ml, machine-learning, classification]
date: 2026-05-15
source_file: raw/madewithml/foundations-logistic-regression.md
---

## Summary
Foundations lesson extending linear regression into multinomial logistic regression — the softmax classifier — implemented from scratch in NumPy and then in PyTorch. Introduces label encoding for categorical targets, the softmax normalization of logits, cross-entropy loss, and standard classification metrics (precision, recall, F1, accuracy). The lesson frames logistic regression as the first true classification model and the canonical "last layer" used in every neural net that follows.

## Key Claims
- Logistic regression is a generalized linear method: instead of predicting a continuous value, it produces a probability distribution over `C` classes via `softmax(XW)`.
- The softmax classifier normalizes logits `z = XW` to non-negative values that sum to one, interpretable as class probabilities.
- Cross-entropy loss is the standard objective: it penalizes low probability assigned to the true class and is what enables gradient-based learning over class distributions.
- Outliers strongly affect logistic regression because cross-entropy magnifies confident wrong predictions; SVMs are noted as a more outlier-robust alternative.
- Class labels must be integer-encoded before training; the lesson uses `LabelEncoder` to map string labels to indices.
- Evaluation requires more than accuracy on imbalanced data — the lesson reports precision, recall, and F1 per class as well.
- The softmax classifier reappears as the final layer in essentially every later neural architecture in the course (MLP, CNN, RNN, attention, transformer).
- PyTorch's `nn.CrossEntropyLoss` internally combines `log_softmax` + `nll_loss`, so the model outputs raw logits.

## Key Quotes
> "Logistic regression is an extension on linear regression (both are generalized linear methods). … Except now we are dealing with classification problems as opposed to regression problems so we'll be predicting probability distributions as opposed to discrete values." — Overview

> "Sensitive to outliers since objective is to minimize cross entropy loss. Support vector machines (SVMs) are a good alternative to counter outliers." — Disadvantages

> "Softmax classifier is widely [used] in neural network architectures as the last layer since it produces class probabilities." — Miscellaneous

## Connections
- [[MadeWithML]] — course this lesson belongs to
- [[GokuMohandas]] — author
- [[PyTorch]] — framework used in the second implementation
- [[NumPy]] — used for the from-scratch implementation
- [[scikit-learn]] — `LabelEncoder`, classification metrics
- [[LogisticRegression]] — model introduced here
- [[Softmax]] — output activation normalizing logits to probabilities
- [[CrossEntropyLoss]] — loss function for classification
- [[LinearRegression]] — direct predecessor, same math without the softmax
- [[SupportVectorMachine]] — mentioned as outlier-robust alternative
- [[LabelEncoding]] — preprocessing for categorical targets
- [[PrecisionRecallF1]] — evaluation metrics for classification
- [[Standardization]] — same preprocessing as linear regression

## Contradictions
- None identified.
