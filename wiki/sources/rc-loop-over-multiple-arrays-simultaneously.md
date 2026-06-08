---
title: "Loop over multiple arrays simultaneously (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, iteration, arrays]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Loop_over_multiple_arrays_simultaneously
---

## Summary
This Rosetta Code task asks the programmer to iterate over several arrays in parallel, accessing the i-th element of each on every step. Given (a,b,c), (A,B,C), and (1,2,3), the program prints aA1 / bB2 / cC3. The key insight is whether a language offers a built-in "zip"-style construct to bind elements from multiple collections per iteration, versus driving everything from a single shared index.

## Task Requirements
- Loop over three arrays simultaneously and display the i-th element of each, concatenated per row.
- Use the language's "for each" loop if available; otherwise iterate in order with an index-based loop.
- Produce the output rows aA1, bB2, cC3.
- If possible, describe behavior when the arrays have different lengths (e.g., truncate to shortest, error, or pad).

## Language Coverage
162 languages implement this task, spanning everything from low-level assembly to high-level functional and scripting languages. Representative implementations include Python, Haskell, Ruby, JavaScript, C, Rust, Go, Common Lisp, and Perl, showing both zip-based and indexed-loop strategies.

## Connections
- [[Iteration]] — the core control-flow pattern being exercised
- [[ZipFunction]] — the idiomatic way to pair elements across collections
- [[ArrayDataStructure]] — the collections being traversed in parallel
- [[ParallelIteration]] — advancing multiple sequences in lockstep

## Contradictions
- None — reference task page.
