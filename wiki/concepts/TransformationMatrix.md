---
title: "Transformation Matrix"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Transformation Matrix

**Definition 2.19** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.7.1): given a [[LinearMapping|linear mapping]] $\Phi:V\to W$ and ordered [[Basis|bases]] $B=(\mathbf{b}_1,\ldots,\mathbf{b}_n)$ of $V$ and $C=(\mathbf{c}_1,\ldots,\mathbf{c}_m)$ of $W$, write each image of a basis vector in the basis $C$:

$$\Phi(\mathbf{b}_j)=\sum_{i=1}^m\alpha_{ij}\mathbf{c}_i,\qquad j=1,\ldots,n.$$

The $m\times n$ matrix $\mathbf{A}_\Phi$ with $A_\Phi(i,j)=\alpha_{ij}$ is the *transformation matrix* of $\Phi$ (w.r.t. bases $B$ and $C$). Its **$j$-th column is the coordinate vector of $\Phi(\mathbf{b}_j)$ w.r.t. $C$**.

## It acts on coordinate vectors

If $\hat{\mathbf{x}}$ is the [[Coordinates|coordinate vector]] of $\mathbf{x}\in V$ w.r.t. $B$ and $\hat{\mathbf{y}}$ that of $\mathbf{y}=\Phi(\mathbf{x})\in W$ w.r.t. $C$, then ([[mml-ch02-linear-algebra|MML Ch 2]] Eq. 2.94):

$$\hat{\mathbf{y}}=\mathbf{A}_\Phi\hat{\mathbf{x}}.$$

So the transformation matrix maps coordinates in $V$ to coordinates in $W$. A matrix can stand for *a linear mapping* or *a collection of vectors* — one must always track which.

## Basis-dependence

The **same** linear mapping has **different** transformation matrices under different bases; they are related by [[BasisChange|basis change]] $\tilde{\mathbf{A}}_\Phi=\mathbf{T}^{-1}\mathbf{A}_\Phi\mathbf{S}$ (Thm 2.20). Choosing a good basis can make $\mathbf{A}_\Phi$ diagonal (Example 2.23). Geometric examples (Example 2.22, Fig. 2.10): rotation $\mathbf{A}_1=\begin{bmatrix}\cos\frac\pi4&-\sin\frac\pi4\\\sin\frac\pi4&\cos\frac\pi4\end{bmatrix}$, stretch $\mathbf{A}_2=\begin{bmatrix}2&0\\0&1\end{bmatrix}$, and a combined reflection/rotation/stretch.

Composition of mappings = product of matrices: $\mathbf{A}_{\Psi\circ\Phi}=\mathbf{A}_\Psi\mathbf{A}_\Phi$.

## Connections

- [[LinearMapping]] — what a transformation matrix represents.
- [[Coordinates]] / [[Basis]] — the inputs and outputs are coordinate vectors.
- [[BasisChange]] — how the matrix changes with the basis.
- [[Matrix]] / [[MatrixMultiplication]] — the underlying object and the composition rule.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.7.1 canonical reference.
