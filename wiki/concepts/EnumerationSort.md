---
title: "Enumeration Sort"
type: concept
tags: [algorithm, sorting, parallel-computing]
sources: [parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# Enumeration Sort

A simple comparison-based sort that determines each element's final position by counting how many other elements are smaller than it.

## Algorithm

For array x of length n (assuming no tied values), placing results in y:

```
for all i in 0..n-1:
    count = 0
    elt = x[i]
    for all j in 0..n-1:
        if x[j] < elt then count++
    y[count] = elt
```

Example: array (12, 5, 13, 18, 6). There are 2 elements less than 12 (namely 5 and 6), so 12 goes to position 2 in the sorted output (5, 6, 12, 13, 18).

## Parallelization

- The **outer loop** is easily parallelized: each iteration i is independent and can be assigned to a different thread.
- Alternatively the **inner loop** can be parallelized for each i, using a parallel reduction to sum the comparisons.

The algorithm is O(n²) work regardless of parallelization; it is not competitive with O(n log n) algorithms for large inputs but is notable for its trivial parallelism structure and freedom from data dependencies between outer iterations.

## Connections

- [[parproc-ch12-parallel-sorting]] — §12.7 source.
- [[OpenMP]] — natural vehicle for outer-loop parallelization.
- [[CUDA]] — each thread can handle one outer-loop iteration.
