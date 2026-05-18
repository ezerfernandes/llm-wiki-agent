---
title: "Dive into Systems — Ch 2.9.3 The void* Type"
type: source
tags: [c-language, void-pointer, generic-pointer, type-cast, malloc, pthread, dive-into-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/advanced_voidstar.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **third subsection of [[dis-2-9-advanced|Ch 2.9]]** of *[[DiveIntoSystems]]* — finally delivers the **[[VoidPointer|`void *`]] type-erased pointer** that [[dis-2-2-pointers|Ch 2.2]] named-and-deferred and that [[dis-2-4-dynamic-memory|Ch 2.4]] silently relied on as [[Malloc|`malloc`]]'s return type. Codifies (a) the **size-uniformity rationale** — every pointer on a given platform occupies the same number of storage bytes (4 on 32-bit, 8 on 64-bit), so the compiler can allocate space for a `void *` without knowing its pointee type; (b) the **mandatory [[TypeCast|recast]] before [[DereferenceOperator|dereference]]** rule — `void *` carries no pointee-type information, so the compiler cannot compute `sizeof(*p)` and the programmer must supply the target type via `(type *)pointer` syntax; (c) the **two canonical use cases** — [[Malloc|`malloc`]]'s [[GenericPointer|generic-return-type]] pattern that fits any caller-chosen [[PointerType|pointer type]], and [[Pthreads|pthread]] thread-main parameters that accept `void *args` for type-erased argument passing. Resolves the [[dis-2-2-pointers|Ch 2.2]] *"`void *` deferred to later Ch 2 sections"* promise.

## Key Claims

- **`void *` is a generic pointer that points to any data type.** The mechanism works because *"every pointer variable requires the same number of storage bytes, and because they're all the same size, the compiler can allocate space for a `void *` variable without knowing the type it points to."* Pointer width is platform-fixed (4 bytes on 32-bit, 8 bytes on 64-bit) — the pointee's size doesn't enter into the pointer-variable's storage size.
- **`void *` cannot be directly dereferenced** — the compiler cannot infer the underlying data's size or interpretation without a pointee type, so `*vp` is a type error. The programmer must explicitly *recast* via `(type *)vp` before dereferencing: `int num = *((int *)args);`.
- **[[Malloc|`malloc`]] returns `void *`** — that's how a single signature `void *malloc(size_t size)` serves callers wanting `int *`, `char *`, `struct studentT *`, or any other pointer type. The recast is conventionally written `int *array = (int *)malloc(sizeof(int) * 10);` though in modern [[CLanguage|C]] the cast is implicit (`void *` assigns to any pointer type without a cast — see [[Malloc|`malloc`]] page for the modern form).
- **[[Pthreads|pthread]] thread main functions take `void *args`** — the type-erased-parameter idiom that lets one thread-creation API ([[PthreadCreate|`pthread_create`]]) carry any caller-defined argument struct. Inside the thread body, the programmer recasts: `int num = *((int *)args);` for an `int` arg, `my_struct *s = (my_struct *)args;` for a struct arg.
- **The recast syntax is `(target_type *)pointer`** — parentheses around the target pointer type, applied as a prefix [[CastOperator|cast operator]]. Combine with dereference using double parentheses: `*((int *)args)` reads "dereference the int-pointer view of args."

## Key Quotes

> "The `void *` type in C represents a generic pointer — a pointer to any data type." — defining the type's role as a [[GenericPointer|generic pointer]].

> "Every pointer variable requires the same number of storage bytes, and because they're all the same size, the compiler can allocate space for a `void *` variable without knowing the type it points to." — the **size-uniformity rationale** that makes type-erased pointers possible at all.

> "Programmers must recast the parameter to access its actual type." — the **mandatory cast** rule for using `void *`.

## Connections

- [[DiveIntoSystems]] — the source textbook; this section is its Ch 2.9.3.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — the authors.
- [[dis-2-9-advanced]] — the hub page that forwards to this subsection.
- [[dis-2-9-2-cmd-line-args]] — the **prior** subsection (command-line arguments).
- [[dis-2-2-pointers]] — names-and-defers `void *` as one of the deferrals Ch 2.9.3 finally resolves.
- [[dis-2-4-dynamic-memory]] — silently relies on `void *` as [[Malloc|`malloc`]]'s return type; this section explains the mechanism.
- [[Pointer]] / [[PointerType]] — the value class and type system that `void *` extends.
- [[CMemoryAddress]] — the underlying value all pointer types share (load-bearing for the size-uniformity rationale).
- [[VoidType]] — the no-value type whose pointer form `void *` plays a fundamentally different role (type-erased pointer rather than no-return-type marker).
- [[VoidPointer]] — the **new** concept page introduced here.
- [[TypeCast]] — the **new** concept page for the `(type *)pointer` recast mechanism.
- [[GenericPointer]] — the **new** concept page naming the *generic-pointer* design pattern.
- [[Malloc]] — already updated by Ch 2.4 with `void *` return; this section explains *why*.
- [[Pthreads]] / [[PthreadCreate]] — the second canonical use case (deferred to Ch 9–10 on concurrency).

## Contradictions

- None. Ch 2.9.3 is purely additive — it *explains* the mechanism [[dis-2-4-dynamic-memory|Ch 2.4]]'s [[Malloc|`malloc`]] signature already exposed, and resolves the `void *` deferral [[dis-2-2-pointers|Ch 2.2]] flagged.
