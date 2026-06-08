---
title: "Josephus problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Josephus_problem
---

## Summary
The Josephus problem is a counting-out puzzle: `n` prisoners stand in a circle numbered `0` to `n-1`, and an executioner repeatedly removes every `k`-th prisoner until one survivor remains. The task is to compute the index of that survivor for arbitrary `n` and `k`. The key insight is that the answer can be found without simulation via the recurrence `J(1)=0`, `J(n) = (J(n-1) + k) mod n`, reducing an `O(kn)` walk-the-circle simulation to an `O(n)` (or `O(m)` per position) computation.

## Task Requirements
- Given any `n, k > 0`, find which prisoner is the final survivor.
- Concrete example: solve the classic case of 41 prisoners with `k=3` and report Josephus's surviving position.
- Extra: generalize so that `m` survivors are freed, and provide a way to compute which prisoner sits at any given position in the killing sequence.
- Numbering may start from `0` or `1`; if `1`-based numbering is chosen it must be stated clearly.

## Language Coverage
97 languages implement this task, spanning a very broad cross-section from assembly to high-level functional languages. Representative implementations include C, C++, C#, Java, Python, Haskell, Rust, Go, Ruby, Perl, and Racket.

## Connections
- [[Recurrence]] — the `J(n) = (J(n-1) + k) mod n` recursive formulation
- [[ModularArithmetic]] — modular reduction drives the closed-form recurrence
- [[CircularLinkedList]] — natural data structure for the direct simulation approach
- [[Recursion]] — the survivor position is naturally expressed recursively
- [[ComputationalComplexity]] — contrast between `O(kn)` simulation and `O(n)` recurrence

## Contradictions
- None — reference task page.
