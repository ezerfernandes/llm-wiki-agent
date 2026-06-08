---
title: "Exponentiation with infix operators in (or operating on) the base (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, operator-precedence, exponentiation, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Exponentiation_with_infix_operators_in_(or_operating_on)_the_base
---

## Summary
The task probes how a language's exponentiation operator interacts with a unary minus (and parentheses) applied to the base. The central insight is precedence: in most languages exponentiation binds tighter than unary negation, so `-x**p` parses as `-(x**p)` rather than `(-x)**p`, which changes the sign of the result for odd powers. The exercise makes those differences visible by evaluating the same numbers and powers under several syntactic groupings.

## Task Requirements
- Compute and display exponentiation where an infix operator (typically unary minus) acts in or on the base.
- Raise the values -5 and +5 to the 2nd and 3rd powers.
- Evaluate each using the expression forms `-x**p`, `-(x)**p`, `(-x)**p`, and `-(x**p)` (where the language supports them).
- Show all four (or more) symbolic expression types for each number and power.
- If the language's exponentiation operator is unusual (not `**`, `^`, or `↑`), comment on how to recognize it.

## Language Coverage
37 languages implement this task, spanning systems, scripting, functional, and array families. Representative entries include Ada, ALGOL 68, Fortran, Haskell, J, JavaScript, Julia, Perl, Python, Raku, REXX, and Wren.

## Connections
- [[OperatorPrecedence]] — exponentiation vs. unary minus binding is the crux of the task
- [[Exponentiation]] — the core arithmetic operation being demonstrated
- [[UnaryOperators]] — negation applied in or on the base
- [[ExpressionParsing]] — how infix grouping and parentheses change evaluation order

## Contradictions
- None — reference task page.
