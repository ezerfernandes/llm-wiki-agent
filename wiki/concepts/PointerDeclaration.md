---
title: "Pointer Declaration (C)"
type: concept
tags: [c-language, pointers, syntax]
sources: [dis-2-2-pointers]
last_updated: 2026-05-17
---

# Pointer Declaration (C)

A **pointer declaration** in [[CLanguage|C]] introduces a variable whose value is a [[CMemoryAddress|memory address]] of a value of a specific type. The syntactic form per [[dis-2-2-pointers|DIS Ch 2.2]] is:

```c
type_name *var_name;
```

Two canonical examples from the chapter:

```c
int *ptr;   // stores the memory address of an int (ptr "points to" an int)
char *cptr; // stores the memory address of a char (cptr "points to" a char)
```

## The `*` in a declaration is part of the type

The chapter is explicit: **the `*` here is *not* the [[DereferenceOperator|dereference operator]].** Same lexeme, different syntactic position:

| Context | Role of `*` |
|---|---|
| Declaration: `int *ptr;` | Part of the type spelling — declares `ptr` as a [[PointerType|pointer to int]] |
| Expression: `*ptr = 8;` | Unary [[DereferenceOperator|dereference operator]] — accesses the pointee |

This dual role is one of [[CLanguage|C]]'s grammatical sharp edges; the [[Pointer|pointer]] page expands on the disambiguation.

## Reading a pointer declaration

[[CLanguage|C]] declarations are read **right-to-left** around the variable name. For `int *ptr;`:

> *"`ptr` is a pointer to `int`"*

The pointee type (`int`) is at the left; the variable (`ptr`) is at the right; the `*` between them says *"pointer to."*

## Whitespace is irrelevant

All three of these declare exactly the same variable:

```c
int *ptr;
int* ptr;
int * ptr;
```

The style chosen depends on the team. The `int *ptr;` form has a subtle advantage in **multi-variable declarations**:

```c
int *p, q;   /* p is int*, q is int (NOT int*) */
int* p, q;   /* MISLEADING: p is int*, q is int — the * binds only to p */
```

The `*` syntactically binds to the *variable*, not the *type* — so the safe rule is **one declaration per line** when pointer types are involved.

## Initialization at declaration

Best practice is to initialize every pointer at declaration to avoid the *garbage-address* footgun:

```c
int x;
int *ptr = &x;     // initialized to the address of x
int *empty = NULL; // initialized to no-address
```

[[dis-2-2-pointers|Ch 2.2]]'s safety rule: **a pointer must be initialized before being [[DereferenceOperator|dereferenced]]** — assign either `&something` or [[NullPointer|`NULL`]] up front.

## Type discipline carries through

The declared [[PointerType|type]] determines what addresses may be assigned:

```c
int x;
char ch;
int *ptr;
char *cptr;

ptr  = &x;    // OK: int * <- int *
cptr = &ch;   // OK: char * <- char *
cptr = &x;    // ERROR: char * expected, int * given — type mismatch
```

The compiler issues a warning; behavior at runtime is *"unpredictable"* per the chapter.

## Connections

- [[CLanguage]] — the language.
- [[Pointer]] — what the declaration introduces.
- [[PointerType]] — the type system the declaration plugs into.
- [[DereferenceOperator]] — the `*` in *expression* context.
- [[AddressOfOperator]] — the operator that produces values fitting a pointer variable's type.
- [[NullPointer]] — the safe default initializer.
- [[VariableDeclaration]] — the broader [[CLanguage|C]] declaration form this specializes.
- [[dis-2-2-pointers]] — defining source.
