---
title: "Memory allocation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, memory-management, systems-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Memory_allocation
---

## Summary
This task asks the programmer to demonstrate how to explicitly allocate and deallocate blocks of memory in a given language. Where applicable, it also asks to show access to different kinds of memory, such as the heap, the system stack, shared memory, and foreign memory. The key insight is that languages differ enormously here: low-level languages expose manual allocation primitives (malloc/free, new/delete), while garbage-collected languages may have little or nothing explicit to show.

## Task Requirements
- Show how to explicitly allocate a block of memory.
- Show how to explicitly deallocate (free) that block.
- If applicable, demonstrate access to different memory regions: heap, stack, shared memory, and foreign memory.

## Language Coverage
72 languages implement this task, spanning low-level assembly and systems languages through high-level managed runtimes. Representative implementations include C, C++, Rust, Ada, Go, Fortran, COBOL, 360 Assembly, X86 Assembly, Python, and Common Lisp.

## Connections
- [[HeapMemory]] — dynamic allocation region the task centers on
- [[StackMemory]] — automatic storage for local/scoped data
- [[ManualMemoryManagement]] — explicit allocate/free model in low-level languages
- [[GarbageCollection]] — contrast in managed languages with no explicit free
- [[Pointer]] — handle returned by allocation primitives

## Contradictions
- None — reference task page.
