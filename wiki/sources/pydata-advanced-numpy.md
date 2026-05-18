---
title: "Python for Data Analysis 3E — Appendix A: Advanced NumPy"
type: source
tags: [book, numpy, ndarray, broadcasting, numba, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/advanced-numpy.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/advanced-numpy.html
chapter: A
---

## Summary
Internals and advanced features of [[NumPy]]: ndarray memory layout (data pointer + dtype + shape + strides), dtype hierarchy, reshape / concatenate / split / tile / repeat / take / put, [[Broadcasting]] (rules and broadcasting-over-other-axes), ufunc instance methods + custom ufuncs via [[Numba]], structured (record) arrays, advanced sorting (`argsort`, `lexsort`, partial sort via `partition`, `searchsorted`), `numpy.memmap` for memory-mapped arrays, HDF5 alternatives, and performance tips (contiguous memory).

## Key Claims
- **ndarray internals** — pointer to data + dtype + `shape` tuple + `strides` tuple (bytes-per-step per axis). Strides enable zero-copy views like `arr[::2, ::-1]`. C-order vs Fortran-order: `arr.flags["C_CONTIGUOUS"]` / `["F_CONTIGUOUS"]`. A C-contiguous 3×4×5 `float64` array has strides `(160, 40, 8)`.
- **dtype hierarchy** — superclasses `np.integer`, `np.floating`, `np.complexfloating`, `np.unsignedinteger`; check with `np.issubdtype(arr.dtype, np.integer)`.
- **Reshape / ravel** — `arr.reshape((rows, cols))` (use `-1` for inferred axis); `arr.ravel()` returns a flat view when possible; `arr.flatten()` always copies.
- **Concatenate / split** — `np.concatenate([a, b], axis=0)`; convenience: `np.vstack`, `np.hstack`, `np.column_stack`, `np.dstack`; `np.split(arr, indices_or_sections, axis=)`.
- **tile / repeat** — `np.tile(arr, reps)` tiles whole array; `arr.repeat(n)` repeats each element.
- **take / put** — `arr.take(indices, axis=)` (fancy-indexing equivalent); `arr.put(indices, values)` sets in place.
- **Broadcasting rules** — operate from trailing axes; sizes must be equal or one of them 1. Use `np.newaxis` (`None`) to inject length-1 axes for explicit broadcasting along other axes.
- **ufunc methods** — `np.add.reduce(arr, axis=)`, `.accumulate(arr)`, `.outer(a, b)`, `.reduceat(arr, indices)`. Custom Python ufuncs via `np.frompyfunc` (slow) or `numba.vectorize` (fast).
- **Structured arrays** — dtype with named fields (`[("x", "f8"), ("y", "i4")]`); access via `arr["x"]`. Nested types and per-field multidimensional fields supported. Useful when SoA / AoS matters or when interfacing with C structs / record-oriented binary files.
- **Sorting** — `arr.sort(axis=, kind=)` (kinds: quicksort, mergesort, heapsort, stable); indirect sort `np.argsort(arr)` returns indices; `np.lexsort(keys)` sorts on multiple keys. `np.partition(arr, k)` puts the smallest `k` at the front (k-th order statistic without full sort); `np.searchsorted(sorted_arr, v)` returns insertion index in `O(log n)`.
- **Numba** — JIT-compiled Python functions reaching C-level speed; `@numba.jit(nopython=True)` (or `@numba.njit`); `@numba.vectorize` to create custom ufuncs; supports a NumPy subset.
- **memmap** — `np.memmap(path, dtype=, mode="r+", shape=...)` exposes a disk file as an ndarray; in-place writes flush via `arr.flush()`. Useful for arrays too large to fit in RAM.
- **HDF5** — `h5py` and `PyTables` for hierarchical disk-backed arrays beyond what `memmap` offers; pandas's `read_hdf`/`to_hdf` build on this.
- **Performance tips** — contiguous arrays vastly outperform strided ones for vectorized operations; `arr.copy(order="C")` to defragment; minimize Python loops via ufuncs and reductions.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[NumPy]] — internals of the array library.
- [[NDArray]] — strides + dtype + shape.
- [[Broadcasting]] — promoted to full coverage here from Ch.4.
- [[Numba]] — JIT compiler for Python numeric code.
- [[pydata-numpy-basics]] — chapter 4 covers the basics.

## Contradictions
- None.
