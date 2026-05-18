---
title: "Trace"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Trace

For $\mathbf{A}\in\mathbb{R}^{n\times n}$, the *trace* is the sum of diagonal entries: $\text{tr}(\mathbf{A}) := \sum_{i=1}^n a_{ii}$ ([[mml-book]] Def. 4.4).

Properties (§4.1):

- **Linear**: $\text{tr}(\mathbf{A}+\mathbf{B}) = \text{tr}(\mathbf{A})+\text{tr}(\mathbf{B})$; $\text{tr}(\alpha\mathbf{A})=\alpha\,\text{tr}(\mathbf{A})$.
- **Identity**: $\text{tr}(\mathbf{I}_n)=n$.
- **Cyclic invariance**: $\text{tr}(\mathbf{A}\mathbf{B}) = \text{tr}(\mathbf{B}\mathbf{A})$, and more generally $\text{tr}(\mathbf{A}\mathbf{K}\mathbf{L}) = \text{tr}(\mathbf{K}\mathbf{L}\mathbf{A})$.
- **Basis invariance** (from cyclic): $\text{tr}(\mathbf{S}^{-1}\mathbf{A}\mathbf{S}) = \text{tr}(\mathbf{A})$ — the trace of a linear mapping is independent of the chosen basis.

The trace is uniquely characterized by the first three properties (Gohberg et al. 2012).

## Eigenvalue identity

$\text{tr}(\mathbf{A}) = \sum_{i=1}^n \lambda_i$ — the trace is the *sum* of eigenvalues, just as the determinant is the *product*. Together they fix the first two coefficients of the [[CharacteristicPolynomial]].

## ML uses

- **Frobenius norm**: $\|\mathbf{A}\|_F^2 = \text{tr}(\mathbf{A}^\top\mathbf{A})$ — most loss functions that "compare matrices" reduce to a trace.
- **Squared error in matrix form**: $\|\mathbf{y}-\mathbf{X}\boldsymbol\theta\|^2 = \text{tr}((\mathbf{y}-\mathbf{X}\boldsymbol\theta)(\mathbf{y}-\mathbf{X}\boldsymbol\theta)^\top)$ — the standard rewriting in regression derivations.
- **Mahalanobis distance** in trace form via $(\mathbf{x}-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu) = \text{tr}(\boldsymbol\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu)(\mathbf{x}-\boldsymbol\mu)^\top)$.

## Connections

- [[mml-book]] — §4.1 canonical reference.
- [[Determinant]] — companion (product vs sum of eigenvalues).
- [[CharacteristicPolynomial]] — both determinant and trace appear as coefficients.
