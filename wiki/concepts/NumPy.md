---
title: "NumPy"
type: concept
tags: [library, python, arrays, numerical-computing]
sources: [pydata-preliminaries, pydata-numpy-basics, pydata-advanced-numpy, d2l-preliminaries, hands-on-llm-ch05-text-clustering-topic-modeling, mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
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

## Role in the framework lineage ([[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]])

Ch 7 places NumPy (2006) on the [[LadderOfAbstraction|Ladder of Abstraction]] as the rung that "solved usability" — wrapping low-level BLAS in high-level Python and establishing the **vectorization contract** (logic in Python, loops in C/Fortran). PyTorch/TensorFlow [[Tensor|tensors]] are "direct descendants" extending the same $n$-dimensional array to GPUs + [[AutomaticDifferentiation|autodiff]]. Ch 7 also uses NumPy as the foil for what a *framework* is: NumPy executes each op immediately (eager), so it cannot defer execution to analyze the full graph for fusion — distinguishing a numerical library from a framework.

## Connections
- [[mlsysbook-ch07-ml-frameworks]] — NumPy's place on the framework ladder; the library-vs-framework distinction.
- [[LadderOfAbstraction]] / [[Tensor]] — the lineage NumPy seeds.
- [[NDArray]] — the central data structure.
- [[Broadcasting]] / [[UniversalFunctions]] / [[Numba]] — see [[pydata-advanced-numpy]].
- [[pandas]] / [[scikitlearn]] / [[statsmodels]] — downstream libraries built on NumPy.
- [[SciPy]] — extends NumPy with higher-level scientific routines.
