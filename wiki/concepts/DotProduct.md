---
title: "Dot Product"
type: concept
tags: [math, linear-algebra, foundational]
sources: [d2l-preliminaries]
last_updated: 2026-05-16
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

## Connections

- [[d2l-preliminaries]] — §Dot Products canonical exposition.
- [[InnerProduct]] — general formulation (any SPD matrix defines one).
- [[Norm]] — $\ell_2$ norm induced by the dot product.
- [[LinearAlgebra]] — parent topic.
- [[CauchySchwarzInequality]] — $|\mathbf{x}^\top\mathbf{y}|\leq\|\mathbf{x}\|\|\mathbf{y}\|$.
