---
title: "Half Adder (1-bit adder)"
type: concept
tags: [computer-architecture, circuits, adder, digital-logic]
sources: [dis-5-4-1-arithmetic-logic-circuits, dis-4-4-1-addition]
last_updated: 2026-05-17
---

# Half Adder (1-bit adder)

A **half adder** is the simplest [[ArithmeticLogicCircuit|arithmetic circuit]] — a combinational [[Circuit|digital circuit]] that adds two 1-bit inputs `A` and `B` and produces two 1-bit outputs: a `SUM` bit and a `CARRY OUT` bit. *"1-bit adder"* in [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]] of [[DiveIntoSystems|*Dive into Systems*]]; the more common textbook name **half adder** captures the *"half"* — it cannot accept an incoming carry (a [[FullAdder|full adder]] adds that third input).

## Truth table

| `A` | `B` | `Sum` | `CarryOut` |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

## Boolean form

- `Sum = A XOR B` — equivalently *"(NOT(A) AND B) OR (A AND NOT(B)) — 1 when exactly one of A or B is 1"* ([[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]]).
- `CarryOut = A AND B` — the carry out is `1` only when the sum overflows the 1-bit position (`1 + 1 = 0b10`).

## Gate-level construction

Two gates suffice:

- One [[XorGate|XOR]] computes `Sum`.
- One [[AndGate|AND]] computes `CarryOut`.

This is the minimal arithmetic circuit — the textbook entry point that demonstrates the [[ArithmeticLogicCircuit|three-step methodology]] (truth table → Boolean → gates) producing a useful primitive.

## Why "half"

The half adder is missing the third input that real multi-bit addition requires: a [[Carry|carry-in]] from the next-lower column. Once the LSB column produces a carry, every higher column needs to accept that carry as a third operand — which the half adder cannot. The [[FullAdder|full adder]] of [[dis-4-4-1-addition|Ch 4.4.1]] adds that third input and becomes the per-bit primitive of multi-bit addition.

## Connections

- [[FullAdder]] — the half adder's three-input successor; two half adders + one OR gate form one full adder.
- [[RippleCarryAdder]] — $N$ full adders cascaded; a half adder may serve as the LSB position when `CarryIn` is hard-wired to `0`.
- [[ArithmeticLogicCircuit]] — this circuit's category.
- [[XorGate]] / [[AndGate]] — the two gates that realize it.
- [[BinaryAddition]] — the bit-pattern-level algorithm this circuit implements at the gate level.
- [[ArithmeticLogicUnit]] — the umbrella circuit this contributes to.
- [[dis-5-4-1-arithmetic-logic-circuits]] — primary source.
- [[dis-4-4-1-addition]] — bit-pattern-level addition algorithm.
