---
title: "Memory layout of a data structure (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, bit-manipulation, hardware-interfacing, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Memory_layout_of_a_data_structure
---

## Summary
This task asks the programmer to control the exact memory layout of fields in a data structure so it matches an externally fixed interface or hardware definition, rather than letting the compiler choose. The concrete example is modeling the RS-232 serial plug pinout (the 9-pin variant for brevity), where each named signal must occupy a specific position. The key insight is that hardware and protocol interfaces require precise field placement, ordering, and packing — something achievable via bit fields, packed structs/records, or explicit offset declarations.

## Task Requirements
- Define a data structure whose field layout in memory is explicitly controlled.
- Match the structure to the RS-232 Plug Definition (interface control definition).
- Use the 9-pin RS-232 definition (rather than the full 25-pin) for brevity.
- Map each named signal (TD, RD, RTS, CTS, DSR, SG, CD, DTR, RI) to its correct pin position.

## Language Coverage
36 languages implement this task, spanning systems and assembly languages with native bit/struct control through higher-level languages that simulate the layout. Representative implementations include 6502 Assembly, 68000 Assembly, Ada, C/C++, D, Forth, Fortran, Go, Java, Nim, OCaml, and PL/I.

## Connections
- [[BitFields]] — packed structures map named signals onto specific bits.
- [[DataStructureAlignment]] — controlling field offsets and padding in memory.
- [[StructPacking]] — eliminating compiler-inserted padding to match an external layout.
- [[RS232]] — the serial interface whose pinout the structure models.
- [[HardwareInterfacing]] — the motivating use case for explicit memory layout.

## Contradictions
- None — reference task page.
