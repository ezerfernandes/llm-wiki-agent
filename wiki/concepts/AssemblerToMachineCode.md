---
title: "Assembler-to-Machine-Code Translation"
type: concept
tags: [computer-architecture, toolchain, assembler, isa]
sources: [dis-5-6-instruction-execution]
last_updated: 2026-05-17
---

# Assembler-to-Machine-Code Translation

**Assembler-to-machine-code translation** is the step in the toolchain that converts human-readable [[AssemblyLanguage|assembly]] mnemonics (e.g. `add r1, r2, r3`) into the [[MachineCode|machine-code]] bit pattern the [[CPU]] actually executes. The program that performs the translation is the **assembler**; the rules it follows are dictated by the target [[InstructionSet|ISA]]'s instruction-format specification — which [[OpCode|opcode]] bits name `add`, how source/destination register selectors are laid out, where immediates and addressing-mode fields live.

In [[dis-5-6-instruction-execution|Ch 5.6]] this translation is the bridge between the abstract instruction the programmer wrote and the binary [[InstructionRegister|IR]] contents the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]] decodes. Each assembly line maps (typically one-to-one) to one machine-code instruction; pseudo-ops and macros may expand to several.

The inverse direction — machine code back to assembly — is **disassembly**, performed by tools such as `objdump` or [[GDB]]'s `disassemble` command.

## Connections

- [[AssemblyLanguage]] — the input side of the translation.
- [[MachineCode]] — the output side.
- [[InstructionSet]] — defines the translation rules.
- [[OpCode]] — the central field assembled into the machine-code instruction.
- [[FetchDecodeExecuteCycle]] — what the output machine code eventually drives.
- [[DiveIntoSystems]] / [[dis-5-6-instruction-execution]] — introducing source.
