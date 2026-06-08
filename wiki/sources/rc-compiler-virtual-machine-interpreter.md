---
title: "Compiler/virtual machine interpreter (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, compilers, virtual-machine, bytecode]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Compiler/virtual_machine_interpreter
---

## Summary
This task asks the programmer to implement a virtual machine interpreter that executes the byte-coded assembly produced by the companion Code Generator task. The VM is a 32-bit, word-based, stack machine: it reads a textual program describing a data segment size, a constant string pool, and a sequence of address-labeled instructions, then runs them. The core insight is that a compact instruction set plus a stack discipline is enough to evaluate arbitrary expressions and control flow without registers beyond a stack pointer and program counter.

## Task Requirements
- Read the generator's output (from a file and/or stdin); the first line gives the data segment size and the number of constant strings, followed by the quoted strings, then the instruction listing.
- Maintain two registers: `sp` (stack pointer into a 32-bit integer stack) and `pc` (program counter into the code).
- Store variable data either in a separate array or at the base of the stack, addressed from index 0.
- Implement instructions with a 32-bit operand: `fetch [index]`, `store [index]`, `push n`, `jmp (n) addr`, `jz (n) addr`.
- Implement binary stack operations: `add`, `sub`, `mul`, `div`, `mod`, `lt`, `gt`, `le`, `ge`, `eq`, `ne`, `and`, `or`.
- Implement unary stack operations `neg` and `not`, and output operations `prtc` (char), `prti` (integer), `prts` (string from pool), plus `halt` to stop.
- Pass the provided sample programs.

## Language Coverage
35 languages implement this task, a broad mix spanning systems, functional, and scripting languages. Representative entries include C, C++, Ada, Go, Java, Python, Common Lisp, Racket, Scheme, Forth, Perl, and Raku; the C and Python versions are designated reference implementations.

## Connections
- [[StackMachine]] — the VM is a 32-bit word stack-based architecture.
- [[Bytecode]] — instructions are encoded as single-byte opcodes with optional 32-bit operands.
- [[Interpreter]] — a fetch-decode-execute loop drives instruction dispatch.
- [[CompilerPipeline]] — final stage consuming the [[CodeGenerator]] output of the lexer/parser/codegen chain.

## Contradictions
- None — reference task page.
