---
title: "Digital Circuit"
type: concept
tags: [hardware, computer-architecture, circuits, digital-logic]
sources: [dis-5-4-circuits, dis-5-3-gates, dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Digital Circuit

A **digital circuit** is a composition of [[LogicGate|logic gates]] and wires that implements a Boolean function (combinational) or a stateful component (sequential). *"Digital circuits implement the core functionality of the [[VonNeumannArchitecture|architecture]]"* ([[dis-5-4-circuits|Ch 5.4]]) — they are the layer between [[dis-5-3-gates|Ch 5.3]]'s individual [[LogicGate|gates]] and [[dis-5-2-von-neumann|Ch 5.2]]'s five functional units.

## Design discipline (from [[dis-5-4-circuits|Ch 5.4]])

- **Hierarchical composition** — *"more complex circuits are constructed by combining simpler subcircuits and basic logic gates."*
- **Black-box [[Abstraction|abstraction]]** — once built, a subcircuit is treated as an opaque unit specified by its **inputs / outputs** alone. The same discipline applies recursively up to the [[ArithmeticLogicUnit|ALU]] and beyond.

## Three categories ([[dis-5-4-circuits|Ch 5.4]] partition)

| Category | Role | Subsection | Canonical example |
|---|---|---|---|
| [[ArithmeticLogicCircuit|Arithmetic & logic]] | Operates on data | Ch 5.4.1 | [[FullAdder]] inside the [[ArithmeticLogicUnit|ALU]] |
| [[ControlCircuit|Control]] | Sequences operations / routes data | Ch 5.4.2 | Decoder driving the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]] |
| [[StorageCircuit|Storage]] | Holds data | Ch 5.4.3 | [[CpuRegister|Register]] / [[RAM|memory]] cell |

Maps onto [[dis-5-2-von-neumann|Ch 5.2]]'s [[ProcessingUnit|processing unit]] = arithmetic-logic + storage; [[ControlUnit|control unit]] = control.

## Connections

- [[LogicGate]] — the primitive building block.
- [[Transistor]] — the physical substrate below the gate.
- [[ArithmeticLogicUnit]] — the headline [[ArithmeticLogicCircuit|arithmetic-and-logic circuit]] of the [[CPU]].
- [[FullAdder]] — already-known gate-level circuit from [[dis-4-4-1-addition|Ch 4.4.1]] — receives its category label here.
- [[VonNeumannArchitecture]] — circuits implement the five functional units.
- [[BooleanAlgebra]] — combinational circuits realize Boolean functions; [[ClaudeShannon|Shannon]]'s 1937 thesis made the correspondence explicit.

## Sources

- [[dis-5-4-circuits]] — Ch 5.4 hub (this page's primary source).
- [[dis-5-3-gates]] — gate primitives below.
- [[dis-5-2-von-neumann]] — architectural units above.
