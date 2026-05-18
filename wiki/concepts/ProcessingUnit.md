---
title: "Processing Unit"
type: concept
tags: [computer-architecture, cpu, von-neumann]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Processing Unit

The **processing unit** is the **data-path half** of a [[VonNeumannArchitecture|von Neumann]] [[CPU]] — together with the [[ControlUnit|control unit]] (the *sequencing* half) it forms the [[CPU]] itself ([[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]]).

It comprises **two pieces**:

- **[[ArithmeticLogicUnit|Arithmetic / Logic Unit (ALU)]]** — the circuit that performs arithmetic and [[BooleanAlgebra|boolean]] operations on operand values.
- **[[CpuRegister|Register file]]** — a small bank of fast storage; each [[CpuRegister|register]] holds one [[DataWord|data word]]. Critically, *"there is no distinction between instructions and data in the von Neumann architecture"* — registers can carry either.

## Role in the architecture

Where the [[ControlUnit|control unit]] *decides* what to do and when (driving the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]] and managing the [[ProgramCounter|PC]] and [[InstructionRegister|IR]]), the processing unit is **how** computation happens — the [[ArithmeticLogicUnit|ALU]] consuming operand values from the [[CpuRegister|registers]] (or from [[RAM|memory]] via the [[Bus|buses]]) and producing the results the [[ControlUnit|control unit]] then writes back.

## Connections

- [[CPU]] — the processing unit is one of its two halves.
- [[ControlUnit]] — the *other* half.
- [[ArithmeticLogicUnit]] — one of the processing unit's two pieces.
- [[CpuRegister]] — the other piece.
- [[FetchDecodeExecuteCycle]] — the processing unit is the *execute* phase's active element.
- [[VonNeumannArchitecture]] — the architecture that places it here.
- [[dis-5-2-von-neumann]] — source.
