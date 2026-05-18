---
title: "OR Gate"
type: concept
tags: [computer-architecture, logic-gate, digital-circuits, boolean]
sources: [dis-5-3-gates]
last_updated: 2026-05-17
---

# OR Gate

The **OR gate** is the two-input [[LogicGate|logic gate]] whose output is `1` **iff at least one input is `1`** — the gate-level instantiation of [[BooleanAlgebra|Boolean]] (inclusive) disjunction (`A+B`).

## Truth table

| A | B | A OR B |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |

## Role

- Member of the functionally-complete basis {[[AndGate|AND]], OR, [[NotGate|NOT]]}.
- Used to **set** bits — `x | MASK` forces positions where `MASK` is `1` to `1` ([[BitwiseOr|`|`]] in [[CLanguage|C]] is an M-bit OR).
- Used in the [[FullAdder|full-adder]] `CarryOut` to combine the three pairwise-AND contributions.
- `A OR A = A`; `A OR 0 = A`; `A OR 1 = 1`.

## Connections

- [[LogicGate]] — umbrella.
- [[BooleanAlgebra]] — formal operator.
- [[NorGate]] — negation.
- [[BitwiseOr]] — language-level M-bit OR.
- [[dis-5-3-gates]] — defining source.
