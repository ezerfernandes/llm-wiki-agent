---
title: "XOR Gate"
type: concept
tags: [computer-architecture, logic-gate, digital-circuits, boolean]
sources: [dis-5-3-gates]
last_updated: 2026-05-17
---

# XOR Gate (Exclusive OR)

The **XOR gate** outputs `1` **iff the inputs differ** (`A⊕B`) — the gate-level instantiation of inequality / exclusive disjunction.

## Truth table

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 0       |

## Role

- The **headline gate for [[BinaryArithmetic|binary arithmetic]]**: in the [[FullAdder|full-adder]] of [[dis-4-4-1-addition|Ch 4.4.1]], `Sum = A XOR B XOR CarryIn`.
- Implements the *"flip operand B controlled by mode wire"* trick from [[dis-4-4-2-subtraction|Ch 4.4.2]] — an XOR with a mode bit selectively inverts.
- Useful for **toggling** bits — `x ^ MASK` flips every position where `MASK` is `1` ([[BitwiseXor|`^`]] in [[CLanguage|C]] is an M-bit XOR).
- `A XOR A = 0`; `A XOR 0 = A`; `A XOR 1 = NOT A`. Self-inverse: `(x ^ k) ^ k = x` — the basis of cheap encryption / hash mixing.
- Constructible from AND/OR/NOT: `A XOR B = (A AND NOT B) OR (NOT A AND B)`.

## Connections

- [[LogicGate]] — umbrella.
- [[XnorGate]] — negation.
- [[BitwiseXor]] — language-level M-bit XOR.
- [[FullAdder]] — direct architectural use.
- [[BooleanAlgebra]] — formal operator.
- [[dis-5-3-gates]] — defining source.
