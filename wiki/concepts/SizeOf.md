---
title: "sizeof"
type: concept
tags: [c-language, types, operator]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# sizeof

**`sizeof`** is a compile-time [[CLanguage|C]] operator that returns the size, in bytes, of a type or expression. Introduced in [[dis-1-1-getting-started|DIS Ch 1.1]] as the canonical way to ask the compiler about [[CPrimitiveType|primitive-type]] widths.

```c
sizeof(int)      /* typically 4 */
sizeof(double)   /* 8 */
sizeof(x)        /* size of whatever x's declared type is */
sizeof("hello")  /* 6 — five chars plus the '\0' terminator */
```

`sizeof` evaluates **at compile time**, not run time — it does not actually execute its operand. This makes it safe to use on expressions with side effects (`sizeof(x++)` does not increment `x`).

## Why this matters

- Lets portable C code avoid hard-coding type widths — important because `long` (and pointer width) is [[CPrimitiveType|platform-dependent]].
- Underlies idiomatic dynamic-allocation patterns: `malloc(n * sizeof(int))`.

## Connections

- [[CLanguage]] — the host language.
- [[CPrimitiveType]] — the canonical operand.
- [[VariableDeclaration]] — the declarations whose widths it measures.
- [[dis-1-1-getting-started]] — introducing source.
