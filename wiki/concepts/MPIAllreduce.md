---
title: "MPI_Allreduce"
type: concept
tags: [mpi, message-passing, collective-ops, reduce, api]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# MPI_Allreduce

All-to-all [[CollectiveCommunication|collective]] reduction in [[MPI]]:

```c
int MPI_Allreduce(const void *sendbuf, void *recvbuf,
                  int count, MPI_Datatype datatype,
                  MPI_Op op,
                  MPI_Comm comm);
```

Every rank contributes `sendbuf`; the operation `op` is applied across all contributions; the result lands in `recvbuf` **at every rank**. Equivalent to [[MPIReduce|`MPI_Reduce`]] followed by [[MPIBcast|`MPI_Bcast`]], collapsed into a single call.

[[parproc-ch08-introduction-to-mpi]] §8.6.3:

> *"MPI also includes a function `MPI_Allreduce()`, which does the same operation, except that instead of just depositing the result at one node, it does so at all nodes. So for instance our code above,*
>
> ```c
> MPI_Reduce(mymin, overallmin, 1, MPI_2INT, MPI_MINLOC, 0, MPI_COMM_WORLD);
> MPI_Bcast(overallmin, 1, MPI_2INT, 0, MPI_COMM_WORLD);
> ```
>
> *could be replaced by*
>
> ```c
> MPI_Allreduce(mymin, overallmin, 1, MPI_2INT, MPI_MINLOC, MPI_COMM_WORLD);
> ```
>
> *Again, these can be optimized for particular platforms."*

Note the signature compared to `MPI_Reduce`: **no `root` argument**, since there is no single destination.

## Why the dedicated call rather than `Reduce` + `Bcast`?

Three reasons:

1. **Performance.** An optimized `MPI_Allreduce` can exchange in both directions of every link simultaneously, achieving `~2× log P` total latency vs the `log P + log P` of separate reduce + broadcast. The **recursive-halving / recursive-doubling** schedule on a logical [[Hypercube]] is the classical algorithm:
   - Step k: each rank exchanges partial results with the partner at distance `2^k`.
   - After `log P` steps, every rank holds the full reduction.
2. **Bandwidth optimality.** The [[RingAllReduce|ring-allreduce]] variant — used by NCCL, Horovod, PyTorch DDP — achieves bandwidth-optimal `2(P-1)/P × |data|` per-rank traffic, which is the basis of modern data-parallel deep-learning training.
3. **Programmer convenience.** One call instead of two.

## Reduction operations

The same 12 built-in `MPI_Op` codes as [[MPIReduce]]: `MPI_MAX`, `MPI_MIN`, `MPI_SUM`, `MPI_PROD`, `MPI_LAND`, `MPI_LOR`, `MPI_LXOR`, `MPI_BAND`, `MPI_BOR`, `MPI_BXOR`, `MPI_MAXLOC`, `MPI_MINLOC`. User-defined ops via `MPI_Op_create`.

## Relationship to deep-learning [[AllReduce]]

The [[AllReduce]] concept page covers the same primitive from the deep-learning vantage point — synchronizing per-worker gradients in data-parallel training. Concretely: a PyTorch DDP call with the MPI backend dispatches into `MPI_Allreduce(grad, grad, count, MPI_FLOAT, MPI_SUM, comm)` for every parameter; with the NCCL backend it dispatches into NCCL's own ring-allreduce implementation on the same logical primitive.

## Connections
- [[MPI]] — host library.
- [[CollectiveCommunication]] — class.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.6.3).
- [[MPIReduce]] — single-destination variant.
- [[MPIBcast]] — second half of the conceptual decomposition.
- [[AllReduce]] — deep-learning data-parallel synchronization primitive (same operation, different vantage).
- [[RingAllReduce]] — bandwidth-optimal algorithm used in production.
- [[Horovod]] — wraps NCCL/MPI all-reduce for deep learning.
- [[NCCL]] — NVIDIA's GPU-optimized all-reduce implementation.
- [[Hypercube]] — the logical topology recursive-halving/doubling assumes.
- [[MPICommunicator]] — scoping.
