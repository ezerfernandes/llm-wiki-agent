---
title: "Shearsort"
type: concept
tags: [algorithm, sorting, parallel-computing, mesh-topology]
sources: [parproc-ch12-parallel-sorting]
last_updated: 2026-05-17
---

# Shearsort

A parallel sorting algorithm designed for a 2D mesh of processing elements. Developed by Sen, Shamir, and Isaac Scherson of UC Irvine. The array length n is assumed to be a perfect square, with data initially distributed among the mesh PEs.

## Algorithm

```
for i = 1 to ceil(log2(n)) + 1:
    if i is odd:
        sort each even row in ascending order
        sort each odd row in descending order
    else:
        sort each column in ascending order
```

Runs for ceil(log₂(n)) + 1 phases total. At the end, numbers are sorted in a "snakelike" pattern: row 1 ascending left-to-right, row 2 descending right-to-left, etc., with the global minimum at position (1,1) and the global maximum at (n, n) or (n, 1) depending on parity.

## Example (2×2 mesh)

Starting array:
```
6 | 12
5 |  9
```
After odd phase (row sort: row 1 ascending, row 2 descending):
```
6 | 12
9 |  5
```
After even phase (column sort ascending):
```
6 |  5
9 | 12
```
After odd phase:
```
5 | 6↓
12 ← 9
```
Final snakelike order: 5, 6, 12, 9 (row 1 ascending, row 2 descending).

## Implementation Notes

- A natural domain decomposition assigns each process a group of rows.
- During even-numbered phases (column sorts), a parallel matrix transpose is required. In MPI, `MPI_Alltoall()` is the relevant collective.

## Connections

- [[CompareExchange]] — the primitive used within each row/column sort.
- [[parproc-ch12-parallel-sorting]] — §12.4 source.
- [[MPI]] — `MPI_Alltoall` handles the transpose for column operations.
