---
title: "Opcode"
type: concept
tags: [computer-architecture, cpu, isa, alu]
sources: [dis-5-5-cpu, dis-5-6-instruction-execution]
last_updated: 2026-05-17
---

# Opcode

The **opcode** is the field of a [[MachineCode|machine-code]] instruction that **names the operation** to perform — e.g. ADD, SUB, OR, AND, load, store, branch. It occupies the high-order bits of an instruction's bit pattern (in typical [[InstructionSet|ISA]] encodings); the remaining bits are operand fields.

In the [[dis-5-5-cpu|Ch 5.5]] [[ProcessorDatapath|data path]] the opcode is one of the three [[ArithmeticLogicUnit|ALU]] inputs (alongside operands A and B); it drives the ALU's internal [[Multiplexer|MUX]] that selects which sub-circuit's output becomes the ALU result. An $N$-operation ALU needs $\lceil \log_2 N \rceil$ opcode bits.

In the [[dis-5-6-instruction-execution|Ch 5.6]] [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]] the opcode is extracted from the [[InstructionRegister|IR]] during **Decode** and routed to the ALU; the operand-field bits in the same instruction route to the [[RegisterFile|register file]]'s read- and write-select inputs.

## Connections

- [[InstructionSet]] — the catalog of legal opcodes.
- [[MachineCode]] — the binary instruction in which the opcode lives.
- [[ArithmeticLogicUnit]] — consumer of the opcode at Execute.
- [[InstructionRegister]] — holds the in-flight opcode + operand bits.
- [[FetchDecodeExecuteCycle]] — the cycle in which the opcode is extracted and used.
- [[Multiplexer]] — the gate-level mechanism the opcode drives inside the ALU.
- [[DiveIntoSystems]] / [[dis-5-5-cpu]] / [[dis-5-6-instruction-execution]] — sources.
