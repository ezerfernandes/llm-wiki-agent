---
title: "Four bit adder (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, digital-logic, bitwise-operations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Four_bit_adder
---

## Summary
The task asks the programmer to "simulate" a four-bit binary adder built bottom-up from primitive logic gates. The key constraint is compositional: only NOT, OR, and AND gates (imitated via bitwise operators) are allowed, and from these you build an XOR, then a half adder, then a full adder, then chain four full adders carrying the carry-out into the next stage. The point is structural clarity over optimization — each higher-order block should visibly connect its smaller constituent blocks.

## Task Requirements
- Build a four-bit adder from four 1-bit full adders.
- Each full adder is made from two half adders plus an OR gate.
- Each half adder is made from an XOR gate and an AND gate.
- The XOR gate must be constructed from two NOTs, two ANDs, and one OR.
- Only NOT, OR, and AND are allowed as primitive gates (imitated with bitwise operators); use a NAND with constant 1 to mask unwanted bits if the language lacks a bit type.
- Do not optimize/reduce gate count — build it in the most straightforward, descriptive way, chaining the carry between stages.
- Demonstrate by showing the sum of two four-bit numbers in binary.

## Language Coverage
80 languages implement this task, spanning general-purpose languages, functional languages, and even hardware description languages. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Lua, Perl, and the HDLs Verilog, VHDL, and SystemVerilog.

## Connections
- [[LogicGates]] — the AND/OR/NOT primitives the adder is built from
- [[BitwiseOperations]] — how the gates are imitated in software
- [[BinaryArithmetic]] — the underlying addition with carry propagation
- [[HalfAdder]] — the XOR+AND building block
- [[FullAdder]] — the half-adder-plus-OR block chained four times

## Contradictions
- None — reference task page.
