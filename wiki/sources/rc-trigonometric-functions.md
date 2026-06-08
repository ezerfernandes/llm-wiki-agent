---
title: "Trigonometric functions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, trigonometry, mathematics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Trigonometric_functions
---

## Summary
This task asks the programmer to demonstrate a language's trigonometry support by showing sine, cosine, and tangent along with their inverses (arcsine, arccosine, arctangent). The key constraint is unit awareness: the regular functions must be called with a radian argument and an equivalent degree argument that evaluate to the same angle, and the inverse functions take a single value and present the result converted to both radians and degrees. If a language lacks built-in trig functions, the programmer must implement them from a known series approximation or identity.

## Task Requirements
- Show examples of sine, cosine, tangent and their inverses.
- For regular functions, pass arguments in radians and in degrees that represent the same angle (e.g., the radian value alongside its degree equivalent multiplied by pi/180).
- The two calls within a single function must use the same angle, but different functions may use different angles.
- For inverse functions, use the same input number and convert the answer to both radians and degrees.
- If trig functions are missing, implement them via a known approximation or trigonometric identity.

## Language Coverage
116 languages implement this task, a very broad cross-section spanning systems, scripting, functional, and math-oriented languages. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Fortran, MATLAB, Julia, R, Perl, and Wren.

## Connections
- [[Trigonometry]] — the mathematical domain the task exercises
- [[RadiansAndDegrees]] — angle unit conversion is central to the requirements
- [[TaylorSeries]] — typical fallback for implementing sine/cosine without a built-in
- [[InverseTrigonometricFunctions]] — arcsine, arccosine, arctangent
- [[FloatingPointArithmetic]] — precision concerns when evaluating these functions

## Contradictions
- None — reference task page.
