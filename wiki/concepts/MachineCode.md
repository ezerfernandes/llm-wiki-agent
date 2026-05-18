---
title: "Machine Code"
type: concept
tags: [computer-architecture, cpu, isa, binary]
sources: [dis-5-6-instruction-execution]
last_updated: 2026-05-17
---

# Machine Code

**Machine code** is the binary bit-pattern encoding of an [[InstructionSet|ISA]]'s instructions — the **only language the CPU directly executes**. Each instruction is a fixed-width (in [[InstructionSet|RISC]]-style ISAs) or variable-width (in CISC-style ISAs) sequence of bits laid out per the ISA's instruction format: an [[OpCode|opcode]] field naming the operation plus operand fields naming source/destination registers, immediates, or memory addresses.

In [[dis-5-6-instruction-execution|Ch 5.6]] the machine-code instruction lives in the [[InstructionRegister|IR]] during execution — fetched from memory at the address the [[ProgramCounter|PC]] holds, decoded into opcode + operand fields, then executed by the [[ArithmeticLogicUnit|ALU]] and written back to the [[RegisterFile|register file]].

Machine code is the **output of the [[AssemblerToMachineCode|assembler]]** (or the back end of a compiler): humans write [[AssemblyLanguage|assembly]] or a higher-level language; the toolchain translates that to the bit patterns the hardware can decode.

## Connections

- [[InstructionSet]] — defines the legal machine-code patterns.
- [[OpCode]] — the operation-naming field within a machine-code instruction.
- [[AssemblerToMachineCode]] — the translation step producing machine code.
- [[AssemblyLanguage]] — the human-readable counterpart.
- [[InstructionRegister]] — holds the in-flight machine-code instruction.
- [[FetchDecodeExecuteCycle]] — the cycle that consumes machine code.
- [[DiveIntoSystems]] / [[dis-5-6-instruction-execution]] — introducing source.
