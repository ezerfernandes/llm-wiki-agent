---
title: "C Constant (#define)"
type: concept
tags: [c-language, preprocessor, constant, define]
sources: [dis-2-9-1-advanced-switch]
last_updated: 2026-05-17
---

# C Constant (`#define`)

A **C constant** is a **preprocessor-managed symbolic alias** for a literal value, declared outside any function with the `#define` directive. It improves readability (named magic numbers) and maintainability (single-point-of-change).

```c
#define const_name (literal_value)
```

Canonical examples from [[dis-2-9-1-advanced-switch|DiS Ch 2.9.1]]:

```c
#define N    (20)
#define PI   (3.14)
#define NAME ("Sarita")
```

## How it works

`#define` is a [[PreprocessorDirective|preprocessor directive]] — before the [[CCompiler|compiler]] proper sees the source, the [[CPreprocessor|preprocessor]] performs textual substitution of every occurrence of `const_name` with `literal_value`. The substituted token has **no storage** — there's no variable at runtime, just an inlined literal.

## Three load-bearing rules

1. **Constants are not [[LValue|lvalues]]** — `N = 50;` is a **compile error** (after substitution it becomes `20 = 50;`, which is syntactically invalid).
2. **Parenthesize the value** — the wrapping `(...)` is the convention that prevents operator-precedence surprises. `#define HALF 1/2` substituted into `x * HALF` yields `x * 1/2` (integer division of `x*1`); `#define HALF (1/2)` keeps the literal isolated.
3. **Conventionally [[UpperSnakeCase|UPPER_SNAKE_CASE]]** — visually distinguishes constants from variables.

## `#define` vs `const` vs `enum` — choosing among the three

| Mechanism | Runtime cost | Type-checked | Debugger sees name | Scoped |
|---|---|---|---|---|
| `#define N (20)` | Zero — preprocessor inlines | No (raw substitution) | No (replaced before compile) | No (file-global from definition line) |
| [[ConstQualifier\|`const int N = 20;`]] | Variable allocation (often optimized away) | Yes | Yes | Yes (block / file / function scope) |
| [[CEnum\|`enum { N = 20 };`]] | Zero — compile-time integer constant | Yes ([[CEnum\|enum]] type) | Yes (named) | Yes (file scope) |

`#define` is the most permissive (any literal type — `int`, `float`, **string**, even expressions). [[ConstQualifier|`const`]] gives type-checking and debugging at the cost of allocation. [[CEnum|`enum`]] is the type-safe replacement for `#define`d **integer** constants only.

## Headline benefit

**Single-point-of-change maintainability**: changing one `#define` updates every usage. This is why `#define MAX_STUDENTS (40)` beats hard-coding `40` in N places.

## Connections

- [[dis-2-9-1-advanced-switch]] — source.
- [[CPreprocessor]] — the phase that performs the substitution.
- [[PreprocessorDirective]] — the directive family (`#include`, `#define`, `#ifdef`, ...).
- [[ConstQualifier]] — the `const` type qualifier: the typed-variable alternative.
- [[CEnum]] — the typed enumerated alternative for integer constants.
- [[CLanguage]] / [[DiveIntoSystems]].
