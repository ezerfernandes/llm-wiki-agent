---
title: "Mandelbrot Set"
type: concept
tags: [parallel-computing, mathematics, examples]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Mandelbrot Set

The set of complex numbers $c$ for which the iteration

$$z \leftarrow z^2 + c, \quad z_0 = 0$$

remains bounded (a standard threshold is the orbit staying within a finite disk after some cutoff number of iterations). The boundary of the set is a famous fractal; the per-point determination is iterative, with **early termination** for points clearly outside the set and **many iterations** for points inside (or near the boundary).

## In the chapter

Used in [[parproc-ch02-recurring-performance-issues]] §2.2 and §2.4 as the recurring **load-balance failure** example, drawn from Chapter 7 of Darryl Gove's *Multicore Application Programming: for Windows, Linux and Oracle Solaris* (Addison-Wesley, 2011).

The textbook setup: a rectangular grid of complex numbers, two threads, with thread 0 handling the left half of the grid and thread 1 handling the right half. The naïve expectation is balanced work — and the naïve expectation is wrong. **Most points of the Mandelbrot set lie in the left half of the image**, so thread 0 spends most of its time iterating long orbits while thread 1 quickly bails out on right-half points and goes idle. [[NormMatloff|Matloff]] uses this throughout §2.4 as the canonical case where:

1. Naïve contiguous-chunk [[StaticTaskAssignment|static assignment]] (Method A) fails because per-task times are **spatially correlated** rather than i.i.d.
2. [[DynamicTaskAssignment|Dynamic scheduling]] (Method B) does help — `dynamic` 21.4s beats `static` 47.8s on the 8000×8000 grid — but loses to randomized static.
3. **Method A'** — randomize the row assignment before computation begins — restores the i.i.d. property at chunk level and wins at 15.7s.

The Mandelbrot example is also Matloff's exemplar of a problem that is [[EmbarrassinglyParallel|embarrassingly parallel]] under both the old (trivially decomposable) and new (low communication) meanings: *"there was no communication between [the two threads]."*

## Why it's a good teaching example

The per-pixel iteration is **easy to write but heterogeneous in cost** — the perfect combination for showcasing what goes wrong when [[LoadBalancing|load balancing]] is taken for granted. The visual output (the iconic fractal) makes the imbalance intuitively visible: just looking at the picture, you can see why the left-half thread has more work.

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.2 and §2.4.
- [[LoadBalancing]] — what Mandelbrot is teaching.
- [[StaticTaskAssignment]] — the randomized fix (Method A').
- [[DynamicTaskAssignment]] — the alternative the chapter ultimately rejects.
- [[EmbarrassinglyParallel]] — Mandelbrot qualifies under both old and new meanings.
- [[OpenMP]] — the chapter's timing table uses `#pragma omp for schedule(static|dynamic|guided|runtime)`.
