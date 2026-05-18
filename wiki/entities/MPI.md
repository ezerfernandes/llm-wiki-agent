---
title: "MPI (Message Passing Interface)"
type: entity
tags: [library, message-passing, parallel-computing, cluster, c, fortran, api-standard]
sources: [parproc-ch01-intro-parallel-processing, parproc-ch07-message-passing-systems, parproc-ch08-introduction-to-mpi]
last_updated: 2026-05-17
---

# MPI

**Message Passing Interface** — *"the de facto standard for message-passing software"* ([[parproc-ch08-introduction-to-mpi]] §8.1). A *"popular public-domain set of interface functions, callable from C/C++, to do message passing"* between processes in a [[MessagePassingArchitecture|message-passing system]] (typically a [[Cluster]] of independent machines, but also usable on a single multicore via shared-memory-backed implementations).

Each MPI process has its own private memory; there is no shared address space. Inter-process communication is **explicit**: every byte that crosses a process boundary is named in user code via `MPI_Send` / `MPI_Recv` (point-to-point) or a [[CollectiveCommunication|collective]] call (`MPI_Bcast`, `MPI_Reduce`, `MPI_Gather`, `MPI_Scatter`, `MPI_Barrier`, `MPI_Allreduce`, `MPI_Allgather`).

## Standard, not implementation

*"MPI is merely a set of Application Programmer Interfaces (APIs), called from user programs written in C, C++ and other languages. It has many implementations, with some being open source and generic, while others are proprietary and fine-tuned for specific commercial hardware."* ([[parproc-ch08-introduction-to-mpi]] §8.1.2).

The original MPI standard (MPI-1) later became **MPI 2** (added one-sided communication, dynamic process creation, parallel I/O). Ch8 is *"intended mainly for the original."*

## Implementation taxonomy

| Implementation | Status | Notes |
|---|---|---|
| **MPICH** | Active | *"offers more tailoring to various networks and other platforms"* — the reference implementation maintained by ANL. |
| **LAM/MPI** | Discontinued | *"runs on networks"*; smaller / simpler than MPICH; *"no longer being developed, and has been replaced by Open MPI."* The author of [[parproc-ch08-introduction-to-mpi]] (Ch 8.1.3) notes a personal preference: *"I still prefer the simplicity of LAM. It is still being maintained."* |
| **Open MPI** | Active | The post-LAM successor. **Not to be confused with [[OpenMP]]** — Open MPI is a distributed-memory message-passing library; [[OpenMP]] is a shared-memory threading pragma compiler extension. |
| **MVAPICH** | Active | MPICH-derived; tuned for [[Infiniband]] (Ohio State / Network-Based Computing Laboratory). |
| **Intel MPI** | Active | Proprietary; ABI-compatible with MPICH. |

Hard real-world warning ([[parproc-ch08-introduction-to-mpi]] §8.1.3): *"If your machine has more than one MPI implementation, make absolutely sure one is not interfering with the other. Make sure all execution and library paths all include one and only one implementation at a time."*

## Execution model: [[SPMD|SPMD]]

*"Single Program Multiple Data"* ([[parproc-ch08-introduction-to-mpi]] §8.1.2). Each MPI process runs the *same compiled program*, but works on different data based on its rank. The chapter uses *nodes* rather than *processes* *"with an eye to the cluster setting"* — though on a multicore one machine can host multiple MPI processes.

Boilerplate every MPI program needs:

```c
#include <mpi.h>

int main(int argc, char **argv) {
    int nnodes, me;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &nnodes);   // total node count
    MPI_Comm_rank(MPI_COMM_WORLD, &me);       // my rank ∈ [0, nnodes)
    /* ... computation ... */
    MPI_Finalize();
    return 0;
}
```

`MPI_Init` is implementation-dependent in its effect: on an Ethernet cluster it sets up TCP/IP sockets between every pair of nodes; on an [[Infiniband]] cluster it establishes IB-protocol connections; on a shared-memory MPI build it sets up local IPC. `MPI_Finalize` is mandatory cleanup.

## Point-to-point: [[MPISend|`MPI_Send`]] / [[MPIRecv|`MPI_Recv`]]

```c
MPI_Send(buf, count, datatype, dest_rank, tag, comm);
MPI_Recv(buf, count, datatype, source_rank, tag, comm, &status);
```

