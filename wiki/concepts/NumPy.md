---
title: "NumPy"
type: concept
tags: [library, python, arrays, numerical-computing]
sources: [pydata-preliminaries, pydata-numpy-basics, pydata-advanced-numpy, d2l-preliminaries]
last_updated: 2026-05-16
---

# NumPy

Foundational numerical-computing package for Python. Provides the [[NDArray|ndarray]] (efficient multidimensional homogeneous array) plus vectorized arithmetic, [[Broadcasting|broadcasting]], [[UniversalFunctions|ufuncs]], linear algebra, FFT, random-number generation, and a mature C API. Underpins essentially every numerical Python library — [[pandas]], [[scikitlearn]], [[statsmodels]], [[matplotlib]], [[SciPy]] — typically via the ndarray as a `lingua franca` for data exchange.

## Origin
- Travis Oliphant forged NumPy in 2005 by merging the Numeric (1995, Jim Hugunin) and Numarray projects.

## Why it's fast
- Contiguous C-level memory, no per-element Python boxing.
- Vectorized operations execute as a single C loop instead of Python-level iteration.
- Empirically 10–100× faster than equivalent pure-Python list code on large arrays.

## Standard import
```python
import numpy as np
```

## Connections
- [[NDArray]] — the central data structure.
- [[Broadcasting]] / [[UniversalFunctions]] / [[Numba]] — see [[pydata-advanced-numpy]].
- [[pandas]] / [[scikitlearn]] / [[statsmodels]] — downstream libraries built on NumPy.
- [[SciPy]] — extends NumPy with higher-level scientific routines.
