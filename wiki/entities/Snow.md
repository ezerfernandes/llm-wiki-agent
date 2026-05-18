---
title: "snow (R package)"
type: entity
tags: [r-package, parallel-computing, scatter-gather, message-passing]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# snow

R package for parallel computing via the [[ScatterGather]] paradigm. Originally an independent user-contributed package; since merged with `multicore` into base R's `parallel` library. [[NormMatloff]] continues to refer to the merged piece "simply as **snow**" in [[parproc-ch01-intro-parallel-processing]].

Programming model: spin up a *cluster* of R processes (via `makePSOCKcluster(rep("localhost", 2))` for two local processes, or `makePSOCKcluster(c("pc28","pc29"))` for actual remote machines), then ship work to them with `clusterApply(cls, list_of_inputs, function)`, which returns a list of results — one per worker. Helper functions: `splitIndices(N, k)` partitions `1..N` into roughly-equal groups; `clusterExport(cls, "name")` copies a global variable from the manager to all workers; `clusterEvalQ(cls, expr)` evaluates an expression on each worker; `Reduce()` combines per-worker results.

Key property the chapter highlights: workers communicate over **TCP/IP sockets** — they are *independent R processes with no shared memory* (this is "a message-passing system, indeed"). Each worker has its own private workspace; mutations are not seen by the manager or other workers.

The chapter's running example is matrix-vector multiplication: partition the rows of `u`, ship a row group to each worker, multiply, `Reduce(c, ...)` to concatenate the partial answers. A second variant (`mmul1`) ships only each worker's slice of the matrix rather than the whole matrix, to avoid the export overhead for large `a`.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces snow with matrix-vector multiply and outlines `splitIndices` / `clusterApply` / `clusterExport` / `clusterEvalQ`.
- [[ScatterGather]] — snow's programming model.
- [[Rlanguage]] — the host language; snow is part of R's base `parallel` package.
- [[Rdsm]] — built on top of snow + `bigmemory` to add quasi-shared-memory semantics.
- [[MessagePassingArchitecture]] — snow's underlying model (TCP/IP sockets between independent R processes).
