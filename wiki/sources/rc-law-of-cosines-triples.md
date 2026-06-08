---
title: "Law of cosines - triples (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Law_of_cosines_-_triples
---

## Summary
The task asks the programmer to find all integer-sided triangles whose angle γ between sides A and B is exactly 90°, 60°, or 120°, using the Law of cosines (A² + B² − 2AB·cos(γ) = C²). The key insight is that for these three special angles cos(γ) takes the clean values 0, ½, and −½, collapsing the formula to A²+B²=C², A²+B²−AB=C², and A²+B²+AB=C² respectively, so no floating-point trigonometry is needed — only integer arithmetic and a search for perfect-square right-hand sides.

## Task Requirements
- Find all integer solutions (in order) for each of the three angle cases (90°, 60°, 120°).
- Restrict all sides to integers in the range 1..13 inclusive.
- Report how many solutions exist for each of the three angles.
- Treat triangles with the same side lengths in different order as identical (avoid double-counting).
- Optional extra credit: count 60° integer triples for sides in 1..10000 where the sides are not all equal.

## Language Coverage
38 languages implement this task, spanning systems, scripting, functional, and array languages. Representative examples include C, C++, C#, Go, Java, JavaScript, Python, Haskell, Julia, Perl, Raku, and J.

## Connections
- [[LawOfCosines]] — the trigonometric identity that defines the problem.
- [[PythagoreanTriples]] — the 90° case is exactly the Pythagorean-triple search.
- [[DiophantineEquations]] — solutions are integer solutions to quadratic-form equations.
- [[BruteForceSearch]] — the typical solution enumerates side pairs and tests for a perfect-square third side.
- [[PerfectSquare]] — recognizing when C² yields an integer C.

## Contradictions
- None — reference task page.
