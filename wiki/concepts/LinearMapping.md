---
title: "Linear Mapping"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-book]
last_updated: 2026-05-16
---

# Linear Mapping

A function $\Phi:V\to W$ between vector spaces that preserves vector-space structure ([[mml-book]] §2.7):

$$\Phi(\mathbf{x}+\mathbf{y}) = \Phi(\mathbf{x})+\Phi(\mathbf{y}), \quad \Phi(\lambda\mathbf{x}) = \lambda\Phi(\mathbf{x}).$$

Also called a *linear transformation* or *linear map*.

## Equivalent characterizations

| Property | Algebraic | Geometric |
|---|---|---|
| **Injective** (kernel = 0) | $\Phi(\mathbf{x})=\mathbf{0}\implies\mathbf{x}=\mathbf{0}$ | Distinct inputs go to distinct outputs |
| **Surjective** (image = $W$) | Every $\mathbf{w}\in W$ is $\Phi(\mathbf{x})$ for some $\mathbf{x}$ | $\Phi$ covers the whole codomain |
| **Bijective / isomorphism** | Both | $V\cong W$ (essentially the same space) |

## Matrices represent linear mappings (in chosen bases)

Once we choose bases $B$ for $V$ and $C$ for $W$, a linear mapping $\Phi:V\to W$ is *uniquely* represented by a matrix $\mathbf{A}_\Phi\in\mathbb{R}^{m\times n}$ — the $j$-th column of $\mathbf{A}_\Phi$ is the coordinate vector of $\Phi(\mathbf{b}_j)$ in basis $C$.

**Crucially**: the *same* linear mapping has *different* matrix representations under different bases. The matrices are related by basis-change formulas $\tilde{\mathbf{A}}_\Phi = \mathbf{T}^{-1}\mathbf{A}_\Phi\mathbf{S}$ ([[mml-book]] §2.7.2).

The properties **invariant under basis change** — [[Determinant]], [[Trace]], eigenvalues, rank — are intrinsic to the *mapping*; everything else is a notational artifact of the chosen basis.

## Why this matters for ML

- **Neural network layers** are (affine + nonlinearity) compositions. The linear part is a linear mapping; choice of weights = choice of which linear mapping.
- **PCA** ([[mml-book]] Ch 10) is a linear mapping from $\mathbb{R}^D$ to $\mathbb{R}^M$ (the encoder $\mathbf{B}^\top$) followed by its transpose (the decoder $\mathbf{B}$).
- **Embeddings** (Word2Vec, sentence-BERT) are linear mappings from a sparse index space to a dense continuous space.
- **Attention** in a Transformer is a sequence of linear mappings (Q, K, V projections) plus a softmax.

## Connections

- [[mml-book]] — §2.7 canonical reference.
- [[VectorSpace]] — domain and codomain.
- [[Determinant]] — basis-invariant of the mapping.
- [[Trace]] — basis-invariant of the mapping.
- [[Rank]] — dimension of the image.
- [[AffineSpace]] — affine generalization (translation + linear).
