---
title: "Logical Operator (C)"
type: concept
tags: [c-language, operator, control-flow]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# Logical Operator (C)

**Logical operators** in [[CLanguage|C]] combine [[CBooleanExpression|boolean expressions]] into compound conditions. They treat any nonzero operand as true and `0` as false, and produce an `int` result of `0` or `1`.

| Operator | Arity  | Name | Meaning                                                |
|---------:|:------:|:-----|:-------------------------------------------------------|
| `!`      | unary  | NOT  | `!x` is `1` if `x` is `0`, else `0`                    |
| `&&`     | binary | AND  | `A && B` is `1` if both `A` and `B` are nonzero        |
| `\|\|`   | binary | OR   | `A \|\| B` is `1` if either `A` or `B` is nonzero      |

## Short-circuit evaluation

Per [[dis-1-3-conditionals-loops|DiS Ch 1.3]]: **"logical operator evaluation stops evaluating a logical expression as soon as the result is known."** See [[ShortCircuitEvaluation]] for the formal treatment.

- In `A && B`, if `A` is false, `B` is **never evaluated** — the result is already known to be false.
- In `A || B`, if `A` is true, `B` is **never evaluated** — the result is already known to be true.

This makes guard idioms safe: `if (p != NULL && *p == 0)` cannot dereference a null pointer because `*p` is skipped when `p == NULL`.

## Combining with relational operators

Logical operators usually compose results of [[RelationalOperator|relational operators]] into multi-clause tests:

```c
if (x > 0 && x % 2 == 0) printf("positive even\n");
if (c == ' ' || c == '\t' || c == '\n') printf("whitespace\n");
if (!is_valid(input)) printf("rejected\n");
```

## Precedence

`!` binds tighter than `&&`, which binds tighter than `||` — but both bind looser than [[RelationalOperator|relational operators]], so `x > 0 && y > 0` parses as `(x > 0) && (y > 0)`. When in doubt, add parentheses.

## Bitwise vs. logical

Do **not** confuse `&&` / `||` / `!` (logical, work on truthiness) with `&` / `|` / `~` (bitwise, work on the bit pattern of integers). `1 & 2` is `0`; `1 && 2` is `1`. The bitwise operators are introduced in a later chapter of [[DiveIntoSystems]].

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[ShortCircuitEvaluation]] — the early-exit semantics that makes guard idioms safe.
- [[RelationalOperator]] — the operator family typically combined by `&&` / `||`.
- [[CBooleanExpression]] — the integer-valued boolean representation.
- [[IfStatement]] / [[WhileLoop]] / [[ForLoop]] / [[DoWhileLoop]] — the tests that use logical operators.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
- [[booleanalgebra]] — the abstract algebra logical operators implement; [[propositionallogic]] — the symbolic logic side.
