---
title: "Array of Arrays (C — Dynamic 2D)"
type: concept
tags: [c-language, arrays, dynamic-allocation, heap, multidimensional]
sources: [dis-2-5-arrays]
last_updated: 2026-05-17
---

# Array of Arrays (C — Dynamic 2D)

The **array-of-arrays** form is the second of the two strategies [[dis-2-5-arrays|DIS Ch 2.5]] gives for dynamically allocating a 2D array in [[CLanguage|C]]: instead of one big `malloc` of `N*M` elements, allocate **N+1 separate heap blocks** — one outer array of `N` row pointers (`int **`), plus one inner array of `M` elements per row (`int *` per row).

The headline payoff: it preserves the **`arr[i][j]` double-indexing syntax** of statically declared 2D arrays — which the single-`malloc` form ([[MultidimensionalArray]] Method 1) gives up in favor of manual `arr[i*M + j]` offset arithmetic.

## The allocation pattern

```c
#define N 50
#define M 100

int **two_d_array;
two_d_array = malloc(sizeof(int *) * N);          /* outer: N row pointers */
if (two_d_array == NULL) { exit(1); }

for (int i = 0; i < N; i++) {
    two_d_array[i] = malloc(sizeof(int) * M);     /* inner: row of M ints */
    if (two_d_array[i] == NULL) { exit(1); }
}

two_d_array[3][7] = 42;                           /* normal double indexing */
```

Per [[dis-2-5-arrays|Ch 2.5]] this is the **programmer-friendly** method: indexing reads exactly like statically declared 2D arrays, and functions take an `int **` parameter that admits the same `m[i][j]` access. The cost is paid in **memory** (N+1 heap headers vs. 1) and **cache locality** (rows live wherever the heap put them — usually not contiguous with one another, and not contiguous with the row-pointer array).

## Comparison with the single-`malloc` method

| Aspect | Single `malloc` (Method 1) | Array of arrays (Method 2) |
|---|---|---|
| **Allocations** | 1 | N+1 |
| **Pointer type** | `int *` | `int **` |
| **Indexing** | `arr[i*M + j]` (manual offset) | `arr[i][j]` (double indexing) |
| **Rows contiguous?** | Yes — one block | No — each row is its own block |
| **Heap header overhead** | 1 header | N+1 headers |
| **Cache locality** | Best — sequential access streams | Worse — pointer indirection + row jumps |
| **Resemblance to static 2D** | Different syntax | **Same syntax** |
| **Function parameter type** | `void f(int *arr, int N, int M)` | `void f(int **arr, int N, int M)` |

Note the parameter types are **not interchangeable** — an `int **` is not the same type as the `int (*)[M]` that a static `int m[N][M]` decays to. Functions written for static 2D arrays (`int m[][M]`) **cannot accept** array-of-arrays inputs without a different signature.

## Cleanup — the order matters

Free in reverse order of allocation:

```c
for (int i = 0; i < N; i++) {
    free(two_d_array[i]);                         /* free each row first */
}
free(two_d_array);                                /* then free the outer array */
two_d_array = NULL;
```

Freeing the outer array first ([[MemoryLeak|leaks]] the rows because their pointers were only reachable through it). Skipping any row [[MemoryLeak|leaks]] that row's M ints.

## When to pick which

[[dis-2-5-arrays|Ch 2.5]] frames the choice as an explicit space/speed/ergonomics tradeoff:

- **Single `malloc`** when memory or cache performance matters, when `N*M` won't overflow `size_t`, when you don't mind the index-math syntax, or when interoperating with column-major linear-algebra libraries.
- **Array of arrays** when readability matters, when rows have *different* lengths (ragged 2D — single-`malloc` can't express this), or when you want to swap rows in O(1) by swapping pointers.

## Connections

- [[dis-2-5-arrays]] — defining source.
- [[MultidimensionalArray]] — the abstraction this is one implementation of.
- [[RowMajorOrder]] — the layout the *single-`malloc`* form uses; array-of-arrays explicitly *does not* guarantee row-major contiguity.
- [[DynamicallyAllocatedArray]] — the 1D base case.
- [[Malloc]] / [[Free]] / [[NullPointer]] — the underlying API; the N+1-`malloc` pattern requires NULL-checking each call.
- [[Pointer]] / [[PointerType]] — `int **` is the headline new pointer-to-pointer type Ch 2.5 introduces.
- [[ArrayDecay]] — what static 2D decays to; explains why `int **` and `int (*)[M]` are not interchangeable parameter types.
- [[MemoryLeak]] — the failure mode of incomplete cleanup.
- [[CLanguage]] / [[DiveIntoSystems]].
