---
title: "Control Circuit"
type: concept
tags: [hardware, computer-architecture, circuits, control, digital-logic]
sources: [dis-5-4-2-control-circuits, dis-5-4-circuits, dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Control Circuit

A **control circuit** is the **second** of the three [[Circuit|digital-circuit]] categories in [[dis-5-4-circuits|Ch 5.4]]'s partition — *"control circuits are used throughout a system. On the processor, they drive the execution of program instructions on program data. They also control loading and storing values to different levels of storage (between registers, cache, and RAM)"* ([[dis-5-4-2-control-circuits|Ch 5.4.2]]). Sibling categories: [[ArithmeticLogicCircuit|arithmetic-and-logic]] (operates on data) and [[StorageCircuit|storage]] (holds data).

## Role

Where [[ArithmeticLogicCircuit|arithmetic-and-logic circuits]] *compute* and [[StorageCircuit|storage circuits]] *remember*, **control circuits *route***:

- **Inside the [[CPU]]** — the [[ControlUnit|control unit]]'s decode phase emits select-bit signals that drive [[Multiplexer|MUXes]] in front of the [[CpuRegister|register file]] (operand read-port selection — *"the CPU may use a multiplexer circuit to select from which CPU register to read an instruction operand value"*) and [[Demultiplexer|DMUXes]] behind the [[ArithmeticLogicUnit|ALU]] (result write-port routing).
- **Across the [[MemoryHierarchy|memory hierarchy]]** — control circuits dispatch data movement *"between registers, cache, and [[RAM|RAM]]"* (Ch 5.4.2).
- **At I/O boundaries** — same selection / routing pattern between the [[CPU]] and [[IODevice|I/O devices]].

## Canonical examples ([[dis-5-4-2-control-circuits|Ch 5.4.2]])

| Circuit | Direction | Inputs → Output |
|---|---|---|
| [[Multiplexer\|Multiplexer (MUX)]] | $N \to 1$ | $N$ data inputs + $\log_2 N$ select bits → 1 output (the selected one) |
| [[Demultiplexer\|Demultiplexer (DMUX)]] | $1 \to N$ | 1 data input + $\log_2 N$ select bits → $N$ outputs (the selected one carries the input; others 0) |
| [[Decoder\|Decoder]] | $\log_2 N \to N$ | $\log_2 N$ encoded bits → one-hot $N$-bit output (exactly one output high) |

The decoder is also the **internal selection mechanism** every $N$-way MUX uses to translate its $\log_2 N$ select bits into the $N$ per-input AND-gate enables.

## Construction

Same hierarchical-composition + black-box [[Abstraction|abstraction]] discipline as [[ArithmeticLogicCircuit|arithmetic-and-logic]]: build a truth table over inputs + select bits, derive a Boolean expression, instantiate as a [[LogicGate|gate]] network of [[AndGate|AND]] / [[OrGate|OR]] / [[NotGate|NOT]]. Two-way 1-bit MUX: `Out = (NOT(S) AND B) OR (S AND A)`. Wider MUXes scale by stacking 1-bit MUXes in parallel on a shared select line.

## Connections

- [[Circuit]] — umbrella; this is one of three categories.
- [[ControlUnit]] — the [[CPU]]-level functional unit these circuits implement.
- [[FetchDecodeExecuteCycle]] — the operational pattern the control circuits dispatch over: decode-phase select-bit emission, execute-phase routing, store-phase write-port routing.
- [[Multiplexer]] / [[Demultiplexer]] / [[Decoder]] — the three named control circuits.
- [[ArithmeticLogicCircuit]] / [[StorageCircuit]] — sibling categories from the [[dis-5-4-circuits|Ch 5.4]] partition.
- [[Abstraction]] — design discipline (each circuit becomes a primitive at the next level up).

## Sources

- [[dis-5-4-2-control-circuits]] — Ch 5.4.2; promotes this page from forward-reference to category page.
- [[dis-5-4-circuits]] — Ch 5.4 hub installs the three-category partition.
- [[dis-5-2-von-neumann]] — Ch 5.2 introduces the [[ControlUnit|control unit]] this category implements.
