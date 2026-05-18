---
title: "Memory Address (C)"
type: concept
tags: [c-language, memory, pointers]
sources: [dis-1-2-input-output, dis-2-2-pointers]
last_updated: 2026-05-17
---

# Memory Address (C)

A **memory address** in [[CLanguage|C]] is the integer-valued *location* of a byte in the process's address space. Every variable with storage has one; the [[AddressOfOperator|`&` operator]] yields it.

[[dis-1-2-input-output|DIS Ch 1.2]] introduces the concept implicitly, through [[Scanf|`scanf`]] — the function needs to know **where** in memory to deposit the value it parses, and `&num1` *is* that *where*. [[dis-2-2-pointers|Ch 2.2]] then makes it concrete: a memory address is *literally a [[Pointer|pointer]] value with a static type attached* — `int *ptr = &x;` stores the address of `x` in a typed variable, and `*ptr` reads it back.

## Three views of the same thing

| View | Notation | Type |
|---|---|---|
| The variable | `num1` | `int` (its value) |
| Its address | `&num1` | `int *` (a pointer-to-int) |
| The byte at the address | `*(&num1)` ≡ `num1` | `int` again |

[[dis-1-2-input-output|Ch 1.2]] only uses the first two; the dereference (`*p`) view arrives in [[dis-2-2-pointers|Ch 2.2]] as the [[DereferenceOperator|`*` operator]].

## What it isn't (yet)

- **Not a pointer type.** Ch 1.2 carefully avoids the `int *p = &num1;` declaration form — addresses appear *only* as arguments to `scanf`. The reader gets the *value of a location* intuition before having to swallow pointer-type syntax.
- **Not a portable integer.** Addresses are platform-sized; comparing them numerically across processes or runs is meaningless (ASLR randomizes them).

## Connections

- [[CLanguage]] — the language.
- [[AddressOfOperator]] — the operator that produces it.
- [[DereferenceOperator]] — the operator that reads the byte(s) at it.
- [[Pointer]] — a typed variable that holds one.
- [[PointerType]] — the static type wrapper around a raw address.
- [[NullPointer]] — the special *no-address* value.
- [[Scanf]] — the introducing use site; takes addresses as receiver arguments.
- [[VariableDeclaration]] — only declared variables (with storage) have addresses.
- [[CPrimitiveType]] — a memory address carries a static type — the type of the byte(s) it points to.
- [[dis-1-2-input-output]] — introducing source.
- [[dis-2-2-pointers]] — the source that promotes addresses to *typed pointer values*.
