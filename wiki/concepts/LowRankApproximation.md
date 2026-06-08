---
title: "Low-Rank Approximation"
type: concept
tags: [linear-algebra, matrix-decomposition, svd, compression, dimensionality-reduction]
sources: [mml-ch04-matrix-decompositions, mml-book, mml-ch10-dimensionality-reduction-pca]
last_updated: 2026-06-05
---

# Low-Rank Approximation

Approximating a matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ of rank $r$ by a matrix of lower rank $k<r$, built from the leading terms of its [[SingularValueDecomposition|SVD]] ([[mml-book]] §4.6). This is the principled, optimal form of lossy matrix compression.

## SVD as a sum of rank-1 matrices

Any rank-$r$ matrix decomposes as a weighted sum of **rank-1 outer products** ([[mml-book]] Eqs. 4.90–4.91):

$$\mathbf{A} = \sum_{i=1}^r \sigma_i\,\mathbf{u}_i\mathbf{v}_i^\top = \sum_{i=1}^r \sigma_i\,\mathbf{A}_i, \qquad \mathbf{A}_i := \mathbf{u}_i\mathbf{v}_i^\top$$

where $\mathbf{u}_i,\mathbf{v}_i$ are the $i$-th left-/right-singular vectors and $\sigma_i$ the singular values. The diagonal structure of $\boldsymbol\Sigma$ makes the cross terms vanish.

## The rank-$k$ approximation

Truncating the sum at $k$ gives ([[mml-book]] Eq. 4.92):

$$\widehat{\mathbf{A}}(k) := \sum_{i=1}^k \sigma_i\,\mathbf{u}_i\mathbf{v}_i^\top, \qquad \operatorname{rk}(\widehat{\mathbf{A}}(k)) = k.$$

It is also called the **truncated SVD**.

## Eckart–Young: it is optimal

The [[EckartYoung|Eckart–Young theorem]] (Thm 4.25) proves $\widehat{\mathbf{A}}(k)$ is the **best** rank-$k$ approximation in the [[SpectralNorm|spectral norm]]:

$$\widehat{\mathbf{A}}(k) = \operatorname*{argmin}_{\operatorname{rk}(\mathbf{B})=k}\|\mathbf{A}-\mathbf{B}\|_2, \qquad \|\mathbf{A}-\widehat{\mathbf{A}}(k)\|_2 = \sigma_{k+1}.$$

The approximation error equals the **first dropped singular value** $\sigma_{k+1}$. Geometrically it is the projection of $\mathbf{A}$ onto the space of rank-$\leq k$ matrices.

## Compression payoff

([[mml-book]] §4.6, Fig. 4.11–4.12): the rank-5 approximation of a $1432\times1910$ Stonehenge image stores $5\cdot(1432+1910+1)=16{,}715$ numbers instead of $2{,}735{,}120$ — **~0.6% of the original** — while keeping the rocks clearly recognizable. Storing a rank-$k$ approximation costs $(m+n)k$ values vs $mn$.

## Where it shows up in ML

- **Dimensionality reduction / [[PrincipalComponentAnalysis|PCA]]** (Ch 10) — low-rank approximation of the data/covariance matrix.
- **Image processing, noise filtering, regularization** of ill-posed problems ([[mml-book]] §4.6).
- **Data compression and decorrelation** of design-matrix predictors ([[mml-book]] §4.8).
- **Latent semantic analysis, collaborative filtering, topic modeling** — truncated SVD on text / user-item matrices.
- **[[LoRA]]-style low-rank adapters** — the parameter-efficient fine-tuning that the rank-$k$ representation justifies.
- Generalizes to higher-order arrays via **tensor decompositions** (Tucker, CP — [[mml-book]] §4.8).

## From [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] (PCA = best rank-$M$ approximation)

[[mml-ch10-dimensionality-reduction-pca|MML §10.3]] shows [[PrincipalComponentAnalysis|PCA]] *is* a low-rank approximation in two senses. (1) The projection matrix $\sum_{m=1}^M\mathbf b_m\mathbf b_m^\top=\mathbf B\mathbf B^\top$ is symmetric of rank $M$, and minimizing the [[ReconstructionError|reconstruction error]] $\frac1N\sum_n\|(\mathbf I-\mathbf B\mathbf B^\top)\mathbf x_n\|^2$ is equivalent to finding the **best rank-$M$ approximation $\mathbf B\mathbf B^\top$ of the identity matrix** (Eq. 10.40). (2) §10.4.1 applies [[EckartYoung|Eckart–Young]] (Thm 4.25) directly to the data matrix: the best rank-$M$ approximation $\tilde{\mathbf X}_M=\operatorname{argmin}_{\mathrm{rk}(\mathbf A)\le M}\|\mathbf X-\mathbf A\|_2$ is the [[SingularValueDecomposition|SVD]] truncated at the top-$M$ singular value, $\tilde{\mathbf X}_M=\mathbf U_M\boldsymbol\Sigma_M\mathbf V_M^\top$ (Eqs. 10.50–10.51) — exactly the principal-subspace projection.

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.6 canonical reference.
- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.3/10.4 PCA as best rank-$M$ approximation.
- [[SingularValueDecomposition]] — the factorization that supplies the rank-1 terms.
- [[EckartYoung]] — the optimality theorem.
- [[SpectralNorm]] — the norm in which the approximation is optimal; error = $\sigma_{k+1}$.
- [[Rank]] — what is being reduced.
- [[PrincipalComponentAnalysis]] / [[LoRA]] — headline ML applications.
