---
title: "XNOR Gate"
type: concept
tags: [computer-architecture, logic-gate, digital-circuits, boolean]
sources: [dis-5-3-gates]
last_updated: 2026-05-17
---

# XNOR Gate (Equivalence)

The **XNOR gate** outputs `1` **iff the inputs are equal** — the negation of [[XorGate|XOR]], also called the **equivalence** gate (`A ≡ B`).

## Truth table

| A | B | A XNOR B |
|---|---|----------|
| 0 | 0 | 1        |
| 0 | 1 | 0        |
| 1 | 0 | 0        |
| 1 | 1 | 1        |

## Role

- Used in **equality comparators** — bitwise XNOR followed by an M-input AND tells whether two M-bit words are equal.
- Composes from a [[NotGate|NOT]] following an [[XorGate|XOR]].
- `A XNOR A = 1`; `A XNOR 1 = A`; `A XNOR 0 = NOT A`.

## Connections

- [[LogicGate]] — umbrella.
- [[XorGate]] — pre-negation.
- [[BooleanAlgebra]] — formal operator (biconditional `↔`).
- [[dis-5-3-gates]] — defining source (mentioned alongside the other derived gates; not given its own truth table in the chapter prose).
