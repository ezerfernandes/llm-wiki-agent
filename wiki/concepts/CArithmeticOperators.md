---
title: "C Arithmetic Operators"
type: concept
tags: [c-language, operators, arithmetic]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# C Arithmetic Operators

The arithmetic operators introduced in [[dis-1-1-getting-started|DIS Ch 1.1]] for [[CLanguage|C]]:

| Operator | Meaning |
|---|---|
| `+` `-` `*` | Addition, subtraction, multiplication |
| `/` | Division — **truncates** when both operands are integers; see [[IntegerDivision]] |
| `%` | Modulo (integer remainder) |
| `=` | Assignment |
| `+=` `-=` `*=` `/=` `%=` | Compound assignment (`x += 1` ≡ `x = x + 1`) |
| `++` `--` | [[IncrementOperator|Increment / decrement]] — with pre- and post- variants that differ in *when* the side effect lands |

## Two traps the chapter calls out explicitly

1. **[[IntegerDivision|Integer division truncates]].** `11 / 2` evaluates to `5`, not `5.5`. Promote one operand to floating-point (`11 / 2.0`) to get real division.
2. **Pre- vs. post-[[IncrementOperator|increment]]** differ in expression semantics. `++x` increments first and yields the new value; `x++` yields the old value and then increments. The chapter recommends *not* mixing these inside larger expressions — separate statements are clearer.

## Connections

- [[CLanguage]] — the host language.
- [[CPrimitiveType]] — the types these operate on.
- [[IntegerDivision]] — the truncation trap.
- [[IncrementOperator]] — the pre/post subtlety.
- [[dis-1-1-getting-started]] — introducing source.
