---
title: "Tree Barrier"
type: concept
tags: [parallel-computing, synchronization, concurrency, shared-memory]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Tree Barrier

A parallelized [[Barrier]] implementation that reduces the critical-section fan-in from $O(n)$ to $O(\log_2 n)$ by structuring the barrier as a **binary tree of sub-barriers**. ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.12.4.2.1).

## Motivation

The naïve `pthread_mutex_lock(&L); count++; unlock(&L); while (count < N) ;` barrier (§3.12.1 / §3.12.3) is correct but **serializes** all `N` threads' increments through one lock. Its critical section is the bottleneck. *"Barriers can be costly to performance, since they rely so heavily on critical sections, i.e. serial parts of a program. Thus in many settings it is worthwhile to parallelize not only the general computation, but also the barrier operations themselves."*

## Construction

For `n = 2^k` threads:

- **Leaf level (0)**: `n / 2` sub-barriers of 2 threads each.
- **Level i** (for `i = 0, …, log₂n−1`): $2^i$ sub-barriers, each composed of $n/2^i$ thread "representatives" from the level below.
- **Root level**: a single sub-barrier of 2 representatives, one per half of the thread pool.

The chapter's worked sketch with `n = 16` and a two-level tree: split into two groups of 8; build a barrier per group; build a third barrier between the two group representatives (thread 0 for the first group, thread 4 for the second). NNodes for the leaf barriers is 8; NNodes for the root barrier is 2. After both leaf barriers fire, threads 0 and 4 participate in the root barrier. Reverse-direction notification then propagates the release: thread 0 wakes its group; thread 4 wakes its group.

## Why it's faster

The level-`i` sub-barriers can execute **simultaneously** — they touch disjoint state. The critical-section serialization at each sub-barrier is now $O(n / 2^i)$ at level `i` and $O(\log n)$ along the tree depth, vs $O(n)$ in the naïve flat barrier.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.12.4.2.1.
- [[Barrier]] — the parent synchronization primitive.
- [[ButterflyBarrier]] — sibling parallelization scheme; a butterfly is essentially "a number of simultaneously tree operations."
- [[CriticalSection]] — what tree barriers fan out.
- [[Pthreads]] — substrate (`pthread_mutex_lock` + `pthread_cond_wait`).
- [[SharedMemoryArchitecture]] — context.
