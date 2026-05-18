---
title: "AND Gate"
type: concept
tags: [computer-architecture, logic-gate, digital-circuits, boolean]
sources: [dis-5-3-gates]
last_updated: 2026-05-17
---

# AND Gate

The **AND gate** is the two-input [[LogicGate|logic gate]] whose output is `1` **iff both inputs are `1`** — the gate-level instantiation of [[BooleanAlgebra|Boolean]] conjunction (`A·B`).

## Truth table

| A | B | A AND B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 1       |

## Role

- Member of the functionally-complete basis {AND, [[OrGate|OR]], [[NotGate|NOT]]}.
- Used to **mask** bits — `x & MASK` zeros out positions where `MASK` is `0` ([[BitwiseAnd|`&`]] in [[CLanguage|C]] is an M-bit AND).
- Used in the [[FullAdder|full-adder]] `CarryOut` generation — `CarryOut = (A·B) + (A·CarryIn) + (B·CarryIn)`.
- `A AND A = A` (idempotence); `A AND 0 = 0`; `A AND 1 = A`.

## Connections

- [[LogicGate]] — umbrella.
- [[BooleanAlgebra]] — formal operator.
- [[NandGate]] — negation.
- [[BitwiseAnd]] — language-level M-bit AND.
- [[dis-5-3-gates]] — defining source.
