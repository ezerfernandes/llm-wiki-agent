---
title: "BubbleSort"
type: concept
tags: [algorithm, sorting, parallel-computing]
sources: [parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# BubbleSort

Classical in-place comparison sort with O(n²) serial time complexity. Despite its poor serial performance, the inner loop's structure makes it amenable to parallelization.

## Sequential Form

```c
void bubblesort(int *x, int n) {
    for (i = n-1 downto 1)
        for (j = 0 to i)
            compare-exchange(x, i, j, n)
}
```

Where `compare-exchange(x, i, j, n)` swaps x[i] and x[j] if x[i] > x[j].

In the first outer iteration (i = n-1), the largest element "bubbles" all the way to the right end. In the second, the second-largest bubbles to the next-to-last position, and so on.

## Parallel Variant

In the shared-memory setting, assign one thread per value of i. Those threads can work in parallel as long as a thread with a larger i value does not overtake a thread with a smaller i (i.e., does not work on a larger j value). Chunking the data is usually more effective than one thread per element.

The [[OddEvenTransposition]] sort is a popular, more regular parallel variant. The [[CUDA]] implementation is in [[parproc-ch12-parallel-sorting]] §12.3.3.

## Connections

- [[OddEvenTransposition]] — parallel cousin; alternating-phase compare-exchange variant.
- [[CompareExchange]] — the primitive inner operation.
- [[parproc-ch12-parallel-sorting]] — §12.3.1 source.
- [[OpenMP]] — shared-memory parallelization vehicle.
