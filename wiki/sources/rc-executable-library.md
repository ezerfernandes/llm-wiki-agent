---
title: "Executable library (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, software-design]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Executable_library
---

## Summary
The task asks the programmer to build a single source file that behaves as both an importable library and a directly-runnable program. When imported, it exposes a `hailstone` function returning the Hailstone (Collatz) sequence for a positive integer; when executed directly from the command line, it runs the demonstration logic. The key insight is the idiom (e.g. Python's `if __name__ == "__main__"`) that lets one file detect whether it is being imported or run as the main program.

## Task Requirements
- Create a library/module/DLL/shared object exposing a `hailstone` function that takes a positive integer and returns its Hailstone sequence.
- When executed directly, the library must satisfy the [[Hailstone sequence]] task: show that the sequence for 27 has 112 elements (27, 82, 41, 124, ... 8, 4, 2, 1) and report the number below 100,000 with the longest sequence plus its length.
- Provide a second executable that reuses the library's `hailstone` function (in standard library-usage fashion) to find the hailstone length returned most often for 1 ≤ n < 100,000.
- Document any extra setup or run steps. For compiled languages the library itself must also be executable, since the toolchain is assumed absent at runtime; interpreters are assumed present.

## Language Coverage
35 languages implement this task, spanning interpreted scripting languages, compiled systems languages, and JVM languages. Representative examples include C, Go, Java, Python, Perl, Ruby, Tcl, Lua, Racket, and Nim.

## Connections
- [[Hailstone sequence]] — the algorithm the library computes
- [[Collatz conjecture]] — the number-theory problem behind the Hailstone sequence
- [[Module System]] — the import-vs-execute mechanism this task exercises
- [[Command Line Interface]] — the direct-execution entry point bundled with the API

## Contradictions
- None — reference task page.
