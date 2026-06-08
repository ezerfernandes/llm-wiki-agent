---
title: "Heronian triangles (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Heronian_triangles
---

## Summary
The task asks the programmer to implement Hero's formula for the area of a triangle from its three side lengths, then enumerate all *primitive* Heronian triangles (integer sides and integer area, with the sides sharing a greatest common divisor of 1) whose sides are at most 200. The key insight is that the area `sqrt(s(s-a)(s-b)(s-c))` must come out an exact integer, and restricting the search to `a <= b <= c` avoids generating permutations of the same triangle.

## Task Requirements
- Define a named function implementing Hero's formula `A = sqrt(s(s-a)(s-b)(s-c))`, where `s = (a+b+c)/2`.
- Generate all primitive Heronian triangles with all sides <= 200 (a Heronian triangle has integer sides and integer area; primitive means gcd of the three sides is 1).
- Show the total count of such triangles found.
- Order the triangles by increasing area, then increasing perimeter, then increasing maximum side length.
- Show the first ten ordered triangles in a table of sides, perimeter, and area.
- Show a similar ordered table restricted to triangles with area = 210.

## Language Coverage
60 languages implement this task, spanning systems, scripting, functional, and array languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, J, and Wren.

## Connections
- [[HeronsFormula]] — the core area computation the task is built around.
- [[GreatestCommonDivisor]] — used to test primitivity of the side triple.
- [[NumberTheory]] — integer-area constraint makes this a Diophantine enumeration problem.
- [[Sorting]] — multi-key ordering by area, then perimeter, then max side.

## Contradictions
- None — reference task page.
