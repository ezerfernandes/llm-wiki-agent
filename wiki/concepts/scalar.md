---
title: "scalar"
type: concept
tags: [math, linear-algebra, foundational]
sources: [d2l-preliminaries, mml-book]
last_updated: 2026-05-16
---

# scalar

A single real-valued number — a 0th-order [[Tensor]]. Denoted by ordinary lowercase italic letters ($x$, $y$, $z$); the space of all real-valued scalars is $\mathbb{R}$ ([[d2l-preliminaries]] §Scalars).

In framework code, scalars are represented as tensors containing exactly one element: `torch.tensor(3.0)` / `np.array(3.0)` / `tf.constant(3.0)` / `jnp.array(3.0)`. Standard arithmetic (`+`, `-`, `*`, `/`, `**`) applies elementwise; on size-1 tensors this reduces to scalar arithmetic.

## Position in the tensor hierarchy

| Object | Order | Notation | Code |
|---|---|---|---|
| **Scalar** | 0 | $x \in \mathbb{R}$ | `torch.tensor(3.0)` |
| Vector | 1 | $\mathbf{x} \in \mathbb{R}^n$ | `torch.arange(n)` |
| Matrix | 2 | $\mathbf{X} \in \mathbb{R}^{m\times n}$ | `torch.arange(mn).reshape(m,n)` |
| Tensor | $k>2$ | $\mathsf{X}$ | `torch.arange(N).reshape(...)` |

## Connections

- [[d2l-preliminaries]] — §Scalars canonical exposition.
- [[Tensor]] — the generalization.
- [[LinearAlgebra]] / [[VectorSpace]] — algebraic context.
- [[d2l-notation]] — symbol conventions.
