---
title: "Cholesky Decomposition"
type: concept
tags: [linear-algebra, matrix-decomposition, numerical-linear-algebra]
sources: [mml-book, mml-ch04-matrix-decompositions]
last_updated: 2026-06-04
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

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

**Theorem 4.18** (§4.3, Eq. 4.44): a symmetric positive definite $\mathbf{A}$ factorizes uniquely into $\mathbf{A}=\mathbf{L}\mathbf{L}^\top$ with $\mathbf{L}$ lower-triangular and **positive on the diagonal** (the *Cholesky factor*). It is the matrix analogue of the square-root operation on positive reals (motivated by $9=3\cdot3$, p. 114).

- **Backward construction** (Example 4.10, Eqs. 4.47–4.48): the entries are computed entry-by-entry from $\mathbf{A}$ and previously computed $l$'s — diagonal $l_{11}=\sqrt{a_{11}}$, $l_{22}=\sqrt{a_{22}-l_{21}^2}$, $l_{33}=\sqrt{a_{33}-(l_{31}^2+l_{32}^2)}$; below-diagonal $l_{21}=a_{21}/l_{11}$, $l_{31}=a_{31}/l_{11}$, $l_{32}=(a_{32}-l_{31}l_{21})/l_{22}$.
- **Efficient determinant**: $\det(\mathbf{A})=\det(\mathbf{L})^2=\prod_i l_{ii}^2$.
- **ML role** (§4.3, §4.8): SPD covariance matrices (multivariate Gaussian, §6.5) need frequent manipulation; the Cholesky factor enables Gaussian sampling and the **reparametrization trick** for differentiable random variables (variational autoencoders — Jimenez Rezende et al. 2014; Kingma & Welling 2014).
- In the [[MatrixPhylogeny|matrix phylogeny]] (§4.7), Cholesky is the operation attached to the *positive definite* branch of symmetric matrices (eigenvalues $>0$, always invertible).

## Connections

- [[mml-book]] — §4.3 canonical reference.
- [[mml-ch04-matrix-decompositions|MML Ch 4]] — full §4.3 deep dive (Thm 4.18).
- [[MatrixPhylogeny]] — the positive-definite branch; [[SpectralTheorem]] — companion result for symmetric matrices.
- [[SymmetricPositiveDefiniteMatrix]] — the input class.
- [[MatrixDecomposition]] — broader taxonomy.
- [[GaussianDistribution]] — primary sampling application.
- [[InnerProduct]] — what SPD matrices encode.
