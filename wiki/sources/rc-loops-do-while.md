---
title: "Loops/Do-while (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, iteration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Loops/Do-while
---

## Summary
This task demonstrates a post-test (do-while) loop, where the loop body always runs at least once before the continuation condition is checked. Starting from a value of 0, the program adds 1 to the value and prints it on each pass, continuing while the value modulo 6 is not zero. The key insight is that the condition is evaluated at the bottom of the loop, so the body executes before any test occurs.

## Task Requirements
- Start with a value at 0.
- Loop while value mod 6 is not equal to 0.
- Each time through the loop, add 1 to the value, then print it.
- The loop must execute at least once (post-test semantics).

## Language Coverage
190 languages implement this task, an exceptionally broad set spanning every major paradigm and era. Representative examples include C, C++, Python, Java, JavaScript, Ada, Haskell, Lua, Rust, Go, and Forth, along with many assembly dialects (x86, ARM, MIPS) that build the construct from conditional branches since most lack a native do-while.

## Connections
- [[ControlFlow]] — the task exercises a fundamental control-flow primitive.
- [[Iteration]] — it is categorized under iterative looping constructs.
- [[ConditionalLoops]] — the loop continues based on a runtime condition.
- [[ModuloOperation]] — the continuation test uses the modulo operator.

## Contradictions
- None — reference task page.
