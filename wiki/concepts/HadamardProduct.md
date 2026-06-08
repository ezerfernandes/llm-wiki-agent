---
title: "Hadamard Product"
type: concept
tags: [linear-algebra, vector-calculus]
sources: [matrix-calculus-for-deep-learning]
last_updated: 2026-06-04
---

# Hadamard Product

The **element-wise** product of two vectors (or matrices) of the same shape, written $\mathbf{w}\odot\mathbf{x}$, with $(\mathbf{w}\odot\mathbf{x})_i = w_i x_i$. Distinct from the [[MatrixMultiplication|matrix/dot product]].

## Why it matters for gradients

Per [[matrix-calculus-for-deep-learning]], element-wise binary operators that satisfy the **element-wise diagonal condition** — each output element depends only on the correspondingly-indexed input element — have **diagonal [[Jacobian|Jacobians]]**. For $\mathbf{w}\odot\mathbf{x}$, $\partial(\mathbf{w}\odot\mathbf{x})/\partial\mathbf{w} = \operatorname{diag}(\mathbf{x})$. The same logic gives $\partial(\mathbf{w}+\mathbf{x})/\partial\mathbf{w} = \mathbf{I}$. Recognizing this collapses many vector-chain-rule products from full matrix multiplies to cheap diagonal scalings.

## Connections

- [[Jacobian]] — element-wise ops yield diagonal Jacobians.
- [[ChainRule]] — the vector chain rule simplifies to $\operatorname{diag}(\partial f_i/\partial g_i)\cdot(\partial\mathbf{g}/\partial\mathbf{x})$ for element-wise inner functions.
- [[MatrixMultiplication]] — contrast: Hadamard is element-wise, not row-times-column.
- [[matrix-calculus-for-deep-learning]] — source.
