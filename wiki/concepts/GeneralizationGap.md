---
title: "Generalization Gap"
type: concept
tags: [foundational, learning-theory, overfitting]
sources: [pml1-murphy, d2l-linear-regression, d2l-linear-classification, d2l-multilayer-perceptrons]
last_updated: 2026-05-16
---

# Generalization Gap

The difference between **population risk** (expected loss on the true data distribution) and **empirical risk** (average loss on the training sample):

$$
\text{Gap} = \mathcal{L}(\boldsymbol\theta; p^*) - \mathcal{L}(\boldsymbol\theta; \mathcal{D}_{\text{train}})
$$

A large gap is the diagnostic signature of **overfitting**: the model has driven empirical loss low (often to zero) by memorizing the training set, but the true loss is high because it failed to capture the underlying distribution. [[pml1-murphy]] §1.2.3.

## How to estimate it

We don't know $p^*$, so we partition data into train and test sets and approximate $\mathcal{L}(\boldsymbol\theta; p^*)$ by $\mathcal{L}(\boldsymbol\theta; \mathcal{D}_{\text{test}})$. Model selection introduces a *third* set — the validation set — so that the test set remains an unbiased estimate of population risk (§1.2.3, §4.5.4).

## The U-shape

Plotting train error vs model complexity on one axis and test error on the other produces the characteristic U: low-complexity models underfit (high train and test loss), high-complexity models overfit (~0 train loss, high test loss), and the "just right" complexity is the minimum-test-loss point (Murphy Fig. 1.7d).

## Modern caveat: double descent

Murphy's introductory U-curve is the classical picture. In overparameterized regimes (notably modern DNNs and LLMs) the curve exhibits **double descent**: test loss falls, rises (classical regime), then falls again past the interpolation threshold. The book treats this in later chapters; the 2020s LLM scaleup operates on the second descent.

## Role in this wiki

- The classical-vs-modern generalization story is what [[2001.08361-scaling-laws]] empirically resolves — the power-law fit *is* a description of how the gap shrinks at scale.
- The [[AverageTrap]] in [[2605.12966-agentic-ai-to-agi]] is *not* a generalization-gap argument per se: it's a *bias* argument about what minimum can be reached, not what gap to that minimum remains.
- Corpus III ([[imlbook-evaluation]]) treats evaluation methodology that bears on gap estimation; Murphy's training/validation/test scaffolding is the prerequisite.

## Connections

- [[pml1-murphy]] — §1.2.3.
- [[d2l-multilayer-perceptrons]] — establishes the over-parametrized / [[InterpolationRegime|interpolation]] view: when training error is ~0 for all models considered, *the gap is the only axis left*.
- [[DoubleDescent]] — the curve that crystallizes the modern caveat.
- [[InterpolationRegime]] / [[NeuralTangentKernel]] — frame for understanding the gap in deep networks.
- [[EmpiricalRiskMinimization]] — what is minimized in training; gap is what's left.
- [[NoFreeLunchTheorem]] — bounds on how small the gap can be without prior assumptions.
- [[ScalingLaws]] — empirical gap-shrinking with $N$, $D$, $C$.
