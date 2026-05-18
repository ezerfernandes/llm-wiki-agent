---
title: "Cholesky Decomposition"
type: concept
tags: [linear-algebra, matrix-decomposition, numerical-linear-algebra]
sources: [mml-book]
last_updated: 2026-05-16
---

# Cholesky Decomposition

For a **symmetric positive-definite** matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$, the Cholesky decomposition is the unique factorization

$$\mathbf{A} = \mathbf{L}\,\mathbf{L}^\top$$

with $\mathbf{L}$ lower-triangular and positive on the diagonal ([[mml-book]] §4.3). Often described as the "square root" of a matrix.

## Why it matters for ML

- **Sampling from a multivariate Gaussian** $\mathcal{N}(\boldsymbol\mu, \boldsymbol\Sigma)$: compute $\mathbf{L}$ such that $\boldsymbol\Sigma = \mathbf{L}\mathbf{L}^\top$, draw $\mathbf{z}\sim\mathcal{N}(\mathbf{0}, \mathbf{I})$, return $\boldsymbol\mu + \mathbf{L}\mathbf{z}$. This is how every modern probabilistic library (NumPyro, Stan, etc.) samples correlated Gaussians.
- **Solving $\mathbf{A}\mathbf{x}=\mathbf{b}$ when $\mathbf{A}$ is SPD**: forward-substitute on $\mathbf{L}\mathbf{y}=\mathbf{b}$, back-substitute on $\mathbf{L}^\top\mathbf{x}=\mathbf{y}$ — roughly **twice as fast** as generic LU.
- **Determinant computation**: $\det(\mathbf{A}) = \left(\prod L_{ii}\right)^2$ — numerically stable.
- **[[GaussianProcess]] kernel matrices** are SPD; their Cholesky factor underlies GP predictive-mean and predictive-variance computations.

## Why SPD matrices are the right object

Inner products on finite-dimensional real vector spaces are *exactly* the symmetric positive-definite matrices in disguise ([[mml-book]] Thm 3.5). So Cholesky is the factorization that respects inner-product structure — it's the linear-algebra analogue of "taking square roots of positive reals."

## Connections

- [[mml-book]] — §4.3 canonical reference.
- [[SymmetricPositiveDefiniteMatrix]] — the input class.
- [[MatrixDecomposition]] — broader taxonomy.
- [[GaussianDistribution]] — primary sampling application.
- [[InnerProduct]] — what SPD matrices encode.
