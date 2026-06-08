---
title: "Multi-dimensional array (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arrays, data-structures, memory-layout]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Multi-dimensional_array
---

## Summary
This task asks the programmer to demonstrate how their language handles arrays with more than one index dimension. The core exercise is to create a four-dimensional array (with index extents of 5, 4, 3, and 2), set an element by its ordered integer indices, read it back, overwrite it, and read again. Beyond mechanics, the task probes language-specific traits: native syntax support, storage order, and memory behavior.

## Task Requirements
- State whether the language natively supports multi-dimensional arrays in syntax and usual implementation.
- State whether storage uses row-major or column-major order (or another scheme).
- Create a 4-D array with index ranges of 5, 4, 3, and 2; set an integer-indexed element, access it, set it to a new value, then access the new value (idiomatic method preferred).
- State if memory allocation is optimized — especially whether contiguous memory is likely allocated.
- Mention any exceptional native support such as optional bounds checking, reshaping, or specifying both lower and upper index bounds.

## Language Coverage
51 languages implement this task, spanning systems languages, scientific/array-oriented languages, BASIC dialects, and functional languages — illustrating how differently each handles nested indexing and memory layout. Representative entries include C, C++, Fortran, Ada, Python, Java, Julia, J, R, Mathematica / Wolfram Language, and Raku.

## Connections
- [[ArrayDataStructure]] — the fundamental indexed-collection type being generalized to multiple dimensions
- [[RowMajorOrder]] — the contiguous-memory layout convention the task asks each language to report
- [[ColumnMajorOrder]] — the alternative layout used by languages like Fortran and R
- [[BoundsChecking]] — an optional native feature the task highlights
- [[MemoryLayout]] — how contiguity and allocation strategy affect array access

## Contradictions
- None — reference task page.
