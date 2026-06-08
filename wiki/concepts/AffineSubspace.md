---
title: "Affine Subspace"
type: concept
tags: [linear-algebra, geometry, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Affine Subspace

**Definition 2.25** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.8.1): let $V$ be a [[VectorSpace|vector space]], $\mathbf{x}_0\in V$, and $U\subseteq V$ a [[VectorSubspace|subspace]]. Then

$$L=\mathbf{x}_0+U:=\{\mathbf{x}_0+\mathbf{u}:\mathbf{u}\in U\}\subseteq V$$

is an *affine subspace* (or *linear manifold*) of $V$. $U$ is the *direction / direction space* and $\mathbf{x}_0$ the *support point*.

Because $L$ **excludes $\mathbf{0}$ whenever $\mathbf{x}_0\notin U$**, an affine subspace is **not** a vector subspace. Examples: points, lines, and planes in $\mathbb{R}^3$ that need not pass through the origin.

## Parametric equation

With an ordered basis $(\mathbf{b}_1,\ldots,\mathbf{b}_k)$ of $U$, every $\mathbf{x}\in L$ is uniquely (MML Eq. 2.131):

$$\mathbf{x}=\mathbf{x}_0+\lambda_1\mathbf{b}_1+\cdots+\lambda_k\mathbf{b}_k,$$

with *directional vectors* $\mathbf{b}_i$ and *parameters* $\lambda_i$.

## Dimension hierarchy (Example 2.26, Fig. 2.13)

| Dimension | Name | Parametric form |
|---|---|---|
| 1 | **line** | $\mathbf{y}=\mathbf{x}_0+\lambda\mathbf{b}_1$ |
| 2 | **plane** | $\mathbf{y}=\mathbf{x}_0+\lambda_1\mathbf{b}_1+\lambda_2\mathbf{b}_2$ |
| $n-1$ | **[[Hyperplane|hyperplane]]** | $\mathbf{y}=\mathbf{x}_0+\sum_{i=1}^{n-1}\lambda_i\mathbf{b}_i$ |

In $\mathbb{R}^2$ a line is a hyperplane; in $\mathbb{R}^3$ a plane is a hyperplane.

## Inhomogeneous systems ↔ affine subspaces

(MML Remark, p. 62) The solution set of an **inhomogeneous** system $\mathbf{A}\boldsymbol\lambda=\mathbf{x}$ is either empty or an affine subspace of dimension $n-\operatorname{rk}(\mathbf{A})$. Conversely, every $k$-dimensional affine subspace of $\mathbb{R}^n$ is the solution set of some $\mathbf{A}\mathbf{x}=\mathbf{b}$ with $\operatorname{rk}(\mathbf{A})=n-k$. The homogeneous case $\mathbf{b}=\mathbf{0}$ recovers a [[VectorSubspace|subspace]] — a special affine space with $\mathbf{x}_0=\mathbf{0}$.

## Connections

- [[AffineSpace]] — the general notion this realizes.
- [[VectorSubspace]] — the direction space $U$; the $\mathbf{x}_0=\mathbf{0}$ special case.
- [[Hyperplane]] — the codimension-1 case.
- [[SystemOfLinearEquations]] — inhomogeneous solution sets are affine subspaces.
- [[Rank]] — controls the affine subspace's dimension.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.8.1 canonical reference.
