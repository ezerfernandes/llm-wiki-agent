---
title: "Work Stealing"
type: concept
tags: [parallel-computing, scheduling]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Work Stealing

A [[DynamicTaskAssignment|dynamic task scheduling]] strategy in which **a thread that has finished its assigned work raids another thread's work queue** for tasks to execute. Distinguished from a centralized task farm by being *peer-to-peer*: each thread owns a local deque, and idle threads pull from a busy peer rather than from a global counter.

## In the chapter

[[parproc-ch02-recurring-performance-issues]] §2.4.4 introduces work stealing as *"another variation to Method A that is of interest today"*, citing **[[Cilk]]** as the canonical implementation: *"This is the approach taken, for example, by the elegant Cilk language."*

[[NormMatloff]] is mildly skeptical — the closing sentence of §2.4.4 reads *"Needless to say, accessing the other work queue is going to be expensive in terms of time and memory contention overhead."* In the chapter's framing, work stealing is just another point on the static-vs-dynamic spectrum, paying a [[CommunicationBottleneck|communication]] price for its load-balancing flexibility, and the same i.i.d.-chunk concentration argument applies: for large enough chunks the dynamic stealing buys you very little.

## When it pays off

Work stealing is typically motivated by **highly irregular task graphs** — recursive divide-and-conquer like quicksort or tree search — where the work decomposition is data-dependent and can't be predicted at the outset. In those settings randomized static (Method A') doesn't have anywhere obvious to apply, and the per-steal communication cost is amortized over substantial subtree work.

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.4.4.
- [[Cilk]] — the canonical work-stealing language.
- [[DynamicTaskAssignment]] — work stealing is a peer-to-peer flavor.
- [[StaticTaskAssignment]] — the alternative Matloff prefers as the default.
- [[LoadBalancing]] — work stealing's nominal motivation.
- [[CommunicationBottleneck]] — the cost work stealing pays.
