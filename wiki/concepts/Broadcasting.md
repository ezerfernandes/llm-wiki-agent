---
title: "Broadcasting"
type: concept
tags: [numpy, arrays, vectorization]
sources: [pydata-numpy-basics, pydata-advanced-numpy, d2l-preliminaries]
last_updated: 2026-05-16
---

# Broadcasting

NumPy's rule for performing element-wise operations on arrays of different shapes without explicit replication. Trailing dimensions are compared; sizes must be equal or one of them 1 (axis is then "stretched" to match). Saves memory and avoids Python-level loops.

## Rules
1. Pad the shorter shape with leading length-1 axes.
2. For each axis, the sizes must match or one must be 1.
3. Broadcasted axes are read-only — the stretched values are not actually copied.

## Examples
- `arr + scalar` — scalar broadcasts to the array's shape.
- `(N, 1)` + `(N, M)` → `(N, M)` — adds a column vector to each column of a matrix.
- `(N, M)` − `(M,)` → `(N, M)` — subtracts a row vector from each row.
- To broadcast along *non-trailing* axes, insert a new axis: `arr - col_means[:, np.newaxis]`.

## Connections
- [[NumPy]] / [[NDArray]] — defines.
- [[UniversalFunctions]] — broadcasting applies to ufunc binary operations.
- [[pydata-advanced-numpy]] — Appendix A covers fully.
