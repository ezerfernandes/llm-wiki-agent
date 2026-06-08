---
title: "Orthogonal Projection"
type: concept
tags: [analytic-geometry, linear-algebra, foundational]
sources: [mml-ch03-analytic-geometry, mml-book, mml-ch09-linear-regression, mml-ch10-dimensionality-reduction-pca]
last_updated: 2026-06-05
---

# Orthogonal Projection

Given a subspace $U\subseteq V$ of an inner-product space, the orthogonal projection $\pi_U(\mathbf{x})$ of a vector $\mathbf{x}\in V$ onto $U$ is the unique closest point in $U$ to $\mathbf{x}$ ([[mml-book]] §3.8). The residual $\mathbf{x}-\pi_U(\mathbf{x})$ is orthogonal to every vector in $U$.

## Closed-form

If $U$ is the column space of $\mathbf{B}\in\mathbb{R}^{D\times M}$ (i.e., $\mathbf{B}$'s columns span $U$):

$$
\pi_U(\mathbf{x}) = \mathbf{B}\,(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top\,\mathbf{x}
$$

The matrix $\mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top$ is the *projection matrix*; it is symmetric and idempotent ($\mathbf{P}^2=\mathbf{P}$).

When $\mathbf{B}$ has orthonormal columns ($\mathbf{B}^\top\mathbf{B}=\mathbf{I}$), this collapses to $\pi_U(\mathbf{x}) = \mathbf{B}\mathbf{B}^\top\mathbf{x}$.

## Why orthogonal projection is everywhere in ML

- **[[LinearRegression|Least-squares regression]]** ([[mml-book]] §9.4): $\boldsymbol\theta_{\text{ML}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$ is exactly the projection coefficients of $\mathbf{y}$ onto the column space of the [[DesignMatrix]] $\mathbf{X}$. The MLE *is* orthogonal projection.
- **[[PrincipalComponentAnalysis|PCA]]** (Ch 10): the reconstructed point $\tilde{\mathbf{x}}_n = \mathbf{B}\mathbf{B}^\top\mathbf{x}_n$ is the orthogonal projection of $\mathbf{x}_n$ onto the $M$-dim principal subspace.
- **[[SupportVectorMachine|SVM margin]]** (Ch 12.2): the distance from a training point to the separating hyperplane is computed via orthogonal projection onto the hyperplane.
- **Gram-Schmidt orthogonalization** is iterated orthogonal projection.

## The single unifying picture

[[mml-book]] §9.4 makes the connection explicit: linear regression *is* orthogonal projection. The normal equations $\mathbf{X}^\top(\mathbf{y}-\mathbf{X}\boldsymbol\theta) = \mathbf{0}$ are exactly the orthogonality condition: the residual is orthogonal to every column of $\mathbf{X}$.

## From [[mml-ch09-linear-regression|MML Ch 9]] (regression *is* projection)

[[mml-ch09-linear-regression|MML Ch 9]] §9.4 ("Maximum Likelihood as Orthogonal Projection") is the chapter's geometric payoff. For the 1-D origin-line model $y=x\theta+\epsilon$, the MLE $\theta_{\text{ML}}=\frac{\mathbf{X}^\top\mathbf{y}}{\mathbf{X}^\top\mathbf{X}}$ (Eq. 9.66) and fitted targets $\mathbf{X}\theta_{\text{ML}}=\frac{\mathbf{X}\mathbf{X}^\top}{\mathbf{X}^\top\mathbf{X}}\mathbf{y}$ (Eq. 9.67) are *exactly* the §3.8.1 projection of $\mathbf{y}$ onto the line spanned by $\mathbf{X}$, with projection matrix $\frac{\mathbf{X}\mathbf{X}^\top}{\mathbf{X}^\top\mathbf{X}}$ and $\theta_{\text{ML}}$ the projection coordinate (Fig. 9.12). In the general [[FeatureMap|feature]] case (Eqs. 9.68–9.71) $\boldsymbol\theta_{\text{ML}}=(\boldsymbol\Phi^\top\boldsymbol\Phi)^{-1}\boldsymbol\Phi^\top\mathbf{y}$ projects $\mathbf{y}$ onto the $K$-dim column space of the [[DesignMatrix|feature matrix]] $\boldsymbol\Phi$ — "closest" meaning minimum squared distance. When the basis is **orthonormal** ($\boldsymbol\Phi^\top\boldsymbol\Phi=\mathbf{I}$) the projection collapses to $\boldsymbol\Phi\boldsymbol\Phi^\top\mathbf{y}=(\sum_k\boldsymbol\phi_k\boldsymbol\phi_k^\top)\mathbf{y}$ — a sum of decoupled 1-D projections onto each basis vector (Eq. 9.71; wavelets / Fourier bases are orthonormal). This is the [[NormalEquations|normal-equations]] orthogonality condition $\boldsymbol\Phi^\top(\mathbf{y}-\boldsymbol\Phi\boldsymbol\theta)=\mathbf{0}$ in geometric dress.

## From [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] (PCA *is* projection)

The **projection perspective** of [[PrincipalComponentAnalysis|PCA]] ([[mml-ch10-dimensionality-reduction-pca|MML §10.3]]) is §3.8 applied to dimensionality reduction. Minimizing the average squared [[ReconstructionError|reconstruction error]] $J_M=\frac1N\sum_n\|\mathbf x_n-\tilde{\mathbf x}_n\|^2$ (Eq. 10.29) shows the optimal reconstruction $\tilde{\mathbf x}_n=\mathbf B(\mathbf B^\top\mathbf B)^{-1}\mathbf B^\top\mathbf x_n=\mathbf B\mathbf B^\top\mathbf x_n$ (orthonormal $\mathbf B$, Eq. 10.34) is exactly the orthogonal projection of $\mathbf x_n$ onto the [[PrincipalSubspace|principal subspace]], with the projection coordinates $z_{in}=\mathbf b_i^\top\mathbf x_n$ (Eq. 10.32) as the code. The displacement vector $\mathbf x_n-\tilde{\mathbf x}_n=\bigl(\sum_{j=M+1}^D\mathbf b_j\mathbf b_j^\top\bigr)\mathbf x_n$ (Eq. 10.38) is itself a projection — onto the [[OrthogonalComplement|orthogonal complement]] $U^\perp$ — so it carries the discarded variance $\sum_{j=M+1}^D\lambda_j$. The book states the punchline: *"the optimal linear projection $\tilde{\mathbf x}_n$ of $\mathbf x_n$ is an orthogonal projection."* The same $\mathbf B\mathbf B^\top$ projection matrix (symmetric, idempotent, rank $M$) is the best rank-$M$ approximation of $\mathbf I$ ([[LowRankApproximation]], Eq. 10.40).

## From [[mml-ch03-analytic-geometry|MML Ch 3]]

§3.8 is the chapter's payload. A [[ProjectionMatrix|projection]] (Def. 3.10) is an idempotent linear map $\pi:V\to U$ ($\pi^2=\pi$); its matrix satisfies $\mathbf{P}_\pi^2=\mathbf{P}_\pi$, and orthogonal-projection matrices are also symmetric (margin, p. 84: *"Projection matrices are always symmetric."*). The chapter derives the projection in a **three-step recipe** (find the coordinate(s) $\lambda$, the projection point $\pi_U(\mathbf{x})$, and the matrix $\mathbf{P}_\pi$):

**Onto a line** spanned by $\mathbf{b}$ (§3.8.1): the orthogonality condition $\langle\mathbf{x}-\pi_U(\mathbf{x}),\mathbf{b}\rangle=0$ with $\pi_U(\mathbf{x})=\lambda\mathbf{b}$ gives $\lambda=\frac{\langle\mathbf{x},\mathbf{b}\rangle}{\|\mathbf{b}\|^2}=\frac{\mathbf{b}^\top\mathbf{x}}{\|\mathbf{b}\|^2}$ (Eqs. 3.40–3.41), so $\pi_U(\mathbf{x})=\frac{\mathbf{b}^\top\mathbf{x}}{\|\mathbf{b}\|^2}\mathbf{b}$ (Eq. 3.42) and $\mathbf{P}_\pi=\frac{\mathbf{b}\mathbf{b}^\top}{\|\mathbf{b}\|^2}$ (Eq. 3.46, symmetric rank 1). The projected length is $\|\pi_U(\mathbf{x})\|=|\cos\omega|\,\|\mathbf{x}\|$ (Eq. 3.44) — recovering the trig picture.

**Onto a general subspace** with basis $\mathbf{B}=[\mathbf{b}_1,\ldots,\mathbf{b}_m]\in\mathbb{R}^{n\times m}$ (§3.8.2): requiring the residual orthogonal to all basis vectors gives the **normal equation** $\mathbf{B}^\top\mathbf{B}\boldsymbol\lambda=\mathbf{B}^\top\mathbf{x}$ (Eq. 3.56), so $\boldsymbol\lambda=(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top\mathbf{x}$ (the **pseudo-inverse** of $\mathbf{B}$), $\pi_U(\mathbf{x})=\mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top\mathbf{x}$ (Eq. 3.58), and $\mathbf{P}_\pi=\mathbf{B}(\mathbf{B}^\top\mathbf{B})^{-1}\mathbf{B}^\top$ (Eq. 3.59). The **projection / reconstruction error** is $\|\mathbf{x}-\pi_U(\mathbf{x})\|$ (Eq. 3.63). In practice a *jitter* $\epsilon\mathbf{I}$ is added to $\mathbf{B}^\top\mathbf{B}$ for stability — the "ridge," derivable via Bayesian inference (p. 86). With an [[OrthonormalBasis|ONB]] ($\mathbf{B}^\top\mathbf{B}=\mathbf{I}$), projection collapses to $\mathbf{B}\mathbf{B}^\top\mathbf{x}$ — no inverse (Eqs. 3.65–3.66).

**Onto an affine subspace** $L=\mathbf{x}_0+U$ (§3.8.4): subtract the support point, project onto the direction space, translate back: $\pi_L(\mathbf{x})=\mathbf{x}_0+\pi_U(\mathbf{x}-\mathbf{x}_0)$ (Eq. 3.72). Distance: $d(\mathbf{x},L)=d(\mathbf{x}-\mathbf{x}_0,U)$ (Eq. 3.73) — used to derive the [[SeparatingHyperplane|separating hyperplane]] (Ch 12.1).

Projection-and-subtract iterated over a basis *is* [[GramSchmidt|Gram-Schmidt orthogonalization]] (§3.8.3).

## Connections

- [[mml-ch03-analytic-geometry]] / [[mml-book]] — §3.8 canonical reference (Def. 3.10).
- [[ProjectionMatrix]] — the matrix $\mathbf{P}_\pi$ (idempotent, symmetric) implementing the projection.
- [[InnerProduct]] / [[Orthogonality]] — the structure projection needs.
- [[OrthonormalBasis]] — collapses the projection to $\mathbf{B}\mathbf{B}^\top$.
- [[GramSchmidt]] — iterated orthogonal projection.
- [[OrthogonalComplement]] — the projection error lives here.
- [[AffineSubspace]] — projection onto offset spaces (§3.8.4).
- [[LinearRegression]] — projection interpretation of MLE / normal equations.
- [[PrincipalComponentAnalysis]] — projection to principal subspace.
- [[mml-ch10-dimensionality-reduction-pca|MML Ch 10]] / [[PrincipalSubspace]] / [[ReconstructionError]] — §10.3 PCA-as-projection.
- [[SupportVectorMachine]] — margin via projection.
