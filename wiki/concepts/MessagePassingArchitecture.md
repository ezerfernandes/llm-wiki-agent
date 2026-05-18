---
title: "Message-Passing Architecture"
type: concept
tags: [parallel-computing, hardware, architecture, cluster]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# Message-Passing Architecture

Parallel hardware paradigm with "a number of independent CPUs, each with its own independent memory" communicating "with each other via networks of some kind." Second of [[parproc-ch01-intro-parallel-processing]]'s three architectures (with [[SharedMemoryArchitecture]] and [[SIMD]]).

The canonical instance is a [[Cluster]] of commodity PCs networked together for parallel processing — [[Beowulf]]-style. Each node is "of course an individual machine, capable of the usual uniprocessor (or now multiprocessor) applications, but by networking them together and using parallel-processing software environments, we can form very powerful parallel systems."

Key features per the chapter:
- **No shared address space.** A value computed on node 2 is invisible to node 15 until explicitly transmitted via `send`/`receive` (or [[MPI]]'s `MPI_Send` / `MPI_Recv`).
- **Network performance matters.** "Ordinary Ethernet and TCP/IP are fine for the applications envisioned by the original designers of the Internet … but is slow in the cluster context. A good network for a cluster is, for instance, [[Infiniband]]."
- **Each node has separate copies** of all data structures. In the chapter's matrix-vector multiply example, every node holds its own copy of A, X, Y; sharing values requires explicit `send(15, 12, "Y[3]")`-style messaging.
- **Heterogeneity is OK.** "MPI 'translates' for you automatically" between big-endian and little-endian CPUs.

Common patterns:
- **Pipelining** — chain nodes such that each performs one filtering/transformation stage on a stream of items.
- **[[ScatterGather]]** — a manager partitions work, workers process chunks, results combine back.

[[Snow]] (R's `parallel` package) is a message-passing system at heart: its worker R processes "communicate via TCP/IP sockets" with no shared memory, even though R isn't itself a systems-programming language. (The chapter contrasts this with [[Rdsm]], which adds a thin shared-memory layer on top via operator overloading on `[`.)

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces it as the second of three architectures.
- [[Cluster]] — physical realization of message-passing systems.
- [[Beowulf]] — commodity-PC cluster recipe.
- [[MPI]] — the canonical message-passing API.
- [[Snow]] — R's message-passing package (TCP/IP sockets).
- [[ScatterGather]] — the dominant programming pattern.
- [[Infiniband]] — high-bandwidth cluster interconnect.
- [[SharedMemoryArchitecture]] — the contrasting paradigm.
- [[SIMD]] — third paradigm.
