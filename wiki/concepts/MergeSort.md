---
title: "MergeSort"
type: concept
tags: [algorithm, sorting, parallel-computing, divide-and-conquer]
sources: [parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# MergeSort

Classic divide-and-conquer comparison sort. Recursively split the array in half, sort each half, then merge the two sorted halves. O(n log n) time, O(n) extra space (for the merge step). Assumes array length is a power of 2 in the standard formulation.

## Sequential Form

```c
// initially called with l = 0 and h = n-1
void seqmergesort(int *x, int l, int h) {
    seqmergesort(x, 0, h/2-1);
    seqmergesort(x, h/2, h);
    merge(x, l, h);
}
```

`merge()` should be done in-place (no auxiliary array). In the message-passing context the merge function corresponds to combining two sorted streams element by element.

## Parallel Forms

### Shared-Memory

Analogous to shared-memory [[Quicksort]]: assign different recursive sub-calls to different threads. One thread handles the left half, another the right half; parallelism is bounded by the recursion depth.

### Message-Passing on a Binary Tree

Organize PEs into a binary tree (e.g. 7 nodes: root 0, children 1 and 2, leaves 3–6). Data is initially distributed in the leaf nodes.

1. Each leaf sorts its local data sequentially.
2. Each leaf streams its sorted elements to its parent one at a time (in ascending order).
3. Each non-leaf node merges the two streams it receives from its children and forwards the merged stream upward.
4. The root eventually holds the full sorted array.

**Load balancing trade-off:** Sending one element at a time maximizes upstream utilization but increases per-element overhead. Buffering larger chunks reduces overhead but causes upstream nodes to idle while waiting for a full chunk. The optimal chunk size must be determined empirically.

## Connections

- [[BitonicMergesort]] — a network-based parallel mergesort using [[CompareExchange]] operations on bitonic sequences.
- [[CompareExchange]] — primitive used in the message-passing and bitonic variants.
- [[Quicksort]] — alternative divide-and-conquer sort; parallel structure is similar.
- [[parproc-ch12-parallel-sorting]] — §12.2 source.
- [[MPI]] — message-passing tree implementation vehicle.
- [[OpenMP]] — shared-memory parallelization vehicle.
