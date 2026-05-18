---
title: "Made With ML — Neural Networks"
type: source
tags: [foundations, made-with-ml, deep-learning, neural-networks]
date: 2026-05-15
source_file: raw/madewithml/foundations-neural-networks.md
---

## Summary
Foundations lesson introducing multilayer perceptrons (MLPs) as the bridge from linear classifiers to deep learning. Motivates non-linear activations by first failing to fit a non-linear spiral dataset with a plain linear model, then adding a hidden layer with a non-linearity to recover. Implements forward and backward pass in NumPy, then in PyTorch, and ends with weight initialization, dropout, and an explicit demonstration of overfitting versus a properly regularized model.

## Key Claims
- A neural net is the same generalized-linear template as logistic regression, but with one or more hidden layers and a non-linear activation `f` between them: `a1 = f(XW1)`, `y_hat = softmax(a1 W2)`.
- Without a non-linear activation, stacking linear layers collapses to a single equivalent linear layer — depth only helps when paired with non-linearity.
- Common activation functions covered: sigmoid, tanh, and [[ReLU]]; ReLU is preferred because it avoids the vanishing-gradient saturation of sigmoid/tanh.
- Backpropagation is just the chain rule applied through the computation graph; PyTorch's autograd computes it automatically once the forward graph is built.
- Proper weight initialization matters: random uniform / Xavier / He initialization keep activation variance stable across layers and prevent dead or saturating units.
- [[Dropout]] randomly zeros activations during training (e.g. p = 0.1–0.5) to regularize the network; it is disabled at evaluation time via `model.eval()`.
- The same training loop introduced in linear regression — forward, loss, backward, step — generalizes unchanged to deep networks.
- The MLP is positioned as a modular feed-forward unit reused inside every later architecture (CNN heads, RNN heads, transformer FFN sub-layers).

## Key Quotes
> "Neural networks are just extensions of the generalized linear methods we've seen so far but with non-linear activation functions since our data will be highly non-linear." — Overview

> "Future neural network architectures that we'll see use the MLP as a modular unit for feed forward operations (affine transformation (XW) followed by a non-linear operation)." — Miscellaneous

> "Overfits easily. Computationally intensive as network increases in size. Not easily interpretable." — Disadvantages

## Connections
- [[MadeWithML]] — course this lesson belongs to
- [[GokuMohandas]] — author
- [[PyTorch]] — framework
- [[NumPy]] — from-scratch implementation
- [[NeuralNetwork]] — the model family introduced here
- [[MultilayerPerceptron]] — the specific architecture
- [[ActivationFunction]] — sigmoid, tanh, ReLU
- [[ReLU]] — preferred activation
- [[Softmax]] — output layer for classification
- [[Backpropagation]] — gradient computation through the chain rule
- [[WeightInitialization]] — Xavier / He
- [[Dropout]] — regularization technique
- [[Overfitting]] — demonstrated explicitly
- [[LogisticRegression]] — special case (no hidden layer)
- [[GradientDescent]] — optimization
- [[Adam]] — optimizer used in PyTorch version

## Contradictions
- None identified.
