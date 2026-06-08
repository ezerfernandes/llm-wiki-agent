---
title: "Singular Value Decomposition"
type: concept
tags: [linear-algebra, matrix-decomposition, foundational, mlsysbook]
sources: [mml-book, mml-ch04-matrix-decompositions, mml-ch10-dimensionality-reduction-pca, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
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

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

**Theorem 4.22** (SVD Theorem, §4.5): a rectangular $\mathbf{A}\in\mathbb{R}^{m\times n}$ of rank $r\in[0,\min(m,n)]$ factors $\mathbf{A}=\mathbf{U}\boldsymbol\Sigma\mathbf{V}^\top$ with orthogonal $\mathbf{U}\in\mathbb{R}^{m\times m}$ (columns = **left-singular vectors** $\mathbf{u}_i$), orthogonal $\mathbf{V}\in\mathbb{R}^{n\times n}$ (columns = **right-singular vectors** $\mathbf{v}_j$), and $\boldsymbol\Sigma\in\mathbb{R}^{m\times n}$ with $\Sigma_{ii}=\sigma_i\geq0$ ordered $\sigma_1\geq\cdots\geq\sigma_r\geq0$. $\boldsymbol\Sigma$ is **unique** and *rectangular* (same shape as $\mathbf{A}$, with zero padding). **The SVD exists for any matrix** — the "fundamental theorem of linear algebra" (Strang 1993).

- **Geometry** (§4.5.1, Figs. 4.8–4.9): three sequential maps — $\mathbf{V}^\top$ (basis change in the **domain** $\mathbb{R}^n$), $\boldsymbol\Sigma$ (scale by singular values + change dimensionality), $\mathbf{U}$ (basis change in the **codomain** $\mathbb{R}^m$). **The SVD changes basis in *both* domain and codomain**, linked by $\boldsymbol\Sigma$ — unlike [[Eigendecomposition]], which acts within one space.
- **Construction** (§4.5.2): right-singular vectors $\mathbf{V}$ = eigenvectors of $\mathbf{A}^\top\mathbf{A}$ (symmetric PSD by Thm 4.14, diagonalizable by the [[SpectralTheorem|spectral theorem]]); left-singular vectors $\mathbf{U}$ = eigenvectors of $\mathbf{A}\mathbf{A}^\top$; singular values $\sigma_i=\sqrt{\lambda_i}$ are square roots of the eigenvalues of $\mathbf{A}^\top\mathbf{A}$ (Eq. 4.75). The **singular value equation** $\mathbf{A}\mathbf{v}_i=\sigma_i\mathbf{u}_i$ (Eq. 4.79) links the two ONBs; the $\mathbf{v}_i$ with $\mathbf{A}\mathbf{v}_i=\mathbf{0}$ span the kernel of $\mathbf{A}$. (Note: the $\mathbf{A}^\top\mathbf{A}$-route is numerically poor — production SVD avoids it.)
- **Conventions** (§4.5.3): the square-$\mathbf{U},\mathbf{V}$ form is the *full SVD*; the *reduced/truncated SVD* uses $\mathbf{U}\in\mathbb{R}^{m\times r}$, $\boldsymbol\Sigma\in\mathbb{R}^{r\times r}$, $\mathbf{V}\in\mathbb{R}^{r\times n}$ (diagonal $\boldsymbol\Sigma$).
- **vs Eigendecomposition** (§4.5.3): SVD always exists (any matrix); $\mathbf{U},\mathbf{V}$ orthonormal (pure rotations) vs $\mathbf{P}$ generally not; $\boldsymbol\Sigma$ real non-negative; for symmetric matrices the two coincide.
- **[[SpectralNorm]]** (Thm 4.24): $\|\mathbf{A}\|_2=\sigma_1$, the largest singular value.
- **Example 4.14** (movie ratings): left-singular vectors = "stereotypical movies", right-singular vectors = "stereotypical viewers" (sci-fi vs French art-house themes).

## From [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] (SVD computes PCA)

[[mml-ch10-dimensionality-reduction-pca|MML §10.4]] uses the SVD as the practical route to [[PrincipalComponentAnalysis|PCA]]. Writing the (column-major) data matrix $\mathbf X=[\mathbf x_1,\dots,\mathbf x_N]\in\mathbb R^{D\times N}$ and its SVD $\mathbf X=\mathbf U\boldsymbol\Sigma\mathbf V^\top$ (Eq. 10.47), the [[DataCovarianceMatrix|data covariance]] factors as $\mathbf S=\frac1N\mathbf X\mathbf X^\top=\frac1N\mathbf U\boldsymbol\Sigma\boldsymbol\Sigma^\top\mathbf U^\top$ (Eq. 10.48). Hence **the columns of $\mathbf U$ are the eigenvectors of $\mathbf S$** (the principal components) and the eigenvalues relate to the singular values via $\lambda_d=\sigma_d^2/N$ (Eq. 10.49) — no need to form $\mathbf S$ explicitly. [[EckartYoung|Eckart–Young]] (Thm 4.25) then gives the optimal rank-$M$ low-dim estimate as the SVD truncated at the top-$M$ singular value, $\tilde{\mathbf X}_M=\mathbf U_M\boldsymbol\Sigma_M\mathbf V_M^\top$ (Eqs. 10.50–10.51). The [[ProbabilisticPCA|PPCA]] MLE $\mathbf B_{\text{ML}}=\mathbf T(\boldsymbol\Lambda-\sigma^2\mathbf I)^{1/2}\mathbf R$ (Eq. 10.78) is "essentially an SVD," unique only up to the orthogonal $\mathbf R$.

## Connections

- [[mml-book]] — §4.5 canonical reference.
- [[mml-ch04-matrix-decompositions|MML Ch 4]] — full §4.5–4.6 deep dive (Thm 4.22).
- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — §10.4 SVD-based PCA ($\lambda_d=\sigma_d^2/N$).
- [[LowRankApproximation]] / [[EckartYoung]] / [[SpectralNorm]] — §4.6 optimal rank-$k$ compression.
- [[SpectralTheorem]] — the construction relies on it; [[MatrixPhylogeny]] — SVD is the one factorization at the taxonomy root.
- [[MatrixDecomposition]] — broader taxonomy.
- [[Eigendecomposition]] — symmetric special case.
- [[CholeskyDecomposition]] — SPD special case.
- [[PrincipalComponentAnalysis]] — direct SVD-based derivation.
- [[ConditionNumber]] — defined via singular values.
- [[LowRankFactorization]] / [[TensorDecomposition]] / [[mlsysbook-ch10-model-compression]] — SVD is the optimal rank-$k$ approximation (Eckart-Young) underlying low-rank model compression: keeping the top $k$ singular values minimizes information loss while cutting storage $\mathcal{O}(mn)\to\mathcal{O}(k(m+n))$.
