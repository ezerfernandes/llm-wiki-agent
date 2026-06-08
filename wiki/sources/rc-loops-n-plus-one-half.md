---
title: "Loops/N plus one half (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, iteration, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Loops/N_plus_one_half
---

## Summary
This task asks the programmer to demonstrate the idiomatic way to handle a loop whose final iteration executes only part of the body — the so-called "loop and a half" pattern. The concrete exercise is printing the comma-separated list `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`, emitting the number and the separating comma as distinct output statements, so that no trailing comma follows the last element. The key insight is that the separator (comma) must be suppressed on the last pass, which is the canonical case where a clean loop structure beats ad-hoc flags.

## Task Requirements
- Write a loop that outputs the list `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`.
- The number and the comma must be printed by separate output statements inside the loop body.
- The final iteration must omit the trailing comma, so only part of the body runs on the last pass.

## Language Coverage
182 languages implement this task, making it one of the most broadly covered entries in the Loops family. Solutions span assembly (360 Assembly, ARM, 8086), systems languages (C, C++, Rust, Zig, Go), functional languages (Haskell, OCaml, Erlang, Clojure), scripting languages (Python, Perl, Ruby, JavaScript, Lua), and esoteric or niche ones (Befunge, FALSE, SNUSP, Uiua).

## Connections
- [[ControlFlow]] — the task is fundamentally about structuring loop body execution.
- [[LoopAndAHalf]] — the named pattern for loops with a partial final iteration.
- [[Iteration]] — the broader programming construct being exercised.
- [[StringJoining]] — the practical problem (joining tokens with a separator without a trailing one) underlying the task.

## Contradictions
- None — reference task page.
