---
title: "Central Processing Unit (CPU)"
type: concept
tags: [systems, hardware, cpu, architecture]
sources: [dis-0-introduction, dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Central Processing Unit (CPU)

The **central processing unit (CPU)** is the [[ComputerHardware|hardware]] component that fetches, decodes, and executes machine instructions. It is the *active* element of a [[ComputerSystem|computer system]] — [[RAM]] and storage hold data, the CPU does work on it.

[[DiveIntoSystems]] Ch 0 names the CPU as one of the four core hardware components (alongside [[RAM]], I/O ports, and secondary storage). In contemporary form the CPU is essentially always a [[MulticoreProcessor|multicore processor]], typically packaged on a [[SystemOnAChip|SoC]] together with [[RAM]] and other peripherals.

## Internal decomposition ([[dis-5-2-von-neumann|Ch 5.2]])

In the [[VonNeumannArchitecture|von Neumann architecture]] the CPU is the combination of **two functional units**:

- **[[ControlUnit|Control unit]]** — drives the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]]; owns the [[ProgramCounter|program counter]] and [[InstructionRegister|instruction register]].
- **[[ProcessingUnit|Processing unit]]** — the data path: the **[[ArithmeticLogicUnit|ALU]]** (arithmetic + [[BooleanAlgebra|boolean]] operations) plus the **[[CpuRegister|register file]]** (each register holds one [[DataWord|word]]).

Ch 5.2 frames this directly: *"the control and processing units combine to form the CPU."*

## Connections

- [[ComputerHardware]] — broader category.
- [[MulticoreProcessor]] — modern default form.
- [[SystemOnAChip]] — typical packaging.
- [[MemoryHierarchy]] — registers / L1 / L2 / L3 sit inside or next to the CPU.
- [[ComputerSystem]] — the CPU is half of the hardware half of a system.
- [[VonNeumannArchitecture]] — the architectural placement.
- [[ControlUnit]] / [[ProcessingUnit]] — the CPU's two halves.
- [[ArithmeticLogicUnit]] / [[CpuRegister]] — what the processing unit contains.
- [[FetchDecodeExecuteCycle]] — the CPU's operational loop.
- [[dis-0-introduction]] / [[dis-5-2-von-neumann]] — sources.
