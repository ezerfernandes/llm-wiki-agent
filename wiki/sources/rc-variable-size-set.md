---
title: "Variable size/Set (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, type-system, memory-layout]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Variable_size/Set
---

## Summary
This task asks the programmer to demonstrate how to specify the minimum size of a variable or a data type. The key insight is that languages vary widely in how much control they expose over the in-memory footprint of a value: some offer explicitly sized integer types or bit-field declarations, while higher-level languages abstract storage away entirely and may not allow any control at all.

## Task Requirements
- Demonstrate how to specify the minimum size of a variable or a data type in the chosen language.

## Language Coverage
52 languages implement this task, spanning low-level assembly and systems languages where exact sizing is routine through to high-level dynamic languages where it is awkward or impossible. Representative entries include C, C++, Ada, D, Fortran, PL/I, Pascal, Nim, Go, Rust-adjacent systems dialects, plus assembly variants (360 Assembly, 6502/68000/8086/Z80 Assembly), and high-level languages such as Python, Perl, Raku, Haskell, Java, and Tcl.

## Connections
- [[TypeSystem]] — the task is fundamentally about how a language's type system exposes storage size
- [[MemoryLayout]] — specifying minimum size concerns how values are laid out in memory
- [[PrimitiveDataType]] — explicitly sized integer and floating-point types are the usual mechanism
- [[BitField]] — some languages allow sub-byte sizing via bit-field declarations

## Contradictions
- None — reference task page.
