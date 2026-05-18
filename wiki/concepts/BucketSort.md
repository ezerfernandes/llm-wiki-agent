---
title: "Bucket Sort"
type: concept
tags: [algorithm, sorting, stub]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# Bucket Sort

Sorting algorithm that partitions input values into a fixed number of *buckets* based on value-range membership, sorts each bucket independently (typically with an internal algorithm like quicksort), then concatenates the bucket contents. Worst-case `O(n^2)`, average `O(n + k)` when keys distribute roughly uniformly across `k` buckets.

In [[parproc-ch01-intro-parallel-processing]], bucket sort is the substrate for the parallel [[SamplingBucketSort]] variant: a single-thread sampling step picks bucket boundaries from the input, then each worker thread is assigned one bucket, sorts it locally with `qsort`, and copies it back to the correct output offset.

## Connections
- [[SamplingBucketSort]] — parallel variant using sampling to set bucket boundaries.
- [[RadixSort]] — special case of bucket sort where boundaries are determined by bit patterns rather than sampling.
- [[parproc-ch01-intro-parallel-processing]] — context where it appears.
- [[parproc-ch12-parallel-sorting]] — §12.5–12.6 treat bucket sort with sampling (MPI) and radix sort.
