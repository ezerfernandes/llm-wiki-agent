---
title: "Soloway's recurring rainfall (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, input-output, averaging, control-flow]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Soloway's_recurring_rainfall
---

## Summary
The task asks the programmer to read a stream of integers and print their floating-point average, terminating as soon as the sentinel value 99999 is encountered. It is the classic "Rainfall Problem" from 1980s CS-education research (originally proposed by Elliot Soloway), used as a benchmark for assessing fundamental programming competence rather than as a literal rainfall calculator. The key insight is that the value 99999 is a loop sentinel and must not be folded into the average.

## Task Requirements
- Read integers until the sentinel value 99999 is input, then stop.
- Accept only integers as input.
- Output the average as a floating-point value (cumulative/arithmetic mean).
- Allow negative values (negative "rainfall" is permitted).
- Support an effectively infinite number of inputs in interactive settings.
- A complete solution handles error cases reasonably: re-prompt, skip bad values, etc.

## Language Coverage
37 languages implement this task, spanning systems, scripting, functional, and BASIC-family tongues. Representative examples include Ada, ALGOL 68, C, C++, C#, Java, Python, Perl, Ruby, Rust, and Fortran.

## Connections
- [[ArithmeticMean]] — the average being computed
- [[SentinelValue]] — 99999 marks end of the input stream
- [[ControlFlow]] — iteration and branching are the core skills exercised
- [[InputValidation]] — handling non-integer or malformed input gracefully
- [[CumulativeAverage]] — the running/cumulative mean referenced by the task

## Contradictions
- None — reference task page.
