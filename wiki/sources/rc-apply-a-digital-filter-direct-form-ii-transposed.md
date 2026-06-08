---
title: "Apply a digital filter (direct form II transposed) (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, digital-signal-processing, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Apply_a_digital_filter_(direct_form_II_transposed)
---

## Summary
The task asks the programmer to implement a digital filter using the "direct form II transposed" structure, a canonical realization that can represent both IIR and FIR filters while being more numerically stable than other forms. The implementation must filter a given 20-sample signal through an order-3 low-pass Butterworth filter defined by feedback coefficients `a` and feedforward coefficients `b`. The key insight is the recurrence that combines past inputs (via `b`) and past outputs (via `a`), with the output normalized by `a[0]`.

## Task Requirements
- Implement the direct form II transposed filter equation.
- Use the supplied Butterworth coefficients: `a = [1.0, -2.77555756e-16, 3.33333333e-01, -1.85037171e-17]` and `b = [0.16666667, 0.5, 0.5, 0.16666667]`.
- Apply the filter to the given 20-element input signal vector.
- Output the resulting filtered signal.

## Language Coverage
44 languages implement this task, spanning systems languages, functional languages, scientific/array languages, and BASIC dialects. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Julia, MATLAB, J, Fortran, and Common Lisp.

## Connections
- [[ButterworthFilter]] — the specific low-pass filter whose coefficients are used
- [[DigitalSignalProcessing]] — the broader field this task belongs to
- [[InfiniteImpulseResponse]] — the filter class this canonical form can represent
- [[FiniteImpulseResponse]] — the other filter class this form supports
- [[NumericalStability]] — the motivation for choosing the transposed form

## Contradictions
- None — reference task page.
