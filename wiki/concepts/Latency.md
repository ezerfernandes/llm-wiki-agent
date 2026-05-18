---
title: "Latency"
type: concept
tags: [parallel-computing, networking, performance]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Latency

**The time it takes for one bit to travel from source to destination** — e.g. from a CPU to memory on a shared-memory system, or from one computer to another on a cluster. One of the two dimensions of [[CommunicationBottleneck|communication delay]] in parallel systems; the other is [[Bandwidth]].

## The chapter's definition

[[parproc-ch02-recurring-performance-issues]] §2.5:
> *"Latency is the time it takes for one bit to travel for source to destination, e.g. from a CPU to memory in a shared memory system, or from one computer to another in a cluster."*

## The bridge analogy

[[NormMatloff]]'s memorable analogy (§2.5):

> *"It's helpful to think of a bridge, with toll booths at its entrance. Latency is the time needed for one car to get from one end of the bridge to the other. Bandwidth is the number of cars that can enter the bridge per unit time. We can reduce latency by increasing the speed limit, and can increase bandwidth by improving the speed by which toll takers can collect tolls, and increasing the number of toll booths."*

Latency and bandwidth are **independent** — you can have a high-latency high-bandwidth pipe (a long fat 10 GbE intercontinental link), or a low-latency low-bandwidth one (a single fast wire from CPU to L1 cache).

## Latency vs bandwidth — what affects each

| Latency depends on | Bandwidth depends on |
|---|---|
| Physical distance | Bus width (shared-memory) |
| Speed-of-light limits | Number of parallel network paths (message-passing) |
| Protocol overhead per packet | Link speed |
| Serialization delays | Toll-booth throughput (in the analogy) |

## Latency hiding

When you can't reduce latency, you can **hide** it — see [[LatencyHiding]]. [[parproc-ch02-recurring-performance-issues]] §2.5: *"For example, GPUs tend to have very long memory access times, but this is solved by having many pending memory accesses at the same time. During the latency of some accesses, earlier ones that have now completed can now be acted upon."* This is one of the things [[GPU|GPUs]] are exceptionally good at.

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.5.
- [[Bandwidth]] — the orthogonal axis.
- [[LatencyHiding]] — the workaround.
- [[CommunicationBottleneck]] — latency is one of the two dimensions of this cost.
- [[GPU]] — exemplar of aggressive latency hiding.
- [[MessagePassingArchitecture]] — network latency is the dominant per-message cost.
- [[SharedMemoryArchitecture]] — memory-access latency drives cache hierarchy design.
