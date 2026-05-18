---
title: "Embarrassingly Parallel"
type: concept
tags: [parallel-computing]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Embarrassingly Parallel

A parallel algorithm whose decomposition is trivial — but the precise meaning of *"trivial"* has shifted. [[NormMatloff]] in [[parproc-ch02-recurring-performance-issues]] §2.3 explicitly flags the terminology drift:

## Old meaning: trivially decomposable

A problem is "embarrassingly parallel" if **there is no intellectual challenge in splitting the work**. Matrix multiplication is the canonical example: just assign each processor a slab of rows of $A$, have each independently multiply by $X$, concatenate the results. Matloff: *"Of course, it's no shame to have an embarrassingly parallel problem! On the contrary, except for showoff academics, having an embarrassingly parallel application is a cause for celebration, as it is easy to program."*

## New (modern) meaning: low communication needs

> *"In recent years, the term **embarrassingly parallel** has drifted to a somewhat different meaning. Algorithms that are embarrassingly parallel in the above sense of simplicity tend to have very low communication between processes, key to good performance. That latter trait is the center of attention nowadays, so the term **embarrassingly parallel** generally refers to an algorithm with low communication needs."* — [[parproc-ch02-recurring-performance-issues]] §2.3.1.

## Worked examples (old vs new)

| Algorithm | Old meaning? | New meaning? | Why |
|---|---|---|---|
| Matrix-vector multiply | Yes | Yes (mostly) | trivially row-partitionable; minimal cross-thread traffic |
| Mandelbrot | Yes | **Yes** | Gove's example — *"there was no communication between [the two threads]"* |
| Sieve-of-Eratosthenes prime finder ([[parproc-ch01-intro-parallel-processing]] §1.5.1) | Yes ("embarrassingly easy to write") | **No** | Heavy locks + shared global array — high communication cost |
| Mergesort | Initial split: yes; merge phase: **no** | No | The merge step requires substantial cross-thread coordination |

## Iterative algorithms

§2.3.2: many parallel algorithms involve iteration with a rendezvous after each iteration. Each iteration's interior is "embarrassingly parallel" — independent work per node — but the per-iteration synchronization counts against the modern definition unless the granularity is coarse. *"Unless the granularity of the problem is coarse, i.e. there is a large amount of work to do in each iteration, the communication overhead will be significant, and the algorithm may not be considered embarrassingly parallel."* See [[IterativeAlgorithms]].

## Why it matters

Under the new meaning, "embarrassingly parallel" is essentially **a synonym for "low [[CommunicationBottleneck|communication]] cost"**, which is what makes [[StaticTaskAssignment|static task assignment]] work and what makes parallelization actually pay off. The old meaning ("easy to decompose") is a *necessary but not sufficient* condition.

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.3.
- [[CommunicationBottleneck]] — the modern definition is essentially "communication-light".
- [[LoadBalancing]] — embarrassingly-parallel problems are also typically easy to balance.
- [[IterativeAlgorithms]] — the per-iteration rendezvous can disqualify an algorithm from the modern definition.
- [[Mandelbrot]] — the chapter's canonical embarrassingly-parallel example.
- [[MatrixVectorMultiply]] — the chapter's running example, embarrassingly parallel under both definitions.
- [[parproc-ch01-intro-parallel-processing]] — the prime-finder is a clean case of "embarrassingly easy to write but **not** embarrassingly parallel" under the new meaning.
