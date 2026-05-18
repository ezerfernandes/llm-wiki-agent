---
title: "Dive into Systems — Ch 2.5 Arrays in C"
type: source
tags: [dive-into-systems, c-language, arrays, pointers, dynamic-allocation, memory-layout]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/arrays.html
sources: []
last_updated: 2026-05-17
---

# Dive into Systems — Ch 2.5 Arrays in C

## Summary

The fifth section of [[DiveIntoSystems]] Ch 2 *A Deeper Dive Into C* — by [[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]] — **returns to [[CArray|arrays]] with the full [[Pointer|pointer]] / [[DynamicMemoryAllocation|dynamic-memory]] toolkit Ch 2.2–2.4 supplied**, deepening the [[dis-1-5-arrays-strings|Ch 1.5]] one-dimensional, statically-declared treatment along three axes: (1) **[[DynamicallyAllocatedArray|dynamically allocated 1D arrays]]** sit alongside statically declared ones with identical `arr[i]` indexing and identical function-parameter signatures — the unification [[dis-2-4-dynamic-memory|Ch 2.4]] previewed and Ch 2.5 now ratifies as the headline take-home for arrays; (2) **[[MultidimensionalArray|two-dimensional arrays]]** — both statically declared (`int matrix[N][M]`) and dynamically allocated — finally introduced (Ch 1.5 deferred them here), with the **[[RowMajorOrder|row-major]] memory layout** rule made explicit and the **`int m[][COLS]` parameter-declaration quirk** (first dimension may be elided, *subsequent dimensions must be specified*) given a load-bearing explanation rooted in offset arithmetic; (3) the **two dynamic-2D allocation strategies** — *single `malloc` of `N*M`* (memory-efficient, cache-friendly, single-`[i*M+j]` indexing) vs. *array-of-arrays via N+1 `malloc`s* (programmer-friendly double-indexing `[i][j]`, rows not contiguous, `int **` parameter type) — laid out as an explicit space/speed/ergonomics tradeoff. Codifies the [[ArrayDecay|array-name-decays-to-pointer]] mechanism as the unifying primitive behind Ch 1.5's pass-by-reference exception, Ch 2.3's pass-by-pointer recipe, and Ch 2.4's heap-array indexing.

## Key Claims

- **Static-vs-dynamic 1D unification at the use site.** Heap-allocated arrays use the identical `arr[i]` indexing syntax as statically declared ones; the only thing that differs is the declaration form (`int s[N];` vs. `int *d = malloc(sizeof(int)*N);`). [[dis-2-4-dynamic-memory|Ch 2.4]] previewed this; Ch 2.5 makes it the textbook's working assumption.
- **Function-parameter unification.** *"When passing an array to a function, C copies the value of the base address to the parameter. That is, both the parameter and the argument refer to the same memory locations."* Both [[CArray|static]] and [[DynamicallyAllocatedArray|dynamic]] 1D arrays accept the same `int *` / `int arr[]` parameter signature — this is the [[dis-2-3-pointers-functions|Ch 2.3]] [[PassByPointer|pass-by-pointer]] mechanism reused (the array name **[[ArrayDecay|decays]]** to a pointer to its first element).
- **2D arrays are stored in [[RowMajorOrder|row-major]] order.** A statically declared `int matrix[N][M]` lays out *all elements of row 0, then all of row 1, ...* in **contiguous memory addresses** — the compiler computes `matrix[i][j]` as `*(matrix_base + i*M + j)`. This is what justifies the parameter-declaration rule below.
- **Multidimensional parameter declarations: first dimension optional, others mandatory.** *"For multidimensional array parameters, you must indicate that the parameter is a multidimensional array, but you can leave the size of the first dimension unspecified (for good generic design). The sizes of other dimensions must be fully specified so that the compiler can generate the correct offsets into the array."* The trailing dimensions feed into the offset arithmetic; without them, the compiler can't compute `&m[i][j]`. Example: `void init_matrix(int m[][COLS], int rows)`.
- **Two dynamic-2D allocation strategies, two tradeoffs.**
    - *Method 1 — single `malloc`* of `N*M` elements stored as `int *`. **Memory-efficient** (one heap header, one contiguous block, best cache locality), but indexing is **manual offset arithmetic**: `arr[i*M + j]` rather than `arr[i][j]`. Function parameter type: `int *`.
    - *Method 2 — array of arrays* via N+1 `malloc` calls (one outer `int **` of `N` row pointers + one inner `int *` per row). **Programmer-friendly** `arr[i][j]` double indexing, but **rows are not contiguous** in memory, N+1 heap headers waste bytes, and pointer-chase per row hurts cache locality. Function parameter type: `int **`.
