---
title: "Einstein Summation"
type: concept
tags: [linear-algebra, tensor, foundational]
sources: [d2l-appendix-mathematics]
last_updated: 2026-05-16
---

# Einstein Summation (einsum)

A compact notation for tensor contractions: **repeated indices are implicitly summed over** ([[d2l-appendix-mathematics]] §geometry-linear-algebraic-ops). Eliminates explicit $\sum$ symbols while making the index structure of the operation visible.

For tensors $X_{ijkl}$ and $A_{jk}$ the expression

$$y_{il} = X_{ijkl}\,A_{jk}$$

implicitly sums over $j$ and $k$ (which appear twice), recovering the more verbose $y_{il}=\sum_{j,k} X_{ijkl}A_{jk}$.

## Common operations as one-liners

| Operation | Einstein notation |
|---|---|
| Dot product | $v_i w_i = \sum_i v_i w_i$ |
| Squared $\ell_2$ norm | $v_i v_i = \|\mathbf{v}\|_2^2$ |
| Matrix–vector product | $(\mathbf{A}\mathbf{v})_i = a_{ij}v_j$ |
| Matrix–matrix product | $(\mathbf{A}\mathbf{B})_{ik} = a_{ij}b_{jk}$ |
| Trace | $\text{tr}(\mathbf{A}) = a_{ii}$ |
| Outer product | $\mathbf{u}\otimes\mathbf{v} = u_i v_j$ |
| Frobenius inner product | $\langle\mathbf{A},\mathbf{B}\rangle_F = a_{ij}b_{ij}$ |
| Batched matmul | $C_{bik} = A_{bij}B_{bjk}$ |

## Framework implementations

All major DL frameworks expose Einstein summation:

```python
np.einsum("ij,j->i", A, v)            # NumPy
torch.einsum("ij,j->i", A, v)         # PyTorch
tf.einsum("ij,j->i", A, v)            # TensorFlow
jax.numpy.einsum("ij,j->i", A, v)     # JAX
```

The string `"ij,j->i"` specifies: two inputs with index patterns `ij` and `j`, output pattern `i` (so the `j` axis is summed). [[d2l-appendix-mathematics]] gives the general-form example

```python
torch.einsum("ijk,il,j->kl", B, A, v)   # c_{kl} = sum_{ij} B_{ijk} A_{il} v_j
```

## Why DL practitioners care

- **Batched / multi-head [[Attention]]**: $Q_{bhij}K_{bhik}\to S_{bhjk}$ is one einsum call instead of multiple reshape + transpose + matmul steps.
- **[[Transformer]] forward passes**: every QKV projection, head-merge, output-projection cleanly expressed as einsum strings.
- **Tensor parallelism**: einsum makes the contraction axes explicit, simplifying the bookkeeping for sharded matmuls across devices.
- **Readability and bug-prevention**: dimension mismatches surface as einsum string errors at parse time rather than as silent broadcast bugs.
- **[[FlashAttention]] / kernel fusion**: many fused-kernel libraries pattern-match on einsum expressions.

## History

Notation introduced by Albert Einstein in 1916 in his general-relativity papers to simplify tensor manipulations. Recovered for ML via NumPy's `einsum` (Travis Oliphant 2011) and propagated to every modern DL framework.

## Connections

- [[d2l-appendix-mathematics]] — §geometry-linear-algebraic-ops canonical reference.
- [[Tensor]] — what einsum operates on.
- [[InnerProduct]] / [[DotProduct]] — special cases.
- [[Attention]] / [[Transformer]] — modern primary use.
- [[LinearAlgebra]] — the underlying mathematics.
