---
title: "MPI_Barrier"
type: concept
tags: [mpi, message-passing, collective-ops, synchronization, api]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# MPI_Barrier

[[CollectiveCommunication|Collective]] synchronization in [[MPI]]:

```c
int MPI_Barrier(MPI_Comm comm);
```

Every rank in `comm` must reach the call before *any* of them returns. The sole argument is the communicator. No data is transferred — only synchronization.

[[parproc-ch08-introduction-to-mpi]] §8.6.9:

> *"This implements a barrier for a given communicator. The name of the communicator is the sole argument for the function. Explicit barriers are less common in message-passing programs than in the shared-memory world."*

## Why rare in MPI?

Most MPI synchronization is **implicit** at the send/recv boundary:

- A `MPI_Recv` blocks until a matching `MPI_Send` arrives — this *is* a barrier between the two ranks.
- Collective calls (`MPI_Bcast`, `MPI_Reduce`, `MPI_Gather`, ...) require all ranks to reach them — each is implicitly a barrier across the communicator.

So most MPI programs synchronize *via data flow* rather than explicit barriers. Compare with [[OpenMP]]'s shared-memory world, where `#pragma omp barrier` (and the implicit barriers inside `omp single` / `omp for`) is essential because threads otherwise have no synchronization at all.

## When `MPI_Barrier` is still useful

- **Timing measurement.** To start a timer when every rank is ready to begin: `MPI_Barrier(MPI_COMM_WORLD); t1 = MPI_Wtime();`
- **Coordinating non-MPI work.** If ranks perform a side-effecting non-MPI operation (writing to a shared filesystem, for instance) that must be globally ordered.
- **Debugging.** Force lockstep progression to make staircase prints intelligible.

## Implementation

Tree-based fan-in + fan-out, O(log P) latency. On [[Infiniband]] hardware-supported barrier operations are common: the chapter notes IB's *"high performance and scalable implementations of distributed locks, semaphores, collective communication operations. An atomic operation takes about 3-5 microseconds."*

## Connections
- [[MPI]] — host library.
- [[CollectiveCommunication]] — class.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.6.9).
- [[Barrier]] — the general synchronization-primitive concept (Pthreads / OpenMP / Rdsm / MPI all expose it).
- [[OpenMP]] — `#pragma omp barrier` is the shared-memory analog.
- [[MPICommunicator]] — scoping.
- [[Infiniband]] — hardware-accelerated barrier implementations.
