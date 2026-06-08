---
title: "Jump anywhere (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, continuations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Jump_anywhere
---

## Summary
This task asks the programmer to demonstrate the various forms of non-sequential control transfer a language supports, from local jumps to truly arbitrary "jump anywhere" mechanisms. The key insight is that jumps differ by how they treat the call stack: a plain `goto` never touches it, stack unwinding tears it down across multiple calls, and a saved continuation preserves the whole stack so execution can resume at a previously visited point even after the enclosing function has returned. It is an open-ended "grab bag" task rather than a single algorithm.

## Task Requirements
- Demonstrate a local jump (within a function) and a global jump (across the program).
- Show whatever other jump types the language offers; jumps may serve any purpose.
- Optionally illustrate non-local / long jumps, unwinding the call stack across multiple function calls, or saving and resuming a continuation.
- It is acceptable to defer to more specific tasks such as Exceptions or Generators.

## Language Coverage
92 languages implement this task, spanning everything from low-level assembly (360, 6502, 68000, 8086, MIPS, Z80) to high-level and functional languages. Representative entries include C, Java, Python, Perl, Haskell, Common Lisp, Racket, Go, Ruby, and Scheme-style continuations in Racket and Koka.

## Connections
- [[ControlFlow]] — the task is a survey of control-transfer constructs
- [[Goto]] — the simplest jump that ignores the call stack
- [[Continuations]] — saving and resuming the full call stack
- [[CallStackUnwinding]] — breaking out of multiple nested calls
- [[ExceptionHandling]] — a structured form of non-local jump

## Contradictions
- None — reference task page.
