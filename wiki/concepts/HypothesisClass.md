---
title: "Hypothesis Class"
type: concept
tags: [learning-theory, modeling, foundational]
sources: [mml-ch08-when-models-meet-data, mml-book]
last_updated: 2026-06-04
---

# Hypothesis Class

The **set of functions the predictor is allowed to take** ([[mml-book]] §8.2.1, p. 259) — the first of the four design choices in [[EmpiricalRiskMinimization|empirical risk minimization]] (the question "what is the set of functions we allow the predictor to take?"). Usually a *parametrized class*: a family $f(\cdot,\boldsymbol\theta):\mathbb{R}^D\to\mathbb{R}$ indexed by parameters $\boldsymbol\theta$.

Given $N$ examples $\mathbf{x}_n\in\mathbb{R}^D$ with scalar labels $y_n\in\mathbb{R}$, learning seeks $\boldsymbol\theta^*$ such that $f(\mathbf{x}_n,\boldsymbol\theta^*)\approx y_n$ for all $n$ (Eq. 8.3), with prediction notation $\hat{y}_n=f(\mathbf{x}_n,\boldsymbol\theta^*)$.

## The canonical example: affine functions

[[mml-book]] Example 8.1 uses the **affine (= linear-in-the-parameters) class**. With the **bias-augmentation trick** — prepend a unit feature $x^{(0)}=1$ — the affine model $f(\mathbf{x}_n,\boldsymbol\theta)=\theta_0+\sum_{d=1}^D\theta_d x_n^{(d)}$ (Eq. 8.5) collapses to the linear predictor $f(\mathbf{x}_n,\boldsymbol\theta)=\boldsymbol\theta^\top\mathbf{x}_n$ (Eq. 8.4), $f:\mathbb{R}^{D+1}\to\mathbb{R}$. Richer (nonlinear) classes come from neural networks or from a [[FeatureMap|feature map]] $\phi(\cdot)$.

## Richness controls overfitting/underfitting

The richness of the hypothesis class is the central knob behind the [[Overfitting|overfitting]]/[[Underfitting|underfitting]] trichotomy (§8.3.3, [[ModelFitting]]):

- **Too rich** (e.g. 7th-order polynomials for linear data) → overfitting; uses its modeling power to fit noise.
- **Not rich enough** (straight lines for sinusoidal data) → underfitting; can't get close to the true model $M^*$.
- **About right** → fits well, generalizes.

Choosing among hypothesis classes (and their structural hyperparameters) is [[ModelSelection|model selection]] (§8.6).

## Connections

- [[mml-ch08-when-models-meet-data]] — §8.2.1 canonical reference.
- [[mml-book]] — §8.2.1.
- [[EmpiricalRiskMinimization]] — the hypothesis class is its first design choice.
- [[Predictor]] — an element of the hypothesis class.
- [[FeatureMap]] — how nonlinear classes are built while staying linear-in-the-parameters.
- [[ModelSelection]] — choosing among hypothesis classes.
- [[Overfitting]] / [[Underfitting]] — failure modes of too-rich / too-poor classes.
- [[VCDimension]] — a formal measure of hypothesis-class capacity.
