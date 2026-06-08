---
title: "Church numerals (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, lambda-calculus, functional-programming, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Church_numerals
---

## Summary
The task asks the programmer to implement Church numerals, an encoding from lambda calculus where the natural number N is represented as a higher-order function that applies its first argument (a function f) exactly N times to its second argument (a value x). The key insight is that all of arithmetic can be expressed purely through function composition, with no built-in integers: zero applies f zero times, and the successor adds one more application. This is a classic demonstration of representing data and operations using only functions.

## Task Requirements
- Define Church Zero (a function that ignores f and returns the identity on x).
- Define a Church successor function that produces the next numeral in the series.
- Define functions for addition, multiplication, and exponentiation over Church numerals.
- Provide a function converting an integer to its corresponding Church numeral, and one converting a Church numeral back to an integer.
- Derive Church 3 and Church 4 from Zero and successor.
- Compute the sum and product of Church 3 and Church 4, plus 4^3 and 3^4, using Church arithmetic.
- Convert each result back to an integer and print it.

## Language Coverage
48 languages implement this task, with strong representation from functional and Lisp-family languages well suited to higher-order functions, including Haskell, OCaml, F#, Common Lisp, Clojure, Scheme/Racket, JavaScript, Python, and even pure Lambda Calculus and Binary Lambda Calculus entries.

## Connections
- [[LambdaCalculus]] — Church numerals originate as a numeral encoding within lambda calculus
- [[ChurchEncoding]] — the general scheme of representing data as functions
- [[HigherOrderFunctions]] — numerals and arithmetic operators are all functions taking functions
- [[FunctionComposition]] — successor and arithmetic are built by composing applications of f
- [[NaturalNumbers]] — the values being modeled

## Contradictions
- None — reference task page.
