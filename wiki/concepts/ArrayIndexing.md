---
title: "Array Indexing (C)"
type: concept
tags: [c-language, arrays, indexing]
sources: [dis-1-5-arrays-strings, dis-2-5-arrays]
last_updated: 2026-05-17
---

# Array Indexing (C)

**Array indexing** in [[CLanguage|C]] is the `arr[i]` subscript syntax that selects the `i`-th element of a [[CArray|C array]]. Two facts make it harder than its Python / Java equivalents look:

1. **Zero-based.** For an `int arr[N]`, valid indices are `0`, `1`, …, `N - 1`. Index `N` is *one past the end* and reading or writing it is **undefined behavior**.
2. **Unchecked.** The [[CLanguage|C]] language performs **no [[BoundsChecking|bounds check]]** at compile time or runtime. `arr[N]`, `arr[-1]`, `arr[1000000]` all *compile*; what they do at runtime depends on whatever happens to be at that memory address and on the optimizer's mood. Per [[dis-1-5-arrays-strings|Ch 1.5]] of [[DiveIntoSystems]]: *"in C, it's up to the programmer to ensure that their code uses only valid index values when indexing into arrays."*

## Example — the off-by-one footgun

```c
int array[10];      // valid indices: 0..9
array[10] = 100;    // UNDEFINED BEHAVIOR — silently writes past the end
```

There is no exception, no `IndexError`, no runtime panic. The compiler may or may not warn (`-Wall` catches some such patterns); the program may *appear* to work, then corrupt a stack frame and crash three function calls later. Diagnosing this is the standard rite of passage into [[CLanguage|C]] programming.

## Pattern: index-walk with a manually-tracked length

Because the *used length* of a [[CArray|C array]] is not stored by the language, idiomatic iteration is a [[ForLoop|`for`]] loop with the length passed alongside:

```c
void print_ints(int a[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}
```

The `i < n` guard is the *only* thing keeping the access in bounds — the language won't help.

## Cross-walk

- [[Python]] `lst[i]` raises `IndexError` on out-of-range access; `lst[-1]` is the last element.
- [[CLanguage|C]] `arr[i]` does whatever the underlying memory access happens to do; `arr[-1]` reads the word *before* the array (sometimes a previous stack variable, sometimes another array, sometimes a guard page).

## Pointer-arithmetic definition and manual 2D offset

[[dis-2-5-arrays|Ch 2.5]] makes explicit the underlying pointer-arithmetic identity: `arr[i]` is defined as `*(arr + i)`. This is what lets statically-declared and [[DynamicallyAllocatedArray|dynamically-allocated]] 1D arrays share the same indexing syntax — both reduce to "add `i` to the base pointer, dereference." It also means the [[ArrayDecay|decayed-pointer]] receiver in a function sees no difference between a stack array and a heap array.

For 2D arrays allocated as a *single* `malloc` (Ch 2.5's Method 1), the programmer writes the [[RowMajorOrder|row-major]] offset by hand:

```c
int *arr = malloc(sizeof(int) * N * M);
arr[i*M + j] = 42;                /* manual 2D offset — no [i][j] available */
```

The double-indexing `arr[i][j]` form is available only for statically declared 2D arrays and for [[ArrayOfArrays|dynamic arrays-of-arrays]] (`int **`); the single-`malloc` `int *` form gives it up in exchange for contiguous memory and a single heap header.

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 §1.5.2 *Array Access Methods* introduces the zero-based, unchecked rule.
- [[dis-2-5-arrays]] — Ch 2.5 names the `arr[i] == *(arr + i)` pointer-arithmetic identity, the manual `arr[i*M + j]` 2D-offset pattern, and the syntactic difference between `int *` and `int **` 2D forms.
