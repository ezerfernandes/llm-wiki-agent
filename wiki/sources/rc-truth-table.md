---
title: "Truth table (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, boolean-logic, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Truth_table
---

## Summary
This task asks the programmer to read a Boolean function supplied by the user as a string, then compute and print a formatted truth table enumerating every combination of input values alongside the function's output. The key insight is that the program must parse and evaluate an arbitrary Boolean expression (in infix or reverse-polish notation) and iterate over all 2^n input assignments, so it generalizes beyond a fixed number of variables.

## Task Requirements
- Accept a Boolean function as a string from the user (input may be assumed correct).
- Calculate and print a formatted truth table for that function.
- Demonstrate output for functions of two and three input variables, while not hard-limiting the variable count.
- Either reverse-polish or infix notation expressions are acceptable.

## Language Coverage
55 languages implement this task, spanning functional, imperative, and array-oriented styles. Representative implementations include Python, Haskell, J, APL, C, C++, Rust, Java, JavaScript, Prolog, and Mathematica.

## Connections
- [[BooleanAlgebra]] — the function and its outputs are Boolean expressions
- [[ExpressionParsing]] — the string input must be parsed into an evaluable form
- [[ReversePolishNotation]] — one permitted input notation, simplifying evaluation
- [[CombinatorialEnumeration]] — all 2^n input assignments must be generated
- [[ExpressionEvaluation]] — each assignment is evaluated to produce a result

## Contradictions
- None — reference task page.
