---
title: "Logic Gate"
type: concept
tags: [computer-architecture, digital-circuits, boolean, hardware]
sources: [dis-5-3-gates]
last_updated: 2026-05-17
---

# Logic Gate

A **logic gate** is the elementary digital-circuit primitive: a small circuit (built from [[Transistor|transistors]]) that computes one [[BooleanAlgebra|Boolean]] operation over one or two 1-bit inputs and emits a 1-bit output. *"Logic gates are the building blocks of the digital circuitry that implements arithmetic, control, and storage functionality in a digital computer"* ([[dis-5-3-gates|DIS Ch 5.3]]).

## The seven canonical gates

Specified by their [[TruthTable|truth tables]]:

- **[[AndGate|AND]]** — `1` iff both inputs are `1`.
- **[[OrGate|OR]]** — `1` iff at least one input is `1`.
- **[[NotGate|NOT]]** — inverter; the only **unary** basic gate.
- **[[NandGate|NAND]]** — negation of AND.
- **[[NorGate|NOR]]** — negation of OR.
- **[[XorGate|XOR]]** — `1` iff inputs differ.
- **[[XnorGate|XNOR]]** — `1` iff inputs are equal.

## Completeness

The three-gate set {[[AndGate|AND]], [[OrGate|OR]], [[NotGate|NOT]]} is **functionally complete** — every digital circuit (including the entire [[CPU]]) can be built from these three. Equivalently, [[NandGate|NAND]] alone or [[NorGate|NOR]] alone is functionally complete. The other gates exist for compactness and clarity. The completeness result traces to [[ClaudeShannon|Shannon]]'s 1937 *"A Symbolic Analysis of Relay and Switching Circuits"*, which proved switching circuits implement [[BooleanAlgebra|Boolean algebra]].

## Multi-bit gates

An **M-bit gate** is just M copies of a 1-bit gate operating in parallel on corresponding input bits — *"an M-bit gate comprises M individual one-bit gates."* This is exactly the per-bit semantics of [[CLanguage|C]]'s [[BitwiseOperator|bitwise operators]] (`&` = M-bit AND, `|` = M-bit OR, `^` = M-bit XOR, `~` = M-bit NOT).

## Connections

- [[BooleanAlgebra]] — the formal algebra each gate implements one operator of.
- [[Transistor]] — the physical switch from which gates are built.
- [[TruthTable]] — the canonical specification format for any gate.
- [[ArithmeticLogicUnit]] — composed from gates; the [[FullAdder|full-adder]] of [[dis-4-4-1-addition|Ch 4.4.1]] is a concrete XOR+AND+OR construction.
- [[BitwiseOperator]] — language-level exposure of M-bit gates.
- [[ClaudeShannon]] — 1937 thesis establishing circuits-as-Boolean-algebra.
- [[dis-5-3-gates]] — introductory source.
