---
title: "MPI_Allgather"
type: concept
tags: [mpi, message-passing, collective-ops, gather, api]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# MPI_Allgather

All-to-all [[CollectiveCommunication|collective]] gather in [[MPI]]:

```c
int MPI_Allgather(const void *sendbuf, int sendcount, MPI_Datatype sendtype,
                        void *recvbuf, int recvcount, MPI_Datatype recvtype,
                  MPI_Comm comm);
```

Identical semantics to [[MPIGather|`MPI_Gather`]] except **every rank receives** the concatenated result, not just a designated root. Equivalent to `MPI_Gather` followed by `MPI_Bcast`, collapsed.

[[parproc-ch08-introduction-to-mpi]] §8.6.4:

> *"There is also `MPI_Allgather()`, which places the result at all nodes, not just one. Its call form is the same as `MPI_Gather()`, but with one fewer argument (since the identity of 'the' gathering node is no longer meaningful)."*

So the signature drops the `int root` argument — there is no single destination.

## Use cases

- **Replicated arrays from per-rank chunks.** Each rank computes its slice of a vector locally; `MPI_Allgather` makes the full vector visible to every rank for the next phase of computation.
- **Symmetric algorithms.** Pre-conditioning algorithms (Jacobi iteration, conjugate-gradient updates) where every rank needs the global state for its next step.
- **`MPI_Alltoall` precursor.** Stride-1 variant of the more general `MPI_Alltoall` (which sends *different* data from each rank to each rank).

## Implementation

Like [[MPIAllreduce]], a recursive-doubling schedule on a logical [[Hypercube]] achieves the all-to-all distribution in `log P` rounds, with the data each rank holds **doubling** every round:

```
Step 0:   each rank knows its own chunk
Step 1:   each rank exchanges with its bit-0 neighbor; both know 2 chunks
Step 2:   each rank exchanges (2 chunks worth) with its bit-1 neighbor; both know 4 chunks
...
Step log P: each rank knows all P chunks
```

Total data each rank sends/receives: `(P-1)/P × |total|` — bandwidth-optimal (same asymptote as ring-allreduce).

## Variants

- **`MPI_Allgatherv`** — variable-length per-rank chunks (parallel to `MPI_Gatherv`).

## Connections
- [[MPI]] — host library.
- [[CollectiveCommunication]] — class.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.6.4).
- [[MPIGather]] — single-destination variant.
- [[MPIBcast]] — second half of the conceptual decomposition.
- [[MPIAllreduce]] — analogous all-destinations reduction.
- [[Hypercube]] — the recursive-doubling topology.
- [[MPICommunicator]] — scoping.
