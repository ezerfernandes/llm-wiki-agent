---
title: "Arena storage pool (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, memory-management, allocator]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Arena_storage_pool
---

## Summary
This task asks the programmer to demonstrate how a language supports custom allocators and user-defined storage pools that back the heap for dynamically allocated objects. Specifically it requires defining an *arena* pool — a region where objects are allocated individually but freed all at once as a group — and allocating some objects (e.g. integers) within it. The key insight is the distinction between binding a storage pool to an object's type versus to the pointer/reference type, which determines where a `new T` allocation actually draws its memory from.

## Task Requirements
- Show how allocators and user-defined storage pools are supported by the language.
- Define an arena storage pool: objects are allocated one at a time, but reclaimed collectively by group.
- Allocate some objects (such as integers) inside that pool.
- Explain what controls the choice of storage pool in the language (object type T vs. pointer type P).

## Language Coverage
35 languages implement this task, spanning systems languages with explicit memory control and higher-level managed runtimes. Representative examples include Ada (whose pointer-bound storage pools motivate the task), C, C++, Rust, Go, Fortran, Pascal, Java, Python, Tcl, and Racket.

## Connections
- [[MemoryManagement]] — the broad topic this task illustrates
- [[Heap]] — the dynamic allocation region a pool backs
- [[ArenaAllocation]] — the specific allocate-individually, free-as-a-group strategy
- [[Pointer]] — pointer/reference type can determine pool selection
- [[Stack]] — the alternative allocation region contrasted with pooled heap allocation

## Contradictions
- None — reference task page.
