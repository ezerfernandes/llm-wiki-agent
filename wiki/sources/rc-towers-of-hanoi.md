---
title: "Towers of Hanoi (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Towers_of_Hanoi
---

## Summary
The task is to solve the classic Towers of Hanoi puzzle using recursion. The puzzle requires moving a stack of differently-sized disks from a source peg to a destination peg using an auxiliary peg, never placing a larger disk atop a smaller one. The key insight is the elegant recursive decomposition: to move n disks, first move the top n-1 disks to the spare peg, move the largest disk to the destination, then move the n-1 disks onto it — yielding 2^n - 1 moves.

## Task Requirements
- Solve the Towers of Hanoi problem.
- The solution must use recursion.

## Language Coverage
209 languages implement this task, making it one of the most widely covered entries — spanning assembly, functional, scripting, and esoteric languages. Representative implementations include C, Python, Haskell, Java, Lisp, Prolog, Forth, Rust, and Brainf***.

## Connections
- [[Recursion]] — the required solution technique
- [[DivideAndConquer]] — the puzzle splits into smaller identical subproblems
- [[ExponentialGrowth]] — the minimal move count is 2^n - 1
- [[ClassicAlgorithms]] — a canonical CS teaching problem

## Contradictions
- None — reference task page.
