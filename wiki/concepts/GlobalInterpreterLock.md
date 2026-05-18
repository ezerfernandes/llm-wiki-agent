---
title: "Global Interpreter Lock (GIL)"
type: concept
tags: [python, concurrency]
sources: [pydata-preliminaries]
last_updated: 2026-05-15
---

# Global Interpreter Lock (GIL)

CPython mechanism that prevents more than one Python instruction from executing at a time. Simplifies the implementation of the interpreter (and of C extension modules) but limits CPU-bound multithreading in pure Python — adding threads does not speed up a CPU-bound Python computation.

## Workarounds
- **Multi-process** (`multiprocessing`, `joblib`, `dask`, `ray`, `mpi4py`) — each process has its own GIL.
- **Release the GIL in C extensions** — NumPy, pandas, scikit-learn, FFI bindings can release the GIL around long-running C/Fortran code, letting other Python threads run concurrently.
- **Numba / Cython `nogil`** — same trick, in JIT or AOT-compiled code.
- **PEP 703** (post-2024) is an in-progress experiment to remove the GIL entirely from CPython.

## Connections
- [[PythonLanguage]] — CPython implementation detail.
- [[Numba]] / [[NumPy]] / [[pandas]] — practical escape hatches for numeric work.
