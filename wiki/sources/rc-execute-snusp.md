---
title: "Execute SNUSP (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, interpreters, esoteric-language]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Execute_SNUSP
---

## Summary
The task is to write a compiler or interpreter for SNUSP, a two-dimensional esoteric programming language whose programs are read as a grid where the instruction pointer moves spatially rather than line-by-line. The key insight is that SNUSP combines a Brainfuck-style tape of memory cells with directional control: characters like `\` and `/` act as mirrors that redirect the instruction pointer across the 2D source code.

## Task Requirements
- Implement at minimum the Core SNUSP instructions: `$` (start), `\` and `/` (mirrors that turn the IP), `+` and `-` (increment/decrement the current cell), `<` and `>` (move the memory pointer), `,` and `.` (input/output a byte), `!` (skip the next cell), and `?` (skip next cell if current cell is zero).
- Optionally support Modular SNUSP (`#`, `@`) and Bloated SNUSP (`:`, `;`, `%`, `&`); any extra characters implemented must be documented.
- Cell size, EOF handling, and bounded vs. unbounded memory are left to the implementer's discretion.

## Language Coverage
34 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative implementations include C, C++, D, Go, Rust-adjacent FreeBASIC, Haskell, OCaml, F#, Java, Python, Ruby, Perl, Racket, and Wren.

## Connections
- [[EsotericProgrammingLanguage]] — SNUSP belongs to this family alongside Brainfuck
- [[Brainfuck]] — SNUSP's memory model and `+ - < > , .` instructions derive from it
- [[Interpreter]] — the task is to build one for SNUSP source programs
- [[TwoDimensionalProgrammingLanguage]] — the instruction pointer navigates a 2D grid via mirror directives

## Contradictions
- None — reference task page.
