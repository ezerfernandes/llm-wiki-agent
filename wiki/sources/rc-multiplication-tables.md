---
title: "Multiplication tables (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arithmetic, formatted-output]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Multiplication_tables
---

## Summary
The task asks the programmer to produce a formatted 12×12 multiplication table, the kind memorized by rote in primary school. Only the upper-triangle of products should be printed (since multiplication is commutative, the lower triangle would simply mirror it). The core challenge is column alignment and text formatting rather than any arithmetic difficulty.

## Task Requirements
- Compute and display a 12×12 grid of products.
- Print only the top-half triangle (omit the redundant lower-triangle entries where row > column).
- Format the output so columns line up neatly (typically with right-justified, fixed-width fields and a header row/column).

## Language Coverage
130 languages implement this task, reflecting its status as a simple, beginner-friendly exercise that exercises nested loops and string formatting in nearly every paradigm. Representative implementations include C, Python, Java, Haskell, Ruby, Go, Rust, Common Lisp, APL, and Forth.

## Connections
- [[Multiplication]] — the underlying arithmetic operation being tabulated.
- [[NestedLoops]] — the standard double-loop construct used to build the grid.
- [[StringFormatting]] — fixed-width, right-justified output for column alignment.
- [[CommutativeProperty]] — why only the upper triangle need be printed.

## Contradictions
- None — reference task page.
