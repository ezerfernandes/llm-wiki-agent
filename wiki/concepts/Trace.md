---
title: "Trace"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-book, mml-ch04-matrix-decompositions]
last_updated: 2026-06-04
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

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

The full §4.1 treatment (book pp. 103–104). Definition 4.4: $\operatorname{tr}(\mathbf{A}):=\sum_{i=1}^n a_{ii}$ (Eq. 4.18). The four characterizing properties (only the trace satisfies all four — Gohberg et al. 2012): linearity in $+$ and scalar; $\operatorname{tr}(\mathbf{I}_n)=n$; and $\operatorname{tr}(\mathbf{A}\mathbf{B})=\operatorname{tr}(\mathbf{B}\mathbf{A})$. The general **cyclic invariance** $\operatorname{tr}(\mathbf{A}\mathbf{K}\mathbf{L})=\operatorname{tr}(\mathbf{K}\mathbf{L}\mathbf{A})$ (Eq. 4.19, marginal "The trace is invariant under cyclic permutations") generalizes to any number of factors; special case $\operatorname{tr}(\mathbf{x}\mathbf{y}^\top)=\mathbf{y}^\top\mathbf{x}$ (Eq. 4.20). Basis-invariance of the trace of a *mapping* follows: $\operatorname{tr}(\mathbf{S}^{-1}\mathbf{A}\mathbf{S})=\operatorname{tr}(\mathbf{A})$ (Eq. 4.21, a [[SimilarityTransform|similarity transform]]). **Theorem 4.17**: $\operatorname{tr}(\mathbf{A})=\sum_{i=1}^n\lambda_i$, the *sum* of eigenvalues (geometrically the perimeter-scaling of the unit square, Fig. 4.6); it is the coefficient $c_{n-1}=(-1)^{n-1}\operatorname{tr}(\mathbf{A})$ of the [[CharacteristicPolynomial]] (Eq. 4.24).

## Connections

- [[mml-book]] — §4.1 canonical reference.
- [[mml-ch04-matrix-decompositions|MML Ch 4]] — full §4.1 deep dive.
- [[Determinant]] — companion (product vs sum of eigenvalues).
- [[CharacteristicPolynomial]] — both determinant and trace appear as coefficients.
- [[SimilarityTransform]] — basis-invariance of the trace.
