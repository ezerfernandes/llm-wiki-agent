---
title: "Principal Subspace"
type: concept
tags: [dimensionality-reduction, pca, linear-algebra, subspace]
sources: [mml-ch10-dimensionality-reduction-pca, mml-book]
last_updated: 2026-06-05
---

# Principal Subspace

The **$M$-dimensional subspace $U\subseteq\mathbb R^D$ onto which [[PrincipalComponentAnalysis|PCA]] projects the data**, spanned by an orthonormal basis $(\mathbf b_1,\dots,\mathbf b_M)$ ([[mml-book]] §10.3, p. 327). The basis vectors are the **principal components** — the eigenvectors of the [[DataCovarianceMatrix|data covariance matrix]] $\mathbf S$ associated with the $M$ **largest** eigenvalues.

## Definition & projection ([[mml-ch10-dimensionality-reduction-pca|MML §10.3]])

With $\mathbf B=[\mathbf b_1,\dots,\mathbf b_M]\in\mathbb R^{D\times M}$ orthonormal, the projection of a data point onto the principal subspace is the [[OrthogonalProjection|orthogonal projection]]

$$\tilde{\mathbf x}=\mathbf B(\mathbf B^\top\mathbf B)^{-1}\mathbf B^\top\mathbf x=\mathbf B\mathbf B^\top\mathbf x\in U\subseteq\mathbb R^D$$

(Eq. 10.34), with coordinates $\mathbf z=\mathbf B^\top\mathbf x\in\mathbb R^M$. Although $\tilde{\mathbf x}$ lives in $\mathbb R^D$, only $M$ coordinates are needed; the coordinates with respect to $\mathbf b_{M+1},\dots,\mathbf b_D$ are always $0$.

## Why the leading eigenvectors

The principal subspace is the subspace that **retains maximal variance** (equivalently minimizes the [[ReconstructionError|reconstruction error]]): variance retained is $V_M=\sum_{m=1}^M\lambda_m$ (Eq. 10.24), maximized by the eigenvectors of the $M$ largest eigenvalues. Its [[OrthogonalComplement|orthogonal complement]] $U^\perp=\mathrm{span}[\mathbf b_{M+1},\dots,\mathbf b_D]$ carries the discarded variance $\sum_{j=M+1}^D\lambda_j$ — exactly where every reconstruction-error displacement vector lives (Eq. 10.38).

## In the latent-variable view

In [[ProbabilisticPCA|probabilistic PCA]] the columns of the MLE loading matrix $\mathbf B_{\text{ML}}=\mathbf T(\boldsymbol\Lambda-\sigma^2\mathbf I)^{1/2}\mathbf R$ (Eq. 10.78) span the same principal subspace — but only up to an arbitrary orthogonal rotation $\mathbf R$. PCA therefore identifies the *subspace*, not a canonical basis within it (the rotation invariance that prevents blind-source separation; see [[IndependentComponentAnalysis]]).

## Connections

- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.3 canonical reference (p. 327).
- [[PrincipalComponentAnalysis]] — the method that finds it.
- [[DataCovarianceMatrix]] — its basis = leading eigenvectors of $\mathbf S$.
- [[OrthogonalProjection]] — how data is mapped onto it ($\mathbf B\mathbf B^\top$).
- [[OrthogonalComplement]] — where the discarded variance / reconstruction error lives.
- [[ReconstructionError]] — minimized over choice of principal subspace.
- [[Eigendecomposition]] / [[SingularValueDecomposition]] — how the basis is computed.
- [[ProbabilisticPCA]] — recovers the same subspace up to rotation.
