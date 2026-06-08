---
title: "Eckart-Young Theorem"
type: concept
tags: [linear-algebra, matrix-decomposition, svd, low-rank, theorem]
sources: [mml-ch04-matrix-decompositions, mml-book, mml-ch10-dimensionality-reduction-pca]
last_updated: 2026-06-05
---

# Eckart–Young Theorem

**Theorem 4.25** (Eckart & Young, 1936; [[mml-book]] §4.6): the truncated [[SingularValueDecomposition|SVD]] is the *optimal* [[LowRankApproximation|low-rank approximation]] of a matrix in the [[SpectralNorm|spectral norm]].

For $\mathbf{A}\in\mathbb{R}^{m\times n}$ of rank $r$, any rank-$k$ matrix $\mathbf{B}\in\mathbb{R}^{m\times n}$ with $k\leq r$, and the rank-$k$ approximation $\widehat{\mathbf{A}}(k)=\sum_{i=1}^k\sigma_i\mathbf{u}_i\mathbf{v}_i^\top$:

$$\widehat{\mathbf{A}}(k) = \operatorname*{argmin}_{\operatorname{rk}(\mathbf{B})=k}\|\mathbf{A}-\mathbf{B}\|_2 \qquad\text{(Eq. 4.94)}$$

$$\|\mathbf{A}-\widehat{\mathbf{A}}(k)\|_2 = \sigma_{k+1} \qquad\text{(Eq. 4.95)}$$

The error of the *best possible* rank-$k$ approximation is exactly the **first discarded singular value** $\sigma_{k+1}$.

## Interpretation

The truncated SVD is the **projection of the full-rank $\mathbf{A}$ onto the space of rank-at-most-$k$ matrices** — and of all such projections, it minimizes the spectral-norm error. This makes the rank-$k$ approximation a principled form of lossy compression.

## Proof sketch

([[mml-book]] §4.6, Eqs. 4.96–4.99): the difference $\mathbf{A}-\widehat{\mathbf{A}}(k)=\sum_{i=k+1}^r\sigma_i\mathbf{u}_i\mathbf{v}_i^\top$ has spectral norm $\sigma_{k+1}$ (Thm 4.24, [[SpectralNorm|spectral norm]] = largest singular value of the difference). Suppose a competitor $\mathbf{B}$ with $\operatorname{rk}(\mathbf{B})\leq k$ achieves $\|\mathbf{A}-\mathbf{B}\|_2<\sigma_{k+1}$. Then $\mathbf{B}$ has an $(n-k)$-dimensional null space $Z$; for $\mathbf{x}\in Z$, $\|\mathbf{A}\mathbf{x}\|_2=\|(\mathbf{A}-\mathbf{B})\mathbf{x}\|_2\leq\|\mathbf{A}-\mathbf{B}\|_2\|\mathbf{x}\|_2<\sigma_{k+1}\|\mathbf{x}\|_2$ (using a matrix Cauchy–Schwarz, Eq. 3.17). But the span of $\mathbf{v}_1,\ldots,\mathbf{v}_{k+1}$ is a $(k+1)$-dimensional space on which $\|\mathbf{A}\mathbf{x}\|_2\geq\sigma_{k+1}\|\mathbf{x}\|_2$. Two subspaces of dimensions summing to $>n$ must intersect non-trivially — a contradiction with the [[RankNullityTheorem|rank–nullity theorem]] (Thm 2.24). Hence no better $\mathbf{B}$ exists.

## Why it matters

It is the theoretical guarantee behind every truncated-SVD compression: PCA, latent semantic analysis, collaborative filtering, image compression, denoising, regularization, and [[LoRA]]-style low-rank adapters all rely on the fact that *keeping the top-$k$ singular triplets is provably the best you can do at rank $k$*.

## From [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] (it justifies PCA's truncation)

[[mml-ch10-dimensionality-reduction-pca|MML §10.4.1]] invokes Eckart–Young as "a direct way to estimate the low-dimensional representation" in [[PrincipalComponentAnalysis|PCA]]: the best rank-$M$ approximation of the data matrix $\mathbf X$, $\tilde{\mathbf X}_M=\operatorname{argmin}_{\mathrm{rk}(\mathbf A)\le M}\|\mathbf X-\mathbf A\|_2$ (Eq. 10.50), is the [[SingularValueDecomposition|SVD]] truncated at the top-$M$ singular value, $\tilde{\mathbf X}_M=\mathbf U_M\boldsymbol\Sigma_M\mathbf V_M^\top$ (Eq. 10.51). Since the columns of $\mathbf U$ are the eigenvectors of the [[DataCovarianceMatrix|data covariance]] $\mathbf S$ (with $\lambda_d=\sigma_d^2/N$), this is precisely PCA's projection onto the leading principal components — so Eckart–Young is the theorem certifying that **keeping the top-$M$ components is optimal**.

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.6 canonical reference (Thm 4.25).
- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.4.1 applies it to PCA's rank-$M$ truncation.
- [[LowRankApproximation]] — the construction this theorem proves optimal.
- [[SingularValueDecomposition]] — supplies the singular triplets.
- [[SpectralNorm]] — the norm in which optimality holds; error = $\sigma_{k+1}$.
- [[RankNullityTheorem]] — invoked in the proof's dimension-counting contradiction.
- [[CauchySchwarzInequality]] — the matrix-norm version used in the proof.
