---
title: "ndarray"
type: concept
tags: [numpy, datastructure]
sources: [pydata-numpy-basics, pydata-advanced-numpy, d2l-preliminaries]
last_updated: 2026-05-16
---

# ndarray

The N-dimensional homogeneous array at the heart of [[NumPy]]. Stores a single dtype's worth of values in a contiguous (or strided) memory block, indexed by an N-tuple `shape`. Every array carries `shape`, `dtype`, `ndim`, `size`, and `strides`. Operations are vectorized — `arr * 2` runs a single C loop, not a Python loop.

## Internals (Appendix A)
- Pointer to data block (in RAM or memory-mapped file).
- dtype describing the per-cell layout.
- Shape tuple.
- Strides tuple — bytes to step per axis, enabling zero-copy views (slicing, transpose, reverse).
- C-contiguous vs Fortran-contiguous; `arr.flags["C_CONTIGUOUS"]`.

## Operations
- Element-wise arithmetic + [[Broadcasting]].
- [[UniversalFunctions]] for unary/binary element-wise ops.
- Reductions (`sum`, `mean`, `argmax`, …) optionally along an axis.
- Indexing: basic slicing (view), boolean (`arr[mask]`, copy), fancy (integer arrays, copy).
- Reshape / concatenate / split / transpose.

## Connections
- [[NumPy]] — defines and operates on ndarrays.
- [[Broadcasting]] — implicit shape-aligning rule.
- [[UniversalFunctions]] — element-wise functions.
- [[pandas]] — `Series` / `DataFrame` columns are backed by ndarrays (or extension arrays).
