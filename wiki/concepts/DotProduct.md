---
title: "Dot Product"
type: concept
tags: [math, linear-algebra, foundational]
sources: [mml-ch03-analytic-geometry, mml-book, d2l-preliminaries]
last_updated: 2026-06-04
---

# Dot Product

The sum of element-wise products of two vectors of the same dimension:

$$\mathbf{x}^\top\mathbf{y} = \langle\mathbf{x},\mathbf{y}\rangle = \sum_{i=1}^d x_i y_i.$$

A measure of alignment. Equivalent definitions ([[d2l-preliminaries]] §Dot Products):

- Sum of element-wise products: `(x * y).sum()`.
- Direct call: `torch.dot(x, y)` / `np.dot(x, y)` / `jnp.dot(x, y)` / `tf.tensordot(x, y, axes=1)`.

## Geometric interpretations

- **Weighted sum**: given values $\mathbf{x}$ and weights $\mathbf{w}$, $\mathbf{x}^\top\mathbf{w}$ is the weighted sum. When weights are nonnegative and sum to 1, it's a weighted average.
- **Cosine of the angle**: after normalizing both vectors to unit length, $\mathbf{x}^\top\mathbf{y} = \cos\omega$. This is *cosine similarity*.
- **Inner product induces a norm**: $\|\mathbf{x}\| = \sqrt{\mathbf{x}^\top\mathbf{x}}$ (the $\ell_2$ [[Norm|norm]]).

## ML uses

- **[[ScaledDotProductAttention|Scaled dot-product attention]]**: $\mathrm{softmax}(\mathbf{Q}\mathbf{K}^\top / \sqrt{d_k})\mathbf{V}$ — the heart of the [[Transformer]].
- **Embedding similarity** (sentence / image / user embeddings).
- **Linear regression prediction**: $\hat y = \mathbf{w}^\top\mathbf{x}$.
- **Matrix–vector / matrix–matrix multiplication** are stacked dot products.

## From [[mml-ch03-analytic-geometry|MML Ch 3]]

[[mml-book]] §3.2.1 (Eq. 3.5) calls $\mathbf{x}^\top\mathbf{y}=\sum_{i=1}^n x_iy_i$ the **scalar product / dot product** and treats it as the *particular* [[InnerProduct]] used by default throughout the book — the one that makes $(\mathbb{R}^n,\langle\cdot,\cdot\rangle)$ a *Euclidean vector space*. It induces the **Euclidean / $\ell_2$ [[Norm]]** $\|\mathbf{x}\|_2=\sqrt{\mathbf{x}^\top\mathbf{x}}$ (Eq. 3.4), the **Euclidean [[Metric|distance]]** $d(\mathbf{x},\mathbf{y})=\|\mathbf{x}-\mathbf{y}\|$, and (via [[CauchySchwarzInequality|Cauchy-Schwarz]]) the standard [[Angle]] $\cos\omega=\frac{\mathbf{x}^\top\mathbf{y}}{\|\mathbf{x}\|\|\mathbf{y}\|}$.

**Important caveat the book stresses**: the dot product is only *one* inner product. Other [[SymmetricPositiveDefiniteMatrix|SPD]]-matrix inner products $\langle\mathbf{x},\mathbf{y}\rangle=\hat{\mathbf{x}}^\top\mathbf{A}\hat{\mathbf{y}}$ give different lengths, angles, and orthogonality for the same vectors (Examples 3.5, 3.7). So "the angle/length/orthogonality" of two vectors is implicitly *w.r.t. the dot product* unless another inner product is named.

## Connections

- [[mml-ch03-analytic-geometry]] / [[mml-book]] — §3.2.1 (Eq. 3.5); the default inner product.
- [[d2l-preliminaries]] — §Dot Products canonical exposition.
- [[InnerProduct]] — general formulation (any SPD matrix defines one).
- [[Norm]] — $\ell_2$ norm induced by the dot product.
- [[Angle]] / [[Metric]] / [[Orthogonality]] — geometry induced by the dot product.
- [[LinearAlgebra]] — parent topic.
- [[CauchySchwarzInequality]] — $|\mathbf{x}^\top\mathbf{y}|\leq\|\mathbf{x}\|\|\mathbf{y}\|$.
