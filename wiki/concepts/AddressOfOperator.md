---
title: "Address-of Operator (C `&`)"
type: concept
tags: [c-language, operators, memory, pointers]
sources: [dis-1-2-input-output, dis-2-2-pointers]
last_updated: 2026-05-17
---

# Address-of Operator (`&`)

The unary **`&`** operator in [[CLanguage|C]] yields the **[[CMemoryAddress|memory address]]** of its operand — *"the location of that variable in the program's memory"* per [[dis-1-2-input-output|DIS Ch 1.2]], and *"`ptr = &x;` — `ptr` gets the address of `x`, pointer 'points to' `x`"* per [[dis-2-2-pointers|DIS Ch 2.2]]. It is the introductory chapter's first sighting of *an address as a first-class value*; Ch 2.2 finally promotes it from *that thing `scanf` needs* to *the operator that produces a [[Pointer|pointer]] value* — `&x` has type *pointer-to-`x`'s-declared-type* (`int x; &x;` is `int *`).

```c
int num1;
scanf("%d", &num1);     /* pass num1's *location* to scanf */
```

## Why [[Scanf|`scanf`]] needs it

C is pass-by-value: a function ordinarily receives a *copy* of the caller's value. If `scanf` were given `num1` directly, it would parse a number, store it into its own private copy, and discard it on return — the caller's `num1` would never change. Passing **`&num1`** lets `scanf` write to the caller's storage cell.

## Distinction from bitwise AND

C reuses `&`:

- **Unary** prefix `&x` — address-of.
- **Binary** infix `a & b` — bitwise AND.

Position disambiguates.

## Relation to the pointer chapter

`&` produces a [[Pointer|pointer]] (`int *` for an `int` variable). Ch 1.2 introduced `&` *without yet introducing pointer types* — it appeared only inside `scanf` calls. [[dis-2-2-pointers|Ch 2.2]] finally explains the operator generally: the value `&x` produces is now storable in a [[PointerDeclaration|pointer variable]] (`int *ptr = &x;`), readable back via the [[DereferenceOperator|`*` operator]] (`*ptr` is `x`), and the inverse `*(&x) == x` identity holds for any addressable `x`. The two operators are conceptual inverses on lvalues.

## Connections

- [[CLanguage]] — the language.
- [[Scanf]] — the chapter's introducing use site.
- [[Pointer]] — what `&` produces a value of.
- [[CMemoryAddress]] — the abstract referent `&` produces.
- [[DereferenceOperator]] — the inverse operator (`*` reads from an address; `&` produces one).
- [[PointerDeclaration]] — the declaration form that consumes `&`-produced values.
- [[PointerType]] — `&x` has static type *pointer-to-T* where `T` is `x`'s declared type.
- [[PassByPointer]] — the calling idiom built on `&` at the call site + `*` in the callee.
- [[CPrimitiveType]] — `&x` has type *pointer-to-T* where `T` is `x`'s declared type.
- [[VariableDeclaration]] — only declared variables (lvalues with storage) have addresses; `&5` is a compile error.
- [[dis-1-2-input-output]] — introducing source.
- [[dis-2-2-pointers]] — the source that promotes `&` from `scanf`-magic to a general-purpose move.
