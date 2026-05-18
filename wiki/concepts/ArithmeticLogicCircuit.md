---
title: "Arithmetic and Logic Circuit"
type: concept
tags: [computer-architecture, circuits, alu, adder, digital-logic]
sources: [dis-5-4-1-arithmetic-logic-circuits, dis-5-4-circuits]
last_updated: 2026-05-17
---

# Arithmetic and Logic Circuit

An **arithmetic-and-logic circuit** is the first of the three categories of [[Circuit|digital circuit]] that [[dis-5-4-circuits|Ch 5.4]] partitions processor circuitry into — circuits whose job is to **operate on data**, producing arithmetic results (sum, difference, product, quotient) or logical results ([[BooleanAlgebra|Boolean]] / comparison outputs). The category sits below the [[ArithmeticLogicUnit|ALU]] umbrella and above the gate-level primitives of [[dis-5-3-gates|Ch 5.3]]; [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]] is its construction layer.

## Three-step design methodology ([[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]])

The methodology for designing any 1-bit combinational arithmetic-or-logic circuit:

1. **Truth table** — enumerate every input combination → output bit ([[TruthTable]]).
2. **Boolean expression** — for each output column, write an expression in [[AndGate|AND]] / [[OrGate|OR]] / [[NotGate|NOT]] that evaluates to `1` on exactly the rows where the output is `1` (sum-of-minterms).
3. **Gate translation** — render the expression as a [[LogicGate|gate]]-level network of wires + gates.

The methodology is **recursive** — each finished circuit becomes a black-box at the next level up, matching the [[Circuit|hierarchical composition]] discipline.

## Canonical examples from [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]]

| Circuit | Inputs | Outputs | Boolean form |
|---|---|---|---|
| [[OneBitEqualityCircuit\|1-bit equals]] | `A`, `B` | `Equal` | `(NOT A AND NOT B) OR (A AND B)` ≡ [[XnorGate\|XNOR]] |
| [[HalfAdder\|1-bit adder]] | `A`, `B` | `Sum`, `CarryOut` | `Sum = A XOR B`, `CarryOut = A AND B` |
| [[FullAdder\|1-bit full adder]] | `A`, `B`, `CarryIn` | `Sum`, `CarryOut` | `Sum = A XOR B XOR CarryIn`, `CarryOut = majority` |
| [[RippleCarryAdder\|N-bit ripple-carry adder]] | $N$ × (`A`, `B`) + LSB `CarryIn` | $N$ × `Sum` + MSB `CarryOut` | $N$ full adders cascaded by carry |
| Subtraction circuit | `A`, `B` | `A − B` | Ripple-carry adder + inverters on `B` + `CarryIn = 1` |

## Relation to the ALU

[[dis-5-4-circuits|Ch 5.4]]'s three-way partition assigns the [[ArithmeticLogicUnit|ALU]]'s internals to this category:

- **Arithmetic side** — adder / subtractor / multiplier / divider constructions, the [[RippleCarryAdder|ripple-carry adder]] being the headline example built in Ch 5.4.1.
- **Logic side** — M-bit gate networks ([[dis-5-3-gates|Ch 5.3]]) plus comparators like the 1-bit equality circuit.

Where the [[ControlCircuit|control circuit]] category sequences operations and the [[StorageCircuit|storage circuit]] category holds data, **arithmetic-and-logic circuits compute**.

## Connections

- [[Circuit]] — umbrella discipline (hierarchical composition + [[Abstraction|black-box abstraction]]).
- [[ArithmeticLogicUnit]] — the CPU-level circuit this category aggregates into.
- [[LogicGate]] — the primitive building blocks.
- [[TruthTable]] — step-1 specification format of the methodology.
- [[BooleanAlgebra]] — the algebra step-2 expressions live in.
- [[OneBitEqualityCircuit]] / [[HalfAdder]] / [[FullAdder]] / [[RippleCarryAdder]] — the four named circuits Ch 5.4.1 constructs.
- [[ControlCircuit]] / [[StorageCircuit]] — the sibling circuit categories.
- [[dis-5-4-1-arithmetic-logic-circuits]] — primary source.
- [[dis-5-4-circuits]] — parent hub.
