---
title: "Halt and catch fire (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, error-handling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Halt_and_catch_fire
---

## Summary
This task asks the programmer to write the shortest possible syntactically valid program that crashes immediately, without damaging the machine. The snippet should be embeddable into another program — useful as a deliberate abort when an internal corruption is detected and continuing would be unsafe. The name alludes to the legendary "Halt and Catch Fire" (HCF) machine instruction.

## Task Requirements
- Create a program that crashes as soon as possible.
- Use as few lines of code as possible.
- Do not damage the computer.
- The code must be syntactically valid.
- The crash logic should be insertable as a subset into another program (e.g., for debugging or safe abort).

## Language Coverage
75 languages implement this task, spanning high-level scripting languages, compiled systems languages, and many bare-metal assembly dialects. Representative implementations include C, C++, Rust, Go, Python, Java, JavaScript, Haskell, Perl, Ruby, and several assembly variants such as 6502, 8086, and Z80.

## Connections
- [[Program Termination]] — directly related Rosetta Code task on exiting cleanly.
- [[Exceptions]] — common crash mechanism via uncaught exceptions or raised errors.
- [[Assertions]] — deliberate aborts on detecting invalid internal state.
- [[Defensive Programming]] — failing fast when corruption is detected rather than continuing unsafely.

## Contradictions
- None — reference task page.
