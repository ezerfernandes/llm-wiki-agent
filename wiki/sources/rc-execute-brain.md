---
title: "Execute Brain**** (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, interpreters, esoteric-language]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Execute_Brain****
---

## Summary
The task asks the programmer to implement a compiler or interpreter for the Brainfuck esoteric programming language (collected on Rosetta Code under the name RCBF). The core insight is that Brainfuck has only eight single-character instructions operating on a tape of memory cells and a data pointer, so a full interpreter reduces to a dispatch loop plus correct matching of the looping brackets. Most of the implementation effort lies in efficiently pairing each `[` with its `]` for the conditional jumps.

## Task Requirements
- Implement the eight instructions: `>` and `<` move the data pointer right/left; `+` and `-` increment/decrement the cell under the pointer; `.` outputs the cell as a character; `,` reads a character into the cell.
- `[` jumps past the matching `]` when the current cell is zero; `]` jumps back to the matching `[` when the current cell is nonzero (the looping construct).
- Any cell size is permitted.
- EOF handling on input is optional.
- Memory may be bounded or unbounded at the implementer's discretion.

## Language Coverage
113 languages implement this task, an unusually broad set spanning high-level scripting, functional, and low-level assembly languages. Representative implementations include C, C++, Rust, Go, Python, Haskell, Java, Common Lisp, Forth, and even 8080/8086 Assembly and Brainfuck itself.

## Connections
- [[Brainfuck]] — the esoteric language being executed
- [[Interpreter]] — the primary structure most solutions adopt (a dispatch loop over instructions)
- [[TuringMachine]] — Brainfuck's tape-and-pointer model is essentially a Turing machine, making it Turing-complete
- [[StackDataStructure]] — used to match `[`/`]` bracket pairs for the jump targets
- [[EsotericProgrammingLanguage]] — the category this task belongs to

## Contradictions
- None — reference task page.
