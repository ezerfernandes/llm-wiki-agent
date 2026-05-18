---
title: "1-bit Equality Circuit"
type: concept
tags: [computer-architecture, circuits, comparator, digital-logic]
sources: [dis-5-4-1-arithmetic-logic-circuits]
last_updated: 2026-05-17
---

# 1-bit Equality Circuit

A **1-bit equality circuit** ("1-bit equals circuit" in [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]] of [[DiveIntoSystems|*Dive into Systems*]]) is a combinational [[ArithmeticLogicCircuit|logic circuit]] with two 1-bit inputs `A`, `B` and one 1-bit output that is `1` exactly when `A == B`. It is the textbook entry point for the three-step circuit design methodology — small enough to walk through end-to-end yet useful enough to be a real comparator primitive.

## Truth table

| `A` | `B` | `A == B` |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## Boolean form

> "(NOT(A) AND NOT(B)) OR (A AND B) # is 1 when A and B are both 0 or both 1" — [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]]

Equivalently, the circuit *is* the [[XnorGate|XNOR]] gate of [[dis-5-3-gates|Ch 5.3]] (`A XNOR B`, or `NOT(A XOR B)`). Ch 5.4.1 builds it from the [[AndGate|AND]] / [[OrGate|OR]] / [[NotGate|NOT]] functionally-complete basis as a methodology demonstration, but the result is equivalent to a single XNOR.

## Why it matters

- **Demonstrates the methodology** — the three-step recipe (truth table → sum-of-minterms Boolean → gate network) applied end-to-end on a small but useful circuit.
- **Building block of multi-bit equality** — M-bit equality (e.g. *"do registers `%rax` and `%rbx` hold the same value?"*) is built from M of these 1-bit equality circuits whose outputs are AND-ed together — the M-bit `XNOR` + M-input `AND` comparator the wiki noted on [[XnorGate]].

## Connections

- [[XnorGate]] — same truth table; this circuit *is* the XNOR (Ch 5.4.1 just constructs it from AND/OR/NOT).
- [[XorGate]] — the negation of this circuit; differs gives `1` instead of equality.
- [[AndGate]] / [[OrGate]] / [[NotGate]] — the functionally-complete basis Ch 5.4.1 builds it from.
- [[ArithmeticLogicCircuit]] — this circuit's category (the logic side).
- [[TruthTable]] — step-1 specification.
- [[ArithmeticLogicUnit]] — comparison circuits live inside the ALU.
- [[dis-5-4-1-arithmetic-logic-circuits]] — primary source.
- [[dis-5-3-gates]] — gate-level basis the construction uses.
