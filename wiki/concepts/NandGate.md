---
title: "NAND Gate"
type: concept
tags: [computer-architecture, logic-gate, digital-circuits, boolean]
sources: [dis-5-3-gates]
last_updated: 2026-05-17
---

# NAND Gate

The **NAND gate** outputs the **negation of AND** — `0` iff both inputs are `1`, else `1` (`¬(A·B)`).

## Truth table

| A | B | A NAND B |
|---|---|----------|
| 0 | 0 | 1        |
| 0 | 1 | 1        |
| 1 | 0 | 1        |
| 1 | 1 | 0        |

## Role

- **Functionally complete on its own**: any digital circuit can be built from NAND gates alone. Industrial CMOS processes often prefer NAND-only or NOR-only fabrics because the universality simplifies layout.
- Composes from a [[NotGate|NOT]] following an [[AndGate|AND]].
- Used in [[StaticRAM|SRAM cells]] (cross-coupled NAND/NOR latches — beyond DIS Ch 5.3's scope).

## Connections

- [[LogicGate]] — umbrella.
- [[AndGate]] — pre-negation.
- [[BooleanAlgebra]] — formal operator (Sheffer stroke `|`).
- [[dis-5-3-gates]] — defining source.
