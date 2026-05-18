---
title: "Control Unit"
type: concept
tags: [computer-architecture, cpu, von-neumann]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Control Unit

The **control unit** is the part of the [[CPU]] that **drives instruction execution** — fetching the next instruction from [[RAM|memory]], decoding its opcode and operand specifiers, dispatching the operation to the [[ArithmeticLogicUnit|ALU]] or the memory subsystem, and writing the result back. Together with the [[ProcessingUnit|processing unit]] it forms the [[CPU]] in the [[VonNeumannArchitecture|von Neumann architecture]] ([[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]]).

## Special registers

The control unit owns two architectural registers that are not user-visible operands:

- **[[ProgramCounter|Program counter (PC)]]** — holds the [[RAM|memory]] address of the **next** instruction to execute.
- **[[InstructionRegister|Instruction register (IR)]]** — holds the **currently-decoding** instruction word, loaded from [[RAM|memory]] at the PC's address.

## Role in the fetch-decode-execute cycle

Per Ch 5.2's [[FetchDecodeExecuteCycle|fetch-decode-execute-store cycle]] the control unit:

1. **Fetch** — reads the instruction at `[PC]` from [[RAM|memory]] into [[InstructionRegister|IR]] and increments PC.
2. **Decode** — parses the [[InstructionRegister|IR]]'s bits to identify the opcode and operand locations; fetches operand values from [[CpuRegister|registers]] or [[RAM|memory]].
3. **Execute** — dispatches the operation to the [[ArithmeticLogicUnit|ALU]].
4. **Store** — writes the result back via the [[DataBus|data]] / [[AddressBus|address]] / [[ControlBus|control]] buses.

## Connections

- [[CPU]] — the control unit is one of its two halves (the other being the [[ProcessingUnit|processing unit]]).
- [[ProcessingUnit]] — the data-path side of the [[CPU]]; control unit *drives* it.
- [[FetchDecodeExecuteCycle]] — the loop the control unit runs.
- [[ProgramCounter]] / [[InstructionRegister]] — the control unit's two special registers.
- [[Bus]] — the channels the control unit uses to issue commands and addresses.
- [[VonNeumannArchitecture]] — the architecture that names it.
- [[dis-5-2-von-neumann]] — source.
