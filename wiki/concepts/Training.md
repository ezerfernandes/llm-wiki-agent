---
title: "Training"
type: concept
tags: [machine-learning, foundations, optimization, mml]
sources: [mml-ch01-introduction-and-motivation]
last_updated: 2026-06-04
---

# Training

**Training** is the *learning* component of machine learning: the procedure that **uses the available data to optimize the parameters of a model with respect to a utility function that evaluates how well the model predicts the training data** (*[[mml-book|Mathematics for Machine Learning]]*, §1.1, pp. 12–13). It is the second of the two senses of "machine learning algorithm" that Chapter 1 disambiguates — a system that *adapts some internal parameters of the [[Predictor|predictor]]* so it performs well on future unseen input data (§1.1, p. 12), as opposed to the predictor itself.

## The hill-climbing metaphor

MML frames training intuitively as *climbing a hill to reach its peak*: most training methods can be thought of as an approach analogous to hill-climbing, where **the peak corresponds to a maximum of some desired performance measure** (§1.1, pp. 12–13). Formally this means optimizing model [[Parameter|parameters]] $\boldsymbol{\theta}$ against a utility / performance function — the realm of [[ContinuousOptimization|continuous optimization]] (Ch 7), which in turn relies on the **gradient** machinery of [[VectorCalculus|vector calculus]] (Ch 5) to know "the direction in which to search for a solution" (§1.2, p. 15).

> Note: Ch 1 phrases this as *maximizing a utility function* (climbing to a peak), whereas later chapters and most of the literature phrase it as *minimizing a loss / cost* (e.g., [[EmpiricalRiskMinimization]], [[Generalization]]'s $R_\text{emp}$). These are the same idea up to a sign — maximizing utility is minimizing negative-loss.

## Training vs. generalization

A core warning of Chapter 1: performing well on **training data** may only mean the model found a good way to *memorize* the data, which need not [[Generalization|generalize]] to unseen data (§1.1, p. 13). In practice we are interested in the model performing well on data *not used for training* — so we often need to expose the system to situations it has not encountered before. The honest evaluation set-ups that guard against overly optimistic estimates are deferred to Chapter 8.

## Where it sits in the book's program

The book's three-bullet summary (§1.1, p. 13) places training as the third step: (1) represent data as vectors; (2) choose a model (probabilistic or optimization view); (3) **learn from available data using numerical optimization methods**, aiming for good performance on held-out data. The mathematical restatement of training as *parameter estimation* comes in Chapter 8.

## Connections

- [[mml-ch01-introduction-and-motivation]] — where training is defined and the hill-climbing metaphor introduced.
- [[Predictor]] — the artifact training produces; the *other* sense of "ML algorithm."
- [[MachineLearning]] — training is the *learning* component of the data / model / learning trichotomy.
- [[ContinuousOptimization]] — training is parameter optimization against a utility function (Ch 7).
- [[VectorCalculus]] — gradients give the search direction during training (Ch 5).
- [[Parameter]] — the internal model parameters that training adapts.
- [[Generalization]] — the goal of training is unseen-data performance, not training-set memorization.
- [[MaximumLikelihoodEstimation]] / [[BayesianLinearRegression]] — concrete training schemes (estimate parameters vs. integrate them out) developed in Ch 9.
- [[EmpiricalRiskMinimization]] — the loss-minimization framing of training (Ch 8).
