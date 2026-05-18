---
title: "Python (language)"
type: concept
tags: [language, programming]
sources: [pydata-preliminaries, pydata-python-basics, pydata-python-builtin]
last_updated: 2026-05-15
---

# Python (programming language)

General-purpose dynamically-typed interpreted programming language created by Guido van Rossum (first release 1991). Significant-indentation syntax, dynamic typing with duck typing, "everything is an object", and large standard library. Despite its initial reputation as a *scripting* language, Python has become the dominant language for data analysis, scientific computing, and machine learning, primarily through the [[NumPy]] / [[pandas]] / [[scikitlearn]] / [[matplotlib]] / [[IPython]] / [[Jupyter]] stack.

## Strengths for data work
- "Glue" language — C / C++ / FORTRAN interop via the C API.
- Solves the two-language problem (research and production in one stack).
- Large community / package ecosystem.

## Caveats
- Interpreted slower than compiled languages — push hot loops into NumPy ufuncs, Cython, or [[Numba]].
- [[GlobalInterpreterLock|GIL]] limits CPU-bound multithreading.

## Connections
- [[GlobalInterpreterLock]] — concurrency limitation.
- [[NumPy]] / [[pandas]] / [[IPython]] / [[Jupyter]] — defining libraries of the modern data-Python stack.
