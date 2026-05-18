---
title: "Array Decay (C)"
type: concept
tags: [c-language, arrays, pointers, calling-convention, type-system]
sources: [dis-2-5-arrays]
last_updated: 2026-05-17
---

# Array Decay (C)

**Array decay** (a.k.a. *pointer decay*) is the [[CLanguage|C]] language rule that an array expression — outside a handful of operator contexts — is **implicitly converted to a [[Pointer|pointer]] to its first element**. The array's bound is lost in the conversion. Per [[dis-2-5-arrays|DIS Ch 2.5]]'s explanation of array-to-function passing: *"when passing an array to a function, C copies the value of the base address to the parameter. That is, both the parameter and the argument refer to the same memory locations."* What's being copied is the decayed pointer.

This is the mechanism that justifies, across the [[DiveIntoSystems]] corpus:

- [[dis-1-5-arrays-strings|Ch 1.5]]'s *"arrays pass by reference"* (the value copied is a pointer; mutations through the pointer reach the caller's storage).
- [[dis-2-2-pointers|Ch 2.2]]'s reconciliation: *C is always pass-by-value; pass-by-reference is just pass-by-value of a pointer.*
- [[dis-2-4-dynamic-memory|Ch 2.4]]'s static-vs-dynamic unification at function parameters (`void f(int *arr, int size)` accepts both — the static array decays, the dynamic array's name *is* the pointer).
- [[dis-2-5-arrays|Ch 2.5]]'s multidimensional generalization — a `int m[N][M]` decays to `int (*)[M]` (a pointer to a row of `M` ints), which is why the trailing dimension is mandatory in the parameter declaration.

## The conversion rule

In an expression context, the array `arr` of type `T[N]` is converted to type `T *`, with value `&arr[0]`:

```c
int arr[10];
int *p = arr;            /* implicit decay: arr -> &arr[0] */
int *q = &arr[0];        /* same value */
size_t n = sizeof(arr);  /* NOT decayed — sizeof keeps array type */
                         /* n == 10 * sizeof(int) */
```

## Where decay does *not* happen

Three contexts preserve the array type:

| Context | Behavior |
|---|---|
| Operand of [[SizeOf|`sizeof`]] | Returns total array size in bytes (`10 * sizeof(int)`), not pointer size |
| Operand of [[AddressOfOperator|`&`]] | Yields `T (*)[N]` — pointer to the whole array — not `T **` |
| String literal initializer for an array | `char s[] = "hi";` initializes the array, no decay |

Everywhere else — function calls, pointer assignments, arithmetic — decay applies.

## At function call sites

The headline [[dis-2-5-arrays|Ch 2.5]] consequence — the three parameter declarations below are **identical** to the compiler:

```c
void f(int arr[10], int n);   /* the [10] is ignored */
void f(int arr[],   int n);   /* equivalent */
void f(int *arr,    int n);   /* equivalent — the actual signature C sees */
```

The function receives an `int *`. There is no array-by-value in [[CLanguage|C]] — you cannot pass an entire array's contents to a function; you can only pass a pointer to its first element. (To pass-by-value, wrap the array in a [[CStruct|struct]] — see [[StructAssignment|whole-record copy]] in [[dis-1-6-structs|Ch 1.6]].)

## Decay for multidimensional arrays

A 2D static array decays to a **pointer to its first row**, *not* to `T **`:

```c
int matrix[N][M];
/* matrix decays to: int (*)[M]  — pointer to "array of M ints"  */
/* matrix DOES NOT decay to: int **                              */
```

This is why the [[dis-2-5-arrays|Ch 2.5]] parameter rule keeps the trailing dimension — `void f(int m[][M], int n)` matches `int (*)[M]`. The [[ArrayOfArrays|array-of-arrays]] dynamic form is a *different type* (`int **`); the two are not interchangeable as parameters despite the visual similarity of `arr[i][j]` access.

## The bound is lost

Once decayed, the pointer carries **no length information**. The receiving function cannot ask "how big is this array?" — the caller must thread the length through a separate argument. This is the underlying reason [[CArray|C arrays]] are *length-manually-tracked* and the root of countless [[BufferOverflow|buffer-overflow]] vulnerabilities.

```c
void print_ints(int a[], int n) {
    for (int i = 0; i < n; i++)   /* n is the only thing keeping us in bounds */
        printf("%d ", a[i]);
}
```

## Cross-walk

- **Python lists / NumPy arrays** carry their length and shape with them — there is no decay.
- **C++** has `std::array<int, N>` which is a true value type with `sizeof` and decay-free function passing.
- **Rust** slices (`&[T]`) carry a length — decay-free by design.

## Connections

- [[dis-2-5-arrays]] — defining source (the array-base-address-copied-into-the-parameter quote).
- [[CArray]] — the type that decays.
- [[Pointer]] / [[PointerType]] — the target of decay.
- [[ArrayIndexing]] — `arr[i]` is defined as `*(arr + i)` — the pointer-arithmetic definition that only works *because* `arr` decays.
- [[PassByReference]] — the [[dis-1-5-arrays-strings|Ch 1.5]] rule whose mechanism is decay.
- [[PassByValue]] / [[PassByPointer]] — the [[dis-2-2-pointers|Ch 2.2]] / [[dis-2-3-pointers-functions|Ch 2.3]] reconciliation grounded in decay.
- [[MultidimensionalArray]] / [[RowMajorOrder]] / [[ArrayOfArrays]] — the multidimensional cases where decay's *target type* matters for parameter signatures.
- [[SizeOf]] / [[AddressOfOperator]] — the operators that *don't* decay.
- [[BufferOverflow]] — the security consequence of the lost-bound property.
- [[CLanguage]] / [[DiveIntoSystems]].
