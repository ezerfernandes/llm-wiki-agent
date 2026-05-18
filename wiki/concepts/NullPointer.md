---
title: "Null Pointer (C `NULL`)"
type: concept
tags: [c-language, pointers, safety, macros]
sources: [dis-2-2-pointers]
last_updated: 2026-05-17
---

# Null Pointer (`NULL`)

A **null pointer** is the special [[Pointer|pointer]] value that *does not refer to any address*. Per [[dis-2-2-pointers|DIS Ch 2.2]]: *"Any pointer can be given the special value `NULL`, which indicates that it doesn't refer to any particular address."*

```c
int *ptr;
ptr = NULL;   /* ptr now holds the no-address value */
```

## What `NULL` is

- A **macro** defined in `<stddef.h>`, `<stdio.h>`, `<stdlib.h>`, `<string.h>`, and `<time.h>`.
- Typically expands to `((void *)0)` on hosted [[CLanguage|C]] implementations.
- **Assignable to any pointer type** — `int *`, `char *`, `struct studentT *`, ... — without a cast.
- **Falsy** in boolean contexts: `if (ptr)` is true iff `ptr` is non-null; `if (!ptr)` is the null-check.
- **Comparable** with `==` and `!=` to any pointer of the same type.

## The cardinal rule

**Never dereference `NULL`.** Per [[dis-2-2-pointers|Ch 2.2]]:

```c
ptr = NULL;
*ptr = 6;    /* CRASH — undefined behavior, typically a segmentation fault */
```

The defensive idiom uses [[ShortCircuitEvaluation|short-circuit]] from [[dis-1-3-conditionals-loops|Ch 1.3]]:

```c
if (ptr != NULL) {
    *ptr = 6;
}

/* equivalent shorthand */
if (ptr) {
    *ptr = 6;
}
```

The short-circuit guard `if (p != NULL && *p == 0)` works because `&&` skips `*p == 0` when `p == NULL`.

## What `NULL` is *for*

[[NullPointer|`NULL`]] is the conventional *"initialized but not yet pointing anywhere"* state. The three idiomatic uses:

1. **Safe initialization.** Every pointer should be initialized at declaration; if there's no real target yet, use `NULL`:
   ```c
   int *ptr = NULL;
   ```
   This converts the *uninitialized-pointer* footgun (garbage address, undefined behavior on dereference) into the *null-pointer* footgun (defined behavior: crash on dereference) — much easier to debug.

2. **Sentinel for "no result."** Functions that allocate or look up may return `NULL` to signal failure: [[Malloc|`malloc`]] returns `NULL` on out-of-memory, `fopen` returns `NULL` on file-not-found, `strchr` returns `NULL` when the character isn't found. The caller **must** check before dereferencing.

3. **Terminator in linked structures.** A [[LinkedDataStructure|linked list]] uses `NULL` for the *no-next-node* end marker.

## What `NULL` is *not*

- **Not the integer 0.** Source-level it often *looks* like `0`, but assigning a non-zero integer literal to a pointer is a type error (warning), and the bit pattern of `NULL` is **implementation-defined** — usually all-zero-bits, but not guaranteed. Use the macro, not the literal.
- **Not the null character `'\0'`.** That's the [[NullTerminator|null byte]] used to end a [[CString|C string]] — a `char` of value `0`, not a pointer.
- **Not the empty string.** `""` is a pointer to a one-byte buffer containing `'\0'`; very much not `NULL`.

## Three null-ish things in [[CLanguage|C]]

| Concept | Type | Value | Used for |
|---|---|---|---|
| **`NULL`** (this page) | pointer (any type) | no-address | "no object" pointer sentinel |
| **`'\0'`** ([[NullTerminator]]) | `char` | byte `0x00` | end-of-[[CString|C-string]] marker |
| **`0`** | `int` | zero | the integer zero |

Conflating them is a classic novice trap.

## Connections

- [[CLanguage]] — the language.
- [[Pointer]] — the type of value `NULL` is.
- [[DereferenceOperator]] — what must **not** be applied to `NULL`.
- [[ShortCircuitEvaluation]] — what makes the `p != NULL && *p` guard idiom safe.
- [[SegmentationFault]] — the typical OS response to a `NULL`-dereference.
- [[NullTerminator]] — the *other* null in [[CLanguage|C]]; not to be confused.
- [[PointerDeclaration]] — `int *p = NULL;` is the canonical safe-default declaration.
- [[Malloc]] — returns `NULL` on allocation failure (deferred to Ch 2.4).
- [[dis-2-2-pointers]] — defining source.
