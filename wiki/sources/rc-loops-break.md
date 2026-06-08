---
title: "Loops/Break (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, loops]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Loops/Break
---

## Summary
This task demonstrates how to terminate a loop early from inside its body using a break (or equivalent) statement. The loop generates random integers from 0 to 19 inclusive; if the value 10 appears it is printed and the loop stops immediately, otherwise a second random number is printed and the loop repeats. The key insight is that a mid-body exit must skip the remaining work in that iteration and abandon any further iterations.

## Task Requirements
- Run a loop that prints freshly generated random numbers in the range 0 to 19 (inclusive) each pass.
- If a generated number equals 10, print it and then stop the loop without generating anything more.
- Otherwise, generate and print a second random number before restarting the loop.
- If 10 is never produced as the first number of a pass, the loop runs forever.

## Language Coverage
195 languages implement this task, an exceptionally broad set spanning systems languages, scripting languages, assembly, and esoteric languages. Representative examples include C, C++, Java, Python, Rust, Go, Haskell, Ruby, Perl, and 6502 Assembly.

## Connections
- [[ControlFlow]] — break is a non-local transfer of control out of a loop
- [[Loops]] — the task is part of the loop-modifier family of exercises
- [[RandomNumberGeneration]] — each iteration depends on freshly generated random values
- [[ConditionalStatements]] — the early exit hinges on testing for the value 10

## Contradictions
- None — reference task page.
