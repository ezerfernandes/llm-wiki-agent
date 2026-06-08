---
title: "Eigenspace"
type: concept
tags: [linear-algebra, eigenvalue, matrix-decomposition]
sources: [mml-ch04-matrix-decompositions, mml-book]
last_updated: 2026-06-04
---

# Eigenspace

For a square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ and an eigenvalue $\lambda$, the **eigenspace** $E_\lambda$ is the set of *all* eigenvectors of $\mathbf{A}$ associated with $\lambda$ — a subspace of $\mathbb{R}^n$ ([[mml-book]] Def. 4.10, §4.2). It is the **solution space of the homogeneous system** $(\mathbf{A}-\lambda\mathbf{I})\mathbf{x}=\mathbf{0}$, equivalently the kernel:

$$E_\lambda = \ker(\mathbf{A}-\lambda\mathbf{I})$$

(Eqs. 4.27a–4.27b), since $\mathbf{A}\mathbf{x}=\lambda\mathbf{x}\iff(\mathbf{A}-\lambda\mathbf{I})\mathbf{x}=\mathbf{0}$. Because every nonzero multiple of an eigenvector is also an eigenvector (Eq. 4.26), $E_\lambda$ is closed under scaling and addition.

## Eigenspectrum / spectrum

The set of *all* eigenvalues of $\mathbf{A}$ is the **eigenspectrum**, or just the **spectrum**, of $\mathbf{A}$ ([[mml-book]] Def. 4.10).

## Geometric meaning

An eigenvector for a nonzero eigenvalue points in a direction **stretched** by the linear mapping; the eigenvalue is the stretch factor (negative ⇒ direction flipped). The eigenspace $E_\lambda$ is the entire subspace of directions stretched by the same factor $\lambda$.

## Dimension = geometric multiplicity

$\dim(E_{\lambda_i})$ is exactly the [[Eigenvalue|geometric multiplicity]] of $\lambda_i$ ([[mml-book]] Def. 4.11): the number of linearly independent eigenvectors for $\lambda_i$. It is always $\geq 1$ and never exceeds the algebraic multiplicity. When it is *strictly less*, the matrix is [[DefectiveMatrix|defective]].

- **Example 4.5** ([[mml-book]] §4.2): $\mathbf{A}=\begin{bmatrix}4&2\\1&3\end{bmatrix}$ has $E_5=\operatorname{span}[[2,1]^\top]$ and $E_2=\operatorname{span}[[1,-1]^\top]$, both 1-D.
- **Example 4.8** ([[mml-book]] §4.2): the symmetric $\begin{bmatrix}3&2&2\\2&3&2\\2&2&3\end{bmatrix}$ has a 2-D eigenspace $E_1=\operatorname{span}[[-1,1,0]^\top,[-1,0,1]^\top]$ for the repeated $\lambda=1$, and 1-D $E_7=\operatorname{span}[[1,1,1]^\top]$.
- **Identity matrix** (Example 4.4): $E_1$ spans all $n$ dimensions.

## Connections

- [[mml-ch04-matrix-decompositions|MML Ch 4]] — §4.2 canonical reference (Def. 4.10).
- [[Eigenvalue]] / [[Eigenvector]] — the scalar and the vectors that span the eigenspace.
- [[CharacteristicPolynomial]] — its roots are the eigenvalues whose eigenspaces these are.
- [[DefectiveMatrix]] — arises when $\dim(E_\lambda)$ < algebraic multiplicity.
- [[SpectralTheorem]] — for symmetric matrices the eigenspaces admit an orthonormal basis.
- [[NullSpace]] — $E_\lambda=\ker(\mathbf{A}-\lambda\mathbf{I})$.
</content>
