---
title: "Address of a variable (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, memory-management, pointers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Address_of_a_variable
---

## Summary
This task asks the programmer to demonstrate two operations on a variable's memory address: getting the address of an existing variable, and setting (forcing) a variable to live at a specific address. The key insight is that direct address manipulation is natural in low-level languages with explicit pointers (C, assembly), while higher-level managed languages often abstract memory away entirely, requiring workarounds or declaring the operation impossible/unsafe.

## Task Requirements
- Demonstrate how to obtain the address of a variable.
- Demonstrate how to set (assign) the address of a variable.

## Language Coverage
107 languages implement this task, spanning the full spectrum from raw assembly to managed runtimes. Representative entries include C / C++, Rust, Ada, Fortran, Go, Swift, Python, Java, Pascal, and several Assembly dialects (8086, 68000, ARM, x86), illustrating how pointer semantics vary across system-level and high-level languages.

## Connections
- [[Pointer]] — the core abstraction for referencing a memory address
- [[MemoryManagement]] — addressing relates directly to how a language lays out and manages memory
- [[Pass By Reference]] — taking a variable's address underlies reference semantics
- [[Memory Safety]] — direct address manipulation is the chief source of unsafe behavior managed languages guard against

## Contradictions
- None — reference task page.
