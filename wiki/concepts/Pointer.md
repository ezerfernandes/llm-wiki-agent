---
title: "Pointer (C)"
type: concept
tags: [c-language, pointers, memory]
sources: [dis-2-2-pointers]
last_updated: 2026-05-17
---

# Pointer (C)

A **pointer** in [[CLanguage|C]] is a variable that stores the [[CMemoryAddress|memory address]] of another variable rather than a value directly. Per [[dis-2-2-pointers|DIS Ch 2.2]]: *"C's pointer variables provide a level of indirection to accessing program memory."* The pointer *points to* the variable whose address it holds; reading or writing that variable requires one extra step — the [[DereferenceOperator|`*` dereference operator]].

This is the page [[dis-1-1-getting-started|Ch 1.1]], [[dis-1-2-input-output|Ch 1.2]], [[dis-1-5-arrays-strings|Ch 1.5]], [[dis-1-6-structs|Ch 1.6]] and [[dis-1-7-summary|Ch 1.7]] forward-referenced — held as a *placeholder* until [[dis-2-2-pointers|Ch 2.2]] supplied the definition.

## What a pointer is

| Aspect | Detail |
|---|---|
| **Stored value** | A [[CMemoryAddress|memory address]] — *where* in the process's [[AddressSpace|address space]] something lives |
| **Static type** | [[PointerType|*pointer to T*]] — `int *`, `char *`, `struct studentT *`, etc. |
| **Size** | Platform-fixed (typically 8 bytes on 64-bit, 4 on 32-bit) — **not** the size of the pointee |
| **Special value** | [[NullPointer|`NULL`]] — *"doesn't refer to any particular address"* |

## The three syntactic moves

```c
int *ptr;       /* 1. DECLARATION: ptr is a pointer to int */
int x = 42;
ptr = &x;       /* 2. INITIALIZATION via address-of: ptr now points to x */
*ptr = 8;       /* 3. DEREFERENCE: write through ptr; x is now 8 */
int y = *ptr;   /*    DEREFERENCE: read through ptr; y is 8 */
```

The unary `*` plays **two roles** depending on context:

- **In a declaration** (`int *ptr;`) — part of the type spelling. `int *` means "pointer to int."
- **In an expression** (`*ptr = 8;`) — the [[DereferenceOperator|dereference operator]] that accesses the pointee.

Same lexeme, two syntactic positions, two meanings. Mastering the distinction is the [[dis-2-2-pointers|Ch 2.2]] learning objective.

## The two `=` views

Given `int *ptr;` and `int x;`:

| Statement | Effect | Mental model |
|---|---|---|
| `ptr = &x;` | Changes *which variable `ptr` points to* | Rewires the pointer |
| `*ptr = 8;` | Changes *the value of the variable `ptr` points to* | Writes through the pointer |

Both use `=` and `ptr`; the `*` decides whether the *pointer* or the *pointee* is modified.

## Why pointers exist

[[dis-2-2-pointers|Ch 2.2]] enumerates the five capabilities pointers unlock:

1. **[[PassByPointer|Pass-by-pointer]] output parameters** — the workaround for [[dis-1-4-functions|Ch 1.4]]'s [[PassByValue|pass-by-value]] rule. Pass `&x`, dereference inside the callee, mutate caller storage.
2. **[[DynamicMemoryAllocation|Dynamic memory allocation]]** — `malloc` / `free` return and consume pointers (Ch 2.4).
3. **Efficient large-struct passing** — pass one address instead of [[StructAssignment|copying a 76-byte]] [[CStruct|struct]].
4. **[[LinkedDataStructure|Linked data structures]]** — linked lists, trees, graphs: each node holds pointers to its neighbors.
5. **Byte reinterpretation** — different pointer types looking at the same memory (the substrate for the [[BufferOverflow|buffer-overflow]] / type-pun stories of later chapters).

## Safety discipline

[[dis-2-2-pointers|Ch 2.2]] codifies two rules pointer-using [[CLanguage|C]] programs live by:

1. **Initialize before use.** An uninitialized pointer holds a garbage address; dereferencing it is undefined behavior. Assign either `&something` or [[NullPointer|`NULL`]] at declaration time.
2. **Never dereference [[NullPointer|`NULL`]].** Guard with `if (ptr != NULL) { *ptr = 6; }` — the [[ShortCircuitEvaluation|short-circuit]] idiom from [[dis-1-3-conditionals-loops|Ch 1.3]].

Violating either gives the canonical [[SegmentationFault|segmentation fault]] — or worse, silent memory corruption that surfaces unpredictably later.

## Pass-by-pointer reconciliation

[[dis-1-4-functions|Ch 1.4]] said [[CLanguage|C]] is pure [[PassByValue|pass-by-value]]; [[dis-1-5-arrays-strings|Ch 1.5]] said [[CArray|arrays]] pass [[PassByReference|by reference]]. Ch 2.2 reconciles: **arrays decay to a pointer to their first element at the call site, and that pointer value is passed by value.** The mechanism is still pass-by-value; the *semantics* look like pass-by-reference because dereferencing the pointer reaches the caller's storage. The same mechanism explicitly applied (`f(&x)` + `*p = ...`) is the [[PassByPointer|pass-by-pointer]] idiom for output parameters.

## What this page doesn't cover (yet)

- **Pointer arithmetic** (`p + 1`, `p[i]`) — deferred to Ch 2.3.
- **Pointer-to-pointer** (`int **`) — deferred.
- **`void *`** (type-erased pointer) — deferred to Ch 2.4.
- **Function pointers** — deferred to Ch 2 / later.
- **The [[ArrowOperator|`->`]] operator** — has its own page from [[dis-1-6-structs|Ch 1.6]] but now backed by Ch 2.2's pointer machinery.

## Connections

- [[CLanguage]] — the language.
- [[CMemoryAddress]] — the underlying value type a pointer holds.
- [[AddressOfOperator]] — the operator that produces a pointer value (`&x`).
- [[DereferenceOperator]] — the operator that accesses the pointee (`*ptr`).
- [[PointerDeclaration]] — the `type_name *var_name;` syntactic form.
- [[PointerType]] — the static-type system (`int *` vs `char *`).
- [[NullPointer]] — the *no-address* value `NULL`.
- [[PassByPointer]] — the parameter-passing idiom unlocked by pointers.
- [[PassByValue]] / [[PassByReference]] — the calling conventions Ch 2.2 reconciles.
- [[SegmentationFault]] — the typical consequence of misusing pointers.
- [[ArrowOperator]] — pointer-to-struct shorthand.
- [[DynamicMemoryAllocation]] — pointers + heap; deferred to Ch 2.4.
- [[LinkedDataStructure]] — pointers chained into nodes; deferred.
- [[BufferOverflow]] — what unchecked pointer writes enable.
- [[RawPointer]] — Rust's equivalent, with the safety story made explicit.
- [[dis-2-2-pointers]] — defining source.
