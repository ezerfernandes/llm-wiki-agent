---
title: "Array (C)"
type: concept
tags: [c-language, arrays, data-structures, memory]
sources: [dis-1-5-arrays-strings, dis-2-5-arrays]
last_updated: 2026-05-17
---

# Array (C)

A **C array** is the [[CLanguage|C]] language's first **aggregate** data type: an ordered, fixed-capacity, contiguous run of elements *all of the same type*. The type and capacity are baked into the declaration — `int arr[10]` is a different type from `int arr[20]` — and the storage is laid out in **consecutive memory locations**. Per [[dis-1-5-arrays-strings|Ch 1.5]] of [[DiveIntoSystems]], *"C dictates the array layout in program memory"*, which is what later lets pointer arithmetic walk an array by adding to its base address.

## Declaration

```c
int arr[10];     // array of 10 ints — capacity is part of the type
char str[20];    // array of 20 chars
double xs[3] = {1.0, 2.0, 3.0};  // declaration + initializer
```

## Fixed capacity, manually-tracked length

The *capacity* (10, 20, …) is a compile-time constant. Unlike a [[Python]] `list` or a Java `ArrayList`, a C array cannot grow. The *used length* (how many of those slots actually hold meaningful data) is **not stored anywhere by the language** — the programmer carries it in a separate variable and threads it through every function call.

## [[ArrayIndexing|Indexing]] is zero-based and unchecked

Valid indices run `0` through `capacity - 1`. No [[BoundsChecking|bounds check]] is performed at compile time or runtime — `arr[10]` on an `int arr[10]` is *undefined behavior*, not a thrown exception. Per [[dis-1-5-arrays-strings|Ch 1.5]]: *"in C, it's up to the programmer to ensure that their code uses only valid index values when indexing into arrays."*

## Arrays in [[Function|function]] calls — the [[PassByValue|pass-by-value]] exception

The chapter's headline pivot: arrays do **not** behave like the scalar parameters [[dis-1-4-functions|Ch 1.4]] introduced. When you pass an array to a function, what's copied at the call boundary is the array's **base address** — so mutating `a[i]` *inside* the function persists in the caller's array. See [[PassByReference]]. Mutating the parameter variable itself (`size = 2;`) still follows the [[PassByValue|pass-by-value]] rule for the parameter slot.

```c
void test(int a[], int size) {
    if (size > 3) {
        a[3] = 8;   // VISIBLE to caller — array passed by base address
    }
    size = 2;       // local-only — int passed by value
}
```

The full mechanism (array-name-decays-to-pointer-to-first-element) is unpacked in Ch 1.6.

## [[CString|C strings]] are a special case

A [[CString|C string]] is a `char` array whose end is marked by the [[NullTerminator|null character `'\0'`]] — see [[CString]] and [[NullTerminator]] for the sentinel discipline. The library `<string.h>` ([[StringLibrary]]) is the standard tooling.

## Multidimensional arrays

`int matrix[3][4]`-style declarations — the **[[MultidimensionalArray|multidimensional]]** generalization — were deferred by [[dis-1-5-arrays-strings|Ch 1.5]] and are introduced in [[dis-2-5-arrays|Ch 2.5]]. They store elements in **[[RowMajorOrder|row-major order]]** (row 0 contiguously, then row 1, ...) and require *every dimension except the first* to be specified in function parameter declarations (`void f(int m[][COLS], int rows)`) so the compiler can compute `&m[i][j]` as `m_base + i*COLS + j`. Dynamic 2D arrays come in two flavors per [[dis-2-5-arrays|Ch 2.5]]: a single-`malloc` `int *` form (memory-efficient, manual `arr[i*M+j]` offset) and an [[ArrayOfArrays|array-of-arrays]] `int **` form (programmer-friendly `arr[i][j]`, N+1 mallocs, rows not contiguous).

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 introduces declaration, indexing, the no-bounds-checking rule, the function-parameter exception, and one-dimensional layout.
- [[dis-2-5-arrays]] — Ch 2.5 returns to arrays with the [[Pointer|pointer]] / [[Malloc|`malloc`]] toolkit: ratifies the static-vs-dynamic [[DynamicallyAllocatedArray|1D array]] unification at the use site and at function parameters (the *"C copies the value of the base address to the parameter"* quote), introduces [[MultidimensionalArray|2D arrays]] (both static and the two dynamic forms), the [[RowMajorOrder|row-major]] layout rule, the trailing-dimension parameter rule, and names the [[ArrayDecay|array-decay]] mechanism underneath the [[dis-1-5-arrays-strings|Ch 1.5]] pass-by-reference exception.
