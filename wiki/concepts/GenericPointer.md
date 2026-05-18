---
title: "Generic Pointer (Design Pattern)"
type: concept
tags: [c-language, pointers, types, generic-programming, design-pattern]
sources: [dis-2-9-3-voidstar]
last_updated: 2026-05-17
---

# Generic Pointer (Design Pattern)

A **generic pointer** is a pointer that can refer to any data type — the design pattern [[CLanguage|C]] implements through [[VoidPointer|`void *`]]. Per [[dis-2-9-3-voidstar|DIS Ch 2.9.3]]: *"the `void *` type in C represents a generic pointer — a pointer to any data type."*

This is C's mechanism for **type-erased programming**: writing one function or storing one value that works across all pointer-bearing types without rewriting it per type.

## Why C needs the pattern

[[CLanguage|C]] has no templates ([[CPlusPlus|C++]]), no generics ([[Java]] / [[Rust]]), no dynamic typing ([[Python]]). Every function signature commits to specific types. To write code that works on *any* type — a container, a callback, a memory mover — C needs an escape hatch from its own type system. `void *` is that escape hatch.

## The three canonical uses

[[dis-2-9-3-voidstar|Ch 2.9.3]] names two; a third is implicit in the broader corpus.

### 1. Generic return type — [[Malloc|`malloc`]]

```c
void *malloc(size_t size);
```

One function, every pointer type. The caller [[TypeCast|recasts]] the return to specialize. Pre-modern code: `int *p = (int *)malloc(...);`. Modern C: implicit cast — `int *p = malloc(...);`.

### 2. Generic parameter — callbacks and threads

```c
int my_thr_main(void *args);                            /* pthread thread main */
int qsort_compare(const void *a, const void *b);        /* qsort comparator */
void apply(void *list, void (*fn)(void *element));      /* generic iterator */
```

The callee receives a type-erased value; the caller and callee agree on the actual type by convention. Inside the callee, the first move is to [[TypeCast|recast]]: `int n = *((int *)args);`.

### 3. Generic storage — heterogeneous containers

A linked list, hash table, or tree that stores `void *` values can hold *any* mix of pointer types:

```c
struct node {
    void *data;       /* points to any payload */
    struct node *next;
};
```

The container code never inspects `data`; only insertion-and-retrieval clients do, after a cast. This is how pre-C++ C libraries (the BSD `<sys/queue.h>` macros, Glib's `GList`, etc.) built reusable data structures.

## The bargain: genericity for type-safety

Generic pointers trade **compile-time type checking** for **runtime flexibility**:

| Property | Concrete `T *` | Generic `void *` |
|---|---|---|
| Compiler checks dereference type | Yes | No (cast required) |
| Pointer arithmetic | Yes (stride `sizeof(T)`) | No (undefined behavior) |
| Type-mismatch caught at compile time | Yes | No — runtime crash or silent corruption |
| One implementation works on all T | No | Yes |

The cost is paid by the programmer enforcing the type discipline that the compiler no longer can. A wrong [[TypeCast|cast]] — `(double *)int_ptr` then dereference — compiles silently and crashes at runtime.

## Comparison with other languages

| Mechanism | Type erasure happens... | Recovery |
|---|---|---|
| C `void *` | At cast time, fully | Programmer-supplied cast |
| C++ templates | Never — monomorphized per type | N/A |
| Java `Object` | At reference time, with retained class metadata | `instanceof` + cast (checked) |
| Rust `&dyn Trait` | At trait-object construction, with vtable | Trait dispatch (no cast) |
| Python | Never — everything is `PyObject *` | Duck typing / `isinstance` |

C's `void *` is the most primitive form — pure address with no retained type info. This is both its strength (zero overhead) and its weakness (zero safety).

## When the pattern is the right tool

**Use `void *` when**:

- Writing a callback API that must serve many callers ([[Pthreads|pthreads]], [[Qsort|`qsort`]]).
- Allocating raw memory before knowing the type ([[Malloc|`malloc`]]).
- Building a container that must hold mixed payload types.
- Treating memory as bytes (the [[Memcpy|`memcpy`]] family).

**Reach for an alternative when**:

- All consumers use the same pointer type — use that type directly.
- Type safety matters and you can sacrifice flexibility — declare the concrete type.
- You're writing C++ — use templates instead of `void *`.

## Connections

- [[dis-2-9-3-voidstar]] — introducing source.
- [[VoidPointer]] — the concrete `void *` form in C.
- [[TypeCast]] — the recovery mechanism that re-specializes a generic pointer.
- [[Malloc]] — canonical generic-return-type consumer.
- [[Memcpy]] — canonical generic-parameter consumer.
- [[Pthreads]] / [[PthreadCreate]] — canonical generic-callback consumer.
- [[Pointer]] / [[PointerType]] — the typed counterpart to the generic-pointer pattern.
- [[CLanguage]] / [[DiveIntoSystems]].
