---
title: "Communication Bottleneck"
type: concept
tags: [parallel-computing, performance]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Communication Bottleneck

The general phenomenon, in any parallel system, of **inter-processor communication becoming the rate-limiting cost** of a computation. [[NormMatloff]] opens [[parproc-ch02-recurring-performance-issues|Chapter 2 of *Programming on Parallel Machines*]] with this as the first recurring issue: *"Whether you are on a shared-memory, message-passing or other platform, communication is always a potential bottleneck"* (§2.1).

## The three flavors

| Platform | What "communication" is | Why it's slow |
|---|---|---|
| [[SharedMemoryArchitecture|Shared-memory]] | Memory loads/stores on the shared bus | Bus contention + [[CoherentCaches|cache-coherency]] transactions |
| [[MessagePassingArchitecture|Message-passing cluster]] | Network packets via [[MPI]] | *"Even a very fast network is very slow compared to CPU speeds"* |
| [[GPU]] | CPU↔GPU host-to-device transfer plus on-device memory contention | PCIe bandwidth; SM contention |

In [[OpenMP]] shared-memory programming, "communication" includes apparently-innocuous things like incrementing a shared `nextchunk` counter: [[parproc-ch02-recurring-performance-issues]] footnote 5 reminds the reader that *"in shared-memory programming, the threads communicate through shared variables. When one thread increments **nextchunk**, it 'communicates' that new value to the other threads by placing it in shared memory."*

## Communication drives load balancing

Communication and [[LoadBalancing|load balancing]] are not independent issues — they trade off. A [[DynamicTaskAssignment|dynamic task scheduler]] gets better balance precisely *by* communicating more (every task pull is a synchronized counter update). A [[StaticTaskAssignment|static scheduler]] communicates less but risks worse balance. The chapter's headline result is that for i.i.d. task times the balance penalty of static is negligible, so its communication savings win.

## Two dimensions: latency and bandwidth

§2.5 of [[parproc-ch02-recurring-performance-issues]] insists communication delays are at least two-dimensional: see [[Latency]] (time for one bit) and [[Bandwidth]] (bits per unit time). These are independently tunable — *"We can reduce latency by increasing the speed limit, and can increase bandwidth by improving the speed by which toll takers can collect tolls, and increasing the number of toll booths."*

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source.
- [[LoadBalancing]] — the inverse-correlated companion concept.
- [[Latency]] / [[Bandwidth]] — the two independent axes of communication cost.
- [[LatencyHiding]] — the workaround when you can't reduce latency.
- [[CoherentCaches]] — a major hidden source of shared-memory communication.
- [[CriticalSection]] — locks are also a communication mechanism (and a serial bottleneck).
- [[parproc-ch01-intro-parallel-processing]] — the prime-finder example demonstrates how lock contention can make an otherwise-trivially-parallel algorithm slow.
