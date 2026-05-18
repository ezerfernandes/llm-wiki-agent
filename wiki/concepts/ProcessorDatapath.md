---
title: "Processor Data Path"
type: concept
tags: [systems, computer-architecture, cpu, datapath]
sources: [dis-5-5-cpu]
last_updated: 2026-05-17
---

# Processor Data Path

The **data path** is [[dis-5-5-cpu|Ch 5.5]]'s integration concept — the assembly of the [[CPU]]'s compute + storage + interconnect subcircuits into one wired unit. Verbatim from §5.5.3:

> "The data path consists of the parts of the CPU that perform arithmetic and logic operations (the ALU) and store data (registers), and the buses that connect these parts."

## What sits inside the data path

- **[[ArithmeticLogicUnit|ALU]]** — performs arithmetic + logic operations on operands; opcode-selected via an internal [[Multiplexer|MUX]] (the gate-level construction is in [[dis-5-4-1-arithmetic-logic-circuits|Ch 5.4.1]]); emits a result + condition-code bits.
- **[[RegisterFile|Register file]]** — the 8–32 [[CpuRegister|general-purpose registers]] with two read ports + one write port ([[dis-5-4-3-storage-circuits|Ch 5.4.3]] built the storage cells, [[dis-5-4-2-control-circuits|Ch 5.4.2]] supplied the [[Decoder]] / [[Multiplexer|MUX]] / [[Demultiplexer|DMUX]] used for port selection).
- **[[Bus|Buses]]** — the wires routing operand values from the register file to the ALU inputs and the ALU result back to the destination register, plus the operand-selection control lines (`Sr0`, `Sr1`, `Sw`, `WE`).
- **[[ProgramCounter|PC]]** and **[[InstructionRegister|IR]]** — special-purpose registers sit alongside the data path, owned by the [[ControlUnit|control unit]] (the architectural split from [[dis-5-2-von-neumann|Ch 5.2]]).

## Data path vs control path

Ch 5.5 names a sibling **control path** that drives instruction execution by emitting the select-bit signals into the data path's MUXes / DMUXes / decoders. The data path *moves data and computes*; the control path *decides what to move and which operation to compute*. The full control-path construction is forward-referenced to the next section ([[FetchDecodeExecuteCycle|fetch-decode-execute]] mechanics).

## Connections

- [[CPU]] — the data path is its compute-and-store half.
- [[ProcessingUnit]] — the [[dis-5-2-von-neumann|Ch 5.2]] architectural unit the data path realizes.
- [[ArithmeticLogicUnit]] / [[RegisterFile]] / [[Bus]] — the three named ingredients.
- [[ControlUnit]] / [[ControlCircuit]] — the sibling control path.
- [[ClockSignal]] / [[ClockCycle]] — the timing reference pacing data movement through the path (mechanism deferred).
- [[dis-5-5-cpu]] — source.
- [[VonNeumannArchitecture]] / [[dis-5-2-von-neumann]] — the architectural parent.
- [[dis-5-4-circuits]] / [[dis-5-4-1-arithmetic-logic-circuits]] / [[dis-5-4-2-control-circuits]] / [[dis-5-4-3-storage-circuits]] — the circuit-category subsections whose building blocks the data path wires together.
