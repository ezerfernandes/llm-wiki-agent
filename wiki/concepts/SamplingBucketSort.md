---
title: "Sampling Bucket Sort"
type: concept
tags: [algorithm, sorting, parallel-computing, openmp, mpi]
sources: [parproc-ch01-intro-parallel-processing, parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# Sampling Bucket Sort

Parallel sorting algorithm used by [[parproc-ch01-intro-parallel-processing]] as its introductory [[OpenMP]] example (forward-referenced to chapter 12.5 for full treatment).

Algorithm sketch from the chapter's `bsort()` implementation:
1. **Determine bucket boundaries by sampling** the input array `x`: take `SAMPLESIZE` samples (1000 if `n > 1000`, else `n/2`), find min/max via `findminmax`, and split that range into `nth - 1` equal-width bucket boundaries `bdries[0..nth-2]`, where `nth` is the OpenMP thread count.
2. **Single-thread setup** with `#pragma omp single` (implicit [[Barrier|barrier]] at end): the boundaries `bdries` and a `counts` array (one slot per bucket) are allocated.
3. **Each thread grabs its bucket.** Thread 0 takes everything `<= bdries[0]`, thread 1 takes `(bdries[0], bdries[1]]`, …, thread `nth-1` takes everything `> bdries[nth-2]`. Each scans the entire input and copies its share into its local `mypart` array (`grab()` increments `nummypart`).
4. **Each thread sorts its bucket locally** with `qsort` — this is the parallel-friendly inner work; no synchronization needed.
5. `counts[me] = nummypart` records each thread's slice size.
6. **`#pragma omp barrier`** so every thread can see all the `counts`.
7. **Each thread copies its sorted slice back into the original array** at the correct offset, computed by summing `counts[0..me-1]`. Implicit barrier at end of the surrounding parallel block ensures `main` doesn't read until all threads are done.

Why it parallelizes well: after the sampling step, each thread works on a disjoint range of values with no inter-thread data dependencies. The only synchronization points are (1) the `single` block for boundary setup and (2) the barrier before the copy-back phase. The chapter uses this example specifically to showcase OpenMP's `parallel` / `single` / `barrier` triumvirate.

## Ch12: MPI Implementation

[[parproc-ch12-parallel-sorting]] §12.5 provides an MPI bucket-sort-with-sampling implementation for a message-passing setting with 10 PEs:

1. Each PE samples some of its local data and sends the sample to PE0.
2. PE0 aggregates all samples and computes decile values (10th, 20th, …, 90th percentiles) as **splitters**.
3. PE0 broadcasts the splitters to all PEs.
4. Each PE scans its local data, distributes it to the appropriate PE according to the splitter intervals, then sorts its bucket locally with `qsort`.
5. Each PE sends its sorted chunk back to PE0 (or the manager), which places chunks at their correct offsets in the output array.

The key design difference from the OpenMP version: splitter computation is centralized at PE0, and data redistribution uses point-to-point MPI sends/receives. The MPI code presented is not claimed to be highly optimized (e.g., a broadcast-based distribution would improve it).

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces this algorithm as the canonical OpenMP example.
- [[parproc-ch12-parallel-sorting]] — §12.5 source for the MPI implementation.
- [[OpenMP]] — the Ch1 example's implementation vehicle.
- [[MPI]] — the Ch12 message-passing implementation vehicle.
- [[Barrier]] — both implicit (`single`) and explicit (`barrier`) used in the OpenMP example.
- [[BucketSort]] — the underlying sequential algorithm; "sampling" is the parallelization-enabling preprocessing step.
- [[RadixSort]] — a special case of bucket sort with bit-level boundaries; no sampling needed when data is uniform.
