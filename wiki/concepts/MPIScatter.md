---
title: "MPI_Scatter"
type: concept
tags: [mpi, message-passing, collective-ops, scatter, api]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# MPI_Scatter

One-to-all [[CollectiveCommunication|collective]] scatter in [[MPI]]:

```c
int MPI_Scatter(const void *sendbuf, int sendcount, MPI_Datatype sendtype,
                      void *recvbuf, int recvcount, MPI_Datatype recvtype,
                int root, MPI_Comm comm);
```

The `root` rank chunks its `sendbuf` into per-rank pieces of `sendcount` elements; rank `i` receives the `i`th chunk into `recvbuf`. Only the root's `sendbuf` is meaningful; every rank's `recvbuf` is.

[[parproc-ch08-introduction-to-mpi]] §8.6.5:

> *"This is the opposite of `MPI_Gather()`, i.e. it breaks long data into chunks which it parcels out to individual nodes."*

## Worked example

From the §8.6.6 edge-counting example:

```c
lenchunk = nv / nnodes;
MPI_Scatter(oh, lenchunk, MPI_INT, ohchunk, lenchunk, MPI_INT, 0, MPI_COMM_WORLD);
```

> *"Node 0 will break up the array oh of type MPI_INT into chunks of length lenchunk, sending the ith chunk to Node i, where lenchunk items will be deposited at ohchunk."*

After the call:
- `oh` at rank 0 is unchanged.
- Rank 0's `ohchunk` holds `oh[0..lenchunk-1]`.
- Rank 1's `ohchunk` holds `oh[lenchunk..2*lenchunk-1]`.
- ...etc.

## Pairing with [[MPIGather|`MPI_Gather`]]

The classical manager/worker [[ScatterGather]] pattern:

```c
// 1. Manager scatters work
MPI_Scatter(work_buf, chunk, MPI_INT, my_work, chunk, MPI_INT, 0, MPI_COMM_WORLD);

// 2. Every rank processes its chunk locally
process(my_work, my_results);

// 3. Manager gathers results
MPI_Gather(my_results, chunk, MPI_INT, result_buf, chunk, MPI_INT, 0, MPI_COMM_WORLD);
```

This is the MPI realization of the **embarrassingly parallel** workload shape (per [[parproc-ch08-introduction-to-mpi]] §8.1.4's recommendation).

## Variant

- **`MPI_Scatterv`** — variable-length chunks per rank (parallel to `MPI_Gatherv` / `MPI_Allgatherv`).

## Implementation

Tree-based scatter (each rank with bit `k` set receives from its bit-`k`-clear partner at level `k`) achieves O(log P) latency. The total bytes sent from root is `O(P × chunk_size)` — bandwidth-bound at root.

## Connections
- [[MPI]] — host library.
- [[CollectiveCommunication]] — class.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.6.5, §8.6.6).
- [[MPIGather]] — inverse operation; the natural pair.
- [[ScatterGather]] — the manager/worker paradigm `MPI_Scatter` opens.
- [[ScatterOperation]] — Thrust's scatter (different semantics; permutation primitive on a single device).
- [[MapReduce]] — Hadoop's *map* phase is conceptually an `MPI_Scatter`+per-rank-map.
- [[MPICommunicator]] — scoping.
- [[EmbarrassinglyParallel]] — workload shape `MPI_Scatter` enables.
