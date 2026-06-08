---
title: "Variable declaration reset (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, scope]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Variable_declaration_reset
---

## Summary
This task probes a subtle semantic difference between languages: whether a variable declared inside a loop's block scope is reset on every iteration or retains its value across iterations. Using a longhand loop over {1,2,2,3,4,4,5}, the program reports the index of each element identical to its immediate predecessor (expected 2,5 zero-based or 3,6 one-based). The key insight is that the result hinges on whether a freshly declared per-iteration variable starts unassigned or carries over the prior iteration's value.

## Task Requirements
- Iterate over the list {1,2,2,3,4,4,5} with a straightforward longhand loop.
- Print the positions of elements equal to the immediately preceding element.
- Expected output is 2,5 (zero-based) or 3,6 (one-based).
- Demonstrate whether a block-scoped declared variable resets each iteration.
- If "unassigned variable" errors occur, initialize the variable (e.g. `int prev = -1`) to show predictable behavior.
- Languages without block scope (e.g. assembly) should be omitted.

## Language Coverage
32 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative examples include C, C++, C#, Java, Go, Nim, Python, Perl, Raku, Ruby, JavaScript, F#, and Wren.

## Connections
- [[VariableScope]] — the task hinges on block-scope semantics
- [[ControlFlow]] — uses iteration over a sequence
- [[VariableInitialization]] — distinguishes unassigned vs default-initialized state
- [[ProgrammingLanguageSemantics]] — highlights cross-language behavioral differences

## Contradictions
- None — reference task page.
