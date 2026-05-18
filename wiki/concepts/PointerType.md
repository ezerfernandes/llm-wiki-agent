---
title: "Pointer Type (C)"
type: concept
tags: [c-language, pointers, types]
sources: [dis-2-2-pointers]
last_updated: 2026-05-17
---

# Pointer Type (C)

A **pointer type** in [[CLanguage|C]] is a static type spelled `T *`, where `T` is any type — *primitive*, *aggregate*, or even another pointer type. A variable of type `T *` holds the [[CMemoryAddress|memory address]] of a value of type `T`. Per [[dis-2-2-pointers|DIS Ch 2.2]]: *"`int *` stores the memory address of an `int`; `char *` stores the memory address of a `char`."*

```c
int     *p1;   /* pointer to int */
char    *p2;   /* pointer to char */
double  *p3;   /* pointer to double */
struct studentT *p4;   /* pointer to struct studentT */
int    **p5;   /* pointer to pointer to int */
```

## Three reasons the pointee type matters

Even though *every* pointer ultimately holds an [[CMemoryAddress|address]] (the same width on a given platform), the static pointee type is load-bearing:

1. **[[DereferenceOperator|Dereference]] yield type.** `*p` has type `T` for a `T *`. The compiler uses this to type-check expressions like `*p + 3` or `s.field = *p;`.
2. **Pointer arithmetic stride.** When pointer arithmetic arrives (Ch 2.3), `p + 1` advances by **`sizeof(T)` bytes**, not 1 byte — the pointee type sets the stride.
3. **Assignment compatibility.** Assigning across pointer types is a **type error** (compiler warning, runtime *"unpredictable behavior"* per Ch 2.2):
   ```c
   int x;
   char *cptr;
   cptr = &x;   /* ERROR: char * expected, int * given */
   ```

## The discipline contract

[[dis-2-2-pointers|Ch 2.2]] uses the type system as the only language-level barrier between disciplined pointer code and arbitrary memory mayhem. The contract:

| Action | Requires |
|---|---|
| `ptr = &x;` | `ptr`'s pointee type **==** `x`'s declared type |
| `*ptr = v;` | `v`'s type **==** `ptr`'s pointee type |
| `q = p;` (pointer copy) | `q` and `p` have the **same** pointer type |

Violating any of these without a cast yields a compiler warning; the runtime consequence is undefined behavior — most often a [[SegmentationFault|segmentation fault]], occasionally silent memory corruption.

## Width vs. pointee size

A common source of confusion:

| Thing | Size |
|---|---|
| The **pointer** itself (e.g. `int *p`) | Platform pointer width — 8 bytes on 64-bit, 4 on 32-bit |
| The **pointee** (`*p`) | `sizeof(T)` — depends on `T` |

`sizeof(int *)` and `sizeof(char *)` and `sizeof(struct studentT *)` are **all equal** on a given platform — but `sizeof(*p)` varies with the pointee type.

## `NULL` is universal

The [[NullPointer|`NULL`]] value is assignable to *any* pointer type without a cast:

```c
int *p = NULL;
char *cp = NULL;
struct studentT *sp = NULL;
```

This is the one type-system relaxation [[CLanguage|C]] grants for pointers — and it's the reason `NULL` works as a universal "no result" sentinel.

## What this page doesn't cover (yet)

- **`void *`** — the *type-erased* pointer, the one assignment-compatible across pointer types via cast. Deferred to Ch 2.4 ([[Malloc|`malloc`]] returns `void *`).
- **`const T *` / `T * const`** — the two `const` positions and their distinct meanings.
- **Function pointer types** — `int (*f)(int, int)`.
- **Pointer-to-array vs array-of-pointers** — the `int (*p)[10]` vs `int *p[10]` distinction.

## Connections

- [[CLanguage]] — the language.
- [[Pointer]] — the value class this types.
- [[PointerDeclaration]] — the syntactic form `T *var;` that introduces a variable of this type.
- [[DereferenceOperator]] — the operator that uses the pointee type to determine yield type.
- [[AddressOfOperator]] — `&x` has type *pointer-to-`x`'s-declared-type*.
- [[CMemoryAddress]] — the underlying value all pointer types share.
- [[NullPointer]] — assignable across all pointer types.
- [[CPrimitiveType]] / [[CStruct]] / [[CArray]] — the pointee types Ch 2.2 examples use.
- [[SizeOf]] — `sizeof(T *)` is uniform per platform; `sizeof(*p)` varies with pointee.
- [[dis-2-2-pointers]] — defining source.
