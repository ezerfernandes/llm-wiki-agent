---
title: "Numba"
type: concept
tags: [library, python, jit, performance]
sources: [pydata-preliminaries, pydata-advanced-numpy]
last_updated: 2026-05-15
---

# Numba

LLVM-based JIT compiler for Python. Decorate a numeric Python function with `@numba.njit` (or `@numba.jit(nopython=True)`) and Numba compiles it to machine code, often matching hand-written C performance. Supports a NumPy-flavored subset of Python — ndarrays, scalar ops, simple loops, ufuncs.

## Patterns
- `@njit` — compile a function.
- `@vectorize` — define a custom ufunc.
- `@guvectorize` — generalized ufunc with shape signature (e.g. matrix kernels).
- `parallel=True` — parallelize loops automatically.
- `prange(N)` — parallel loop primitive (drop-in for `range`).
- Release the GIL inside `@njit(nogil=True)` for threading.

## Connections
- [[NumPy]] / [[NDArray]] — primary data substrate.
- [[GlobalInterpreterLock]] — Numba can release it.
- [[UniversalFunctions]] — `@vectorize` produces real ufuncs.
- [[pydata-advanced-numpy]] — Appendix A covers Numba briefly.
