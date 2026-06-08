---
title: "Subleq (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, virtual-machine, esoteric-language]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Subleq
---

## Summary
Subleq is a One-Instruction Set Computer (OISC) whose sole instruction "SUBtract and Branch if Less than or EQual to zero". The task is to write an interpreter that emulates such a machine: memory is an array of signed integers that double as values, addresses, and characters. The key insight is that a single subtract-and-conditional-branch primitive is Turing-complete, so an entire program (including I/O and self-modifying control flow) can be expressed as triples of integers.

## Task Requirements
- Load initial memory (an array of signed integers) starting at address 0 and set the instruction pointer to 0.
- Each step reads three consecutive words A, B, C and advances the pointer by 3.
- If A is -1, read a character from input and store it at address B (C unused).
- If B is -1, write the character at address A to output (C unused).
- Otherwise subtract mem[A] from mem[B], storing the result in B; if the result is <= 0, jump the instruction pointer to C, else continue.
- Halt when the instruction pointer becomes negative.
- Demonstrate output by running the provided "Hello, world!" machine-code program.

## Language Coverage
75 languages implement this task, spanning assembly through high-level and esoteric languages. Representative implementations include C, C++, Python, Rust, Go, Java, Haskell, Forth, Befunge, REXX, and several BASIC dialects.

## Connections
- [[OneInstructionSetComputer]] — the architecture class Subleq exemplifies
- [[TuringCompleteness]] — why a single instruction suffices for general computation
- [[VirtualMachine]] — the interpreter emulates a simple abstract machine
- [[SelfModifyingCode]] — the Hello, world program rewrites its own instruction operands
- [[EsotericProgrammingLanguage]] — Subleq's lineage as a minimalist computing model

## Contradictions
- None — reference task page.
