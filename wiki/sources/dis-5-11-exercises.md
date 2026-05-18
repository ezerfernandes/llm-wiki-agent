---
title: "Dive into Systems — Ch 5.11 Exercises"
type: source
tags: [dive-into-systems, computer-architecture, exercises]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C5-Arch/exercises.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 5.11** of *[[DiveIntoSystems]]* — the **exercise-set close of Ch 5 *Computer Architecture*** that **fully completes Ch 5**. Drills the [[dis-5-3-gates|Ch 5.3]] / [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]] / [[dis-5-4-2-control-circuits|Ch 5.4.2]] / [[dis-5-4-3-storage-circuits|Ch 5.4.3]] circuit-construction surface area: (1) **build a 1-bit [[XorGate|XOR]] from [[AndGate|AND]] / [[OrGate|OR]] / [[NotGate|NOT]]** — derives the gate network from a [[TruthTable|truth table]], exercising the *truth-table → Boolean expression → gate network* methodology of [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]]; (2) **full 1-bit [[FullAdder|adder]] truth table** — three inputs (A / B / [[CarryIn|carry-in]]), two outputs ([[Sum|sum]] / [[CarryOut|carry-out]]); (3) **4-bit [[TwosComplement|two's-complement]] negation circuit** — combines [[LogicGate|logic gates]] with [[FullAdder|adder]] functionality to implement *flip-and-add-one*; (4) **[[Multiplexer|multiplexer]] analysis** — trace a 4-way MUX's selection-input → output mapping; (5) **MUX scaling** — determine select-bit width for a 16-way MUX ($\log_2 16 = 4$ bits); (6) **[[SRLatch|RS latch]] state tracing** — sequential-storage state changes under input transitions; (7) **gated [[DLatch|D latch]] behavior** — [[WriteEnable|`WE`]] control signal analysis. **Structural sibling of [[dis-1-8-exercises|Ch 1.8]] / [[dis-2-11-exercises|Ch 2.11]] / [[dis-4-10-exercises|Ch 4.10]]** — drills foundational concepts via [[TruthTable|truth-table]] derivation, combinational-logic synthesis, sequential-storage elements, and control-signal timing — *all essential for understanding processor construction discussed earlier in the chapter*. No new conceptual material.

## Key Claims

- **Exercise set drills [[dis-5-3-gates|Ch 5.3]]–[[dis-5-4-3-storage-circuits|Ch 5.4.3]]** — gate-level XOR construction, [[FullAdder|full-adder]] truth tables, [[TwosComplement|two's-complement]] negation circuits, [[Multiplexer|MUX]] selection-bit analysis, [[SRLatch|RS]] / [[DLatch|D latch]] state tracing.
- **Truth-table → Boolean → gate methodology** ([[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]]) is the load-bearing technique exercised throughout.
- **MUX select-bit rule** $\log_2 N$ exercised on the 16-way case (4 select bits).
- **Sequential storage** exercises ([[SRLatch|RS]] / [[DLatch|D latch]]) reinforce the feedback-loop signature of [[StorageCircuit|storage circuits]] vs the combinational [[ArithmeticLogicCircuit|arithmetic-logic]] / [[ControlCircuit|control]] siblings.

## Connections

- [[DiveIntoSystems]] — the source textbook; Ch 5.11 closes Ch 5 *Computer Architecture* — the chapter is now **fully complete** (5.1 through 5.11).
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-5-3-gates]] — [[LogicGate|logic gates]] exercised by problem 1 (XOR from AND/OR/NOT).
- [[dis-5-4-1-arithmetic-logic-circuits]] — [[FullAdder|full-adder]] truth table (problem 2) and [[TwosComplement|two's-complement]] negation circuit (problem 3).
- [[dis-5-4-2-control-circuits]] — [[Multiplexer|MUX]] analysis (problems 4–5).
- [[dis-5-4-3-storage-circuits]] — [[SRLatch|RS latch]] and [[DLatch|D latch]] tracing (problems 6–7).
- [[dis-5-10-summary]] — immediate predecessor; the prose-body recap this exercise set drills.
- [[dis-1-8-exercises]] / [[dis-2-11-exercises]] / [[dis-4-10-exercises]] — structural siblings (exercise-set-closes-chapter pattern across the corpus).
- [[TruthTable]] / [[FullAdder]] / [[Multiplexer]] / [[SRLatch]] / [[DLatch]] / [[TwosComplement]] — the load-bearing concepts exercised.

## Contradictions

None — exercise set only, no new claims.
