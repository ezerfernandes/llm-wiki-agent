---
title: "Identity Matrix"
type: concept
tags: [linear-algebra, foundational, matrix-algebra]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Identity Matrix

**Definition 2.2** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.2.1, Eq. 2.17): in $\mathbb{R}^{n\times n}$, the *identity matrix* $\mathbf{I}_n$ has 1 on the main diagonal and 0 everywhere else.

It is the **neutral element** for [[MatrixMultiplication|matrix multiplication]]:

$$\mathbf{I}_m\mathbf{A}=\mathbf{A}\mathbf{I}_n=\mathbf{A}\quad\text{for }\mathbf{A}\in\mathbb{R}^{m\times n}\ \text{(Eq. 2.20)}.$$

Note that $\mathbf{I}_m\neq\mathbf{I}_n$ for $m\neq n$ — the identity is shape-specific.

## Roles

- Defines the [[MatrixInverse|inverse]]: $\mathbf{B}=\mathbf{A}^{-1}$ iff $\mathbf{A}\mathbf{B}=\mathbf{I}_n=\mathbf{B}\mathbf{A}$.
- Anchors the augmented-matrix inversion method $[\mathbf{A}\,|\,\mathbf{I}_n]\rightsquigarrow[\mathbf{I}_n\,|\,\mathbf{A}^{-1}]$ ([[GaussianElimination]]).
- Is the neutral element making $(\mathbb{R}^{n\times n},\cdot)$ on its invertible elements the [[GeneralLinearGroup|general linear group]].

## Connections

- [[MatrixMultiplication]] — $\mathbf{I}$ is the multiplicative neutral element.
- [[MatrixInverse]] — defined via $\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$.
- [[GeneralLinearGroup]] / [[GroupTheory]] — the identity is the group neutral element.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.2.1 canonical reference.
