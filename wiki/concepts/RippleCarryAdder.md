---
title: "Ripple-Carry Adder"
type: concept
tags: [computer-architecture, circuits, adder, digital-logic, alu]
sources: [dis-5-4-1-arithmetic-logic-circuits, dis-4-4-1-addition, dis-4-4-2-subtraction]
last_updated: 2026-05-17
---

# Ripple-Carry Adder

A **ripple-carry adder** is the canonical N-bit [[ArithmeticLogicCircuit|arithmetic circuit]] for [[BinaryAddition|binary addition]] — *"an N-bit adder circuit, built from N 1-bit adder circuits"* ([[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]] of [[DiveIntoSystems|*Dive into Systems*]]). $N$ [[FullAdder|full adders]] are cascaded: each adder's `CarryOut` is wired to the next-higher position's `CarryIn`. The name captures its dynamics — *"the SUM result ripples or propagates through the circuit from the low-order to the high-order bits."*

## Construction

```
A[N-1] B[N-1]   A[1] B[1]   A[0] B[0]
   |     |       |    |      |    |
   v     v       v    v      v    v
  +---FA---+ ...+---FA---+  +---FA---+
  |        |   |        |  |        |
CarryOut  Sum[N-1]  ... Sum[1]  Sum[0]
                                  ^
                                CarryIn[0]
```

- $N$ instances of the [[FullAdder|full adder]] (`A_i`, `B_i`, `CarryIn_i` → `Sum_i`, `CarryOut_i`).
- Carry wiring: `CarryIn_{i+1} = CarryOut_i` for `i = 0..N-2`.
- LSB position's `CarryIn_0` is wired to `0` for addition (and `1` to deliver [[BinarySubtraction|subtraction]] — see below).
- MSB position's `CarryOut_{N-1}` is the **N-bit carry-out flag** (`CF` in [[dis-4-5-overflow|Ch 4.5]]'s sense).

## Operational characterization

> "The SUM result ripples or propagates through the circuit from the low-order to the high-order bits." — [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]]

Because each adder cannot produce its `Sum` until its `CarryIn` is valid, the result is computed sequentially from `i = 0` upward. Worst-case propagation delay is therefore $\Theta(N)$ gate delays — the **ripple latency** that motivates the (out-of-scope) carry-lookahead, carry-select, and Kogge-Stone optimizations real CPU adders use.

## Doubles as subtractor

Per [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]]: *"a subtraction circuit that computes (A − B) can be built from adder and negation circuits."* Standard wiring:

1. Route `B` bits through a row of [[NotGate|inverters]] (or [[XorGate|XOR]] gates driven by a `mode` bit so the same circuit can add **or** subtract).
2. Wire `CarryIn_0 = 1` (or to the `mode` bit, with `mode = 1` ⇒ subtract).

The two together deliver the *flip-and-add-one* [[TwosComplement|two's-complement]] negation from [[dis-4-4-2-subtraction|Ch 4.4.2]] **for free** — same N full adders, no new arithmetic hardware. The mode-XOR variant is the canonical adder/subtractor block found in classic ALU diagrams.

## Where it lives

A ripple-carry adder is the headline arithmetic constituent of the [[ArithmeticLogicUnit|ALU]] — the data-path circuit that executes `ADD` / `SUB` instructions. The same physical block emits both `CF` (unsigned carry) and `OF` (signed overflow) flags from its MSB position ([[dis-4-5-overflow|Ch 4.5]]), so software / the [[CCompiler|C compiler]] chooses which to inspect based on operand types.

## Connections

- [[FullAdder]] — the per-bit primitive cascaded $N$ times.
- [[HalfAdder]] — may sit at the LSB position when `CarryIn = 0` is hard-wired.
- [[ArithmeticLogicCircuit]] — this circuit's category.
- [[ArithmeticLogicUnit]] — the umbrella circuit this is the arithmetic core of.
- [[BinaryAddition]] / [[BinarySubtraction]] — the bit-pattern-level algorithms it implements.
- [[Carry]] — the 1-bit values that ripple between positions.
- [[IntegerOverflow]] — MSB `CarryOut` is the source of `CF` / `OF` flags.
- [[NotGate]] / [[XorGate]] — the inverter row that enables the subtraction mode.
- [[Circuit]] — design discipline (hierarchical composition).
- [[dis-5-4-1-arithmetic-logic-circuits]] — primary source.
- [[dis-4-4-1-addition]] / [[dis-4-4-2-subtraction]] — bit-pattern-level algorithm sources.
- [[dis-4-5-overflow]] — flag-emission semantics.
