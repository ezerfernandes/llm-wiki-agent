---
title: "Minimum positive multiple in base 10 using only 0 and 1 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, breadth-first-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Minimum_positive_multiple_in_base_10_using_only_0_and_1
---

## Summary
Every positive integer n has infinitely many base-10 multiples whose decimal representation contains only the digits 0 and 1; the task asks to find the smallest such multiple (abbreviated "B10"). The naive approach of testing successive multiples is correct but slow, so the key insight is to search over the candidate {0,1}-digit strings themselves rather than over multiples of n, typically using a breadth-first search on remainders modulo n. This corresponds to OEIS sequence A004290.

## Task Requirements
- Write a routine that, given a positive integer n, returns its B10 (least positive multiple using only digits 0 and 1).
- Display B10 for n = 1 through 10, 95 through 105, 297, 576, 594, 891, 909, and 999.
- Optionally compute B10 for 1998, 2079, 2251, 2277.
- Stretch goal: compute B10 for 2439, 2997, 4878.
- Avoid magic numbers where possible; if used, explain their purpose briefly.

## Language Coverage
36 languages implement this task, spanning systems, functional, scripting, and array languages. Representative examples include C, C++, C#, Go, Java, Haskell, Python, Perl, Raku, Julia, J, and REXX.

## Connections
- [[NumberTheory]] — finding multiples with a constrained digit set
- [[ModularArithmetic]] — search proceeds over remainders mod n
- [[BreadthFirstSearch]] — BFS over {0,1}-digit candidates yields the minimal solution
- [[BigInteger]] — B10 values can exceed native integer width (e.g. n=9 gives 111111111)

## Contradictions
- None — reference task page.
