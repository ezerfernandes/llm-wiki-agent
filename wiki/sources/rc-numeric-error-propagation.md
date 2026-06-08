---
title: "Numeric error propagation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, operator-overloading]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numeric_error_propagation
---

## Summary
The task asks the programmer to build an "uncertain number" type that carries a value together with an associated uncertainty (standard error), and to define arithmetic on it. The key insight is that errors combine differently per operation: errors add in quadrature for addition/subtraction, while relative errors add in quadrature for multiplication/division, and exponentiation scales the relative error by the exponent. The demonstration computes the Pythagorean distance between two error-bearing points and reports the propagated uncertainty.

## Task Requirements
- Add an uncertain-number type supporting addition, subtraction, multiplication, division, and exponentiation, mixing uncertain numbers with plain floats.
- Implement the propagation rules: f = a ± c gives σf = σa; f = a ± b gives σf² = σa² + σb²; f = ca gives σf = |cσa|; f = ab or a/b gives σf² = f²((σa/a)² + (σb/b)²); f = aᶜ gives σf = |fc(σa/a)|.
- Given x1 = 100 ± 1.1, y1 = 50 ± 1.2, x2 = 200 ± 2.2, y2 = 100 ± 2.3, compute the distance d = √((x1−x2)² + (y1−y2)²).
- Print both d and its propagated error.
- Assumption: a and b are independent (the multiplication rule must not be applied to a*a).

## Language Coverage
36 languages implement this task, spanning systems and functional languages well-suited to operator overloading and numeric record types. Representative implementations include Ada, C++, Common Lisp, D, F#, Haskell, Java, Julia, Python, Racket, Raku, and Wren.

## Connections
- [[ErrorPropagation]] — the core statistical technique the task models.
- [[OperatorOverloading]] — how most implementations expose arithmetic on the uncertain type.
- [[PythagoreanTheorem]] — the distance formula used in the demonstration.
- [[Quaternion type]] — related task building a custom numeric type with overloaded operators.

## Contradictions
- None — reference task page.
