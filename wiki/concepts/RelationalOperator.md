---
title: "Relational Operator (C)"
type: concept
tags: [c-language, operator, control-flow]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# Relational Operator (C)

**Relational operators** in [[CLanguage|C]] compare two operands and produce an integer result — `1` if the comparison holds, `0` if it does not. They are the building blocks of [[CBooleanExpression|boolean expressions]] for [[IfStatement|`if`]] / [[WhileLoop|`while`]] / [[ForLoop|`for`]] tests.

| Operator | Meaning                  |
|---------:|:-------------------------|
| `==`     | equal to                 |
| `!=`     | not equal to             |
| `<`      | less than                |
| `<=`     | less than or equal to    |
| `>`      | greater than             |
| `>=`     | greater than or equal to |

## Semantics (per [[dis-1-3-conditionals-loops|DiS Ch 1.3]])

- **Result type is `int`**, value `0` or `1`. This is the *integer-valued boolean* representation that [[CBooleanExpression]] codifies — the chapter's first statement is that C has no dedicated boolean type.
- **Operand promotion rules apply**: arithmetic operands are promoted to a common type before comparison (so `int < double` compares two `double`s after promotion).
- **`==` vs `=` is a frequent footgun**: `x == 0` *tests*, `x = 0` *assigns* (and the assigned value `0` then acts as a false test). [[DiveIntoSystems]] warns explicitly.
- **String comparison is *not* `==`**. `"hello" == "hello"` compares two pointer addresses, not characters. Use `strcmp` from [[HeaderFile|`<string.h>`]].

## Combining with logical operators

Relational operators alone produce single-comparison results. Compound conditions ("positive **and** even", "zero **or** negative") are built by combining relational results with [[LogicalOperator|logical operators]] `&&` / `||` / `!`, with [[ShortCircuitEvaluation|short-circuit evaluation]] applying.

## Example

```c
if (x >= 0 && x < 100) {
    printf("in [0, 100)\n");
}
```

`x >= 0` and `x < 100` each evaluate to `0` or `1`; the [[LogicalOperator|`&&`]] returns `1` only if both are nonzero.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[LogicalOperator]] — sibling family for combining relational results.
- [[ShortCircuitEvaluation]] — early-exit semantics of `&&` / `||`.
- [[CBooleanExpression]] — the integer-valued result type that relational operators produce.
- [[CArithmeticOperators]] — the *non*-relational operator family from [[dis-1-1-getting-started|Ch 1.1]]; `=` (assignment) is in that family and is famously confused with `==`.
- [[IfStatement]] / [[WhileLoop]] / [[ForLoop]] / [[DoWhileLoop]] — the constructs whose tests use relational operators.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
