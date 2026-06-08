---
title: "Stair-climbing puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Stair-climbing_puzzle
---

## Summary
A stair-climbing robot exposes only a `step()` primitive that tries to climb one stair and returns true on success or false if it instead slips down one stair. The puzzle (originally from Chung-Chieh Shan via Lambda the Ultimate) asks for a `step_up()` function that reliably advances exactly one stair, written as compactly as possible. The key insight is a self-referential recursion: on failure (a net drop of one), two recursive `step_up()` calls regain the lost stair plus the intended one, so no counters or variables are needed.

## Task Requirements
- Implement `step_up()` using only the boolean-returning `step()` primitive.
- It must end exactly one stair higher than where it started, regardless of how many times `step()` fails.
- Assume the robot is never at the top or bottom of the stairs.
- Make the function as small as possible; ideally avoid variables (even immutable ones) and numbers.
- A simple recursive solution and an inductive correctness proof are provided; the tail recursion may be converted to a loop.

## Language Coverage
78 languages implement this task, spanning functional, imperative, and esoteric styles. Representative entries include C, C++, C#, Java, Python, Haskell, Scheme, Common Lisp, Prolog, Rust, and Forth.

## Connections
- [[Recursion]] — the canonical solution relies on doubly recursive self-calls.
- [[TailRecursion]] — the outer recursion is tail-recursive and convertible to iteration.
- [[MathematicalInduction]] — the page proves correctness by induction on `step()` outcomes.
- [[RandomWalk]] — repeated success/failure steps model a one-dimensional walk.

## Contradictions
- None — reference task page.
