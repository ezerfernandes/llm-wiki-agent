---
title: "Program Counter (PC)"
type: concept
tags: [computer-architecture, cpu, von-neumann, register]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Program Counter (PC)

The **program counter (PC)** is the special [[CpuRegister|register]] inside the [[ControlUnit|control unit]] that holds the **[[RAM|memory]] address of the *next* instruction to execute**. It is the single piece of state that makes the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]] **sequential** — without it the [[CPU]] would not know where to read the next instruction word from. ([[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]])

## Role in the cycle

At each fetch phase, the [[ControlUnit|control unit]]:

1. Reads `[PC]` (the instruction word at the PC's address) from [[RAM|memory]] into the [[InstructionRegister|IR]].
2. **Increments** the PC to point at the following instruction.
3. *(Branch / jump instructions later overwrite the PC with the branch target.)*

## Architectural names

The PC is the architecture-neutral name. On concrete ISAs:

- **x86 / x86-64** — `%eip` / `%rip` (the [[InstructionPointer|instruction pointer]]; see [[CpuRegister]] for the [[GDB]] surface).
- **ARM / AArch64** — `r15` / `pc`.
- **RISC-V** — `pc` (architectural, not in the general register file).
- **6502 / 8080** historically — `PC`.

## Connections

- [[ControlUnit]] — the PC's owner.
- [[InstructionRegister]] — sibling control register; holds the instruction whose address came from the PC.
- [[CpuRegister]] — broader category.
- [[FetchDecodeExecuteCycle]] — the loop the PC sequences.
- [[InstructionPointer]] — the x86 surface form already in the wiki.
- [[RAM]] — what the PC addresses into.
- [[VonNeumannArchitecture]] — the architectural context.
- [[dis-5-2-von-neumann]] — source.
