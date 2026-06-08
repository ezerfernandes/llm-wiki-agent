---
title: "Create a two-dimensional array at runtime (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-structures, arrays, memory-management]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Create_a_two-dimensional_array_at_runtime
---

## Summary
This task asks the programmer to read two integers from the user at runtime and use them as the row and column dimensions of a dynamically allocated two-dimensional array. After creation, the program writes a value into one element, reads it back to output, and finally releases the array if the language does not reclaim it automatically. The key insight is that the dimensions are not known at compile time, so the language's mechanism for runtime (dynamic) allocation and natural element access must be demonstrated.

## Task Requirements
- Obtain two integers from the user to serve as the array's two dimension sizes.
- Allocate a 2D array of those sizes at runtime (not fixed at compile time).
- Access the array "in the most natural way possible" for the language.
- Write a value to some element, then read and output that same element.
- Destroy or free the array at the end, unless the language handles deallocation itself.

## Language Coverage
122 languages implement this task, spanning low-level assembly with manual allocation, systems languages, scripting languages, and array-oriented or functional languages. Representative examples include C, C++, Rust, Java, Go, Python, Perl, Haskell, Fortran, and APL.

## Connections
- [[Arrays]] — the core data structure being constructed
- [[DynamicMemoryAllocation]] — runtime sizing requires heap allocation in many languages
- [[MultidimensionalArrays]] — the two-dimensional indexing model
- [[GarbageCollection]] — determines whether explicit destruction is needed

## Contradictions
- None — reference task page.
