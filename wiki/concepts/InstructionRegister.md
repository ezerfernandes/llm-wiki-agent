---
title: "Instruction Register (IR)"
type: concept
tags: [computer-architecture, cpu, von-neumann, register]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Instruction Register (IR)

The **instruction register (IR)** is the special [[CpuRegister|register]] inside the [[ControlUnit|control unit]] that holds the **currently-decoding instruction word** — the bit pattern just fetched from [[RAM|memory]] at the address that was in the [[ProgramCounter|program counter]]. The [[ControlUnit|control unit]] parses the IR's bits to determine the opcode and operand locations before dispatching to the [[ArithmeticLogicUnit|ALU]]. ([[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]])

## Role in the cycle

Within the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]]:

- **Fetch** — `IR ← memory[PC]`; `PC ← PC + instruction_size`.
- **Decode** — the [[ControlUnit|control unit]] examines the bits in `IR` to extract opcode, operand-register IDs, immediate values, addressing-mode flags.
- The IR is **not user-visible** in most ISAs — it's an internal pipeline buffer.

## Connections

- [[ControlUnit]] — the IR's owner.
- [[ProgramCounter]] — sibling control register; the PC's address is *where* the IR's contents came from.
- [[CpuRegister]] — broader category.
- [[FetchDecodeExecuteCycle]] — the loop the IR participates in.
- [[VonNeumannArchitecture]] — the architectural context.
- [[dis-5-2-von-neumann]] — source.
