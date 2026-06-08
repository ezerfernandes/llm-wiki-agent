---
title: "Covariance Matrix"
type: concept
tags: [probability, statistics, linear-algebra, foundational]
sources: [mml-ch06-probability-and-distributions, mml-book]
last_updated: 2026-06-04
---

# Covariance Matrix

The **covariance matrix** of a multivariate [[RandomVariable]] $X$ with states $\mathbf x\in\mathbb{R}^D$ and mean $\boldsymbol\mu$ is the matrix form of the [[Variance|variance]] $\mathbb{V}_X[\mathbf x]=\mathrm{Cov}_X[\mathbf x,\mathbf x]$ ([[mml-book]] §6.4.1, Def. 6.7, Eq. 6.38):

$$\boldsymbol\Sigma=\mathbb{V}_X[\mathbf x]=\mathbb{E}_X[(\mathbf x-\boldsymbol\mu)(\mathbf x-\boldsymbol\mu)^\top]=\mathbb{E}_X[\mathbf x\mathbf x^\top]-\mathbb{E}_X[\mathbf x]\mathbb{E}_X[\mathbf x]^\top=\begin{bmatrix}\mathrm{Cov}[x_1,x_1]&\cdots&\mathrm{Cov}[x_1,x_D]\\\vdots&\ddots&\vdots\\\mathrm{Cov}[x_D,x_1]&\cdots&\mathrm{Cov}[x_D,x_D]\end{bmatrix}.$$

## Structure

- **Diagonal** $\mathrm{Cov}[x_i,x_i]$ = the **marginal variances** of each coordinate.
- **Off-diagonal** $\mathrm{Cov}[x_i,x_j]$, $i\ne j$ = the **cross-covariances** ([[mml-book]] Eq. 6.39).
- **Symmetric** and **positive semidefinite**; it "tells us something about the spread of the data" ([[mml-book]] p. 190). The book generally **assumes positive definiteness** to "enable better intuition," sidestepping low-rank corner cases (§6.4.1 Remark, p. 191).

## Why it's the central object of probabilistic ML

- Together with the mean $\boldsymbol\mu$, the covariance matrix $\boldsymbol\Sigma$ **fully specifies a [[GaussianDistribution|multivariate Gaussian]]** $\mathcal{N}(\boldsymbol\mu,\boldsymbol\Sigma)$ (§6.5).
- Under an affine transform $\mathbf y=\mathbf A\mathbf x+\mathbf b$: $\boldsymbol\Sigma_Y=\mathbf A\boldsymbol\Sigma\mathbf A^\top$ (Eq. 6.51) — the rule behind Gaussian sampling via [[CholeskyDecomposition|Cholesky]] ($\boldsymbol\Sigma=\mathbf A\mathbf A^\top$, §6.5.4) and behind change-of-variables (Example 6.17 recovers $\boldsymbol\Sigma=\mathbf A\mathbf A^\top$).
- The **[[DataCovarianceMatrix|empirical covariance matrix]]** $\boldsymbol\Sigma=\frac1N\sum_n(\mathbf x_n-\bar{\mathbf x})(\mathbf x_n-\bar{\mathbf x})^\top$ (Eq. 6.42) is the data estimate driving [[PrincipalComponentAnalysis|PCA]].

## Correlation matrix

Standardizing each coordinate by its standard deviation ($x_i/\sigma(x_i)$) turns the covariance matrix into the **correlation matrix** ([[mml-book]] p. 191) — see [[Correlation]].

## Connections

- [[mml-ch06-probability-and-distributions]] — §6.4.1 deep dive.
- [[mml-book]] — §6.4.1 canonical reference.
- [[Variance]] — the covariance matrix is the multivariate variance.
- [[Covariance]] — its entries.
- [[Correlation]] — its standardized version.
- [[DataCovarianceMatrix]] — the empirical / sample version (PCA).
- [[GaussianDistribution]] — parameterized by $\boldsymbol\mu$ and $\boldsymbol\Sigma$.
- [[SymmetricPositiveDefiniteMatrix]] — the class $\boldsymbol\Sigma$ belongs to.
- [[CholeskyDecomposition]] — factorization for sampling.
