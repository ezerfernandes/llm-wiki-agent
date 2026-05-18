---
title: "Full Adder"
type: concept
tags: [computer-architecture, circuits, adder, digital-logic]
sources: [dis-5-4-1-arithmetic-logic-circuits, dis-4-4-1-addition, dis-4-4-2-subtraction, dis-4-5-overflow]
last_updated: 2026-05-17
---

# Full Adder

A **full adder** is the per-bit primitive of multi-bit [[BinaryAddition|binary addition]] — a combinational [[ArithmeticLogicCircuit|arithmetic circuit]] with **three** 1-bit inputs (`A`, `B`, `CarryIn`) and **two** 1-bit outputs (`Sum`, `CarryOut`). It is the [[HalfAdder|half adder]] extended with a `CarryIn` port so that one full adder can be cascaded into the next position of a multi-bit add.

*Promoted from forward-reference stub in [[dis-4-4-1-addition|Ch 4.4.1]] (bit-pattern level) and [[dis-5-3-gates|Ch 5.3]] / [[dis-4-5-overflow|Ch 4.5]] (forward references) to a first-class concept page by [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]], which supplies the gate-level construction.*

## Truth table (8 rows)

| `A` | `B` | `CarryIn` | `Sum` | `CarryOut` |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

Pattern: `Sum = 1` iff an odd number of inputs are `1`; `CarryOut = 1` iff a majority of inputs are `1`.

## Boolean form

- `Sum = A XOR B XOR CarryIn` — the parity / XOR-cascade.
- `CarryOut = (A AND B) OR (A AND CarryIn) OR (B AND CarryIn)` — the **majority function** of three bits.

## Gate-level construction

The classic two-half-adder construction:

1. First [[HalfAdder|half adder]]: `(s1, c1) = HalfAdd(A, B)`.
2. Second [[HalfAdder|half adder]]: `(Sum, c2) = HalfAdd(s1, CarryIn)`.
3. `CarryOut = c1 OR c2`.

Total: two [[XorGate|XOR]] gates, two [[AndGate|AND]] gates, one [[OrGate|OR]] gate.

## Why this matters

- **Per-column primitive of multi-bit addition** — [[dis-4-4-1-addition|Ch 4.4.1]] noted *"every column above the LSB needs a 3-input adder because of carry propagation"*; the full adder is exactly that 3-input adder.
- **Cascadable** — `N` full adders wired `CarryOut[i] → CarryIn[i+1]` form a [[RippleCarryAdder|ripple-carry adder]] — Ch 5.4.1's headline N-bit construction.
- **Powers subtraction** — with `CarryIn[0] = 1` and `B` routed through inverters (or [[XorGate|XOR]] gates driven by a mode bit), the same adder implements [[BinarySubtraction|two's-complement subtraction]] via [[dis-4-4-2-subtraction|Ch 4.4.2]]'s flip-and-add-one trick. No new arithmetic hardware needed.
- **Source of both overflow flags** — the same N-bit adder emits both `CF` (unsigned) and `OF` (signed) flags from its MSB position ([[dis-4-5-overflow|Ch 4.5]]).

## Connections

- [[HalfAdder]] — the two-input ancestor; two of them + one OR form one full adder.
- [[RippleCarryAdder]] — N full adders cascaded by carry; this section's namesake circuit.
- [[ArithmeticLogicCircuit]] — this circuit's category.
- [[XorGate]] / [[AndGate]] / [[OrGate]] — the gates the construction uses.
- [[TruthTable]] — 8 rows; first appeared in [[dis-4-4-1-addition|Ch 4.4.1]].
- [[BinaryAddition]] — the bit-pattern-level algorithm implemented per column.
- [[BinarySubtraction]] — same adder + inverters + `CarryIn=1`.
- [[Carry]] — the 1-bit value `CarryOut` produces and the next full adder's `CarryIn` consumes.
- [[ArithmeticLogicUnit]] — the umbrella circuit this contributes to.
- [[dis-5-4-1-arithmetic-logic-circuits]] — primary gate-level construction source.
- [[dis-4-4-1-addition]] — bit-pattern-level truth table source.
- [[dis-4-4-2-subtraction]] — adder-reuse for subtraction.
- [[dis-4-5-overflow]] — `CF` / `OF` flag emission.
