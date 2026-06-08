---
title: "Continued fraction/Arithmetic/G(matrix ng, continued fraction n1, continued fraction n2) (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, continued-fractions, number-theory, exact-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Continued_fraction/Arithmetic/G(matrix_ng,_continued_fraction_n1,_continued_fraction_n2)
---

## Summary
This task extends Bill Gosper's continued-fraction arithmetic to binary operations on two continued fractions at once. The implementation maintains a 2x4 integer matrix (the "NG" tensor) holding eight coefficients, and incrementally consumes terms from inputs N1 and N2 while emitting output terms whenever all four integer-part candidates agree. The key insight is that any homographic function of two continued fractions can be computed term-by-term in exact arithmetic without ever evaluating the fractions numerically.

## Task Requirements
- Maintain internal state as a 2x4 matrix with rows of coefficients a12, a1, a2, a and b12, b1, b2, b.
- Output a term only when the integer parts of a/b, a1/b1, a2/b2, and a12/b12 are all equal; otherwise ingest another input term.
- Apply the specified matrix transposition rules when ingesting a term t from N1, ingesting a term t from N2, or producing an output term t.
- Inject infinity (the exhaustion rules) when an input continued fraction runs out of terms.
- Decide which input to draw from using the b/b2-zero special cases, then compare abs(a1/b1 - a/b) against abs(a2/b2 - a/b).
- Detect or bound the case where the result is rational (e.g. sqrt(2) * sqrt(2) = 2) by limiting the number of input terms taken without output.

## Language Coverage
34 languages implement this task, a moderate spread reflecting the demanding bookkeeping involved. Representative solutions include Ada, C, C++, C#, Common Lisp, Go, Haskell, Java, Python, Raku, Rust, and Scheme.

## Connections
- [[ContinuedFractions]] — the input/output representation the algorithm operates on.
- [[GosperAlgorithm]] — the underlying technique generalized here to two inputs.
- [[ExactArithmetic]] — terms are emitted without numerical evaluation.
- [[NumberTheory]] — homographic and bihomographic transformations on rationals.
- [[StateMachine]] — the matrix update rules form an incremental ingest/emit automaton.

## Contradictions
- None — reference task page.
