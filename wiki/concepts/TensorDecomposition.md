---
title: "Tensor Decomposition"
type: concept
tags: [model-compression, linear-algebra, low-rank, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Tensor Decomposition

**Extending [[LowRankFactorization|low-rank matrix factorization]] to multi-dimensional tensors — the 4D weight tensors of convolutional layers, attention mechanisms, and embedding tables — by expressing them as products/sums of smaller factor tensors.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], a structured-approximation compression technique that exploits mathematical redundancy directly rather than removing parameters.

## Methods

- **CP decomposition** — sum of rank-one components: $\mathcal{A} \approx \sum_{r=1}^{k} u_r \otimes v_r \otimes w_r$.
- **Tucker decomposition** — a core tensor with factor matrices: $\mathcal{A} \approx \mathcal{G} \times_1 U \times_2 V \times_3 W$.
- **Tensor-Train (TT)** — a sequence of lower-rank matrices, effective for very high-dimensional tensors.

## Trade-offs

Mirrors LRMF: compression vs information loss, plus the inference overhead of tensor contractions. Higher compression potential than LRMF but more complex storage and iterative rank selection. In practice, fully connected layers use LRMF while conv kernels use tensor decomposition.

## Connections

- [[LowRankFactorization]] — the 2D matrix special case.
- [[SingularValueDecomposition]] — the matrix-factorization workhorse.
- [[ModelCompression]] — a structural-optimization technique.
- [[mlsysbook-ch10-model-compression]] — source.
