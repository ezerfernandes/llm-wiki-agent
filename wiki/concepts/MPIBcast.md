---
title: "MPI_Bcast"
type: concept
tags: [mpi, message-passing, collective-ops, broadcast, api]
sources: [parproc-ch08-introduction-to-mpi, parproc-ch07-message-passing-systems]
last_updated: 2026-05-17
---

# MPI_Bcast

One-to-all [[CollectiveCommunication|collective]] broadcast in [[MPI]]:

```c
int MPI_Bcast(void *buffer, int count, MPI_Datatype datatype,
              int root, MPI_Comm comm);
```

The `root` rank sends the contents of `buffer` to all other ranks in the communicator; every rank — including `root` — executes this same call. After the call, every rank's `buffer` holds the data the root provided.

## Pedagogical clarification

[[parproc-ch08-introduction-to-mpi]] §8.6.2 issues the canonical *all-nodes-execute-the-collective* point:

> *"Note my word 'participate' above. The name of the function is 'broadcast,' which makes it sound like only node 0 executes this line of code, which is not the case; all the nodes in the group execute this line. The only difference is the action; most nodes participate by receiving, while node 0 participates by sending."*

So `MPI_Bcast` is **not** an `if (me == root)` send call. It is a single line every rank must reach; the implementation dispatches send-vs-receive internally.

## Worked example: refactoring Dijkstra

[[parproc-ch08-introduction-to-mpi]] §8.6.2 replaces a hand-rolled loop:

```c
if (me == 0) {
    for (i = 1; i < nnodes; i++) {
        MPI_Send(overallmin, 2, MPI_INT, i, OVRLMIN_MSG, MPI_COMM_WORLD);
    }
} else {
    MPI_Recv(overallmin, 2, MPI_INT, 0, OVRLMIN_MSG, MPI_COMM_WORLD, &status);
}
```

with the single line:

```c
MPI_Bcast(overallmin, 2, MPI_INT, 0, MPI_COMM_WORLD);
```

The if/else disappears; all ranks execute the same statement.

## Why use it instead of a send loop?

[[parproc-ch08-introduction-to-mpi]] §8.6.2 gives two reasons:

1. **Clarity.** *"It would obviously be much clearer. That makes the program easier to write, easier to debug, and easier for others (and ourselves, later) to read."*
2. **Hardware exploitation.** *"Using the broadcast may improve performance. We may, for instance, be using an implementation of MPI which is tailored to the platform on which we are running MPI. If for instance we are running on a network designed for parallel computing, such as Myrinet or [[Infiniband]], an optimized broadcast may achieve a much higher performance level than would simply a loop with individual send calls. On a shared-memory multiprocessor system, special machine instructions specific to that platform's architecture can be exploited, as for instance IBM has done for its shared-memory machines. Even on an ordinary Ethernet, one could exploit Ethernet's own broadcast mechanism, as had been done for PVM."*

## The "not magic" caveat

[[parproc-ch07-message-passing-systems]] §7.3.1 issues the matching warning:

> *"Note carefully that even though MPI has its `MPI_Bcast()` function, it will send things out one at a time unless your network hardware is capable of multicast, and the MPI implementation you use is configured specifically for that hardware."*

So `MPI_Bcast`'s asymptotic cost depends entirely on the implementation + hardware:

- **Naive linear send-loop fallback:** O(P) message latencies sequentially — *no better than the manual loop*.
- **Binomial tree:** O(log P) latencies — common in MPICH/Open MPI default builds.
- **Hardware multicast (e.g. Ethernet / Infiniband):** O(1) latency in the limit.
- **[[Hypercube|Hypercube]] / recursive doubling:** O(log P) latencies; the *logical-hypercube* algorithmic descendant.

## Connections
- [[MPI]] — host library.
- [[CollectiveCommunication]] — class.
- [[parproc-ch08-introduction-to-mpi]] — primary source (§8.6.2).
- [[parproc-ch07-message-passing-systems]] — the *"not magic without hardware support"* warning.
- [[MPIReduce]] — the inverse-direction collective (all → one); often paired with `MPI_Bcast`.
- [[MPIAllreduce]] — `MPI_Reduce` + `MPI_Bcast` collapsed into one call.
- [[MPICommunicator]] — scoping.
- [[Hypercube]] — the logical topology used by recursive-doubling broadcast implementations.
- [[Infiniband]] — the canonical fabric supporting true hardware multicast.
- [[Broadcasting]] — the NumPy broadcast concept (distinct; same name, different meaning).
