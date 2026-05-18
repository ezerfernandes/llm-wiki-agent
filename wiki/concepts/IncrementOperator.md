---
title: "Increment / Decrement Operators"
type: concept
tags: [c-language, operators, arithmetic]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# Increment / Decrement Operators

C's **`++`** and **`--`** operators add or subtract `1` from an integer variable in place. Each has two forms that differ in *when* the side effect lands relative to the expression's value ([[dis-1-1-getting-started|DIS Ch 1.1]]):

| Form | Name | Behaviour |
|---|---|---|
| `++x` | **Pre-increment** | Increment first, then yield the new value of `x`. |
| `x++` | **Post-increment** | Yield the current value of `x`, then increment. |
| `--x` | **Pre-decrement** | Mirror of pre-increment, subtracting 1. |
| `x--` | **Post-decrement** | Mirror of post-increment. |

Standalone (`x++;` on its own line) the two are interchangeable. They diverge only when used inside a larger expression:

```c
int x = 5;
int a = ++x;   /* x becomes 6, a = 6 */
int y = 5;
int b = y++;   /* b = 5, then y becomes 6 */
```

## Style guidance from Ch 1.1

The chapter explicitly recommends **not** mixing `++` / `--` inside larger expressions — write them as standalone statements for clarity:

```c
/* Cleaner: */
x++;
int a = x;

/* Avoid: */
int a = x++ + ++x;   /* hard to read; technically UB in many forms */
```

## Connections

- [[CLanguage]] — the host language.
- [[CArithmeticOperators]] — the operator family this belongs to.
- [[VariableDeclaration]] — the declarations whose state these mutate.
- [[dis-1-1-getting-started]] — introducing source.
