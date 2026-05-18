---
title: "NOR Gate"
type: concept
tags: [computer-architecture, logic-gate, digital-circuits, boolean]
sources: [dis-5-3-gates]
last_updated: 2026-05-17
---

# NOR Gate

The **NOR gate** outputs the **negation of OR** — `1` iff both inputs are `0`, else `0` (`¬(A+B)`). [[dis-5-3-gates|DIS Ch 5.3]] gives the textbook composition: *"(A NOR B) ≡ NOT(A OR B)"*.

## Truth table

| A | B | A NOR B |
|---|---|---------|
| 0 | 0 | 1       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 0       |

## Role

- **Functionally complete on its own**, symmetric to [[NandGate|NAND]].
- Composes from a [[NotGate|NOT]] following an [[OrGate|OR]].
- Historically the first transistor logic family (RTL — Resistor-Transistor Logic) was NOR-centric; the **Apollo Guidance Computer** was built entirely from 3-input NOR gates.

## Connections

- [[LogicGate]] — umbrella.
- [[OrGate]] — pre-negation.
- [[BooleanAlgebra]] — formal operator (Peirce arrow `↓`).
- [[dis-5-3-gates]] — defining source.
