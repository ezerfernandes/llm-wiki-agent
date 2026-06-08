---
title: "Execute Computer/Zero (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, virtual-machine, emulator, assembly]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Execute_Computer/Zero
---

## Summary
The task is to build an emulator for the Computer/zero, a minimal pedagogical virtual machine with a tiny instruction set. The implementation must execute the machine's bytecode and crucially support self-modifying code, since programs can rewrite their own instructions in memory while running, matching the behavior of the reference implementation. Output is produced when the STP (stop) opcode returns the accumulator value, which is then printed using the host language's standard routines.

## Task Requirements
- Create a Computer/zero Assembly emulator following the referenced reference implementation.
- Run and output the results of the sample programs "2+2" and "7*8".
- The virtual machine bytecode must be able to modify itself (or appear to) while running, for consistency with the reference.
- Implement the STP opcode so it returns the accumulator to the host language for printing.
- Bonus: run all 5 sample programs from the reference website and output their results.

## Language Coverage
25 languages implement this task, spanning systems languages, scripting languages, and even native assembly targets. Representative implementations include C, Go, Java, Python, Perl, Raku, Forth, Lua, Nim, and Z80 Assembly.

## Connections
- [[VirtualMachine]] — emulates a register/memory machine and its instruction cycle
- [[Emulator]] — software reproduction of another machine's behavior
- [[SelfModifyingCode]] — programs rewrite their own instructions in memory at runtime
- [[InstructionSet]] — the minimal opcode set (including STP) the VM decodes and executes
- [[Bytecode]] — the encoded program representation the emulator interprets

## Contradictions
- None — reference task page.
