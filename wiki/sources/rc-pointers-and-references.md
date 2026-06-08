---
title: "Pointers and references (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, memory-management, pointers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pointers_and_references
---

## Summary
This task asks the programmer to demonstrate common operations on pointers and references: taking the address of a variable, dereferencing a pointer to read or modify the value it points to, and reassigning what a pointer refers to. The examples illustrate stack-based pointer manipulation, which the task notes is dangerous and rarely done in practice — pointers and references are normally paired with heap memory allocation.

## Task Requirements
- Show how to obtain a pointer or reference to an existing variable (take its address).
- Demonstrate dereferencing to read and to modify the pointed-to value.
- Show reassigning a pointer to refer to a different object.
- Note that these stack-based demonstrations are unsafe relative to typical heap-backed usage.

## Language Coverage
64 languages implement this task, spanning low-level assembly through high-level managed and functional languages, reflecting how differently the pointer/reference concept manifests across paradigms. Representative implementations include C, C++, Ada, Go, Rust-adjacent systems languages, 8086/68000/Z80 Assembly, Haskell, OCaml, Common Lisp, Python, Java, and C#.

## Connections
- [[MemoryAllocation]] — pointers/references are typically used with dynamic heap allocation
- [[Heap]] — the safer storage region for pointer targets versus the stack
- [[Dereferencing]] — the operation of accessing the value a pointer addresses
- [[CallByReference]] — passing references to allow callees to mutate caller variables
- [[PointerArithmetic]] — low-level address manipulation common in systems languages

## Contradictions
- None — reference task page.
