---
title: "Truth Table"
type: concept
tags: [computer-architecture, logic, digital-circuits, boolean, specification]
sources: [dis-5-3-gates, dis-4-4-1-addition]
last_updated: 2026-05-17
---

# Truth Table

A **truth table** enumerates **every possible combination of input values** for a Boolean function and records the resulting output(s). For $N$ binary inputs the table has $2^N$ rows — exhaustive and finite, making truth tables the canonical specification format for combinational digital circuits.

## Examples in this corpus

- **Single gates** ([[dis-5-3-gates|DIS Ch 5.3]]): the 4-row tables for [[AndGate|AND]] / [[OrGate|OR]] / [[NandGate|NAND]] / [[NorGate|NOR]] / [[XorGate|XOR]] / [[XnorGate|XNOR]], the 2-row table for [[NotGate|NOT]].
- **Multi-input circuits** ([[dis-4-4-1-addition|DIS Ch 4.4.1]]): the **8-row [[FullAdder|full-adder]] truth table** (`DigitA` × `DigitB` × `CarryIn` → `Sum` + `CarryOut`) — `Sum = XOR`, `CarryOut = majority`.

## Uses

- **Specification** — gives a precise, implementation-agnostic definition of any combinational function.
- **Verification** — testing $2^N$ rows is feasible for small $N$ (exhaustive testing).
- **Synthesis** — algorithms like Karnaugh maps and Quine-McCluskey turn truth tables into minimized gate networks (synthesis level beyond [[dis-5-3-gates|DIS Ch 5.3]]'s scope).

## Connections

- [[LogicGate]] — every gate is specified by a truth table.
- [[BooleanAlgebra]] — truth tables are the **semantic** view; Boolean algebra is the **syntactic** view; the two are equivalent.
- [[FullAdder]] — first non-trivial truth table in the corpus.
- [[dis-5-3-gates]] / [[dis-4-4-1-addition]] — sources.
- [[PropositionalLogic]] — truth tables give the semantics of the four logical connectives ([[logic-text-v2|Van Cleave]] Ch 2); the **truth-table test of validity** (no row with all premises true and conclusion false) is propositional logic's decision procedure for [[Validity|validity]].
- [[RulesOfInference]] — proofs are the shorter, validity-only alternative to the $2^N$-row truth table.
