---
title: "Collective Communication"
type: concept
tags: [parallel-computing, mpi, message-passing, collective-ops]
sources: [parproc-ch08-introduction-to-mpi, parproc-ch07-message-passing-systems]
last_invariant: 2026-05-17
last_updated: 2026-05-17
---

# Collective Communication

A class of message-passing primitives where **all processes in a communicator participate simultaneously**, each contributing to or consuming from a coordinated operation across the whole group. The opposite of pairwise point-to-point send/recv.

[[parproc-ch08-introduction-to-mpi]] §8.6: *"MPI features a number of collective communication capabilities."* The defining semantic clarification ([[parproc-ch08-introduction-to-mpi]] §8.6.2, on `MPI_Bcast`):

> *"The name of the function is 'broadcast,' which makes it sound like only node 0 executes this line of code, which is not the case; all the nodes in the group execute this line. The only difference is the action; most nodes participate by receiving, while node 0 participates by sending."*

So every collective call is a *single program line that all ranks must reach* — the semantics dispatch on the calling rank's role (source vs destination, contributor vs receiver).

## The MPI collective set

| Primitive | Role pattern | Use |
|---|---|---|
| [[MPIBcast|`MPI_Bcast`]] | one → all | Root distributes a buffer; all receive the same data. |
| [[MPIReduce|`MPI_Reduce`]] | all → one | Apply an associative op (`SUM`/`MIN`/...) across all contributions; result at root. |
| [[MPIAllreduce|`MPI_Allreduce`]] | all → all | `Reduce` + `Bcast` collapsed. |
| [[MPIGather|`MPI_Gather`]] | all → one | Concatenate per-rank chunks at root in rank order. |
| [[MPIAllgather|`MPI_Allgather`]] | all → all | `Gather` + `Bcast` collapsed. |
| [[MPIScatter|`MPI_Scatter`]] | one → all | Chunk root's buffer; each rank receives its slice. |
| [[MPIBarrier|`MPI_Barrier`]] | all ↔ all | Synchronization only; no data. |
| `MPI_Reduce_scatter` | all → all | Reduce then scatter the result vector. |
| `MPI_Alltoall` | all → all | Each rank sends a distinct chunk to each other rank. |

The §8.6 chapter focuses on the **named six** plus barrier; the more exotic `Alltoall` / `Reduce_scatter` get mentioned but not worked.

## Why use collectives over hand-coded loops?

Two arguments, both from [[parproc-ch08-introduction-to-mpi]] §8.6.2:

1. **Clarity.** *"It would obviously be much clearer. That makes the program easier to write, easier to debug, and easier for others (and ourselves, later) to read."*
2. **Hardware exploitation.** *"On a network designed for parallel computing, such as Myrinet or [[Infiniband]], an optimized broadcast may achieve a much higher performance level than would simply a loop with individual send calls. On a shared-memory multiprocessor system, special machine instructions specific to that platform's architecture can be exploited. Even on an ordinary Ethernet, one could exploit Ethernet's own broadcast mechanism."*

## The "collectives are not magic" caveat

[[parproc-ch07-message-passing-systems]] §7.3.1 issues the matching warning:

> *"Note carefully that even though MPI has its `MPI_Bcast()` function, it will send things out one at a time unless your network hardware is capable of multicast, and the MPI implementation you use is configured specifically for that hardware."*

So **collective semantics are guaranteed; collective performance is conditional** on the network hardware + MPI build supporting the optimization (hardware multicast, RDMA-based fan-out, [[Hypercube|hypercube-style]] recursive-halving / recursive-doubling schedules).

## Internal algorithms (sketch)

When the hardware does *not* provide native multicast, an optimized `MPI_Bcast` typically uses one of:

- **Binomial tree broadcast** — at step `k`, rank `r` with bit `k` clear sends to rank `r + 2^k`. `O(log P)` rounds; on a logical hypercube each round is a single bit-flip neighbor exchange.
- **Pipelined ring broadcast** — better for very large messages; chunk the message and pipeline along a ring of length P.
- **Recursive halving / doubling** for `MPI_Allreduce` — each rank exchanges with a partner at distance `2^k`, doubling the *combined* dataset each round; in `O(log P)` rounds every rank holds the full sum. The basis for [[RingAllReduce|ring-allreduce]] and NCCL's deep-learning collectives.

The [[Hypercube]]'s d-cube bit-flip-neighbor structure is the *logical topology* these algorithms assume — even on physical networks with no hypercube structure.

## Collective vs blocking semantics

Standard MPI collectives are **blocking**: every participant waits until the collective is complete before returning. MPI 3 added **nonblocking collectives** (`MPI_Ibcast`, `MPI_Ireduce`, etc.) but [[parproc-ch08-introduction-to-mpi]] focuses on the original (MPI-1) blocking forms.

## Connections
- [[MPI]] — host library.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.6).
- [[parproc-ch07-message-passing-systems]] — caveat about hardware-multicast dependence.
- [[MPIBcast]] / [[MPIReduce]] / [[MPIAllreduce]] / [[MPIGather]] / [[MPIAllgather]] / [[MPIScatter]] / [[MPIBarrier]] — the named operations.
- [[MPICommunicator]] — collectives scope to a communicator.
- [[SPMD]] — collectives are SPMD-natural: every rank executes the line.
- [[Hypercube]] — the logical topology many optimized collective algorithms assume.
- [[RingAllReduce]] — bandwidth-optimal collective algorithm used in deep-learning frameworks.
- [[AllReduce]] — the deep-learning collective primitive at the heart of data-parallel training.
- [[ScatterGather]] — manager/worker pattern realized by `MPI_Scatter` + `MPI_Gather`.
- [[Infiniband]] — the canonical low-level fabric exposing hardware multicast / RDMA primitives.
