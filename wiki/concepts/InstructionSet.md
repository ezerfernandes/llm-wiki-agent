---
title: "Instruction Set"
type: concept
tags: [computer-architecture, cpu, isa, machine-code]
sources: [dis-5-6-instruction-execution]
last_updated: 2026-05-17
---

# Instruction Set

The **instruction set** (or **instruction set architecture**, **ISA**) is the catalog of operations a particular [[CPU]] can execute. Each instruction has an [[OpCode|opcode]] (the bit-pattern that names the operation) and a defined layout of operand fields (source-register selectors, destination-register selector, immediate values, addressing-mode bits). The ISA is the **hardware/software contract**: compilers, assemblers and OS toolchains emit code targeting *this* set of operations and *this* encoding; the CPU's [[ControlCircuit|control circuits]] are wired to decode and execute exactly these patterns.

[[dis-5-6-instruction-execution|Ch 5.6]] introduces the term while walking through the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]]: during Decode the [[InstructionRegister|IR]] bits are partitioned into opcode + operand fields per the ISA's instruction format, then routed to the [[ArithmeticLogicUnit|ALU]] and [[RegisterFile|register file]] accordingly. An $N$-operation ISA needs $\lceil \log_2 N \rceil$ opcode bits (the same MUX-selector arithmetic from [[dis-5-4-2-control-circuits|Ch 5.4.2]]).

The ISA also determines instruction width — e.g. a 32-bit ISA stores each instruction in 4 bytes, so the [[ProgramCounter|PC]] increments by 4 during Fetch.

## Connections

- [[OpCode]] / [[MachineCode]] / [[AssemblerToMachineCode]] — the binary-encoding layer of an ISA.
- [[AssemblyLanguage]] — the human-readable form of an ISA.
- [[CPU]] / [[ControlCircuit]] — the hardware side of the contract.
- [[ProgramCounter]] — increments by the ISA-defined instruction width per Fetch.
- [[FetchDecodeExecuteCycle]] — the cycle that consumes ISA-encoded instructions.
- [[DiveIntoSystems]] / [[dis-5-6-instruction-execution]] — introducing source.
