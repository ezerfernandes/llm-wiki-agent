---
title: "Static Task Assignment"
type: concept
tags: [parallel-computing, scheduling]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Static Task Assignment

A task-to-processor assignment strategy in which **the code decides at the outset (before computation starts) which processor will handle which tasks**. Contrasted with [[DynamicTaskAssignment]], where processors determine their tasks as the computation proceeds.

[[parproc-ch02-recurring-performance-issues]] §2.4: *"In **static** assignment, our code would decide at the outset which processors will handle which tasks. The alternative, **dynamic** assignment, would have processors determine their tasks as the computation proceeds."*

## Why it's the chapter's recommended default

The headline claim of [[parproc-ch02-recurring-performance-issues]] is in the section title itself: *"Static (But Possibly Random) Task Assignment Typically Better Than Dynamic."* The argument:

1. Static assignment incurs **zero scheduler-side communication** during execution. No shared counter to lock, no work-queue raids, no manager-worker handshakes.
2. The intuitive worry about static assignment is **load imbalance**: a thread that finishes early sits idle. But if per-task times $T_i$ are i.i.d., then a chunk of $m$ tasks has total time with coefficient of variation $\sigma/\mu \sim O(1/\sqrt{m})$. For chunks of even moderate size, **chunk runtime is essentially constant**, so there's no imbalance to fix.
3. Therefore the [[DynamicTaskAssignment|dynamic alternative]]'s flexibility buys nothing in the i.i.d. case, while still paying the per-task communication tax.

## When i.i.d. breaks: randomize

The i.i.d. assumption fails when tasks-within-a-chunk are correlated. The chapter's two examples:

- **Mandelbrot**: spatial correlation — neighboring points tend to be jointly in-or-out of the set. Chunking by contiguous rows of the image gives one thread a chunk dominated by in-set (slow) points and another a chunk dominated by out-of-set (fast) points.
- **Mutual web outlinks**: structural correlation — the inner loop length depends on the outer index, so contiguous chunking of outer indices is intrinsically uneven.

The fix is **Method A'** (still static!): randomize the chunk composition. *"In the matrix-multiply example above, with 10000 rows and chunk size 1000, do NOT assign the chunks contiguously. Instead, generate a random permutation of the numbers 0,1,...,9999, naming them $i_0, i_1, ..., i_{9999}$. Then assign thread 0 rows $i_0 - i_{999}$, thread 1 rows $i_{1000} - i_{1999}$, etc."* (footnote 3: *"This is still static, as the randomization is done at the outset, before starting computation."*)

For mutual outlinks, an even smarter static trick: **pair rows symmetrically** — thread 0 gets rows `0..499` *and* `9500..9999`, thread 1 gets `500..999` *and* `9000..9499`, etc. Same Method A flavor, exploiting the known structure of the problem.

## OpenMP implementation

`#pragma omp for schedule(static)` is the standard implementation, with default chunk size $n/p$. Matloff's preferred Method A' corresponds to `schedule(runtime)` with `OMP_SCHEDULE=random` or to explicit pre-permutation of the loop indices.

## Mandelbrot timings (from the chapter)

| Policy | Time (s) |
|---|---|
| `static` (contiguous chunks — Method A) | 47.8 |
| `dynamic` | 21.4 |
| `guided` | 29.6 |
| **`random` (Method A')** | **15.7** |

Pure static is worst on Mandelbrot precisely because of the spatial-correlation failure of i.i.d. — but **randomized** static is best of all four.

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.4.
- [[DynamicTaskAssignment]] — the foil.
- [[LoadBalancing]] — what static assignment trades off.
- [[CommunicationBottleneck]] — what static assignment saves.
- [[MatrixVectorMultiply]] — running example.
- [[OpenMP]] — `schedule(static)` / `schedule(runtime)`.
- [[WorkStealing]] — a peer-to-peer flavor of dynamic.
