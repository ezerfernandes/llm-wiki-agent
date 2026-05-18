---
title: "ParProcBook Ch12: Introduction to Parallel Sorting"
type: source
tags: [textbook, parallel-computing, sorting, openmp, cuda]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch12: Introduction to Parallel Sorting

Chapter 12 (book pp. 257–272, PDF pp. 277–292) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. The chapter surveys parallel sorting algorithms across all three paradigms (shared memory, message passing, GPU) with emphasis on structural properties that make a sequential algorithm parallelizable: [[Quicksort]] (separation process, [[OpenMP]] fork, [[Hyperquicksort|hyperquicksort]] on hypercubes), [[MergeSort]] (sequential form, shared-memory variant, message-passing on a binary tree, [[CompareExchange|compare-exchange]] operations, [[BitonicMergesort|bitonic mergesort]]), [[BubbleSort]] (sequential form, [[OddEvenTransposition|odd-even transposition]] variant, [[CUDA]] implementation), [[Shearsort]] (2D mesh algorithm), [[SamplingBucketSort|bucket sort with sampling]] (MPI version), [[RadixSort]] (CUDPP library), and [[EnumerationSort]].

## Summary

§12.1 treats [[Quicksort]] as a divide-and-conquer sort that partitions via a `separate()` function (in-place pivot-and-partition returning the pivot's final index m, so x[l..m-1] < x[m] < x[m+1..h]); an alternative separation uses prefix scan from Ch10. The [[OpenMP]] implementation uses `#pragma omp parallel` + `#pragma omp for nowait` over two sub-calls, or the earlier `omp task` version from §4.5. §12.1.3 introduces [[Hyperquicksort]] for hypercubes: each d-cube root broadcasts its median as pivot; partner pairs exchange data and keep their respective halves; after d steps the array is globally sorted across PEs. §12.2 covers [[MergeSort]]: sequential pseudocode, shared-memory variant analogous to quicksort parallelization, binary-tree message-passing (leaf nodes sort locally and stream upward; non-leaf nodes merge two child streams), [[CompareExchange|compare-exchange / compare-split]] operations (each pair pools data and splits by rank), and [[BitonicMergesort]] (a sequence is bitonic if nondecreasing-then-nonincreasing or rotationally equivalent; pairwise compare-exchanges on a bitonic sequence of length k produce two bitonic halves with all-left ≤ all-right; applied iteratively to build a full sort in O(log² n) parallel steps). §12.3 treats [[BubbleSort]] and [[OddEvenTransposition]]: standard bubble sort is O(n²) serially but its inner loop parallelizes; odd-even transposition assigns one thread per element, alternating odd-phase (even-indexed elements trade with right neighbor) and even-phase (even-indexed elements trade with left neighbor); the [[CUDA]] kernel (`oekern`) maps array positions to blocks, alternates phases host-side, and uses pointer-swapping between a primary array and scratch space. §12.4 describes [[Shearsort]] for a 2D mesh: ceil(log₂(n))+1 phases alternating row-sorts (odd rows ascending, even rows descending) with column-sorts; produces a "snakelike" sorted layout; column operations in MPI handled via `MPI_Alltoall`. §12.5 gives the MPI [[SamplingBucketSort|bucket-sort-with-sampling]] implementation: PE0 collects samples from all PEs, computes decile splitters, broadcasts them; each PE sorts its local bucket with `qsort` and sends it back to PE0. §12.6 notes that [[RadixSort]] is a special case of bucket sort where buckets are formed bit-by-bit; CUDPP implements this using segmented scan. §12.7 describes [[EnumerationSort]]: for each element, count how many elements are smaller and place it at that index; the outer or inner loop parallelizes trivially.

## Key Claims

- **The `separate()` partition places x[m] in its final position.** After `separate(l, h)` returns m, x[l..m-1] < x[m] ≤ x[m+1..h] and x[m] will never move again; the sub-ranges will stay within [l,m-1] and [m+1,h] respectively. An alternative using exclusive prefix scan of a binary indicator array (Ch10) can perform separation in parallel. (§12.1.1, pp. 257–259)
- **OpenMP quicksort uses `nowait` because sub-ranges are disjoint.** Since different threads operate on different subarrays, no synchronization is needed between the two recursive calls spawned for the two piles. (§12.1.2, p. 260)
- **Hyperquicksort requires a power-of-2 number of nodes.** On a d-cube, d rounds suffice: root broadcasts median, each partner pair in i-subcubes exchanges and splits data, lower-numbered PE keeps smaller half. After d steps, PE i holds a globally sorted chunk with all elements at PE i < all elements at PE j for i < j. (§12.1.3, pp. 260–261)
- **Binary-tree mergesort has a load-balancing tension.** Sending one element at a time to the parent reduces upstream idle time but increases latency per element; buffering chunks reduces overhead but starves the parent. The optimal chunk size must be determined empirically per platform. (§12.2.3, p. 262)
- **Compare-exchange (compare-split) is a foundational primitive.** Two nodes pool their combined data, then lower-ID node keeps the lower half and higher-ID node keeps the upper half. This operation is key to bitonic mergesort and hyperquicksort alike. (§12.2.4, p. 262)
- **A bitonic sequence of length k (k a power of 2) can be split into two bitonic halves by pairwise compare-exchanges.** Compare-exchange a_i with a_{n/2+i} for i=0..n/2-1: the resulting lower and upper halves are both bitonic and every element of the lower half ≤ every element of the upper half. Applying `sortbitonic()` recursively yields a complete sort. To sort a general sequence, build successively larger bitonic sequences from adjacent pairs, quadruples, etc. (§12.2.5, pp. 262–264)
- **Bubble sort is inefficient serially but its inner-loop parallelizes directly.** Each outer iteration bubbles the current maximum to the right end; the inner compare-exchange sweep is data-parallel within an iteration (subject to ordering constraints). (§12.3.1, p. 264)
- **Odd-even transposition alternates two coupling phases.** In the odd phase, even-indexed thread i trades with i+1; in the even phase, even-indexed thread i trades with i-1. The CUDA implementation limits each kernel launch to one iteration because separate blocks cannot synchronize, alternating control on the host side; a scratch array `daaux` eliminates in-place write hazards, with pointer-swapping between iterations. (§12.3.2–12.3.3, pp. 265–266)
- **Shearsort runs on a 2D mesh in ceil(log₂n)+1 phases.** Odd phases sort each row (odd rows descending, even rows ascending); even phases sort each column ascending. Column operations in MPI require a matrix transpose, implementable via `MPI_Alltoall`. Result is a "snakelike" global ordering. (§12.4, p. 267)
- **Bucket sort with sampling uses decile splitters broadcast from PE0.** Each PE samples its local data, PE0 aggregates samples and computes the (p-1)-quantile boundaries as splitters, broadcasts them to all PEs; each PE then extracts its bucket and sorts locally with `qsort`. (§12.5, pp. 267–270)
- **Radix sort is bucket sort with bit-level buckets.** With 16 threads, the bucket for a datum is its lower 4 bits. CUDPP implements this with a segmented scan. No sampling needed if data is uniform mod the bucket width. (§12.6, p. 271)
- **Enumeration sort is trivially parallelizable but O(n²) work.** For each element, count elements less than it and place it at that rank. The outer loop (one iteration per element) or inner loop (one comparison per pair) parallelizes directly; no inter-element dependencies. (§12.7, p. 271)

## Key Quotes

> *"Sorting is one of the most common operations in parallel processing applications. For example, it is central to many parallel database operations, and important in areas such as image processing, statistical methodology and so on."* — p. 257. Motivates the chapter.

> *"You learned in your algorithms class that this is a very inefficient algorithm—when used serially. But it's actually rather usable in parallel systems."* — p. 264. On bubble sort's surprising parallel utility.

> *"Recall that in CUDA code, separate blocks of threads cannot synchronize with each other. Unless we deal with just a single block, this necessitates limiting the kernel to a single iteration of the algorithm, so that as iterations progress, execution alternates between the device and the host."* — p. 266. The fundamental constraint on the CUDA odd-even implementation.

> *"This algorithm was originally developed for hypercubes, but can be used on any message-passing system having a power of 2 for the number of nodes."* — p. 260. On hyperquicksort's generality.

## Connections

- [[NormMatloff]] — author.
- [[UCDavis]] — author's institution.
- [[Quicksort]] — §12.1; parallelized with OpenMP and extended to hyperquicksort.
- [[Hyperquicksort]] — §12.1.3; new concept page; hypercube-based distributed quicksort.
- [[MergeSort]] — §12.2; sequential and parallel forms.
- [[BitonicMergesort]] — §12.2.5; new concept page; compare-exchange on bitonic sequences.
- [[CompareExchange]] — §12.2.4; new concept page; pool-and-split primitive.
- [[BubbleSort]] — §12.3.1; new concept page; O(n²) serially, parallelizable.
- [[OddEvenTransposition]] — §12.3.2–12.3.3; new concept page; parallel bubble-sort variant.
- [[Shearsort]] — §12.4; new concept page; 2D-mesh sorting algorithm.
- [[SamplingBucketSort]] — §12.5; MPI implementation added to existing page.
- [[RadixSort]] — §12.6; new concept page; bit-level bucket sort.
- [[EnumerationSort]] — §12.7; new concept page; rank-count sort.
- [[OpenMP]] — §12.1.2 quicksort; §12.3.1 bubble sort.
- [[CUDA]] — §12.3.3 odd-even transposition sort implementation.
- [[MPI]] — §12.1.3 hyperquicksort; §12.4 shearsort column ops; §12.5 bucket sort.
- [[PrefixScan]] — §12.1.1 alternative separation process; §12.6 radix sort (CUDPP segmented scan).
- [[parproc-ch04-introduction-to-openmp]] — §4.5 quicksort with `omp task` cross-referenced.
- [[parproc-ch07-message-passing-systems]] — hypercube topology defined in Ch7.
- [[parproc-ch10-parallel-prefix-problem]] — prefix scan used in §12.1.1 and §12.6.

## Contradictions

- **Bubble sort as "much-maligned" vs practical parallel utility.** The chapter section heading calls bubble sort "the much-maligned bubble sort" and acknowledges the serial O(n²) reputation, then immediately argues it is "rather usable in parallel systems." This is not a contradiction with prior wiki content but is a notable reframing: no prior wiki page discusses bubble sort in a parallel context.
- **No contradiction with [[SamplingBucketSort]].** The MPI implementation here (PE0 collects samples, computes decile splitters, broadcasts) is structurally consistent with the OpenMP version in Ch1 (sampling then distributing), extending it to the message-passing setting.