- **The double-indexing-syntax restriction.** *"The double-indexing syntax (`[i][j]`) of statically declared 2D arrays cannot be used when allocating a 2D array using [Method 1]."* That syntactic affordance is the headline ergonomic reason a programmer might choose Method 2 despite its memory cost.
- **Cleanup discipline scales with allocation method.** Method 1: one `free`. Method 2: free each row in a loop, *then* free the outer pointer array.
- **`#define` for array sizes.** The chapter's style recommendation — use `#define N 50` and `#define M 100` at the top of the file rather than literal sizes scattered through the code. Pays off as soon as dimensions need to change and shows up in every Ch 2.5 example.
- **`malloc` NULL-checking is uniform across 1D and 2D.** Both allocation methods require the [[dis-2-4-dynamic-memory|Ch 2.4]] guard pattern — and Method 2 needs it on *each* of the N+1 calls.

## Key Quotes

> "When passing an array to a function, C copies the value of the base address to the parameter. That is, both the parameter and the argument refer to the same memory locations."

> "For multidimensional array parameters, you must indicate that the parameter is a multidimensional array, but you can leave the size of the first dimension unspecified (for good generic design). The sizes of other dimensions must be fully specified so that the compiler can generate the correct offsets into the array."

> "The double-indexing syntax (`[i][j]`) of statically declared 2D arrays cannot be used when allocating a 2D array using this method."

## Connections

- [[DiveIntoSystems]] — the textbook; this is Ch 2.5 of Ch 2 *A Deeper Dive Into C*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-1-5-arrays-strings]] — the Ch 1 introduction to [[CArray|arrays]] that *deferred multidimensional arrays to Ch 2.5*. Ch 2.5 picks up that thread.
- [[dis-2-2-pointers]] / [[dis-2-3-pointers-functions]] / [[dis-2-4-dynamic-memory]] — the [[Pointer]] / [[PassByPointer]] / [[Malloc]] machinery Ch 2.5 reuses.
- [[CArray]] — extended here from 1D static to include 2D static + dynamic forms.
- [[DynamicallyAllocatedArray]] — the heap 1D array now formally tied to the static-arr-decays-to-pointer story.
- [[MultidimensionalArray]] — the new aggregate shape introduced this chapter.
- [[RowMajorOrder]] — the layout rule for static 2D arrays.
- [[ArrayDecay]] — the array-name-as-pointer-to-first-element mechanism Ch 2.5 finally names.
- [[ArrayOfArrays]] — Method 2's dynamic 2D representation (`int **`, N+1 mallocs).
- [[ArrayIndexing]] — extended with the `arr[i*M + j]` manual-offset pattern.
- [[PassByReference]] — the Ch 1.5 array-by-reference rule re-explained mechanistically via [[ArrayDecay]].
- [[Malloc]] / [[Free]] / [[SizeOf]] / [[Pointer]] / [[PointerType]] — the underlying machinery.
- [[CMemoryAddress]] — the base-address concept central to the "C copies the value of the base address" quote.

## Contradictions

- None. Ch 2.5 *completes* [[dis-1-5-arrays-strings|Ch 1.5]]'s multidimensional-array deferral and *ratifies* [[dis-2-4-dynamic-memory|Ch 2.4]]'s static/dynamic array unification. The chapter explicitly grounds [[dis-1-5-arrays-strings|Ch 1.5]]'s [[PassByReference|pass-by-reference]] exception in the [[ArrayDecay|array-decay]] mechanism the [[dis-2-2-pointers|Ch 2.2]] pointer machinery makes nameable — closing the loop opened in Ch 1.4/1.5 and reconciled in Ch 2.2.
