---
title: "Fetch-Decode-Execute Cycle"
type: concept
tags: [computer-architecture, cpu, von-neumann]
sources: [dis-5-2-von-neumann, dis-5-1-history]
last_updated: 2026-05-17
---

# Fetch-Decode-Execute Cycle

The **fetch-decode-execute(-store) cycle** is the repeating four-phase loop that constitutes program execution on a [[VonNeumannArchitecture|von Neumann]] [[CPU]] — driven by the [[ControlUnit|control unit]], sequencing operands through the [[ArithmeticLogicUnit|ALU]], and writing results back via the [[Bus|system buses]]. [[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]] presents it as the architecture's *operational heart*.

## The four phases

1. **Fetch** — the [[ControlUnit|control unit]] reads the instruction stored at the address in the [[ProgramCounter|program counter (PC)]] from [[RAM|memory]] into the [[InstructionRegister|instruction register (IR)]], then **increments the PC** so the next iteration finds the following instruction.
2. **Decode** — the [[ControlUnit|control unit]] parses the [[InstructionRegister|IR]]'s bit pattern to identify the **opcode** (what to do) and the **operand locations** (which [[CpuRegister|registers]] or [[RAM|memory]] addresses hold the inputs). Operand values are fetched.
3. **Execute** — the [[ArithmeticLogicUnit|ALU]] performs the operation (addition, comparison, boolean op, etc.) on the operand values.
4. **Store** — the [[ControlUnit|control unit]] writes the result back to a [[CpuRegister|register]] or [[RAM|memory]] location, using the [[DataBus|data bus]] (the value), [[AddressBus|address bus]] (the destination), and [[ControlBus|control bus]] (the write command).

The loop then repeats from step 1 — with the [[ProgramCounter|PC]] now pointing at the next instruction (or at a branch target, if the just-executed instruction was a jump).

## Why the cycle defines the architecture

Because *every* instruction goes through the same four phases, the cycle is what makes the [[VonNeumannArchitecture|architecture]] **general-purpose**: the same hardware can run any [[StoredProgram|stored program]] — the only difference between two programs is the bit patterns sitting at the addresses the [[ProgramCounter|PC]] visits.

## Connections

- [[VonNeumannArchitecture]] — the architecture this cycle defines.
- [[ControlUnit]] — drives phases 1, 2, and 4.
- [[ArithmeticLogicUnit]] — drives phase 3.
- [[ProgramCounter]] / [[InstructionRegister]] — the control-unit registers the cycle revolves around.
- [[CpuRegister]] — typical operand / result location.
- [[RAM]] — backing store for instructions and data.
- [[Bus]] / [[ControlBus]] / [[AddressBus]] / [[DataBus]] — the wires every phase uses.
- [[StoredProgram]] — the principle this cycle operationalizes.
- [[dis-5-2-von-neumann]] — primary source.
