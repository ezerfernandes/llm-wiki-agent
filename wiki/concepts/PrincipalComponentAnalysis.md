---
title: "Principal Component Analysis"
type: concept
tags: [dimensionality-reduction, statistics, foundational]
sources: [madewithml-preprocessing, islr-seventh-printing, mml-book, parproc-ch14-statistics-data-mining]
last_updated: 2026-05-17
---

# Principal Component Analysis

An unsupervised linear technique that decomposes data into orthogonal components ordered by explained variance. The canonical baseline for dimensionality reduction; see [[PCA]] for the acronym and [[CurseOfDimensionality]] for motivation. Used as the regression preprocessor in [[PrincipalComponentsRegression|PCR]] ([[islr-seventh-printing|ISLR]] §6.3.1) and as an exploratory tool in §10.2 (NCI60 gene-expression demo).

## The four equivalent derivations ([[mml-book]] Ch 10)

[[mml-book]] develops PCA from first principles, exhibiting **four equivalent characterizations** of the same algorithm:

1. **Maximum variance** (§10.2): find a direction $\mathbf{b}_1$ that maximizes the variance of projected data. [[LagrangeMultipliers]] yield $\mathbf{S}\mathbf{b}_1 = \lambda_1\mathbf{b}_1$ — eigenvector of the [[DataCovarianceMatrix]] $\mathbf{S}$.
2. **Minimum reconstruction error** (§10.3): minimize $\|\mathbf{x}_n - \mathbf{B}\mathbf{B}^\top\mathbf{x}_n\|^2$ over orthonormal $\mathbf{B}\in\mathbb{R}^{D\times M}$. Same eigenvalue problem.
3. **Karhunen-Loève transform** (§10.1, signal processing perspective): same algorithm under a different name.
4. **Latent-variable / probabilistic PCA** (§10.7): assume $\mathbf{x} = \mathbf{B}\mathbf{z} + \boldsymbol\mu + \boldsymbol\epsilon$ with $\mathbf{z}\sim\mathcal{N}(\mathbf{0},\mathbf{I})$, $\boldsymbol\epsilon\sim\mathcal{N}(\mathbf{0},\sigma^2\mathbf{I})$. MLE for $\mathbf{B}$ recovers (truncated to leading eigenvectors of $\mathbf{S}$) the same answer.

The **variance retained** by the top-$M$ projection is exactly $\sum_{m=1}^M\lambda_m/\sum_{d=1}^D\lambda_d$ (Eq. 10.23) — the standard scree-plot quantity.

## Parallel PCA ([[parproc-ch14-statistics-data-mining]] §14.4)

PCA finds r < p variables consisting of linear combinations of the original p variables that carry most of the information of the full set — **dimension reduction**. These r variables are the eigenvectors corresponding to the r largest eigenvalues of the p×p covariance matrix. Because PCA reduces to a matrix eigenvector problem, it is parallelized via the parallel eigenvector algorithms in [[parproc-ch11-parallel-matrix-operations]] §11.6.

## Connections

- [[mml-book]] — Ch 10 canonical reference.
- [[PCA]] — acronym disambiguation.
- [[DataCovarianceMatrix]] — the object PCA diagonalizes.
- [[Eigendecomposition]] — algebraic engine.
- [[SingularValueDecomposition]] — equivalent route via centered $\mathbf{X}$ directly.
- [[OrthogonalProjection]] — geometric interpretation of $\mathbf{B}\mathbf{B}^\top$.
- [[CurseOfDimensionality]] — motivation.
- [[KarhunenLoeveTransform]] — alternative name in signal processing.
- [[islr-seventh-printing]] — Ch 10 ISLR treatment.
- [[parproc-ch14-statistics-data-mining]] — §14.4 parallel PCA via Ch11 eigenvector methods.
- [[parproc-ch11-parallel-matrix-operations]] — §11.6 parallel eigenvector algorithms used by parallel PCA.
