---
title: "Jensen's Device (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, call-by-name, evaluation-strategy]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Jensen's_Device
---

## Summary
Jensen's Device is a classic computer-science demonstration of the call-by-name parameter-passing technique, devised by Jørn Jensen after studying the ALGOL 60 report. The canonical program defines a generic `sum(i, lo, hi, term)` procedure and computes the 100th harmonic number by passing the loop index `i` and the term expression `1/i` by name, so that `1/i` is re-evaluated in the caller's context on each iteration. The key insight is that call-by-name makes the actual argument behave like a thunk re-evaluated on every access, letting one summation routine express arbitrary sums; passing `term` by value instead would wrongly yield 100 × 1/1 = 100 rather than the correct 5.187.

## Task Requirements
- Implement (or faithfully emulate) the ALGOL 60 `sum` procedure that adds `term` over `i` from `lo` to `hi`.
- Pass the `term` argument by name (or simulate it, e.g. via a thunk, closure, or lambda) so it is re-evaluated each iteration.
- Pass the loop/bound variable `i` by name or reference so updates inside `sum` are visible when evaluating `term`.
- Use the device to compute the 100th harmonic number (sum of 1/i for i = 1..100), expecting ≈ 5.187.

## Language Coverage
84 languages implement this task, spanning historic ALGOL-family languages that have native call-by-name through to modern languages that simulate it with closures or lambdas. Representative entries include ALGOL 60, ALGOL 68, Simula, C, C++, Java, JavaScript, Python, Haskell, Scheme, Rust, and Forth.

## Connections
- [[CallByName]] — the parameter-passing strategy the task exists to demonstrate
- [[EvaluationStrategy]] — broader category of by-name vs by-value argument evaluation
- [[Thunk]] — the deferred-evaluation mechanism used to simulate call-by-name in languages lacking it
- [[HarmonicNumber]] — the mathematical quantity computed by the canonical program
- [[ManOrBoyTest]] — Knuth's more rigorous follow-up exercise on the same evaluation semantics

## Contradictions
- None — reference task page.
