---
title: "Pythagorean quadruples (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pythagorean_quadruples
---

## Summary
A Pythagorean quadruple is a set of positive integers a, b, c, d satisfying a² + b² + c² = d² (for example, 2² + 3² + 6² = 7²). The task is to find which values of d up to 2,200 cannot be expressed this way. The key insight is that rather than brute-forcing all combinations of a, b, c, one can mark every reachable d and report the unrepresentable ones; the answer turns out to be only the values 1, 2, 4, 5, 8, 10, 16, 20, 32, 40, ... (powers of 2 and 5 times powers of 2).

## Task Requirements
- Treat a, b, c, d as positive integers up to and including 2,200.
- Find all values of d in that range for which no a, b, c satisfy a² + b² + c² = d².
- Show those unrepresentable values of d on a single line of output (a title is optional).

## Language Coverage
47 languages implement this task, showing broad coverage across systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, C#, Go, Rust, Java, Haskell, Python, Perl, Raku, Julia, and Wren.

## Connections
- [[NumberTheory]] — the task is rooted in integer relations and Diophantine equations.
- [[DiophantineEquation]] — solving a² + b² + c² = d² over the integers.
- [[PythagoreanTriples]] — the closely related three-term analogue.
- [[SieveTechnique]] — efficient solutions mark reachable d values rather than enumerating all triples.

## Contradictions
- None — reference task page.
