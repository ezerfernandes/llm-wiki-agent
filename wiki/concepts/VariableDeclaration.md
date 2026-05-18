---
title: "Variable Declaration (C)"
type: concept
tags: [c-language, types, syntax]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# Variable Declaration (C)

In [[CLanguage|C]], **all variables must be declared before they can be used** ([[dis-1-1-getting-started|DIS Ch 1.1]]). The syntax is:

```c
type_name variable_name;          /* uninitialized */
type_name variable_name = value;  /* initialized */
```

Examples:

```c
int   count = 0;
float ratio = 0.5f;
char  letter = 'h';
```

## Why this matters

- C is [[StaticallyTyped|statically typed]] — every variable has a fixed type known at compile time, and the type drives memory layout, arithmetic semantics ([[IntegerDivision|integer vs. real division]]), and ABI.
- The compiler uses declarations to allocate the right number of bytes on the stack / in the data segment — see [[CPrimitiveType]] and [[SizeOf]] for the byte-width table.
- This rule is one of the big differences from [[Python]], where variables come into existence on first assignment and carry a runtime type tag.

## Style note from [[dis-1-1-getting-started|Ch 1.1]]

The book recommends declaring variables **at the beginning of a block** (function-body or sub-block) as a matter of style, though modern C (C99+) permits declarations anywhere a statement is allowed.

## Connections

- [[CLanguage]] — the host language.
- [[CPrimitiveType]] — the set of type names allowed on the left.
- [[StaticallyTyped]] — the typing discipline this enforces.
- [[SizeOf]] — the operator that returns the byte width the declaration reserves.
- [[Python]] — the dynamic-typed contrast.
- [[dis-1-1-getting-started]] — introducing source.