- **`buf`** — pointer to the bytes to send (or address where bytes are deposited).
- **`count, datatype`** — the message has this many objects of this MPI type. Standard types: `MPI_INT`, `MPI_DOUBLE`, `MPI_CHAR`, `MPI_FLOAT`, etc.; composite types like `MPI_2INT` for `(int, int)` pairs used by `MAXLOC`/`MINLOC` reductions.
- **`dest_rank` / `source_rank`** — peer's rank within the communicator. Wildcard `MPI_ANY_SOURCE` on receive.
- **`tag`** — programmer-defined integer message type. Receiver filters by tag. Wildcard `MPI_ANY_TAG` on receive.
- **`comm`** — the [[MPICommunicator|communicator]] context (typically `MPI_COMM_WORLD`).
- **`status`** — `MPI_Status` struct output: `MPI_SOURCE` / `MPI_TAG` fields recoverable after wildcard receives; `MPI_Get_count(&status, type, &count)` recovers the variable-length payload size.

### Why typed messages?

*"We want to be able to run MPI on a heterogeneous set of machines, with MPI serving as the 'broker' between them in case different architectures among those machines handle data differently."* ([[parproc-ch08-introduction-to-mpi]] §8.3.3.3). Two heterogeneity sources MPI hides:

1. **Endianness** — Intel little-endian vs Sun SPARC big-endian; *"some of the machines literally receive the data backwards!"* if raw bytes are blindly transmitted.
2. **Word width** — 32-bit vs 64-bit integers.

### Send semantics: *"safe to overwrite the send buffer"*

*"`MPI_Send(x,...)` will return only when it is safe for the application program to write over the array which it is using to store its message, i.e. x."* ([[parproc-ch08-introduction-to-mpi]] §8.7.1). This is **not** the same as *"the receiver has the data"* — buffering can decouple the two events.

## [[CollectiveCommunication|Collective operations]]

All-nodes-in-the-communicator execute the same line; semantics depend on rank.

| Operation | Signature (abbrev.) | Effect |
|---|---|---|
| [[MPIBcast|`MPI_Bcast`]] | `(buf, count, type, root, comm)` | `root` sends `buf` to all (including itself). |
| [[MPIReduce|`MPI_Reduce`]] | `(sendbuf, recvbuf, count, type, op, root, comm)` | All nodes contribute `sendbuf`; result of `op` lands at `root`'s `recvbuf`. |
| [[MPIAllreduce|`MPI_Allreduce`]] | `(sendbuf, recvbuf, count, type, op, comm)` | Reduce + Bcast collapsed; result at all nodes. |
| [[MPIGather|`MPI_Gather`]] | `(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, root, comm)` | Each node's `sendbuf` concatenated in rank order at `root`'s `recvbuf`. |
| [[MPIAllgather|`MPI_Allgather`]] | same minus `root` | Gather + Bcast collapsed. |
| [[MPIScatter|`MPI_Scatter`]] | `(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, root, comm)` | `root`'s `sendbuf` chunked into per-node `recvbuf`s. |
| [[MPIBarrier|`MPI_Barrier`]] | `(comm)` | All nodes wait until all reach. *"Less common in message-passing programs than in the shared-memory world."* |

### Reduce operations

12 built-in op codes ([[parproc-ch08-introduction-to-mpi]] §8.6.3 table): `MPI_MAX`, `MPI_MIN`, `MPI_SUM`, `MPI_PROD`, `MPI_LAND`, `MPI_LOR`, `MPI_LXOR`, `MPI_BAND`, `MPI_BOR`, `MPI_BXOR`, `MPI_MAXLOC`, `MPI_MINLOC`. The `MAXLOC` / `MINLOC` variants reduce over `(value, index)` pairs (`MPI_2INT`) and return both the extremal value *and* the rank-or-index attaining it.

### Why collectives over hand-written loops?

Two reasons ([[parproc-ch08-introduction-to-mpi]] §8.6.2):

1. **Clarity.** *"It would obviously be much clearer. That makes the program easier to write, easier to debug, and easier for others (and ourselves, later) to read."*
2. **Hardware exploitation.** *"On a network designed for parallel computing, such as Myrinet or [[Infiniband]], an optimized broadcast may achieve a much higher performance level than would simply a loop with individual send calls."*

**But** ([[parproc-ch07-message-passing-systems]] §7.3.1 caveat): if the underlying network does *not* support hardware multicast, or the MPI build is not configured for it, then *"`MPI_Bcast()` will send things out one at a time"* — i.e. degenerate to O(P) sequential sends. *"Note carefully that even though MPI has its MPI_Bcast() function, it will send things out one at a time unless your network hardware is capable of multicast, and the MPI implementation you use is configured specifically for that hardware."*

