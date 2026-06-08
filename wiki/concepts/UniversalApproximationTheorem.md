---
title: "Universal Approximation Theorem"
type: concept
tags: [theory, neural-networks, foundational]
sources: [d2l-multilayer-perceptrons, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Universal Approximation Theorem

The result that a feedforward [[NeuralNetwork]] with a *single* [[HiddenLayer|hidden layer]] of finite (but possibly very large) width, and a suitable [[ActivationFunction|activation function]] (sigmoidal in the original setting; more broadly any non-polynomial bounded activation), can approximate any continuous function on a compact subset of $\mathbb{R}^n$ to arbitrary accuracy. Established for sigmoidal nets by [[GeorgeCybenko|Cybenko (1989)]] and for [[RBFNetwork|RBF / kernel]] networks by Micchelli (1984), with subsequent generalizations to broader activation classes.

## What it does *not* say

[[d2l-multilayer-perceptrons]] §Universal Approximators:

> "Just because a single-hidden-layer network *can* learn any function does not mean that you should try to solve all of your problems with one."

- **No bound on width.** "Possibly absurdly many" units may be required.
- **No algorithmic guarantee.** Finding the right weights is the [[Optimization|optimization]] problem; existence is not learnability.
- **No sample-complexity bound.** Generalizing from finite data is a separate problem.

## Why depth still matters

Deeper networks can represent some function classes *exponentially more compactly* than shallow ones — formalized for ReLU networks by Telgarsky, Eldan & Shamir, and others. The empirical D2L take: deeper-rather-than-wider is the practical choice (Simonyan & Zisserman 2014; VGG).

## Analogy from D2L

> "You might think of your neural network as being a bit like the C programming language. The language … is capable of expressing any computable program. But actually coming up with a program that meets your specifications is the hard part."

## Connections

- [[d2l-multilayer-perceptrons]] — §Universal Approximators.
- [[MultilayerPerceptron]] / [[NeuralNetwork]] — the model class the theorem speaks about.
- [[HiddenLayer]] — what "single layer of arbitrary width" refers to.
- [[ActivationFunction]] — non-polynomial activation is the technical prerequisite.
- [[KernelMethods]] / [[RBFNetwork]] — alternative universal-approximator family (Micchelli).
- [[NeuralTangentKernel]] — infinite-width limit makes the kernel analogy precise.
- [[GeorgeCybenko]] — the 1989 author (entity / stub).
- [[Compositionality]] / [[mlsysbook-ch05-neural-computation]] — Ch 5 stresses the theorem is *non-constructive* and that the single-hidden-layer width can grow exponentially; depth trades this exponential width for polynomial depth, achieving the same approximation with exponentially fewer parameters — *why* deep beats wide.
