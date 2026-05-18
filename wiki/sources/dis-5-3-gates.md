---
title: "Dive into Systems — Ch 5.3 Logic Gates"
type: source
tags: [computer-architecture, logic-gates, digital-circuits, boolean, textbook]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C5-Arch/gates.html
---

## Summary

Chapter 5.3 of [[DiveIntoSystems]] introduces **[[LogicGate|logic gates]]** as the **building blocks of digital circuitry** — the level just below the [[ArithmeticLogicUnit|ALU]] / [[CpuRegister|registers]] of [[dis-5-2-von-neumann|Ch 5.2]]. Each gate implements a single [[BooleanAlgebra|Boolean]] operation over one or two 1-bit inputs, physically realized by [[Transistor|transistors]] acting as voltage-controlled switches. The chapter codifies seven gates organized into two tiers: the **complete set** [[AndGate|AND]] / [[OrGate|OR]] / [[NotGate|NOT]] (from which any digital circuit can be built) and the **derived gates** [[NandGate|NAND]] / [[NorGate|NOR]] / [[XorGate|XOR]] (convenience extensions). Each gate is specified by its [[TruthTable|truth table]] and a schematic symbol. Multi-bit gates are constructed by replicating a 1-bit gate $M$ times across $M$ pairs of input bits in parallel.

## Key Claims

- **Logic gates are *"the building blocks of the digital circuitry that implements arithmetic, control, and storage functionality in a digital computer."*** They sit one layer below the [[ArithmeticLogicUnit|ALU]] of [[dis-5-2-von-neumann|Ch 5.2]] — the [[ArithmeticLogicUnit|ALU]]'s addition, subtraction, [[BitwiseOperator|bitwise]], and comparison circuits are all composed from gates.
- **Gates are built from [[Transistor|transistors]]** — *"a transistor can switch its state between on or off (between a high or low voltage output)"* — and a transistor is fundamentally a voltage-controlled switch regulating electrical flow.
- **The complete set is [[AndGate|AND]] / [[OrGate|OR]] / [[NotGate|NOT]]** — any digital circuit, including the full [[CPU]], can be built from these three primitives alone. [[NandGate|NAND]] / [[NorGate|NOR]] / [[XorGate|XOR]] / [[XnorGate|XNOR]] are derivable but commonly provided as named gates for compactness.
- **Each gate has a fixed [[TruthTable|truth table]]** mapping every possible combination of 1-bit inputs to a 1-bit output:
  - **[[AndGate|AND]]**: output `1` iff *both* inputs are `1` (`A·B`).
  - **[[OrGate|OR]]**: output `1` iff *at least one* input is `1` (`A+B`).
  - **[[NotGate|NOT]]**: output is the inverse of the single input (`¬A`); the only **unary** basic gate.
  - **[[NandGate|NAND]]**: negation of AND (`¬(A·B)`).
  - **[[NorGate|NOR]]**: negation of OR (`¬(A+B)`).
  - **[[XorGate|XOR]]**: output `1` iff inputs *differ* (`A⊕B`).
  - **[[XnorGate|XNOR]]**: output `1` iff inputs are *equal* (negation of XOR).
- **Derived gates compose from the basic set** — e.g. *"NOR can be built using a NOT combined with an OR gate, (A NOR B) ≡ NOT(A OR B)."* Equivalently every gate is expressible as a NAND-only or NOR-only circuit (functional completeness — the textbook foundation for [[ClaudeShannon|Shannon]]'s 1937 thesis result).
- **M-bit gates parallelize 1-bit gates** — *"an M-bit gate comprises M individual one-bit gates"* operating on corresponding input bits independently. This is exactly the per-bit semantics of [[CLanguage|C]]'s [[BitwiseOperator|bitwise operators]] (`&`, `|`, `^`, `~`) from [[dis-4-6-bitwise|Ch 4.6]] — bitwise operators are M-bit gates at the language level.
- **Gates feed the [[ArithmeticLogicUnit|ALU]]** — the [[FullAdder|full-adder]] of [[dis-4-4-1-addition|Ch 4.4.1]] uses [[XorGate|XOR]] for `Sum` and [[AndGate|AND]] + [[OrGate|OR]] for `CarryOut`, and the *"flip operand B and add 1"* subtraction trick of [[dis-4-4-2-subtraction|Ch 4.4.2]] uses a row of [[XorGate|XORs]] controlled by a mode wire — concrete gate-level instances of Ch 5.3's abstraction.

## Key Quotes

> "Logic gates are the building blocks of the digital circuitry that implements arithmetic, control, and storage functionality in a digital computer." — chapter thesis.

> "A transistor can switch its state between on or off (between a high or low voltage output)." — the physical substrate beneath every gate.

> "NOR can be built using a NOT combined with an OR gate, (A NOR B) ≡ NOT(A OR B)." — composability of derived gates from the AND/OR/NOT basis.

## Connections

- [[DiveIntoSystems]] — parent corpus; this is the third section of Ch 5 *Computer Architecture*, sitting between [[dis-5-2-von-neumann|Ch 5.2]]'s functional-units decomposition and later sections' circuit assembly.
- [[dis-5-2-von-neumann]] — Ch 5.2 introduced the [[ArithmeticLogicUnit|ALU]] as the *"unit that performs arithmetic + boolean operations"*; Ch 5.3 supplies the gate-level primitives the ALU is built from.
- [[ArithmeticLogicUnit]] — composed from the seven gates of this chapter; the [[FullAdder|full-adder]] in [[dis-4-4-1-addition|Ch 4.4.1]] is a concrete construction.
- [[BooleanAlgebra]] — the formal algebra each gate implements one operator of; promoted from stub via this chapter.
- [[ClaudeShannon]] — 1937 master's thesis *"A Symbolic Analysis of Relay and Switching Circuits"* established that switching circuits implement [[BooleanAlgebra|Boolean algebra]] — the theoretical foundation Ch 5.3 stands on; named historically in [[dis-5-1-history|Ch 5.1]].
- [[dis-4-6-bitwise]] — Ch 4.6's [[BitwiseOperator|bitwise operators]] (`&`, `|`, `^`, `~`) are the [[CLanguage|C]]-language exposure of M-bit gates; Ch 5.3 supplies the hardware mechanism.
- [[dis-4-4-1-addition]] — the [[FullAdder|full-adder]] truth table is a direct application of XOR + AND + OR gates.
- [[LogicGate]] — umbrella concept introduced here; seven concrete gate pages.
- [[TruthTable]] — the canonical specification format for each gate (and for any combinational circuit).
- [[Transistor]] — the physical building block beneath every gate.

## Contradictions

None. Ch 5.3 is the gate-level *zoom-in* below [[dis-5-2-von-neumann|Ch 5.2]]'s [[ArithmeticLogicUnit|ALU]] and the hardware substrate beneath [[dis-4-6-bitwise|Ch 4.6]]'s [[BitwiseOperator|bitwise operators]] — strictly compatible with both. [[ClaudeShannon|Shannon]] and [[BooleanAlgebra|Boolean algebra]] are *not* named in the chapter prose itself — that lineage was supplied historically in [[dis-5-1-history|Ch 5.1]] and is added here as wiki-side connection.