## [[MPICommunicator|Communicators]] and groups

A communicator is *"our node group"* ([[parproc-ch08-introduction-to-mpi]] §8.3.3.2). `MPI_COMM_WORLD` is the universal communicator containing every MPI node in the job. Subgroups are created when collectives need to apply to a *proper* subset (e.g. rows of a 2D physics grid, or splitting a job in half for two-way parallel branches).

The four-step recipe ([[parproc-ch08-introduction-to-mpi]] §8.6.10):

```c
MPI_Group worldgroup, subgroup;
MPI_Comm  subcomm;
int *subranks = malloc(n2 * sizeof(int));
/* populate subranks with the desired ranks */

MPI_Comm_group (MPI_COMM_WORLD, &worldgroup);          // 1. group from communicator
MPI_Group_incl (worldgroup, n2, subranks, &subgroup);  // 2. subgroup from rank list
MPI_Comm_create(MPI_COMM_WORLD, subgroup, &subcomm);   // 3. communicator from subgroup
MPI_Group_rank (subgroup, &subme);                     // 4. my rank in new group
```

Then `subcomm` replaces `MPI_COMM_WORLD` in subsequent collectives to scope them to the sub-group.

## [[BufferingMPI|Buffering, synchrony, deadlock]]

What happens inside `MPI_Send` on a TCP/IP cluster ([[parproc-ch08-introduction-to-mpi]] §8.7.1):

1. `MPI_Init` opened a TCP/IP socket from A to B (and to every other peer).
2. `MPI_Send` writes the message bytes to the socket. *"The TCP/IP stack will transmit that data to the TCP/IP socket at B. The TCP/IP stack at B will then send whatever bytes come in to MPI at B."*
3. **TCP/IP coalesces.** *"In TCP/IP the totality of bytes sent by A to B during lifetime of the connection is considered one long message."* MPI at B continually reads the stream and re-decomposes it into discrete MPI messages, ordered however the application's receive calls request.
4. **Flow control caps the OS buffer.** *"The buffer space the OS at B has set up for receiving data is limited. As A is sending to B, the TCP layer at B is telling its counterpart at A when A is allowed to send more data."*

### [[Deadlock|Deadlock]] patterns

- **Synchronous tag mismatch.** *"A wants to send two messages to B, of types U and V, but B wants to receive V first."* A blocks waiting for B's go-ahead on U; B is waiting for V; **deadlock**.
- **Buffer exhaustion.** Even buffered async sends can fail if the receiver's OS buffer fills and the sender can't progress.

MPI labels async/buffered communication **unsafe**: *"the program may run fine on most systems, as most systems are buffered, but fail on some systems."* But the synchronous alternative has *"such a performance penalty for doing things synchronously, most people are willing to go ahead with their 'unsafe' code."*

## "Living dangerously": [[NonblockingComm|nonblocking variants]]

```c
MPI_Isend(buf, count, type, dest, tag, comm, &request);
MPI_Irecv(buf, count, type, source, tag, comm, &request);
MPI_Wait(&request, &status);   // blocks until completion
MPI_Probe(...);                // asks whether completion has happened
```

Returns immediately; the application overlaps communication and computation. **Until completion, the buffer is off-limits** — touching the send buffer before `MPI_Wait` confirms, or reading the receive buffer before its `MPI_Wait` returns, is undefined behavior.

## Safe exchange: `MPI_Sendrecv` / `MPI_Sendrecv_replace`

When A and B need to swap data, the naive *"both send first then both receive"* deadlocks under synchronous semantics. The lower-rank-sends-first idiom works but is awkward. MPI provides:

```c
int MPI_Sendrecv_replace(void *buf, int count, MPI_Datatype datatype,
                         int dest, int sendtag,
                         int source, int recvtag,
                         MPI_Comm comm, MPI_Status *status);
```

*"A more convenient, safer and possibly faster alternative."* The buffer is overwritten in place; *"the sent and received messages can be of different lengths and can use different tags."* ([[parproc-ch08-introduction-to-mpi]] §8.7.4).

## Bindings in other languages

MPI's primary host languages are C and C++. Bindings exist for:

- **Fortran** — first-class in the standard.
- **Python** — `mpi4py` is the dominant binding ([[parproc-ch08-introduction-to-mpi]] §8.8 forward-references a Python chapter).
- **R** — `Rmpi` and the [[Snow]] / `snow`-on-MPI variants.
- **Julia** — `MPI.jl`.

## Performance shape

