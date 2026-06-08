---
title: "Roots of unity (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, complex-numbers, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Roots_of_unity
---

## Summary
This task asks the programmer to compute the n-th roots of unity for a given integer n, that is, all complex numbers z satisfying z^n = 1. The key insight is that these roots are evenly spaced points on the unit circle in the complex plane, given by e^(2*pi*i*k/n) for k = 0, 1, ..., n-1. The task is primarily an exercise in working with complex numbers and the exponential/trigonometric form of complex values.

## Task Requirements
- Given an integer n, find all n n-th roots of unity.
- Each root is the complex number cos(2*pi*k/n) + i*sin(2*pi*k/n) for k from 0 to n-1.
- Demonstrate the computation, typically printing the roots for several small values of n.

## Language Coverage
81 languages implement this task, reflecting how commonly complex-number arithmetic is exercised across both general-purpose and mathematical languages. Representative implementations include C, C++, C#, Java, Python, Haskell, Julia, Rust, Go, MATLAB, and Mathematica/Wolfram Language.

## Connections
- [[ComplexNumbers]] — the roots live in the complex plane and require complex arithmetic
- [[EulersFormula]] — roots are computed via e^(2*pi*i*k/n) = cos + i*sin
- [[UnitCircle]] — all n roots are equally spaced points on the unit circle
- [[NumberTheory]] — roots of unity underpin cyclotomic and modular structure

## Contradictions
- None — reference task page.
