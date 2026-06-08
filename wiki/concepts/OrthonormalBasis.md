---
title: "Orthonormal Basis"
type: concept
tags: [analytic-geometry, linear-algebra, foundational]
sources: [mml-ch03-analytic-geometry, mml-book]
last_updated: 2026-06-04
---

# Orthonormal Basis (ONB)

An **orthonormal basis** of an $n$-dimensional inner-product space $V$ is a [[Basis]] $\{\mathbf{b}_1,\ldots,\mathbf{b}_n\}$ whose vectors are mutually orthogonal *and* each of unit length ([[mml-ch03-analytic-geometry|MML Ch 3]] Def. 3.9, §3.5):

$$\langle\mathbf{b}_i,\mathbf{b}_j\rangle = 0 \;\text{ for } i\neq j, \qquad \langle\mathbf{b}_i,\mathbf{b}_i\rangle = 1.$$

If only the first condition holds (orthogonal but not unit length) it is an **orthogonal basis**; the second condition says every basis vector has norm 1.

> This page resolves the forward-reference left by [[mml-ch02-linear-algebra|MML Ch 2]], where [[Basis]] / [[Dimension]] were defined but the *orthonormal* special case was deferred to Ch 3.

## Examples

- The **canonical / standard basis** $\{\mathbf{e}_1,\ldots,\mathbf{e}_n\}$ of Euclidean $\mathbb{R}^n$ is an ONB under the dot product ([[mml-book]] Example 3.8).
- In $\mathbb{R}^2$, $\mathbf{b}_1=\tfrac{1}{\sqrt2}[1,1]^\top$, $\mathbf{b}_2=\tfrac{1}{\sqrt2}[1,-1]^\top$ form an ONB ($\mathbf{b}_1^\top\mathbf{b}_2=0$, $\|\mathbf{b}_1\|=\|\mathbf{b}_2\|=1$) — a $45°$-rotated standard basis (Eq. 3.35).

## Construction

Apply the **[[GramSchmidt|Gram-Schmidt process]]** to any basis to produce an orthogonal basis, then normalize to get an ONB. Equivalently ([[mml-book]] p. 79), concatenate the (non-orthogonal, unnormalized) vectors into $\tilde{\mathbf{B}}$ and run Gaussian elimination on the augmented matrix $[\tilde{\mathbf{B}}\tilde{\mathbf{B}}^\top\,|\,\tilde{\mathbf{B}}]$.

## Why an ONB is convenient

- **Coordinates are inner products**: for an ONB, the coordinate of $\mathbf{x}$ along $\mathbf{b}_i$ is just $\langle\mathbf{x},\mathbf{b}_i\rangle$ — no linear system to solve.
- **[[OrthogonalProjection|Projection]] simplifies**: with an ONB matrix $\mathbf{B}$, $\mathbf{B}^\top\mathbf{B}=\mathbf{I}$, so $\pi_U(\mathbf{x})=\mathbf{B}\mathbf{B}^\top\mathbf{x}$ — **no matrix inverse** ([[mml-book]] Eqs. 3.65–3.66).
- An ONB matrix is an [[OrthogonalMatrix]] ($\mathbf{B}^{-1}=\mathbf{B}^\top$).

## ML uses

- **PCA** (Ch 10) works in the orthonormal eigenbasis of the [[DataCovarianceMatrix]].
- **SVM** (Ch 12) and many numerical algorithms exploit ONBs ([[mml-book]] §3.5).
- **Fourier / wavelet bases** are orthonormal function bases (cf. [[InnerProductOfFunctions]]).

## Connections

- [[mml-ch03-analytic-geometry]] — §3.5 canonical reference (Def. 3.9).
- [[Basis]] / [[Dimension]] — the Ch 2 base concept this specializes.
- [[Orthogonality]] — the property the basis vectors satisfy.
- [[GramSchmidt]] — constructs an ONB from any basis.
- [[OrthogonalMatrix]] — a matrix whose columns are an ONB.
- [[OrthogonalProjection]] — projection collapses to $\mathbf{B}\mathbf{B}^\top$ under an ONB.
- [[InnerProductOfFunctions]] — orthonormal function bases (Fourier).
