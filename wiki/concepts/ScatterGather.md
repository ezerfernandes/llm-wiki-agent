---
title: "Scatter/Gather"
type: concept
tags: [parallel-computing, paradigm, message-passing, manager-worker]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# Scatter/Gather

Manager/worker programming pattern, "technically a special case of message passing" but "so pervasive as to merit its own section" in [[parproc-ch01-intro-parallel-processing]].

Structure: "one node, say node 0, serves as a **manager**, while the others serve as **workers**. The parcels out work to the workers, who process their respective chunks of the data and return the results to the manager. The latter receives the results and combines them into the final product."

The chapter's worked example: matrix-vector multiplication. Manager distributes the rows of matrix A across workers (one chunk each), broadcasts X to all workers, each worker computes its partial Y from its rows of A times X, the manager collects and concatenates the partial Y vectors.

The chapter lists three concrete instances of scatter/gather:
- **[[MPI]] scatter and gather functions** (forward-referenced to §7.4).
- **Hadoop / [[MapReduce]] computing** — "basically a scatter/gather operation."
- **The [[Snow]] R package** — `splitIndices` partitions inputs, `clusterApply` ships partitions to workers, `Reduce` combines the per-worker results back.

This pattern is the natural fit for embarrassingly-parallel workloads where each chunk can be processed independently and combined trivially — which makes it the dominant cluster programming idiom outside of low-level [[MPI]].

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces scatter/gather and surveys MPI/Hadoop/snow instances.
- [[MPI]] — has explicit scatter/gather collectives.
- [[MapReduce]] — Hadoop's programming model is a scatter/gather instance.
- [[Snow]] — R's scatter/gather package (`clusterApply` + `Reduce`).
- [[MessagePassingArchitecture]] — scatter/gather is a special case.
- [[Cluster]] — typical deployment substrate.
