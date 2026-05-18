---
title: "Sparse Matrix"
type: concept
tags: [linear-algebra, parallel-computing, data-structures]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Sparse Matrix

A matrix in which most entries are zero. Storing and operating on a sparse matrix as if it were dense wastes memory and computation. Sparse matrices arise naturally in large-scale parallel applications: adjacency matrices of real-world graphs, finite-element models, and PDE discretizations.

## Categories

1. **Structured sparse:** Zeros occur at known positions (e.g., tridiagonal matrices — nonzeros only on the main diagonal and the two adjacent diagonals). Code can exploit the pattern directly without a general sparse format.

2. **Amorphous sparse:** Nonzero positions are unpredictable ("random"). Requires a general compressed representation.

## Compressed Sparse Row (CSR) Format

For an $m \times n$ matrix A with $k$ nonzero entries, CSR uses three arrays:

- **`avals[k]`** — the nonzero values, in row-major order.
- **`cols[k]`** — the column index of each element in `avals`.
- **`rowplaces[m+1]`** — `rowplaces[i]` is the index in `avals` of the first nonzero element of row $i$; the last element is $k$.

To find all nonzeros in row $i$: iterate `avals[rowplaces[i]]` through `avals[rowplaces[i+1] - 1]`, reading their column indices from `cols`.

## Parallel Considerations

Parallelizing sparse operations by assigning rows to threads is straightforward, but load balancing is a challenge since rows may have very different numbers of nonzeros. Standard techniques (dynamic scheduling, work-stealing) apply.

Libraries: CUSP (CUDA), CULA, and general sparse BLAS routines.

## Connections

- [[MatrixMultiplication]] — sparse-matrix multiply requires specialized algorithms.
- [[GaussianElimination]] — fill-in during elimination makes sparse direct solvers more complex.
- [[GraphConnectedness]] — adjacency matrices of real graphs are typically sparse.
- [[parproc-ch11-parallel-matrix-operations]] — §11.7 primary source.
