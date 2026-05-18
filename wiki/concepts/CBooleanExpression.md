---
title: "Boolean Expression (C)"
type: concept
tags: [c-language, control-flow, type-system]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# Boolean Expression (C)

A **boolean expression** in [[CLanguage|C]] is an expression whose value is used as a truth value in a control-flow test ([[IfStatement|`if`]], [[WhileLoop|`while`]], [[ForLoop|`for`]], [[DoWhileLoop|`do`–`while`]], the ternary `?:`).

## Integer-as-boolean

Per [[dis-1-3-conditionals-loops|DiS Ch 1.3]]: **C has no dedicated boolean type.** Instead:

> "Zero (0) evaluates to false, and nonzero (any positive or negative value) evaluates to true."

So a boolean expression is just an integer-valued expression evaluated in a truth context. Consequences:

- `if (x)` is valid C — it tests `x != 0`.
- `while (1)` is the idiomatic infinite loop (along with `for (;;)`).
- [[RelationalOperator|Relational operators]] produce `0` or `1`, never an arbitrary nonzero "true" — but the language accepts any nonzero value as true on input.

## Building boolean expressions

[[dis-1-3-conditionals-loops|DiS Ch 1.3]] introduces two operator families that produce / combine truth values:

- **[[RelationalOperator|Relational operators]]** `==` `!=` `<` `<=` `>` `>=` — compare two operands.
- **[[LogicalOperator|Logical operators]]** `!` `&&` `||` — negate / combine, with [[ShortCircuitEvaluation|short-circuit semantics]].

## `_Bool` and `<stdbool.h>` (C99)

C99 added the `_Bool` type and the `<stdbool.h>` header providing `bool` / `true` / `false` aliases — but [[dis-1-3-conditionals-loops|DiS Ch 1.3]] does not introduce these and teaches the original integer-as-boolean model that the rest of the textbook uses. The integer-as-boolean model is still the dominant idiom in systems-level C code.

## The `=` vs `==` trap

Because assignment `=` *is itself an expression* whose value is the assigned value, `if (x = 0)` is legal C — it assigns `0` to `x` and tests the resulting `0` (always false). The intended `if (x == 0)` is one character away. Compile with `-Wall` to be warned.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[RelationalOperator]] / [[LogicalOperator]] — the operator families that produce / combine boolean expressions.
- [[ShortCircuitEvaluation]] — early-exit semantics of `&&` / `||`.
- [[IfStatement]] / [[ElseStatement]] / [[SwitchStatement]] / [[WhileLoop]] / [[DoWhileLoop]] / [[ForLoop]] — the constructs that consume boolean expressions.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
- [[booleanalgebra]] / [[propositionallogic]] — the underlying mathematical theory.
