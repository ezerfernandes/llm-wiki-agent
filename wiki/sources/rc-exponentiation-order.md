---
title: "Exponentiation order (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, operator-associativity, arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Exponentiation_order
---

## Summary
This task demonstrates how a language evaluates a chain of exponentiations such as `5**3**2` when multiple exponents are present. The key insight is operator associativity: mathematically exponentiation is right-associative, so `5**3**2` should equal `5**(3**2) = 5**9 = 1953125` rather than `(5**3)**2 = 15625`. Languages differ — some treat their exponentiation operator as right-associative (matching math), others as left-associative or report a syntax error.

## Task Requirements
- Show the language's evaluation of multiple exponentiation (integer or floating point).
- If the exponentiation operator is unusual, comment on how to recognize it.
- Print three identified lines: `5**3**2`, `(5**3)**2`, and `5**(3**2)`.
- If other methods or formats of multiple exponentiation exist, show them as well.

## Language Coverage
89 languages implement this task, spanning numeric-heavy languages, scripting languages, and functional languages. Representative implementations include Python, Perl, Raku, Haskell, Julia, J, APL, Ruby, Fortran, and Mathematica, several of which highlight differing associativity rules.

## Connections
- [[Exponentiation]] — the core operation being chained
- [[OperatorAssociativity]] — determines whether `5**3**2` groups right or left
- [[OperatorPrecedence]] — governs how the exponentiation operator binds relative to others
- [[ArbitraryPrecisionArithmetic]] — large results like 5**9 motivate bignum support

## Contradictions
- None — reference task page.