[[parproc-ch08-introduction-to-mpi]] §8.1.4: *"MPI applications that run well on networks tend to be of the 'embarrassingly parallel' type, with very little communication between the processes."* The headline arithmetic: at 1 GB/s + 1 μs [[Latency]], a 2000-bit message takes 3 μs; at 10 GB/s, 1.2 μs — *"so latency is a major problem even if the bandwidth is high."*

On a shared-memory multicore where all MPI processes co-reside, *"the problem is less severe. In fact, some implementations of MPI communicate directly through shared memory in that case, rather than using the TCP/IP or other network protocol."*

## Pedagogical example: parallel [[DijkstraAlgorithm|Dijkstra]]

The chapter walks Dijkstra single-source shortest-paths twice ([[parproc-ch08-introduction-to-mpi]] §8.3, §8.6.1):
- First with hand-rolled `MPI_Send` / `MPI_Recv` for find-overall-min, disseminate-overall-min, collect-final-distances.
- Then refactored: those three functions disappear into `MPI_Reduce(MPI_MINLOC)` + `MPI_Bcast` + `MPI_Gather` — collectives subsume the manual loops.

This same Dijkstra problem is used in [[parproc-ch04-introduction-to-openmp]] for OpenMP and in earlier CUDA chapters — giving a unified cross-paradigm worked example.

## Other Ch1–Ch8 examples written in MPI

- **Pipelined prime-number finder** — [[parproc-ch01-intro-parallel-processing]] §1.6.2.2.
- **Parallel Dijkstra** — [[parproc-ch08-introduction-to-mpi]] §8.3, §8.6.1.
- **Removing 0s from an array** (stream compaction with variable-length receive via `MPI_Get_count`) — §8.4.
- **Cumulative sums** (two-phase scan: local-scan, share local totals, add prefix-of-locals) — §8.6.7.
- **Counting edges in a directed graph** (scatter + reduce-sum) — §8.6.6.
- **Mutual outlinks** (broadcast matrix + round-robin row partition + reduce-sum) — §8.6.8.
- **Bucket sort with sampling** — forward-referenced to §12.5.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces MPI via the pipelined prime finder.
- [[parproc-ch07-message-passing-systems]] — hardware substrate (NOW / cluster / Infiniband / RDMA + the `MPI_Bcast`-is-not-magic warning).
- [[parproc-ch08-introduction-to-mpi]] — dedicated MPI chapter; primary source for this entity page's expanded surface.
- [[MessagePassingArchitecture]] — the paradigm MPI implements.
- [[Cluster]] / [[NetworkOfWorkstations]] / [[Beowulf]] — typical deployment targets.
- [[Hypercube]] — historical predecessor message-passing hardware; modern MPI collectives use logical-hypercube schedules.
- [[Infiniband]] — the low-latency / high-bandwidth / RDMA-capable interconnect MPI exploits when present.
- [[SPMD]] — the execution model.
- [[CollectiveCommunication]] — the all-nodes-execute primitive class.
- [[MPISend]] / [[MPIRecv]] — point-to-point pair.
- [[MPIBcast]] / [[MPIReduce]] / [[MPIAllreduce]] / [[MPIGather]] / [[MPIAllgather]] / [[MPIScatter]] / [[MPIBarrier]] — collective operations.
- [[MPICommunicator]] — group-scoping context for all calls.
- [[BufferingMPI]] — TCP/IP socket / OS-buffer / MPI-internals layering.
- [[NonblockingComm]] — `MPI_Isend` / `MPI_Irecv` / `MPI_Wait` / `MPI_Probe`.
- [[Deadlock]] — synchronous-tag-mismatch and buffer-exhaustion failure modes.
- [[ScatterGather]] — manager/worker pattern MPI's collectives realize.
- [[Snow]] — R package built on the same scatter/gather pattern (and `Rmpi`-backed in cluster mode).
- [[MapReduce]] — Hadoop's scatter/gather framework; conceptual cousin to MPI's `MPI_Scatter` + `MPI_Reduce`.
- [[OpenMP]] — distinct technology, frequently *confused* with Open MPI. Hybrid MPI+OpenMP is the canonical multi-core-cluster programming model.
- [[Latency]] / [[Bandwidth]] — the two metrics governing MPI performance.
- [[EmbarrassinglyParallel]] — the workload shape MPI works best on.
- [[DijkstraAlgorithm]] — the chapter-spanning worked example.
- [[GDB]] — attach-style multi-process debugging is MPI's debugger pattern.
