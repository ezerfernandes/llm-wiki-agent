---
title: "SPMD (Single Program Multiple Data)"
type: concept
tags: [parallel-computing, execution-model, mpi, message-passing]
sources: [parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# SPMD

**Single Program Multiple Data** — the dominant execution model for [[MPI]] programs. [[parproc-ch08-introduction-to-mpi]] §8.1.2:

> *"Though the nodes are all running the same program, they will likely be working on different parts of the program's data. This is called the Single Program Multiple Data (SPMD) model. This is the typical approach, but there could be different programs running on different nodes."*

Every MPI node loads the *same compiled binary*. Branching by rank (`if (me == 0) ... else ...`) is how different nodes execute different code paths within that single program. Pure-MPMD (Multiple Program Multiple Data) — where different binaries run on different nodes — is supported but uncommon.

## SPMD vs SIMD

- **[[SIMD]]** — same *instruction* applied to many data lanes in lockstep on one processor (GPU warp, vector unit, SSE/AVX).
- **SPMD** — same *program* run on many processors, each independently sequencing through its own instructions. No lockstep; sync only at explicit `MPI_Send` / `MPI_Recv` / collective boundaries.

GPU programming models (e.g. CUDA's per-thread kernel code) are often called **SPMD at the thread level** *and* SIMD at the warp level — the language model is per-thread independent, but the hardware groups 32 threads into one SIMD instruction stream.

## How SPMD looks in MPI

```c
int main(int argc, char **argv) {
    int me, nnodes;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &nnodes);
    MPI_Comm_rank(MPI_COMM_WORLD, &me);

    if (me == 0) {
        manager_logic();   // only rank 0
    } else {
        worker_logic();    // every other rank
    }

    MPI_Finalize();
}
```

Or the partition-by-rank pattern:

```c
int chunk = N / nnodes;
int startv = me * chunk;
int endv   = startv + chunk - 1;
for (int i = startv; i <= endv; i++) {
    /* my chunk of the work */
}
```

This *"data partitioning by rank"* is the workhorse of MPI numerical codes — every node sees the full program but computes on its own slice.

## SPMD on a single machine vs cluster

[[parproc-ch08-introduction-to-mpi]] §8.1.2 acknowledges the multicore reality: *"Now that multicore machines are commonplace, one might indeed run two or more cooperating MPI processes — where now we use the term *processes* in the real OS sense — on the same multicore machine."* The chapter uses *nodes* uniformly *"with an eye to the cluster setting,"* but the SPMD model itself works identically on a 4-core laptop and a 1024-node cluster — only the cost of `MPI_Send` differs.

## Connections
- [[MPI]] — the canonical SPMD runtime.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.1.2).
- [[CollectiveCommunication]] — collectives are SPMD-natural: *all nodes execute the collective line*, semantics differ by rank.
- [[SIMD]] — adjacent execution-model concept; distinguished by per-processor independence.
- [[CUDA]] — uses SPMD-at-thread-level + SIMD-at-warp-level.
- [[MessagePassingArchitecture]] — the architectural substrate.
- [[Cluster]] / [[NetworkOfWorkstations]] — typical deployment targets.
