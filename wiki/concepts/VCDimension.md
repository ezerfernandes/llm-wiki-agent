---
title: "VC Dimension"
type: concept
tags: [learning-theory, generalization-bounds, foundational]
sources: [d2l-linear-classification]
last_updated: 2026-05-16
---

# VC Dimension

**Vapnik–Chervonenkis dimension** (1971): the largest set size that a binary-classifier hypothesis class can *shatter* — produce every possible labeling of. Foundational complexity measure for generalization bounds in binary classification; generalized to multi-class by [[NatarajanDimension]] (Natarajan 1989).

## Worked examples

- **Linear models** on $d$-dimensional inputs have VC dimension $d+1$. A line can produce every labeling of any 3 points in $\mathbb R^2$ (in general position), but no line can shatter 4 points (consider XOR).
- **Axis-aligned rectangles** in $\mathbb R^2$ have VC dimension 4.
- **$k$-th order polynomials** on $\mathbb R$ have VC dimension $k+1$.
- **Memorization machines** have VC dimension $\infty$ — they shatter any finite set but generalize abysmally.

## Generalization bound

Per [[d2l-linear-classification]]:

$$
P\big(R[p, f] - R_{\mathrm{emp}}[\mathbf X,\mathbf Y, f] < \alpha\big) \geq 1 - \delta \quad\text{for}\quad \alpha \geq c\sqrt{\tfrac{\mathrm{VC} - \log\delta}{n}}.
$$

Plug in desired $(\delta, \alpha)$ to determine how many samples to collect for a given confidence-and-precision target. The $\mathcal O(1/\sqrt n)$ rate matches the central-limit-theorem decay for the test-error estimate of a *fixed* classifier — the VC bound is the multi-classifier (uniform-convergence) generalization.

## Why it fails to explain deep learning

[[d2l-linear-classification]] is candid: VC-based bounds are "powerless (as straightforwardly applied) for explaining why deep neural networks generalize. Deep neural networks often have millions of parameters (or more), and can easily assign random labels to large collections of points. Nevertheless, they generalize well on practical problems and, surprisingly, they often generalize better, when they are larger and deeper, despite incurring higher VC dimensions." This is the central puzzle the wiki's [[DoubleDescent|double-descent]] / overparameterization material addresses.

## Connections

- [[UniformConvergence]] — VC-based bounds are the canonical uniform-convergence result.
- [[HoeffdingsInequality]] — the per-classifier concentration; VC adds the union-bound-over-class layer.
- [[Generalization]] / [[GeneralizationGap]] — what the VC bound controls (in classical regimes).
- [[NatarajanDimension]] — multi-class generalization.
- [[EmpiricalRiskMinimization]] — the procedure whose convergence to risk minimization VC dimension provides bounds for.
- [[d2l-linear-classification]] — corpus anchor (Section *Statistical Learning Theory*).
- [[2605.12966-agentic-ai-to-agi]]
