---
title: "Iterative Algorithms"
type: concept
tags: [parallel-computing, algorithms]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Iterative Algorithms

Parallel algorithms structured as **a loop of independent-per-iteration computation followed by a per-iteration rendezvous** (synchronization point) before the next iteration begins. Canonical examples: Jacobi / Gauss-Seidel iterative linear solvers, gradient-descent style optimization, BSP-style supersteps, simulation timesteps.

## The chapter's framing

[[parproc-ch02-recurring-performance-issues]] §2.3.2:

> *"Many parallel algorithms involve iteration, with a rendezvous of the tasks after each iteration. Within each iteration, the nodes act entirely independently of each other, which makes the problem seem embarrassingly parallel."*
>
> *"But unless the granularity of the problem is coarse, i.e. there is a large amount of work to do in each iteration, the communication overhead will be significant, and the algorithm may not be considered embarrassingly parallel."*

## Granularity is everything

The rendezvous at the end of each iteration is a [[Barrier|barrier]] — and a barrier is a communication event. Whether an iterative algorithm counts as [[EmbarrassinglyParallel|embarrassingly parallel]] under the modern (low-communication) meaning depends entirely on **per-iteration granularity**:

| Per-iteration work | Verdict |
|---|---|
| Hours of compute, occasional barrier | Embarrassingly parallel ✓ |
| Milliseconds of compute, frequent barriers | Communication-bound ✗ |

The same algorithm can flip categories depending on problem size.

## Strategies to improve iterative-algorithm scaling

The chapter doesn't operationalize these but they follow from the §2.3.2 framing:
- **Coarsen the iterations** — do more work per superstep.
- **Hide barrier latency** — overlap useful computation with synchronization (the [[LatencyHiding]] idea).
- **Relax the synchronization** — asynchronous / chaotic relaxation; doesn't always converge but when it does, eliminates the barrier entirely.

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.3.2.
- [[EmbarrassinglyParallel]] — iterative algorithms are *conditionally* embarrassingly parallel, depending on granularity.
- [[CommunicationBottleneck]] — per-iteration barriers are the communication cost.
- [[Barrier]] — the synchronization primitive at each rendezvous.
- [[LatencyHiding]] — one mitigation.
