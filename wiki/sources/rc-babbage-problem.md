---
title: "Babbage problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, brute-force-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Babbage_problem
---

## Summary
Find the smallest positive integer whose square ends in the digits 269696, a challenge Charles Babbage posed in 1837 while anticipating what his Analytical Engine could solve. He guessed 99736 (squaring to 9947269696) but was unsure. The added constraint is that the program should be clear and well-documented enough that Babbage himself, an intelligent mathematician familiar with early tabular programs, could read it and trust the result. The key insight is that a simple ascending search over integers, testing `n*n mod 1000000 == 269696`, both confirms the answer and stays efficient enough to mirror a pencil-and-paper approach.

## Task Requirements
- Determine the smallest positive integer n such that n² ends in the digits 269696.
- Verify whether Babbage's guess of 99736 is in fact the smallest such integer.
- Write the solution as clearly and legibly as possible — readable by Babbage, an intelligent person versed in mathematics and early computing.
- Prefer an efficient solution analogous to Babbage's own pencil-and-paper method.

## Language Coverage
137 languages implement this task, spanning a very broad range from historical and assembly targets (EDSAC order code, VAX Assembly, x86 Assembly, 360 Assembly) to modern general-purpose languages and niche entries. Representative implementations include C, Python, Java, Haskell, Rust, Go, Fortran, COBOL, Lisp, and Plain English.

## Connections
- [[NumberTheory]] — the problem concerns properties of squares modulo a power of ten.
- [[ModularArithmetic]] — the test reduces n² modulo 1000000 to inspect its last six digits.
- [[BruteForceSearch]] — the canonical solution scans integers in ascending order until the condition holds.
- [[CharlesBabbage]] — the task is framed around a problem Babbage posed for his Analytical Engine.

## Contradictions
- None — reference task page.
