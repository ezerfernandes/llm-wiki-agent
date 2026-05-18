---
title: "Pointer Arithmetic (C)"
type: concept
tags: [c-language, pointers, arrays, pointer-arithmetic, type-system]
sources: [dis-2-9-4-pointer-arithmetic]
last_updated: 2026-05-17
---

# Pointer Arithmetic (C)

**Pointer arithmetic** is the [[CLanguage|C]] language rule that adding or subtracting an integer to/from a [[Pointer|pointer]] advances the pointer by that many **elements of the pointed-to type**, not by that many **bytes**. Per [[dis-2-9-4-pointer-arithmetic|DIS Ch 2.9.4]]: *"`ptr + N` makes the pointer point `N` storage locations beyond its current value (or makes it point to `N` elements beyond the current element)."*

This is the page [[dis-2-2-pointers|Ch 2.2]] named-and-deferred, [[dis-2-5-arrays|Ch 2.5]] silently relied on for its `arr[i] == *(arr + i)` identity, and [[dis-2-4-dynamic-memory|Ch 2.4]] presupposed for the static-vs-dynamic indexing parity.

## The core rule: type-scaled stride

Given `T *ptr`, the address arithmetic is:

| Expression | Address computed | Bytes advanced |
|---|---|---|
| `ptr + 1` | `ptr` + `sizeof(T)` | `sizeof(T)` |
| `ptr + N` | `ptr` + `N * sizeof(T)` | `N * sizeof(T)` |
| `ptr - 1` | `ptr` − `sizeof(T)` | `sizeof(T)` (backward) |
| `ptr - N` | `ptr` − `N * sizeof(T)` | `N * sizeof(T)` (backward) |

The compiler — not the programmer — multiplies `N` by [[SizeOf|`sizeof(T)`]]. Programmer writes elements; compiler emits bytes. Per Ch 2.9.4: *"a programmer can simply write `ptr++` to make a pointer point to the next element value. The compiler generates code to add the appropriate number of bytes."*

## Concrete byte counts (typical 64-bit platform)

| Pointer type | `ptr++` advances by |
|---|---|
| `char *` | 1 byte |
| `short *` | 2 bytes |
| `int *` | 4 bytes |
| `long *` | 8 bytes |
| `double *` | 8 bytes |
| `struct studentT *` | `sizeof(struct studentT)` bytes |

The type system is what makes pointer arithmetic safe — wrong-type pointers produce wrong-stride traversal. Casting `(char *)iptr` then incrementing walks one byte at a time through an `int` array; useful for byte-level inspection, dangerous for element access.

## The `arr[i] == *(arr + i)` identity

Pointer arithmetic is the **definition** of [[ArrayIndexing|array indexing]] in [[CLanguage|C]]. `arr[i]` is syntactic sugar for `*(arr + i)`:

```c
int arr[10];
arr[3] = 7;           /* identical to */ *(arr + 3) = 7;
```

Because `arr` [[ArrayDecay|decays]] to `int *` and pointer arithmetic auto-scales by `sizeof(int)`, the indexing operator works for any element type without programmer-supplied stride math. The unification of static and dynamic [[CArray|arrays]] at `arr[i]` ([[dis-2-4-dynamic-memory|Ch 2.4]]) is grounded here: both forms produce an `int *`, both feed into the same `*(p + i)` reduction.

## The three operations

| Operation | Result type | Meaning |
|---|---|---|
| `ptr + n` (or `n + ptr`) | `T *` | Pointer to element `n` positions later |
| `ptr - n` | `T *` | Pointer to element `n` positions earlier |
| `p1 - p2` (same type) | `ptrdiff_t` | Element-count distance between two pointers (see [[PointerDifference]]) |

What you **cannot** do: `ptr + ptr` (no meaning), `ptr * n` (no meaning), arithmetic on [[VoidPointer|`void *`]] (no `sizeof(*p)` available — the compiler has no stride to multiply by).

## The `void *` carve-out

[[VoidPointer|`void *`]] **cannot be the operand of pointer arithmetic** in standard [[CLanguage|C]]. The compiler needs `sizeof(*p)` to compute the stride, and a `void` pointee has no size. GCC permits it as a non-standard extension (treating `void *` arithmetic as `char *` arithmetic — 1-byte stride), but portable code casts to a concrete type first: `((char *)vp) + n`.

