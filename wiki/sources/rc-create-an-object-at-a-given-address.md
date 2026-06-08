---
title: "Create an object at a given address (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, systems-programming, memory-management, pointers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Create_an_object_at_a_given_address
---

## Summary
This systems-programming task asks the programmer to place a language object at a specific machine address — the technique used for memory-mapped I/O registers and hardware interrupt vectors. Because most OSes block access to unmapped physical memory, the demonstration instead uses the address of an existing object: create an integer, print its address, then construct a second object that aliases the same location and confirm the two stay in sync.

## Task Requirements
- Create an integer object.
- Print the machine (memory) address of that object.
- Take that address and create another integer object located at it.
- Print the second object's value to verify it matches the original.
- Change the original's value and verify the aliased object reflects the change.

## Language Coverage
42 languages implement this task, spanning low-level assembly (6502, 68000, 8086, ARM, Z80), systems languages (C, C++, D, Rust, Nim, Ada), and higher-level or interpreted languages (Go, Julia, Kotlin, Lua, Perl, Racket, Raku, Tcl), plus several BASIC dialects (FreeBASIC, BBC BASIC, PureBasic). The breadth highlights how directly each language exposes raw memory addressing.

## Connections
- [[Pointers]] — taking and dereferencing an address to alias an object
- [[MemoryMappedIO]] — the real-world motivation for placing objects at fixed addresses
- [[SystemsProgramming]] — domain where hardware-level memory control matters
- [[AddressOperations]] — the address-of / dereference primitives the task relies on

## Contradictions
- None — reference task page.
