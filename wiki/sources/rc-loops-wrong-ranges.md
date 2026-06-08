---
title: "Loops/Wrong ranges (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, iteration, control-flow, edge-cases]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Loops/Wrong_ranges
---

## Summary
This task probes how a language's range syntax or function behaves when fed degenerate or contradictory parameters. After picking a range construct that normally yields at least two increasing values from a start, stop, and positive increment, the programmer must reuse that *same* construct with nine awkward parameter sets and report what actually happens. The key insight is that "wrong" ranges expose each language's design choices: some raise errors, some produce empty sequences, and some loop infinitely.

## Task Requirements
- Choose a range syntax/function that generates at least two increasing numbers given stop > start and a positive increment less than half the difference.
- Apply that same construct to nine parameter triples and show the resulting behavior.
- Cover the cases: (-2,2,1) normal; (-2,2,0) zero increment; (-2,2,-1) increment away from stop; (-2,2,10) first step beyond stop; (2,-2,1) start>stop with positive increment; (2,2,1) start=stop positive; (2,2,-1) start=stop negative; (2,2,0) start=stop zero; (0,0,0) all zero.
- Document errors, empty ranges, or infinite loops rather than hiding them.

## Language Coverage
58 languages implement this task, spanning a broad mix of functional, imperative, and array-oriented styles. Representative entries include Python, C, C++, Java, JavaScript, Haskell, Julia, Raku, Ruby, Go, and REXX.

## Connections
- [[Iteration]] — the task centers on loop/range generation semantics.
- [[ControlFlow]] — degenerate parameters change how control flow terminates (or fails to).
- [[EdgeCaseTesting]] — the exercise is essentially boundary-condition analysis of a range API.
- [[ErrorHandling]] — several cases hinge on whether a language errors versus returns empty.

## Contradictions
- None — reference task page.
