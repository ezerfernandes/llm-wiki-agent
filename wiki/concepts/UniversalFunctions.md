---
title: "Universal Functions (ufuncs)"
type: concept
tags: [numpy, vectorization]
sources: [pydata-numpy-basics, pydata-advanced-numpy]
last_updated: 2026-05-15
---

# Universal Functions (ufuncs)

Element-wise functions in [[NumPy]] that operate on entire [[NDArray|ndarrays]] in a single C loop. Unary (`np.sqrt`, `np.exp`, `np.log`, `np.abs`, `np.isnan`, `np.negative`); binary (`np.add`, `np.multiply`, `np.maximum`, `np.power`); both support [[Broadcasting]].

## Methods on a ufunc
- `np.add.reduce(arr, axis=)` — like `arr.sum(axis=)` (equivalent to `np.sum`).
- `np.add.accumulate(arr)` — cumulative sum.
- `np.multiply.outer(a, b)` — outer product (any binary op generalizes).
- `np.add.reduceat(arr, indices)` — segmented reduce.

## Custom ufuncs
- `np.frompyfunc(func, nin, nout)` — wrap any Python function; slow (loop in Python).
- `@numba.vectorize` ([[Numba]]) — compile a Python function to a fast custom ufunc.

## Connections
- [[NumPy]] / [[NDArray]] — the data they operate on.
- [[Broadcasting]] — the shape-alignment rule for binary ufuncs.
- [[Numba]] — fastest path for writing custom ufuncs.
