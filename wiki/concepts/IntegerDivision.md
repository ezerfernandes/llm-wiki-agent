---
title: "Integer Division"
type: concept
tags: [c-language, arithmetic, numerics]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# Integer Division

**Integer division** in [[CLanguage|C]] **truncates** — the result is the integer quotient, with the fractional part discarded. Introduced as a load-bearing trap in [[dis-1-1-getting-started|DIS Ch 1.1]].

```c
11 / 2     /* → 5     (both operands are int) */
11 / 2.0   /* → 5.5   (2.0 is a double — real division) */
11.0 / 2   /* → 5.5   (one float operand suffices) */
```

The rule: **if either operand is a floating-point type, the division is real**; **if both are integer types, the division is integer**. This means a one-character source change (`2` → `2.0`) silently flips the semantics of the program.

## Why this trap matters

- **Off-by-many bugs.** A formula like `(a + b) / 2` returns an integer midpoint even if `a` and `b` are wildly different.
- **Loss-of-precision bugs in averages, ratios, normalization.** `count / total` is almost always `0` when both are integer counts and `count < total`.
- **Performance side benefit.** Integer division is faster than floating-point on most hardware; library writers sometimes rely on the truncation deliberately.

The companion operator [[CArithmeticOperators|`%`]] gives the integer remainder; together `/` and `%` provide quotient-and-remainder.

## Connections

- [[CLanguage]] — the host language.
- [[CArithmeticOperators]] — the operator family this belongs to.
- [[CPrimitiveType]] — `int` vs. `float`/`double` distinction.
- [[dis-1-1-getting-started]] — introducing source.
