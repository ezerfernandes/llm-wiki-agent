---
title: "Host introspection (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, systems-programming, low-level]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Host_introspection
---

## Summary
The task asks the programmer to detect and print two fundamental properties of the machine the program is running on: the native word size (typically the bit-width of the CPU's integer registers / pointers, e.g. 32 or 64 bits) and the byte order, or endianness (big-endian vs. little-endian). The key insight is that these values are determined by the hardware and runtime rather than chosen by the program, so a robust solution either queries a platform API or probes memory directly by inspecting the byte layout of a known multi-byte value.

## Task Requirements
- Print the word size of the host machine.
- Print the endianness of the host machine.

## Language Coverage
72 languages implement this task, spanning low-level assembly (68000, 8086, ARM, MIPS, Z80) where endianness is probed directly in memory, systems languages (C, C++, D, Rust, Go, Nim), and higher-level/managed environments (Python, Java, C#, Ruby, Haskell, Racket, Julia) that expose word size and byte order through standard-library introspection.

## Connections
- [[Endianness]] — byte-ordering property the task must detect
- [[WordSize]] — the CPU/pointer bit-width the task must report
- [[SystemsProgramming]] — querying hardware/runtime properties at the platform level
- [[MemoryLayout]] — probing the byte representation of values to infer byte order

## Contradictions
- None — reference task page.
