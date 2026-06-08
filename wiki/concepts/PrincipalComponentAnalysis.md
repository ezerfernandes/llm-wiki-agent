---
title: "Principal Component Analysis"
type: concept
tags: [dimensionality-reduction, statistics, foundational]
sources: [madewithml-preprocessing, islr-seventh-printing, mml-book, mml-ch10-dimensionality-reduction-pca, parproc-ch14-statistics-data-mining]
last_updated: 2026-06-05
---

# Principal Component Analysis

An unsupervised linear technique that decomposes data into orthogonal components ordered by explained variance. The canonical baseline for dimensionality reduction; see [[PCA]] for the acronym and [[CurseOfDimensionality]] for motivation. Used as the regression preprocessor in [[PrincipalComponentsRegression|PCR]] ([[islr-seventh-printing|ISLR]] §6.3.1) and as an exploratory tool in §10.2 (NCI60 gene-expression demo).

## The four equivalent derivations ([[mml-ch10-dimensionality-reduction-pca|MML Ch 10]])

[[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] develops PCA from first principles, exhibiting **four equivalent characterizations** of the same algorithm (the book itself counts *three derivations*; the KLT is an alias, not an independent derivation — see the [[mml-ch10-dimensionality-reduction-pca|deep dive]]'s note):

1. **Maximum variance** (§10.2): find a direction $\mathbf{b}_1$ that maximizes the variance of projected data. [[LagrangeMultipliers]] yield $\mathbf{S}\mathbf{b}_1 = \lambda_1\mathbf{b}_1$ — eigenvector of the [[DataCovarianceMatrix]] $\mathbf{S}$.
2. **Minimum reconstruction error** (§10.3): minimize $\|\mathbf{x}_n - \mathbf{B}\mathbf{B}^\top\mathbf{x}_n\|^2$ over orthonormal $\mathbf{B}\in\mathbb{R}^{D\times M}$. Same eigenvalue problem.
3. **Karhunen-Loève transform** (§10.1, signal processing perspective): same algorithm under a different name.
4. **Latent-variable / probabilistic PCA** (§10.7): assume $\mathbf{x} = \mathbf{B}\mathbf{z} + \boldsymbol\mu + \boldsymbol\epsilon$ with $\mathbf{z}\sim\mathcal{N}(\mathbf{0},\mathbf{I})$, $\boldsymbol\epsilon\sim\mathcal{N}(\mathbf{0},\sigma^2\mathbf{I})$. MLE for $\mathbf{B}$ recovers (truncated to leading eigenvectors of $\mathbf{S}$) the same answer.

The **variance retained** by the top-$M$ projection is exactly $\sum_{m=1}^M\lambda_m/\sum_{d=1}^D\lambda_d$ (Eq. 10.23) — the standard scree-plot quantity.

## From [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] (full deep dive)

Ch 10 is the **second of the four ML pillars** (dimensionality reduction). PCA is set up as a linear **coder/decoder** ([[Autoencoder|auto-encoder]]): encoder $\mathbf z_n=\mathbf B^\top\mathbf x_n\in\mathbb R^M$, decoder $\tilde{\mathbf x}_n=\mathbf B\mathbf z_n=\mathbf B\mathbf B^\top\mathbf x_n$, with orthonormal $\mathbf B=[\mathbf b_1,\dots,\mathbf b_M]\in\mathbb R^{D\times M}$ spanning the [[PrincipalSubspace|principal subspace]] (§10.1, Eqs. 10.1–10.3). Framed as lossy compression "similar to jpeg or mp3."

- **Centering is WLOG** (§10.2): the code's variance is mean-invariant ($\mathbb V[\mathbf B^\top(\mathbf x-\boldsymbol\mu)]=\mathbb V[\mathbf B^\top\mathbf x]$, Eq. 10.6), so the data is assumed mean $\mathbf 0$.
- **Max-variance derivation** (§10.2): maximize $\mathbf b_1^\top\mathbf S\mathbf b_1$ s.t. $\|\mathbf b_1\|=1$ → [[LagrangeMultipliers|Lagrangian]] → $\mathbf S\mathbf b_1=\lambda_1\mathbf b_1$ (Eq. 10.13). Variance along $\mathbf b_1$ equals its eigenvalue $\lambda_1$ (Eq. 10.15). The $m$-th PC follows by **deflation** (Eq. 10.17); each $\mathbf b_m$ is also an eigenvector of $\mathbf S$ (Eq. 10.21).
- **Variance retained** $V_M=\sum_{m=1}^M\lambda_m$ (Eq. 10.24); **variance lost** $J_M=\sum_{j=M+1}^D\lambda_j$ (Eq. 10.25); relative captured $V_M/V_D$ — the scree-plot quantity (Example 10.2, MNIST "8").
- **Min-reconstruction-error derivation** (§10.3): minimize $J_M=\frac1N\sum_n\|\mathbf x_n-\tilde{\mathbf x}_n\|^2$ (Eq. 10.29). Optimal coordinates are the [[OrthogonalProjection|orthogonal-projection]] coordinates $z_{in}=\mathbf b_i^\top\mathbf x_n$ (Eq. 10.32); the [[ReconstructionError|displacement]] lives in the [[OrthogonalComplement|orthogonal complement]] (Eq. 10.38); PCA = best rank-$M$ approximation $\mathbf B\mathbf B^\top$ of $\mathbf I$ (Eq. 10.40, [[LowRankApproximation]]). The loss reduces to $\sum_{j=M+1}^D\lambda_j$ (Eq. 10.44) — **identical solution to max-variance**.
- **Eigenvector computation** (§10.4): eigendecompose $\mathbf S=\frac1N\mathbf X\mathbf X^\top$ directly, or take the [[SingularValueDecomposition|SVD]] $\mathbf X=\mathbf U\boldsymbol\Sigma\mathbf V^\top$ — columns of $\mathbf U$ are the eigenvectors of $\mathbf S$, with $\lambda_d=\sigma_d^2/N$ (Eq. 10.49). [[EckartYoung|Eckart–Young]] (Thm 4.25) gives the optimal truncation; [[PowerIteration|power iteration]] (Eq. 10.52, the PageRank algorithm) is cheapest for a few leading PCs.
- **High dimensions $N\ll D$** (§10.5): solve the small $N\times N$ eigenproblem $\frac1N\mathbf X^\top\mathbf X\,\mathbf c_m=\lambda_m\mathbf c_m$ (Eq. 10.56), which shares the nonzero eigenvalues of $\mathbf S$; recover the original eigenvectors as $\mathbf X\mathbf c_m$ (Eq. 10.57, normalize).
- **Practical pipeline** (§10.6): (1) mean subtraction, (2) [[DataStandardization|standardization]] / [[Whitening|whitening]], (3) eigendecomposition of $\mathbf S$, (4) projection $\mathbf z_*=\mathbf B^\top\mathbf x_*$ (Eq. 10.60) — **PCA returns the coordinates, not the projection** — then undo standardization to map back (Eq. 10.61). Reconstruction sharpens with $M$ (Example 10.4, MNIST "8" at 1/10/100/500 PCs).
- **Latent-variable derivation** (§10.7): [[ProbabilisticPCA|probabilistic PCA]] — $\mathbf x=\mathbf B\mathbf z+\boldsymbol\mu+\boldsymbol\epsilon$, marginal likelihood $\mathcal N(\mathbf x\mid\boldsymbol\mu,\mathbf B\mathbf B^\top+\sigma^2\mathbf I)$; MLE recovers the leading eigenvectors of $\mathbf S$ (up to rotation $\mathbf R$), and the noise-free limit $\sigma\to0$ gives classical PCA.
- **Auto-encoder & relatives** (§10.8): PCA is the optimal linear [[Autoencoder|auto-encoder]] (Eq. 10.76); nonlinear → deep auto-encoder; [[FactorAnalysis|factor analysis]] (per-dim noise), [[IndependentComponentAnalysis|ICA]] (non-Gaussian prior, blind-source separation), kernel PCA, GP-LVM are the relatives.

## Parallel PCA ([[parproc-ch14-statistics-data-mining]] §14.4)

PCA finds r < p variables consisting of linear combinations of the original p variables that carry most of the information of the full set — **dimension reduction**. These r variables are the eigenvectors corresponding to the r largest eigenvalues of the p×p covariance matrix. Because PCA reduces to a matrix eigenvector problem, it is parallelized via the parallel eigenvector algorithms in [[parproc-ch11-parallel-matrix-operations]] §11.6.

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — exhaustive per-chapter deep dive (the canonical reference).
- [[mml-book]] — Ch 10 within the umbrella.
- [[PCA]] — acronym disambiguation.
- [[DataCovarianceMatrix]] — the object PCA diagonalizes.
- [[Eigendecomposition]] — algebraic engine.
- [[SingularValueDecomposition]] — equivalent route via centered $\mathbf{X}$ directly.
- [[OrthogonalProjection]] — geometric interpretation of $\mathbf{B}\mathbf{B}^\top$.
- [[PrincipalSubspace]] / [[ReconstructionError]] — the projection-perspective objects.
- [[ProbabilisticPCA]] — the latent-variable generative derivation.
- [[PowerIteration]] / [[LowRankApproximation]] / [[EckartYoung]] — eigenvector computation & optimal truncation.
- [[DataStandardization]] / [[Whitening]] — the practical preprocessing step.
- [[FactorAnalysis]] / [[IndependentComponentAnalysis]] / [[Autoencoder]] — the §10.8 relatives.
- [[CurseOfDimensionality]] — motivation.
- [[KarhunenLoeveTransform]] — alternative name in signal processing.
- [[islr-seventh-printing]] — Ch 10 ISLR treatment.
- [[parproc-ch14-statistics-data-mining]] — §14.4 parallel PCA via Ch11 eigenvector methods.
- [[parproc-ch11-parallel-matrix-operations]] — §11.6 parallel eigenvector algorithms used by parallel PCA.
