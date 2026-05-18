---
title: "Norm"
type: concept
tags: [analytic-geometry, foundational]
sources: [mml-book, d2l-preliminaries, d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Norm

A function $\|\cdot\|:V\to\mathbb{R}$ on a vector space $V$ that assigns each vector $\mathbf{x}$ a *length*, satisfying ([[mml-book]] Def. 3.1):

1. **Absolutely homogeneous**: $\|\lambda\mathbf{x}\| = |\lambda|\,\|\mathbf{x}\|$.
2. **Triangle inequality**: $\|\mathbf{x}+\mathbf{y}\|\leq\|\mathbf{x}\|+\|\mathbf{y}\|$.
3. **Positive definite**: $\|\mathbf{x}\|\geq 0$ and $\|\mathbf{x}\|=0\iff\mathbf{x}=\mathbf{0}$.

## Standard examples

| Norm | Definition | Used in |
|---|---|---|
| **Manhattan / $\ell_1$** | $\|\mathbf{x}\|_1 = \sum_i |x_i|$ | Lasso, sparsity-inducing regularization |
| **Euclidean / $\ell_2$** | $\|\mathbf{x}\|_2 = \sqrt{\sum_i x_i^2} = \sqrt{\mathbf{x}^\top\mathbf{x}}$ | Default for [[mml-book]]; ridge regression; SVM margin |
| **Maximum / $\ell_\infty$** | $\|\mathbf{x}\|_\infty = \max_i |x_i|$ | Robustness / adversarial-perturbation bounds |
| **Frobenius** (matrices) | $\|\mathbf{A}\|_F = \sqrt{\text{tr}(\mathbf{A}^\top\mathbf{A})}$ | Low-rank approximation; Eckart-Young |

## Relation to inner products

Every [[InnerProduct]] induces a norm via $\|\mathbf{x}\| := \sqrt{\langle\mathbf{x},\mathbf{x}\rangle}$ (Eq. 3.16, [[mml-book]] §3.3). But not every norm comes from an inner product — the Manhattan / $\ell_1$ norm is the standard counter-example.

A norm comes from an inner product iff it satisfies the **parallelogram law** $\|\mathbf{x}+\mathbf{y}\|^2 + \|\mathbf{x}-\mathbf{y}\|^2 = 2(\|\mathbf{x}\|^2 + \|\mathbf{y}\|^2)$.

## ML uses

- **Regularization** in regression: $\ell_2$ → ridge / weight decay; $\ell_1$ → Lasso / sparsity.
- **Distance metrics** for nearest-neighbor methods.
- **Gradient clipping**: rescale gradients whose $\ell_2$ norm exceeds a threshold (RNN training).
- **Adversarial robustness**: $\ell_\infty$-ball or $\ell_2$-ball perturbations are the standard threat models.

## Connections

- [[mml-book]] — §3.1 canonical reference.
- [[InnerProduct]] — induces norms.
- [[absolute-value]] — algebrica.org page; the 1-D special case.
- [[CauchySchwarzInequality]] — links norms and inner products.
