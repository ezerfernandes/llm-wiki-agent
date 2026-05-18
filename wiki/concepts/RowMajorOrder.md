---
title: "Row-Major Order"
type: concept
tags: [c-language, arrays, memory-layout, cache, parallel-computing]
sources: [dis-2-5-arrays, parproc-appA-systems-issues]
last_updated: 2026-05-17
---

# Row-Major Order

**Row-major order** is the memory layout convention [[CLanguage|C]] uses for [[MultidimensionalArray|multidimensional arrays]]: all elements of row 0 are stored contiguously, followed by all elements of row 1, and so on. Per [[dis-2-5-arrays|DIS Ch 2.5]] a statically declared `int matrix[N][M]` is *"allocated to contiguous memory addresses"* with the row-by-row arrangement.

## The indexing formula

For an `N × M` matrix laid out in row-major order, the element at logical position `(i, j)` lives at byte offset:

```
offset_bytes(i, j) = (i * M + j) * sizeof(elem)
```

This is what the compiler emits for `matrix[i][j]` on a static 2D array, and what the programmer writes by hand when using [[dis-2-5-arrays|Ch 2.5]]'s **single-`malloc`** dynamic-2D method:

```c
int *arr = malloc(sizeof(int) * N * M);
arr[i*M + j] = 42;                  /* manual row-major offset */
```

## Why the trailing dimension matters in function parameters

The chapter's load-bearing consequence: when a multidimensional array is a function parameter, *every dimension except the first* must be specified, because the offset formula needs `M` (and any further trailing dimensions). Per [[dis-2-5-arrays|Ch 2.5]]: *"the sizes of other dimensions must be fully specified so that the compiler can generate the correct offsets into the array."*

```c
void init(int m[][COLS], int rows);   /* COLS required — first dim optional */
```

## Cache-locality implication

Row-major layout means **the rightmost (innermost) index varies fastest in memory**. Loops should walk the rightmost index in the inner loop to traverse memory sequentially, hit the same cache line repeatedly, and let the hardware prefetcher do its job:

```c
/* CACHE-FRIENDLY — inner loop walks contiguous memory */
for (int i = 0; i < N; i++)
    for (int j = 0; j < M; j++)
        sum += m[i][j];

/* CACHE-HOSTILE — inner loop strides by M elements */
for (int j = 0; j < M; j++)
    for (int i = 0; i < N; i++)
        sum += m[i][j];
```

The latter form fetches one element per cache line and ejects it before the next iteration of the inner loop reuses the same line. For large `N`, `M` this can run an order of magnitude slower than the row-major-aligned version.

## Contrast — column-major

[[Fortran]], [[MATLAB]], R, and most numerical-linear-algebra libraries store matrices in **column-major** order — the *leftmost* index varies fastest. [[CUBLAS|cuBLAS]] is FORTRAN-style column-major even when called from [[CLanguage|C]] — a notable trap when mixing CUDA and C code (already flagged on the [[CUBLAS]] page). [[Numpy|NumPy]] arrays default to row-major (`C order`) but support both via the `order='F'` flag.

## Parallel programming community usage (from [[parproc-appA-systems-issues]])

[[NormMatloff]]'s Appendix A §A.3.1 explicitly states: *"You'll see this fact used a lot in this book, and in general in code written in the parallel processing community."* The row-major indexing formula `i*c + j` (element (i,j) of a c-column array stored at flat index i*c+j) appears throughout parallel matrix and image-processing code. The appendix also shows subarray access via pointer arithmetic: `sum(z+20, 10)` accesses row 2 of a 3×10 array by passing a pointer to the start of that row.

## Connections

- [[dis-2-5-arrays]] — defining source.
- [[parproc-appA-systems-issues]] — §A.3.1; parallel-community usage note and subarray pointer arithmetic.
- [[MultidimensionalArray]] — the structure this layout applies to.
- [[CArray]] / [[ArrayIndexing]] — the 1D base case extended.
- [[ArrayDecay]] — paired mechanism; explains why `int (*)[M]` (pointer-to-row-of-M-ints) is the post-decay type of a 2D static array.
- [[Malloc]] / [[DynamicallyAllocatedArray]] — the single-`malloc` dynamic 2D method uses the row-major formula explicitly.
- [[CUBLAS]] — column-major counterexample inside CUDA.
- [[CLanguage]] / [[DiveIntoSystems]].
