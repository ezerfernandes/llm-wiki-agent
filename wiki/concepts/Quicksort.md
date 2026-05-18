---
title: "Quicksort"
type: concept
tags: [algorithm, sorting, recursion, parallel-computing]
sources: [parproc-ch04-introduction-to-openmp, parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# Quicksort

Classical divide-and-conquer comparison sort. Pick a pivot, partition the array so all elements ≤ pivot precede it and all elements > pivot follow, then recurse on the two halves. Average $O(n \log n)$, worst-case $O(n^2)$ (pathological pivot choice — usually mitigated by median-of-three or randomized pivot).

[[parproc-ch04-introduction-to-openmp]] §4.5.1 uses Quicksort as the canonical [[OpenMPTaskDirective|`omp task`]] worked example — because the recursion tree is irregular and dynamically generated, [[ParallelFor|`omp for`]]'s static iteration-distribution model is a poor fit. `task` is the right tool.

## Skeleton

```c
void qs(int *z, int zstart, int zend, int firstcall) {
    #pragma omp parallel
    {
        if (firstcall == 1) {
            #pragma omp single nowait
            qs(z, 0, zend, 0);
        } else {
            if (zstart < zend) {
                int part = separate(z, zstart, zend);
                #pragma omp task
                qs(z, zstart, part-1, 0);
                #pragma omp task
                qs(z, part+1, zend, 0);
            }
        }
    }
}
```

`separate()` partitions in-place around the leftmost element as pivot, returning the pivot's final index.

## Why this structure

- **`omp parallel`** outside — establishes the thread team that will service the task queue.
- **`omp single nowait`** for `firstcall == 1` — exactly one thread enters the root `qs(z, 0, zend, 0)` call. Without `single`, every thread in the team would launch its own full sort. `nowait` removes the implicit barrier so other threads can immediately start grabbing tasks.
- **`omp task`** for each recursive subcall — each subtree is queued as a task; any idle team thread can pick it up. The encountering thread continues to the second `task` without waiting.

The chapter's terse summary: *"OMP system, please make sure that this subtree is handled by some thread eventually."*

## Refinements

- `#pragma omp taskwait` — barrier-like wait for direct child tasks; useful if the parent needs results before continuing.
- Better pivot choice: *"would be better to take, e.g., median of 1st 3 elts"* (in `separate`'s comment).
- Another Quicksort implementation is cross-referenced in §12.1.2 (§4.16).

## Ch12: Separation Process Detail

[[parproc-ch12-parallel-sorting]] §12.1.1 describes the `separate()` function explicitly: `separate(l, h)` returns m such that x[l..m-1] < x[m] ≤ x[m+1..h], and x[m] is in its final resting place. The sub-ranges x[l..m-1] and x[m+1..h] will never leave those index ranges. An alternative separation uses an **exclusive prefix scan** (Ch10) on a binary indicator array (1 = less than pivot) to compute element destinations in parallel.

## Ch12: OpenMP Variant

§12.1.2 gives a second OpenMP form using `#pragma omp for nowait` over a loop of two iterations (i=0 and i=1), calling `qs(newl[i], newh[i])` for each sub-range. `nowait` is correct here because the two sub-ranges are disjoint — no synchronization is needed between threads.

## Ch12: Hyperquicksort Extension

[[Hyperquicksort]] (§12.1.3) extends Quicksort to distributed-memory hypercubes: each d-cube root broadcasts its median as pivot; partner pairs exchange data and split by rank; after d rounds the array is globally sorted across PEs with PE i holding only values less than PE j for all i < j.

## Connections
- [[parproc-ch04-introduction-to-openmp]] — §4.5.1 source.
- [[parproc-ch12-parallel-sorting]] — §12.1.1–12.1.3 source; separation process, OpenMP variant, hyperquicksort.
- [[OpenMPTaskDirective]] — the directive at the heart of the parallelization.
- [[OpenMPSingle]] — `single nowait` for the recursive root.
- [[ParallelPragma]] — outer team-spawner.
- [[OpenMP]] — parent.
- [[ParallelFor]] — the work-sharing alternative that *does not* fit recursion.
- [[LoadBalancing]] — task-queue + work-stealing handles imbalanced recursion trees.
- [[Hyperquicksort]] — distributed-memory extension for hypercube topologies.
- [[PrefixScan]] — alternative parallel separation process via exclusive scan.
