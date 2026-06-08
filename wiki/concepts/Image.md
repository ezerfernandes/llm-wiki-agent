---
title: "Image (of a Linear Mapping)"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Image (of a Linear Mapping)

> Disambiguation: this is the linear-algebra *image / range* of a mapping. For pixel/photo "image" topics see the `Image*` pages (e.g. [[ImageNet]], [[ImageEncoder]]).

**Definition 2.23** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.7.3): for a [[LinearMapping|linear mapping]] $\Phi:V\to W$, the *image / range* is

$$\operatorname{Im}(\Phi):=\Phi(V)=\{\mathbf{w}\in W\mid\exists\mathbf{v}\in V:\Phi(\mathbf{v})=\mathbf{w}\}.$$

It is the set of vectors in $W$ "reached" from $V$ by $\Phi$. $V$ is the *domain* and $W$ the *codomain*. $\operatorname{Im}(\Phi)\subseteq W$ is always a [[VectorSubspace|subspace]] of $W$.

## Image = column space

For $\Phi(\mathbf{x})=\mathbf{A}\mathbf{x}$ with $\mathbf{A}=[\mathbf{a}_1,\ldots,\mathbf{a}_n]$ ([[mml-ch02-linear-algebra|MML Ch 2]] Eqs. 2.124):

$$\operatorname{Im}(\Phi)=\{\mathbf{A}\mathbf{x}:\mathbf{x}\in\mathbb{R}^n\}=\operatorname{span}[\mathbf{a}_1,\ldots,\mathbf{a}_n]\subseteq\mathbb{R}^m,$$

i.e. the image is the **[[ColumnSpace|column space]]** — the span of the columns, a subspace of $\mathbb{R}^m$ (the "height" $m$ of the matrix). Its dimension is the [[Rank|rank]]: $\operatorname{rk}(\mathbf{A})=\dim(\operatorname{Im}(\Phi))$.

## Surjectivity and rank–nullity

$\Phi$ is **surjective** iff $\operatorname{Im}(\Phi)=W$. The dimension of the image is tied to that of the [[NullSpace|kernel]] by the [[RankNullityTheorem|rank–nullity theorem]]: $\dim(\ker(\Phi))+\dim(\operatorname{Im}(\Phi))=\dim(V)$.

## Connections

- [[NullSpace]] — the complementary subspace ($\ker$ in the domain).
- [[ColumnSpace]] — the image of $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$.
- [[Rank]] — $\dim(\operatorname{Im}(\Phi))=\operatorname{rk}(\mathbf{A})$.
- [[RankNullityTheorem]] — relates image and kernel dimensions.
- [[LinearMapping]] / [[Span]] / [[VectorSubspace]] — parent concepts.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.7.3 canonical reference.
