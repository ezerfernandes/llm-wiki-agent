---
title: "Reconstruction Error"
type: concept
tags: [dimensionality-reduction, pca, linear-algebra, optimization, autoencoder]
sources: [mml-ch10-dimensionality-reduction-pca, mml-book]
last_updated: 2026-06-05
---

# Reconstruction Error

The **average squared Euclidean distance between original data points and their lower-dimensional reconstructions** — the objective minimized in the *projection perspective* of [[PrincipalComponentAnalysis|PCA]] (Pearson 1901; [[mml-book]] §10.3, Eq. 10.29):

$$J_M:=\frac1N\sum_{n=1}^N\bigl\lVert\mathbf x_n-\tilde{\mathbf x}_n\bigr\rVert^2,$$

where $\tilde{\mathbf x}_n=\mathbf B\mathbf z_n=\sum_{m=1}^M z_{mn}\mathbf b_m$ is the reconstruction from the $M$-dimensional code and $(\mathbf b_1,\dots,\mathbf b_M)$ is an orthonormal basis of the [[PrincipalSubspace|principal subspace]].

## Minimizing it *is* orthogonal projection ([[mml-ch10-dimensionality-reduction-pca|MML §10.3.2]])

A two-step optimization (coordinates first, then basis) shows the optimal coordinates are the [[OrthogonalProjection|orthogonal-projection]] coordinates $z_{in}=\mathbf b_i^\top\mathbf x_n$ (Eq. 10.32), so $\tilde{\mathbf x}_n=\mathbf B\mathbf B^\top\mathbf x_n$ is the orthogonal projection of $\mathbf x_n$ onto the principal subspace, and **an orthogonal projection is the best linear map** for this objective.

## The displacement lives in the orthogonal complement ([[mml-ch10-dimensionality-reduction-pca|MML §10.3.3]])

The error vector $\mathbf x_n-\tilde{\mathbf x}_n=\bigl(\sum_{j=M+1}^D\mathbf b_j\mathbf b_j^\top\bigr)\mathbf x_n$ (Eq. 10.38a) is the projection of $\mathbf x_n$ onto the [[OrthogonalComplement|orthogonal complement]] $U^\perp$ of the principal subspace. Hence (Eqs. 10.40, 10.76):

$$J_M=\frac1N\sum_n\bigl\lVert(\mathbf I-\mathbf B\mathbf B^\top)\mathbf x_n\bigr\rVert^2,$$

making PCA the **best rank-$M$ approximation $\mathbf B\mathbf B^\top$ of the identity** ([[LowRankApproximation]], §4.6).

## Equals the sum of discarded eigenvalues ([[mml-ch10-dimensionality-reduction-pca|MML §10.3.3]])

Rewriting the loss as a trace of the projected [[DataCovarianceMatrix|covariance]] and reducing (Eqs. 10.41–10.44, 10.62):

$$J_M=\sum_{j=M+1}^D\lambda_j,$$

the **sum of the $D-M$ smallest eigenvalues** of $\mathbf S$. Minimizing $J_M$ therefore means discarding the smallest eigenvalues — equivalently **maximizing the variance retained in the principal subspace** ($V_M=\sum_{m=1}^M\lambda_m$). This is why the projection and [[PrincipalComponentAnalysis|maximum-variance]] perspectives give the *same* solution.

## In auto-encoders

With the linear encoder $\mathbf z_n=\mathbf B^\top\mathbf x_n$ the squared auto-encoding loss $\frac1N\sum_n\lVert\mathbf x_n-\mathbf B\mathbf B^\top\mathbf x_n\rVert^2$ is identical to $J_M$ — so PCA is the optimal linear [[Autoencoder|auto-encoder]] (Eq. 10.76); deep/nonlinear auto-encoders minimize the same kind of reconstruction error with nonlinear maps.

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.3 canonical reference (Eq. 10.29).
- [[PrincipalComponentAnalysis]] — the projection perspective minimizes this.
- [[OrthogonalProjection]] / [[OrthogonalComplement]] — the optimal reconstruction is a projection; the error lives in the complement.
- [[PrincipalSubspace]] — the subspace onto which we project.
- [[DataCovarianceMatrix]] — $J_M$ = sum of its discarded eigenvalues.
- [[LowRankApproximation]] / [[EckartYoung]] — $\mathbf B\mathbf B^\top$ is the best rank-$M$ approximation of $\mathbf I$.
- [[Autoencoder]] — same loss with (non)linear maps.
