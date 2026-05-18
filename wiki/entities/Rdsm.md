---
title: "Rdsm (R Distributed Shared Memory)"
type: entity
tags: [r-package, parallel-computing, shared-memory, threading, operator-overloading]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# Rdsm

R package by [[NormMatloff]] that gives R "a quasi-thread interface" with genuinely shared memory — despite the fact that R itself is not threaded. Built on top of [[Snow]] (for the cluster/API plumbing) and the `bigmemory` package (for shared-memory keys addressing actual shared memory regions).

The trick is **operator overloading on `[`**: in R every operator is really a function (`1 + 1` is `"+"(1, 1)`; array access `x[i]` is `"["(x, i)`). Rdsm redefines `[` so that indexed access on its special "shared variable" objects reaches into a shared memory segment managed by `bigmemory`. The "rthreads" then operate independently but "genuinely share memory."

Programming pattern from [[parproc-ch01-intro-parallel-processing]]:
```r
mgrinit(cls)                       # initialize Rdsm on a snow cluster
mgrmakevar(cls, "a", 6, 2)         # shared variable, dimensions 6x2
mgrmakevar(cls, "b", 2, 6)
mgrmakevar(cls, "c", 6, 6)
a[,] <- 1:12                       # fill shared a from manager
clusterExport(cls, "mmultthread")
clusterEvalQ(cls, mmultthread(a, b, c))   # run on all workers, in place
print(c[,])                        # NOT print(c) — the latter prints the wrapper
```

Each worker computes its assigned slice of the matrix product directly into the shared `c`, then issues a `barr()` (Rdsm's barrier) before one designated worker does any wrap-up. A second worked example in the chapter is **maximal-burst-in-a-time-series**: workers compute moving averages over their slice using the `zoo` package's `rollmean`, write into a shared scratch vector `mas`, barrier, and let thread 1 do the final `which.max`.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces Rdsm via matrix multiply and time-series-burst examples.
- [[NormMatloff]] — author of the package and the book.
- [[Snow]] — Rdsm uses it for cluster setup and inter-process plumbing.
- [[Rlanguage]] — host language; Rdsm exists *because* base R lacks true threads.
- [[SharedMemoryArchitecture]] — Rdsm's programmer-facing model (shared variables addressed by overloaded `[`).
- [[Barrier]] — Rdsm exposes one as `barr()`.
