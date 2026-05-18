---
title: "Singular Value Decomposition"
type: concept
tags: [linear-algebra, matrix-decomposition, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Singular Value Decomposition (SVD)

Every real matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ factors as

$$\mathbf{A} = \mathbf{U}\,\boldsymbol\Sigma\,\mathbf{V}^\top$$

where $\mathbf{U}\in\mathbb{R}^{m\times m}$ and $\mathbf{V}\in\mathbb{R}^{n\times n}$ are orthogonal and $\boldsymbol\Sigma\in\mathbb{R}^{m\times n}$ is diagonal (with non-negative *singular values* $\sigma_1\geq\sigma_2\geq\cdots\geq 0$).

"Considered one of the fundamental concepts in linear algebra" ([[mml-book]] Ch 4 intro, p. 98); §4.5.

## Why SVD generalizes everything

| Other decomposition | When SVD reduces to it |
|---|---|
| [[Eigendecomposition]] $\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ | $\mathbf{A}$ symmetric: $\mathbf{U}=\mathbf{V}=\mathbf{P}$, $\boldsymbol\Sigma=|\mathbf{D}|$ |
| [[CholeskyDecomposition]] | $\mathbf{A}$ symmetric positive definite |
| Polar decomposition | $\mathbf{A} = (\mathbf{U}\mathbf{V}^\top)(\mathbf{V}\boldsymbol\Sigma\mathbf{V}^\top)$ — rotation $\cdot$ stretch |

## ML uses

- **Low-rank approximation** (§4.6, Eckart-Young): the best rank-$k$ approximation in Frobenius norm is $\mathbf{A}_k = \sum_{i=1}^k \sigma_i \mathbf{u}_i \mathbf{v}_i^\top$. Drops the smallest $\sigma_i$ first.
- **[[PrincipalComponentAnalysis|PCA]]**: the SVD of the centered data matrix gives the principal components directly (no need to form the covariance matrix explicitly).
- **[[ConditionNumber]]** ($\kappa = \sigma_{\max}/\sigma_{\min}$): controls gradient-descent convergence rate ([[mml-book]] §7.1.1).
- **Latent semantic analysis** and **collaborative filtering**: classical applications of truncated SVD on text/user-item matrices.
- **[[LoRA]]** and modern **low-rank adapter** methods: the rank-$k$ representation that SVD justifies is the parameter-efficient way to fine-tune large models.

## Connections

- [[mml-book]] — §4.5 canonical reference.
- [[MatrixDecomposition]] — broader taxonomy.
- [[Eigendecomposition]] — symmetric special case.
- [[CholeskyDecomposition]] — SPD special case.
- [[PrincipalComponentAnalysis]] — direct SVD-based derivation.
- [[ConditionNumber]] — defined via singular values.
