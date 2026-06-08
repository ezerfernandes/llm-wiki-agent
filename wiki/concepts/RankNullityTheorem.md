---
title: "Rank-Nullity Theorem"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Rank-Nullity Theorem

**Theorem 2.24** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.7.3, Eq. 2.129): for vector spaces $V,W$ and a [[LinearMapping|linear mapping]] $\Phi:V\to W$,

$$\dim(\ker(\Phi))+\dim(\operatorname{Im}(\Phi))=\dim(V).$$

Also called the *fundamental theorem of linear mappings* (Axler 2015, Thm 3.22). The two parts split $\dim(V)$: the **nullity** $\dim(\ker(\Phi))$ (the [[NullSpace|kernel]] dimension) plus the **rank** $\dim(\operatorname{Im}(\Phi))=\operatorname{rk}(\mathbf{A})$ (the [[Image|image]] / [[ColumnSpace|column space]] dimension).

## Direct consequences (MML p. 60)

- If $\dim(\operatorname{Im}(\Phi))<\dim(V)$, the kernel is **non-trivial**: $\dim(\ker(\Phi))\geq1$, so $\mathbf{A}_\Phi\mathbf{x}=\mathbf{0}$ has **infinitely many solutions**.
- If $\dim(V)=\dim(W)$, the three-way equivalence holds:

$$\Phi\text{ injective}\iff\Phi\text{ surjective}\iff\Phi\text{ bijective}.$$

This is why, for square matrices, "has trivial kernel," "is onto," and "is invertible" all coincide.

## Connections

- [[Rank]] — $\operatorname{rk}(\mathbf{A})=\dim(\operatorname{Im}(\Phi))$ is the "rank" half.
- [[NullSpace]] — $\dim(\ker(\Phi))$ is the "nullity" half.
- [[Image]] / [[ColumnSpace]] — the image side.
- [[Dimension]] / [[LinearMapping]] — the quantities related.
- [[MatrixInverse]] — square + trivial kernel ⇔ invertible.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.7.3 canonical reference.