## The 2D-array divergence

For dynamically allocated 2D arrays ([[dis-2-5-arrays|Ch 2.5]] / [[MultidimensionalArray|MultidimensionalArray]]), pointer arithmetic behaves differently across the two allocation strategies:

| Form | Rows contiguous? | Pointer-arithmetic walk |
|---|---|---|
| Single `malloc(N*M*sizeof(int))` ([[RowMajorOrder|row-major]] flat block) | Yes | One `ptr` can walk all `N*M` elements via `ptr++` — no per-row reset |
| [[ArrayOfArrays|Array-of-arrays]] (`int **`, N+1 mallocs) | **No** | Pointer must be **reset to the row base** at each row — cross-row arithmetic walks into unrelated heap chunks |

Per Ch 2.9.4: *"if the 2D array is allocated as a single `malloc` of total rows times columns space … then all the rows are in contiguous memory … the pointer only needs to be initialized to point to the base address, and then pointer arithmetic will correctly access any element."* And conversely: *"if … a program uses multiple `malloc` calls to dynamically allocate individual rows … then the pointer must be reset to point to the address of the starting element of every row."*

## The standing recommendation: don't

The chapter closes with an unusually direct anti-recommendation: *"in most cases, we recommend against using pointer arithmetic to access array elements: it's easy to make errors and more difficult to debug when you do."*

Because `arr[i]` generates **identical machine code** to `*(arr + i)`, the only reason to prefer the pointer-arithmetic form is style or specific iteration patterns where carrying a pointer is cleaner than carrying an index. The cost — off-by-one errors that walk into adjacent memory, no compiler help — usually outweighs the benefit. The idiom survives in performance-critical inner loops, byte-level routines (where the pointer *is* the cursor), and library code that genuinely needs a `T *` cursor parameter.

## Worked example

```c
#define N 10
int arr[N];
int *p = arr;           /* array decay: p = &arr[0] */

/* Equivalent loops — same generated code */

/* Indexing form (preferred): */
for (int i = 0; i < N; i++)
    arr[i] = i * i;

/* Pointer-arithmetic form: */
for (int i = 0; i < N; i++) {
    *p = i * i;
    p++;                /* advances by sizeof(int) bytes */
}
```

The second form is what [[dis-2-9-4-pointer-arithmetic|Ch 2.9.4]] illustrates; the first is what the chapter recommends for production code.

## Cross-walk

- **[[Python]]** has no pointer arithmetic — list indexing carries its own bounds-checked offset computation.
- **[[CPlusPlus|C++]]** inherits [[CLanguage|C]]'s pointer arithmetic and adds iterator arithmetic (`it + n`, `it1 - it2`) over standard containers; same hazards.
- **[[Rust]]** restricts raw-pointer arithmetic to `unsafe` blocks via `ptr.add(n)` / `ptr.offset(n)`; safe code uses [[ArrayDecay|slice]] indexing with bounds checks.

## Connections

- [[dis-2-9-4-pointer-arithmetic]] — defining source.
- [[Pointer]] / [[PointerType]] — the value class and type system the arithmetic operates over.
- [[PointerIncrement]] — `ptr++` / `ptr--` / `ptr += N` — the specific increment forms.
- [[PointerDifference]] — `p1 - p2` — the subtractive companion operation.
- [[ArrayDecay]] — the mechanism that produces the pointer the arithmetic starts from.
- [[ArrayIndexing]] — `arr[i]` defined as `*(arr + i)` — sugar over pointer arithmetic.
- [[DereferenceOperator]] — the partner operator; arithmetic produces an address, dereference produces the value.
- [[SizeOf]] — what the compiler multiplies by to convert element offsets into byte offsets.
- [[VoidPointer]] — the pointer type that **cannot** be the operand of pointer arithmetic.
- [[MultidimensionalArray]] / [[ArrayOfArrays]] / [[RowMajorOrder]] — the 2D cases where arithmetic continuity vs per-row reset diverges.
- [[BufferOverflow]] — the failure mode that motivates Ch 2.9.4's anti-recommendation.
- [[CLanguage]] / [[DiveIntoSystems]].
