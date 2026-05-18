---
title: "Dynamically Allocated Array (C)"
type: concept
tags: [c-language, dynamic-allocation, heap, arrays, pointers]
sources: [dis-2-4-dynamic-memory]
last_updated: 2026-05-17
---

# Dynamically Allocated Array (C)

A **dynamically allocated array** is an [[CArray|array]]-shaped buffer obtained at runtime from the [[HeapSection|heap]] via a single [[Malloc|`malloc`]] call sized for `N` elements:

```c
int *arr  = malloc(sizeof(int)  * N);   // N-element int array
char *str = malloc(sizeof(char) * N);   // N-byte char buffer
```

Per [[dis-2-4-dynamic-memory|DIS Ch 2.4]]: *"a dynamically allocated array allocates contiguous space for storing multiple values of the same type."* The pointer [[Malloc|`malloc`]] returns *is* the array's base address — same role the name of a [[dis-1-5-arrays-strings|Ch 1.5]] static array plays.

## The unification with static arrays

The chapter's headline payoff: **dynamically allocated arrays use the same indexing syntax as statically declared arrays**.

```c
int s_array[20];                       // static — Ch 1.5
int *d_array = malloc(sizeof(int)*20); // dynamic — Ch 2.4

s_array[5] = 42;       // same syntax
d_array[5] = 42;       // same syntax
```

`arr[i]` is defined as `*(arr + i)` — pointer arithmetic plus dereference. It works on any [[Pointer|pointer]] whose pointee is a real array's first element, regardless of how that array was allocated. The two **look** identical at use sites; they **differ** in:

| Aspect | Static (Ch 1.5) | Dynamic (Ch 2.4) |
|---|---|---|
| Declaration | `int s_array[20];` | `int *d_array;` then `malloc(...)` |
| Storage region | [[StackSection|stack]] (locals) or [[DataSection|data]] (globals) | [[HeapSection|heap]] |
| Size known at | Compile time | Runtime — `N` can come from input |
| Lifetime | [[StackFrame|frame]] / program-lifetime | Programmer-controlled — until [[Free|`free`]] |
| Underlying type | `int[20]` (array type) | `int *` (pointer type) |
| Cleanup | Automatic | Must call `free` |
| Failure mode | Stack overflow if too large | [[NullPointer|`NULL`]] return from `malloc` |

The compile-time-vs-runtime split is the headline reason dynamic arrays exist — when `N` depends on `scanf` input, file size, or any runtime quantity, the static form can't express the allocation.

## Function-parameter unification

The chapter's second payoff: *"functions can use the same parameter declarations to receive both statically and dynamically allocated arrays as parameters."* A function written for one accepts both:

```c
void init_array(int *arr, int size) {     // accepts either
    for (int i = 0; i < size; i++)
        arr[i] = i;
}

int  s_array[10];
int *d_array = malloc(sizeof(int) * 10);
init_array(s_array, 10);                  // works
init_array(d_array, 10);                  // also works
```

This is the [[dis-2-3-pointers-functions|Ch 2.3]] [[PassByPointer|pass-by-pointer]] mechanism reused — both call sites pass a [[CMemoryAddress|base address]] (the static array decays to a pointer; the dynamic array's name *is* a pointer). The function sees identical types.

## Cleanup

A dynamically allocated array follows the [[dis-2-4-dynamic-memory|Ch 2.4]] discipline:

```c
free(d_array);
d_array = NULL;
```

One `free` releases the whole contiguous run — the array is a single allocation, not `N` allocations.

## Connections

- [[dis-2-4-dynamic-memory]] — introducing source.
- [[Malloc]] / [[Free]] / [[SizeOf]] — the API.
- [[CArray]] — the static counterpart from [[dis-1-5-arrays-strings|Ch 1.5]].
- [[CString]] — a dynamically allocated `char` array with a [[NullTerminator|`'\0'`]] terminator.
- [[Pointer]] / [[PointerType]] — the underlying type of the allocation handle.
- [[PassByPointer]] — the calling convention that unifies static and dynamic arrays at function parameters.
- [[HeapSection]] / [[StackSection]] / [[DataSection]] — the alternative storage regions.
- [[DynamicMemoryAllocation]] — the headline mechanism.
- [[CLanguage]] / [[DiveIntoSystems]].
