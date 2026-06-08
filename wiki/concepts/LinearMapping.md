---
title: "Linear Mapping"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-book, mml-ch02-linear-algebra]
last_updated: 2026-06-04
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

## From [[mml-ch02-linear-algebra|MML Ch 2]]

**Definition 2.15** (§2.7): $\Phi:V\to W$ is a linear mapping (a.k.a. *vector space homomorphism* / *linear transformation*) iff $\Phi(\lambda\mathbf{x}+\psi\mathbf{y})=\lambda\Phi(\mathbf{x})+\psi\Phi(\mathbf{y})$ for all $\mathbf{x},\mathbf{y}\in V$, $\lambda,\psi\in\mathbb{R}$ (the single combined form of the two preservation axioms above).

**Special mappings** (Def 2.16, p. 49): *isomorphism* (linear & bijective $V\to W$); *endomorphism* (linear $V\to V$); *automorphism* (linear & bijective $V\to V$); the identity $\operatorname{id}_V$. Compositions, sums, and scalar multiples of linear maps are linear; an isomorphism's inverse is an isomorphism.

**Theorem 2.17** (= Axler 2015, Thm 3.59): finite-dimensional $V,W$ are isomorphic **iff** $\dim(V)=\dim(W)$. Hence every $n$-dimensional space is isomorphic to $\mathbb{R}^n$ — the justification for the book working entirely in $\mathbb{R}^n$, and for treating $\mathbb{R}^{m\times n}\cong\mathbb{R}^{mn}$.

**Representation** is via a [[TransformationMatrix|transformation matrix]] $\mathbf{A}_\Phi$ once ordered [[Basis|bases]] are chosen (Def 2.19): column $j$ of $\mathbf{A}_\Phi$ is the [[Coordinates|coordinate vector]] of $\Phi(\mathbf{b}_j)$ in the codomain basis, and $\hat{\mathbf{y}}=\mathbf{A}_\Phi\hat{\mathbf{x}}$. Changing bases gives $\tilde{\mathbf{A}}_\Phi=\mathbf{T}^{-1}\mathbf{A}_\Phi\mathbf{S}$ ([[BasisChange]], Thm 2.20). The mapping's [[NullSpace|kernel]] and [[Image|image]] are subspaces tied by the [[RankNullityTheorem|rank–nullity theorem]] $\dim(\ker\Phi)+\dim(\operatorname{Im}\Phi)=\dim(V)$ (Thm 2.24).

## Connections

- [[mml-book]] / [[mml-ch02-linear-algebra|MML Ch 2]] — §2.7 canonical reference.
- [[TransformationMatrix]] / [[BasisChange]] / [[Coordinates]] — matrix representation and its basis-dependence.
- [[Image]] / [[NullSpace]] / [[RankNullityTheorem]] — image, kernel, and their dimensions.
- [[AffineMapping]] — the affine generalization $\mathbf{x}\mapsto\mathbf{a}+\Phi(\mathbf{x})$.
- [[VectorSpace]] — domain and codomain.
- [[Determinant]] — basis-invariant of the mapping.
- [[Trace]] — basis-invariant of the mapping.
- [[Rank]] — dimension of the image.
- [[AffineSpace]] — affine generalization (translation + linear).
