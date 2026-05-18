---
title: "Made With ML — Linear Regression"
type: source
tags: [foundations, made-with-ml, machine-learning, regression]
date: 2026-05-15
source_file: raw/madewithml/foundations-linear-regression.md
---

## Summary
Foundations lesson implementing linear regression from scratch in NumPy and then in PyTorch. Walks through the full supervised-learning loop — generate data, split, standardize, initialize weights, forward pass, MSE loss, gradient computation, weight updates with a learning rate, training over epochs, evaluation, inference, interpretability, and L2 regularization — building the mental model that every later deep-learning lesson reuses.

## Key Claims
- The linear model is `y_hat = XW + b`; the goal is to learn `W` and `b` that minimize MSE on training data.
- Data should be split into train / val / test (e.g. 70 / 15 / 15) and standardized using statistics computed only on the training set to avoid leakage.
- Inputs `X` and outputs `y` should not be shuffled independently — they must be permuted in lockstep so rows still match.
- Mean squared error `J = (1/N) Σ (y − y_hat)^2` is a standard objective for continuous regression; its gradients w.r.t. `W` and `b` have clean closed-forms used in vanilla backprop.
- Weight updates use a small learning rate `α`; values typically explored in `[1e-8, 1e-1]`. Too small means slow convergence, too large means overshoot and divergence.
- The same five-step loop — forward, loss, backward (gradients), update, repeat — is the template used by every subsequent model in the course.
- PyTorch reproduces the NumPy implementation via [[PyTorch]]'s `nn.Linear`, `nn.MSELoss`, and the [[Adam]] optimizer, which is described as the standard default for most cases.
- Linear regression is highly interpretable: each coefficient `W_j` directly quantifies how much `y` changes per unit change in `x_j` (after un-scaling).
- L2 regularization (ridge) penalizes large weights via `λ W^T W`; in PyTorch this is exposed as the `weight_decay` argument on the optimizer. L1 (lasso) drives sparsity; elastic net mixes both.

## Key Quotes
> "Use inputs X to predict the output y_hat using a linear model. The model will be a line of best fit that minimizes the distance between the predicted (model's output) and target (ground truth) values." — Overview

> "Be careful not to shuffle X and y separately because then the inputs won't correspond to the outputs!" — Split data warning

> "The ADAM optimizer has become a standard algorithm for most cases." — Optimizer section

> "Regularization is not just for linear regression. You can use it to regularize any model's weights including the ones we will look at in future lessons."

## Connections
- [[MadeWithML]] — course this lesson belongs to
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher
- [[PyTorch]] — framework used for the second implementation
- [[NumPy]] — used for the from-scratch implementation
- [[scikit-learn]] — provides `train_test_split` and `StandardScaler`
- [[LinearRegression]] — the model class introduced here
- [[MeanSquaredError]] — loss function for regression
- [[GradientDescent]] — optimization procedure derived by hand
- [[Backpropagation]] — gradient computation and weight update step
- [[LearningRate]] — scalar controlling update step size
- [[Adam]] — PyTorch optimizer used in the second pass
- [[Regularization]] — L2 / ridge, L1 / lasso, elastic net
- [[Overfitting]] — motivation for regularization
- [[Standardization]] — preprocessing step before training
- [[TrainValTestSplit]] — data partitioning discipline
- [[Interpretability]] — linear coefficients as feature importance

## Contradictions
- None identified against existing wiki content.
