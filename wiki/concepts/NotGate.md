---
title: "NOT Gate (Inverter)"
type: concept
tags: [computer-architecture, logic-gate, digital-circuits, boolean]
sources: [dis-5-3-gates]
last_updated: 2026-05-17
---

# NOT Gate (Inverter)

The **NOT gate** — also called an **inverter** — is the unique single-input [[LogicGate|logic gate]]: its output is the **inverse** of its input (`¬A`). The only **unary** basic gate.

## Truth table

| A | NOT A |
|---|-------|
| 0 | 1     |
| 1 | 0     |

## Role

- Member of the functionally-complete basis {[[AndGate|AND]], [[OrGate|OR]], NOT}.
- The negation primitive — combined with [[AndGate|AND]] / [[OrGate|OR]] it produces [[NandGate|NAND]] / [[NorGate|NOR]] / [[XnorGate|XNOR]].
- Used in the *"flip operand B"* step of [[dis-4-4-2-subtraction|two's-complement subtraction]] (one inverter per operand bit).
- `NOT(NOT A) = A` (involution); language-level [[BitwiseNot|`~`]] is an M-bit NOT.

## Connections

- [[LogicGate]] — umbrella.
- [[BooleanAlgebra]] — formal operator (complement).
- [[BitwiseNot]] — language-level M-bit NOT.
- [[dis-5-3-gates]] — defining source.
