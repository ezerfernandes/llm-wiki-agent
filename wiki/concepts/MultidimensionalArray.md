---
title: "Multidimensional Array (C)"
type: concept
tags: [c-language, arrays, memory-layout, multidimensional]
sources: [dis-2-5-arrays]
last_updated: 2026-05-17
---

# Multidimensional Array (C)

A **multidimensional array** in [[CLanguage|C]] is an [[CArray|array]] whose elements are themselves arrays — declared with two or more bracketed dimensions: `int matrix[N][M]`, `double cube[A][B][C]`. Per [[dis-2-5-arrays|DIS Ch 2.5]] the canonical case is the **two-dimensional array** (`int matrix[50][100]`), a grid of `N` rows × `M` columns of same-type elements. [[dis-1-5-arrays-strings|Ch 1.5]] introduced 1D arrays and explicitly **deferred** multidimensional arrays to Ch 2.5.

## Static declaration

```c
#define ROWS 50
#define COLS 100
int matrix[ROWS][COLS];      /* 5,000-int grid */
int val = matrix[3][7];      /* element at row 3, column 7 */
```

Both dimensions are part of the type — `int[50][100]` is a different type from `int[50][101]`. Storage is **contiguous in [[RowMajorOrder|row-major order]]**: all elements of row 0, followed by all of row 1, ... — `matrix[i][j]` is computed as `*(matrix_base + i*COLS + j)`.

## Iteration pattern — nested loops

```c
for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
        matrix[i][j] = i * COLS + j;
    }
}
```

Walking the *inner* index `j` fastest matches the [[RowMajorOrder|row-major]] layout and is cache-friendly; walking `i` fastest causes column-strided access that thrashes cache lines.

## Function parameters — the trailing-dimension rule

[[dis-2-5-arrays|Ch 2.5]]: *"for multidimensional array parameters, you must indicate that the parameter is a multidimensional array, but you can leave the size of the first dimension unspecified (for good generic design). The sizes of other dimensions must be fully specified so that the compiler can generate the correct offsets into the array."*

```c
void init_matrix(int m[][COLS], int rows) {
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < COLS; j++)
            m[i][j] = 0;
}
```

The compiler needs `COLS` to compute `&m[i][j]` as `m_base + i*COLS + j`. The first dimension can be left blank (`int m[][COLS]`) because it's only used by the caller's bounds discipline — not by offset arithmetic.

## Dynamic 2D allocation — two methods

Heap-allocated 2D arrays have two idioms with different tradeoffs ([[dis-2-5-arrays|Ch 2.5]]):

| Method | Allocation | Indexing | Param type | Cache locality | Memory cost |
|---|---|---|---|---|---|
| **Single `malloc`** | `int *arr = malloc(sizeof(int)*N*M);` | `arr[i*M + j]` (manual offset) | `int *` | **Best** — one contiguous block | One heap header |
| **[[ArrayOfArrays|Array of arrays]]** | N+1 `malloc`s — outer `int **` + N row `int *` | `arr[i][j]` (double indexing) | `int **` | Worse — rows scattered, pointer chase | N+1 headers |

The chapter notes: *"the double-indexing syntax (`[i][j]`) of statically declared 2D arrays cannot be used when allocating a 2D array using [the single-`malloc`] method."* That syntactic restriction is the headline ergonomic reason for picking the [[ArrayOfArrays|array-of-arrays]] form despite its memory cost.

## Cleanup

```c
/* Method 1: single malloc */
free(arr); arr = NULL;

/* Method 2: array of arrays */
for (int i = 0; i < N; i++) free(arr[i]);
free(arr); arr = NULL;
```

## Three-dimensional and higher

The same rules generalize: `int cube[A][B][C]` lays out row-major as `cube[i][j][k] == *(base + i*B*C + j*C + k)`; the parameter form `void f(int c[][B][C], int a)` requires every dimension except the first.

## Connections

- [[dis-2-5-arrays]] — defining source.
- [[CArray]] — the 1D base case.
- [[ArrayIndexing]] — extended here with the `arr[i*M + j]` manual-offset pattern.
- [[RowMajorOrder]] — the layout rule.
- [[ArrayDecay]] — the mechanism that turns `int matrix[N][M]` into `int (*)[M]` at function call sites.
- [[ArrayOfArrays]] — the `int **` dynamic-2D representation.
- [[Malloc]] / [[Free]] — the heap-allocation primitives.
- [[CLanguage]] / [[DiveIntoSystems]].
