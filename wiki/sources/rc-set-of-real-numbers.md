---
title: "Set of real numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, set-theory, computational-geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Set_of_real_numbers
---

## Summary
The task asks the programmer to represent arbitrary sets of real numbers and implement the standard set operations on them. The chosen representation must cover any set expressible as a finite union of convex sets (intervals), where each interval can have independently open or closed endpoints. The key insight is that membership, union, intersection, and difference can all be reduced to a membership predicate over interval boundaries, so a set can be modeled as a predicate function rather than an explicit collection.

## Task Requirements
- Devise a representation for any real set that is a finite union of convex sets (intervals), with open/closed boundaries; Cantor-like sets are out of scope.
- Implement membership (x ∈ A), union (A ∪ B), intersection (A ∩ B), and difference (A − B).
- Handle infinities gracefully; NaN may be ignored. Native IEEE floating point is acceptable.
- Test whether 0, 1, 2 belong to: (0,1] ∪ [0,2); [0,2) ∩ (1,2]; [0,3) − (0,1); [0,3) − [0,1].
- Optional: an emptiness test, and computing the measure (length) of A − B for two trigonometric sets defined over (0,10).

## Language Coverage
36 languages implement this task, spanning systems, functional, scripting, and array languages. Representative examples include C, C++, C#, Haskell, F#, Common Lisp, Racket, Python, Ruby, Perl, Raku, Julia, Go, Rust, J, and Mathematica/Wolfram Language.

## Connections
- [[SetTheory]] — the four interval types and the union/intersection/difference operations are core set-theoretic constructs.
- [[Interval]] — convex real sets are exactly closed/open/half-open intervals.
- [[HigherOrderFunctions]] — many solutions represent a set as a membership predicate (a function returning a boolean), composing operations by combining predicates.
- [[Measure]] — the optional task computes the Lebesgue measure (total length) of a set difference.

## Contradictions
- None — reference task page.
