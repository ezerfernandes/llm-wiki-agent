---
title: "MPI_Gather"
type: concept
tags: [mpi, message-passing, collective-ops, gather, api]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# MPI_Gather

All-to-one [[CollectiveCommunication|collective]] gather in [[MPI]]:

```c
int MPI_Gather(const void *sendbuf, int sendcount, MPI_Datatype sendtype,
                     void *recvbuf, int recvcount, MPI_Datatype recvtype,
               int root, MPI_Comm comm);
```

Every rank contributes `sendcount` items from `sendbuf`; the root receives all contributions and places them in `recvbuf` **in rank order** (rank 0's contribution first, then rank 1's, etc.). Only the root's `recvbuf` is meaningful.

## Worked example

[[parproc-ch08-introduction-to-mpi]] §8.6.4 uses it in the refined Dijkstra (`Dijkstra.coll1.c`):

```c
MPI_Gather(mind + startv, chunk, MPI_INT, mind, chunk, MPI_INT, 0, MPI_COMM_WORLD);
```

> *"At this point all nodes participate in a gather operation, in which each node (including Node 0) contributes chunk number of MPI integers, from a location mind+startv in that node's program. Node 0 then receives chunk items sent from each node, stringing everything together in node order and depositing it all at mind in the program running at Node 0."*

This replaces the hand-coded `updateallmind` function from §8.3.2 which did `nnodes-1` separate `MPI_Send` / `MPI_Recv` pairs.

## API-design wart

[[parproc-ch08-introduction-to-mpi]] §8.6.4 notes:

> *"(Yes, the fifth argument is redundant with the second; same for the third and sixth.)"*

`sendcount` and `recvcount` are typically equal — the root expects the same chunk size from each rank. The redundancy persists for historical reasons (and because `MPI_Gatherv` *does* allow per-rank variable chunk sizes, so the symmetry of the signatures is preserved).

## Variants

- **`MPI_Gatherv`** — variable-length gather; each rank can send a different `count`, and the root specifies an array of *displacements* into `recvbuf` so different chunks land at different offsets. Useful when the per-rank chunk size depends on data.
- **[[MPIAllgather|`MPI_Allgather`]]** — gather with **all** ranks receiving the concatenated result, not just root.

## Relationship to [[MPIScatter|`MPI_Scatter`]]

`MPI_Gather` and `MPI_Scatter` are inverses:

- `MPI_Scatter`: root's single buffer → chunked across all ranks.
- `MPI_Gather`: each rank's chunk → concatenated single buffer at root.

The classical *"manager scatters work, workers compute, manager gathers results"* pattern uses these two as bookends, with worker computation in between. This is the canonical [[ScatterGather]] paradigm at the MPI API level.

## Implementation

Tree-based gather (every rank with bit `k` clear receives from its bit-`k`-set partner at level `k`) achieves O(log P) latency. Total bytes received at root is `O(P × chunk_size)` — bandwidth-bound.

## Connections
- [[MPI]] — host library.
- [[CollectiveCommunication]] — class.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.6.4).
- [[MPIScatter]] — inverse operation.
- [[MPIAllgather]] — all-destinations variant.
- [[ScatterGather]] — the manager/worker paradigm `MPI_Gather` realizes.
- [[GatherOperation]] — Thrust's gather (different semantics; permutation primitive on a single device).
- [[MPICommunicator]] — scoping.
- [[Hypercube]] — the logical topology O(log P) gather trees use.
- [[MapReduce]] — Hadoop's *reduce* phase is conceptually a `MPI_Gather`+merge.
