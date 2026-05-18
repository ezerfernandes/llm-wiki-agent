---
title: "void * (Generic Pointer, C)"
type: concept
tags: [c-language, pointers, types, generic, void-pointer]
sources: [dis-2-9-3-voidstar]
last_updated: 2026-05-17
---

# `void *` (Generic Pointer, C)

**`void *`** in [[CLanguage|C]] is the *type-erased* pointer — a [[Pointer|pointer]] that points to *any* data type without statically committing to which one. Per [[dis-2-9-3-voidstar|DIS Ch 2.9.3]]: *"the `void *` type in C represents a generic pointer — a pointer to any data type."* It is the deferral [[dis-2-2-pointers|Ch 2.2]] flagged and the mechanism [[dis-2-4-dynamic-memory|Ch 2.4]] silently relied on for [[Malloc|`malloc`]]'s return.

## Why it works: pointer-size uniformity

Per [[dis-2-9-3-voidstar|Ch 2.9.3]]: *"every pointer variable requires the same number of storage bytes, and because they're all the same size, the compiler can allocate space for a `void *` variable without knowing the type it points to."*

| Platform | `sizeof(any T *)` |
|---|---|
| 32-bit | 4 bytes |
| 64-bit | 8 bytes |

A [[CMemoryAddress|memory address]] is just an integer index into the [[AddressSpace|address space]] — its width is fixed by the architecture, not by the pointee. The compiler can therefore reserve storage for a `void *` knowing only the platform's pointer width.

## What it loses: pointee type

The price of genericity is that the compiler cannot:

- compute `sizeof(*vp)` (no pointee type → no size),
- type-check `*vp + 3` or `vp->field` (no type → no member resolution),
- step `vp + 1` (no [[PointerType|pointer arithmetic stride]] — `sizeof(T)` is unknown).

Direct [[DereferenceOperator|dereference]] of a `void *` is a **type error** (`error: invalid use of void expression`). To use the pointee, the programmer must first [[TypeCast|recast]] to a concrete pointer type.

## Use case 1 — [[Malloc|`malloc`]]'s return type

[[Malloc|`malloc`]] is declared `void *malloc(size_t size)`. One signature serves callers wanting `int *`, `char *`, `struct studentT *`, or any other [[PointerType|pointer type]]:

```c
int *array  = (int *)malloc(sizeof(int) * 10);
char *str   = (char *)malloc(sizeof(char) * 20);
struct studentT *s = (struct studentT *)malloc(sizeof(struct studentT));
```

The `(type *)` recast tells the compiler *"treat this address as a pointer-to-`type` from here on."* In modern [[CLanguage|C]] (C89 onward) the cast is **implicit** — `void *` assigns to any pointer type without an explicit cast — so `int *array = malloc(sizeof(int) * 10);` is also legal and idiomatic. (C++ requires the explicit cast.)

## Use case 2 — [[Pthreads|pthread]] thread-main parameters

Per [[dis-2-9-3-voidstar|Ch 2.9.3]]: *"thread main functions accept `void *` parameters, enabling generic thread creation. Programmers must recast the parameter to access its actual type."*

```c
int my_thr_main(void *args) {
    int num = *((int *)args);     // recast then dereference
    /* ... */
}
```

The `void *args` parameter lets a single [[PthreadCreate|`pthread_create`]] API carry any caller-defined argument — a single `int`, a `struct`, an array — without committing the library to any particular argument type at compile time.

## Use case 3 — [[Memcpy|`memcpy`]] and the byte-level memory API

[[CStandardLibrary|`<string.h>`]] generic-buffer routines all take `void *`:

```c
void *memcpy(void *dest, const void *src, size_t n);
void *memset(void *s, int c, size_t n);
int   memcmp(const void *s1, const void *s2, size_t n);
```

Callers pass any pointer type; the routines work byte-by-byte without caring about the pointee type. This is the *byte reinterpretation* capability [[dis-2-2-pointers|Ch 2.2]] named as pointers' fifth use case.

## The recast-before-deref pattern

The general shape:

```c
void *vp = /* something */;
T *tp = (T *)vp;       // recast
T v = *tp;             // now safe to dereference
/* or in one expression: */
T v = *((T *)vp);
```

The double parentheses in `*((T *)vp)` matter: the inner pair binds the cast to `vp`; the outer `*` then dereferences the resulting `T *`. Writing `*(T *)vp` works because `(cast)` binds tighter than `*` — but the double-parens form is the corpus-recommended idiom for clarity.

## What `void *` doesn't fix

- **Pointer arithmetic** — `vp + 1` is undefined by the C standard (some compilers accept it as 1-byte step as an extension); cast first.
- **Type-safety** — once erased, the type system can't catch a wrong cast. `(double *)int_ptr` compiles silently and crashes spectacularly at runtime.
- **Const-correctness** — the recast also erases [[ConstQualifier|`const`]]; production code uses `const void *` for read-only inputs (see [[Memcpy|`memcpy`]]'s `const void *src`).

## Contrast: `void *` vs `void`

Beginner trap: `void` (the [[VoidType|no-value type]]) and `void *` (the type-erased pointer) are **fundamentally different**:

| Form | Role | Example |
|---|---|---|
| `void` | "no value" — function returns nothing / takes no params | `void print_table(int n) { ... }` |
| `void *` | "any pointer" — generic pointer to any type | `void *malloc(size_t n)` |

`void` is a non-type; `void *` is a real pointer type with all-pointer-type-uniform storage size. The `*` changes everything.

## Connections

- [[dis-2-9-3-voidstar]] — defining source.
- [[Pointer]] / [[PointerType]] — the value class and type system `void *` extends.
- [[CMemoryAddress]] — the underlying value (uniform width is what makes `void *` work).
- [[VoidType]] — the *no-value* type whose pointer form is this page.
- [[TypeCast]] — the `(T *)vp` recast mechanism.
- [[GenericPointer]] — the design pattern this implements.
- [[Malloc]] — the canonical `void *` consumer (return type).
- [[Memcpy]] — byte-level routine that takes `void *` parameters.
- [[Pthreads]] / [[PthreadCreate]] — the second canonical use case (thread args).
- [[DereferenceOperator]] — what cannot be applied to a `void *` without a cast first.
- [[NullPointer]] — `NULL` assigns to any pointer type including `void *`.
- [[ConstQualifier]] — `const void *` for read-only generic-pointer parameters.
- [[CLanguage]] / [[DiveIntoSystems]].
