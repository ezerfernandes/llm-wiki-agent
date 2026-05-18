---
title: "Python for Data Analysis 3E — Ch.4: NumPy Basics: Arrays and Vectorized Computation"
type: source
tags: [book, numpy, arrays, vectorization, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/numpy-basics.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/numpy-basics.html
chapter: 4
---

## Summary
Introduces the [[NumPy]] [[NDArray|ndarray]] — a fast multidimensional homogeneous container — and the array-oriented style of computing it enables. Covers construction, dtypes, vectorized arithmetic, broadcasting basics, indexing (basic / slicing / boolean / fancy), transposing, [[UniversalFunctions|universal functions (ufuncs)]], conditional-as-array via [[NumpyWhere|np.where]], descriptive statistics on arrays, sorting / unique / set logic, file I/O, [[numpyLinalg|numpy.linalg]], pseudorandom number generation, and a random-walks example.

## Key Claims
- **Why ndarray** — contiguous C-level memory + C algorithms; 10–100× faster than equivalent pure-Python list code on a million-element multiply (`np.arange(1_000_000) * 2` ≈ 309 µs vs 46 ms list comprehension).
- **Array attributes** — `shape` (tuple), `dtype` (e.g. `float64`, `int64`); `ndim` for rank.
- **Creation** — `np.array`, `np.zeros`, `np.ones`, `np.empty` (uninitialized!), `np.arange`, `np.full`, `np.eye`/`np.identity`.
- **Dtype** — explicit conversion via `arr.astype(...)`; `astype` always copies.
- **Vectorized arithmetic** — element-wise `*`, `+`, `-`, `/`, `**`; equal-shape arrays operate element-wise; differently-shaped arrays trigger [[Broadcasting]] (full coverage in Appendix A).
- **Indexing** — basic slicing returns a **view** (not a copy); explicit `.copy()` needed; 2D indexing `arr[i, j]` and `arr[i][j]` equivalent.
- **Boolean indexing** — `arr[mask]` selects rows / elements where mask is True; can combine with `~`, `&`, `|` (NOT bitwise on numpy; `and`/`or` don't work on arrays).
- **Fancy indexing** — index with integer arrays; always returns a copy; `arr[[1,5,7],[0,3,1]]` selects diagonal-style elements.
- **ufuncs** — unary (`np.sqrt`, `np.exp`, `np.abs`, `np.isnan`) and binary (`np.maximum`, `np.add`); operate element-wise; faster than Python loops.
- **np.where(cond, x, y)** — vectorized ternary, replaces `if-else` over arrays.
- **Stats methods** — `arr.sum`, `mean`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, `cumsum`, `cumprod`; accept `axis=` argument for reducing along an axis.
- **Boolean array methods** — `arr.any()`, `arr.all()`; `(arr > 0).sum()` counts trues.
- **Sorting** — `arr.sort()` in-place vs `np.sort(arr)` returns copy; `axis=` argument.
- **Set logic** — `np.unique`, `np.intersect1d`, `np.union1d`, `np.in1d`, `np.setdiff1d`, `np.setxor1d`.
- **File I/O** — `np.save`/`np.load` (.npy binary), `np.savez`/`np.savez_compressed` (.npz multi-array archive).
- **Linear algebra** — `np.dot`/`@`; `numpy.linalg` provides `inv`, `solve`, `qr`, `svd`, `eig`, `det`.
- **PRNG** — modern API uses `np.random.default_rng(seed)`; methods like `rng.standard_normal`, `rng.integers`, `rng.uniform`.
- **Random walks example** — vectorized many-walks-at-once: `steps = rng.choice([-1, 1], size=(nwalks, nsteps))` then `walks = steps.cumsum(axis=1)`.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[NumPy]] — central library; this chapter is its primer.
- [[NDArray]] — the core data structure.
- [[Broadcasting]] — promoted to full Appendix A coverage.
- [[UniversalFunctions]] — vectorized element-wise functions.
- [[pandas]] — built on NumPy semantics; many idioms carry over.
- [[pydata-pandas-basics]] — chapter 5 next.
- [[pydata-advanced-numpy]] — Appendix A deepens this material.

## Contradictions
- None.
