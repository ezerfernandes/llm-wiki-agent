---
title: "Eigendecomposition"
type: concept
tags: [linear-algebra, matrix-decomposition, foundational]
sources: [mml-book, mml-ch04-matrix-decompositions, d2l-appendix-mathematics, mml-ch10-dimensionality-reduction-pca]
last_updated: 2026-06-05
---

# Eigendecomposition

A diagonalizable square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ factors as

$$\mathbf{A} = \mathbf{P}\,\mathbf{D}\,\mathbf{P}^{-1}$$

where $\mathbf{D}$ is diagonal (containing eigenvalues $\lambda_1,\dots,\lambda_n$) and $\mathbf{P}$ has the corresponding eigenvectors as columns ([[mml-book]] §4.4).

When $\mathbf{A}$ is **symmetric**, the spectral theorem (Thm 4.15) guarantees $\mathbf{P}$ is orthogonal — i.e., $\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^\top$ with $\mathbf{P}^\top\mathbf{P}=\mathbf{I}$. This is the case for every [[DataCovarianceMatrix]] (Ch 10) and every [[GramMatrix]] in kernel methods (Ch 12).

## Connection to the characteristic polynomial

Eigenvalues are roots of the [[CharacteristicPolynomial]] $p_\mathbf{A}(\lambda) = \det(\mathbf{A}-\lambda\mathbf{I})$ ([[mml-book]] Def 4.5). Hence the algebrica.org pages [[roots-of-a-polynomial]] / [[polynomial-equations]] are the prerequisites for computing eigenvalues by hand.

## ML uses

- **[[PrincipalComponentAnalysis|PCA]]** (Ch 10): principal components = eigenvectors of the data covariance matrix, ordered by eigenvalue magnitude. The fraction of variance captured by the first $M$ components is $\sum_{m=1}^M \lambda_m / \sum_{m=1}^D \lambda_m$.
- **PageRank** and **spectral clustering**: dominant eigenvector of a transition / similarity matrix.
- **Stability analysis** of dynamical systems and RNNs: eigenvalues of the recurrence matrix.

## From [[mml-ch04-matrix-decompositions|MML Ch 4]]

**Theorem 4.20** (§4.4, Eq. 4.55): a square $\mathbf{A}\in\mathbb{R}^{n\times n}$ factors $\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^{-1}$ (with $\mathbf{D}$ diagonal of eigenvalues, $\mathbf{P}$ of eigenvectors) **iff the eigenvectors of $\mathbf{A}$ form a basis of $\mathbb{R}^n$** — i.e. iff $\mathbf{A}$ is non-[[DefectiveMatrix|defective]] / [[Diagonalization|diagonalizable]]. The eigendecomposition is the [[SimilarityTransform|similarity transform]] $\mathbf{D}=\mathbf{P}^{-1}\mathbf{A}\mathbf{P}$ that diagonalizes $\mathbf{A}$.

- **Symmetric case** (Thm 4.21 via [[SpectralTheorem|spectral theorem]] Thm 4.15): $\mathbf{P}$ can be chosen *orthogonal*, so $\mathbf{A}=\mathbf{P}\mathbf{D}\mathbf{P}^\top$ with $\mathbf{P}^\top\mathbf{P}=\mathbf{I}$ and all $\lambda_i$ real — symmetric matrices *always* diagonalize. The **Jordan normal form** (Lang 1987) handles defective matrices but is beyond MML's scope.
- **Consequences** (Eqs. 4.62–4.63): cheap matrix powers $\mathbf{A}^k=\mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$ and determinant $\det(\mathbf{A})=\prod_i d_{ii}$.
- **Geometric intuition** (Fig. 4.7): three sequential maps — $\mathbf{P}^{-1}$ (basis change into the eigenbasis), $\mathbf{D}$ (scale along eigen-axes), $\mathbf{P}$ (restore standard coordinates). The eigendecomposition **applies and then undoes the same basis change within one vector space** — unlike the [[SingularValueDecomposition|SVD]], which changes basis in *both* domain and codomain. Worked Example 4.11: $\mathbf{A}=\tfrac12\begin{bmatrix}5&-2\\-2&5\end{bmatrix}$ diagonalizes with $\lambda_1=\tfrac72,\lambda_2=\tfrac32$ and orthonormal $\mathbf{P}$.
- **Relation to SVD** (§4.5.2–4.5.3): for an SPD matrix the eigendecomposition *is* the SVD ($\mathbf{U}=\mathbf{P}=\mathbf{V}$, $\mathbf{D}=\boldsymbol\Sigma$); generally the SVD's right-/left-singular vectors are the eigenvectors of $\mathbf{A}^\top\mathbf{A}$ / $\mathbf{A}\mathbf{A}^\top$.

## From [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] (the engine of PCA)

[[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] is the headline ML consumer. The [[DataCovarianceMatrix|data covariance]] $\mathbf S=\frac1N\sum_n\mathbf x_n\mathbf x_n^\top$ is symmetric, so the [[SpectralTheorem|spectral theorem]] (Thm 4.15) gives a real orthonormal eigenbasis; [[PrincipalComponentAnalysis|PCA]] projects onto the eigenvectors of the $M$ largest eigenvalues. All three PCA derivations land on the eigenvalue equation $\mathbf S\mathbf b_m=\lambda_m\mathbf b_m$ (max-variance Eq. 10.13 via [[LagrangeMultipliers|Lagrange multipliers]]; min-reconstruction-error §10.3; latent-variable §10.7). Because the **Abel–Ruffini theorem** forbids closed-form characteristic-polynomial roots beyond $4\times4$, the eigenvectors are computed *iteratively* — full eigendecomposition / [[SingularValueDecomposition|SVD]], or [[PowerIteration|power iteration]] for just the leading few (§10.4.2).

## Connections

- [[mml-book]] — §4.4 canonical reference.
- [[mml-ch04-matrix-decompositions|MML Ch 4]] — full §4.4 deep dive (Thm 4.20).
- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] — eigendecomposition of $\mathbf S$ is PCA (§10.2/10.4).
- [[Diagonalization]] / [[SimilarityTransform]] — the construction; [[DefectiveMatrix]] — the obstruction; [[SpectralTheorem]] — guarantees the symmetric case.
- [[eigenvalues-and-eigenvectors]] — algebrica.org's eigenvalue page.
- [[matrix-diagonalization]] — algebrica.org's diagonalization page.
- [[SingularValueDecomposition]] — generalization to non-square / non-symmetric.
- [[PrincipalComponentAnalysis]] — primary ML application.
- [[CharacteristicPolynomial]] — algebraic route to eigenvalues.
