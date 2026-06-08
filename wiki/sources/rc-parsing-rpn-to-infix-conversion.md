---
title: "Parsing/RPN to infix conversion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, parsing, expression-trees, stack]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Parsing/RPN_to_infix_conversion
---

## Summary
The task asks the programmer to convert a Reverse Polish Notation (postfix) expression, given as a space-separated token string, back into equivalent infix notation. The core insight is to use a stack of partial subexpressions: each operand is pushed as a leaf, and each operator pops its two operands and combines them, inserting parentheses only when a child's operator binds more loosely than the parent (accounting for precedence and associativity) to keep the output minimally and correctly parenthesized.

## Task Requirements
- Accept a correct, space-separated string of RPN tokens as input.
- Produce a space-separated infix-notation string representing the same expression.
- Show how the program's main data structure (the stack) changes as each token is parsed.
- Respect the given operator precedence/associativity: `^` (precedence 4, right-associative), `*` and `/` (precedence 3, left), `+` and `-` (precedence 2, left).
- Test with `3 4 2 * 1 5 - 2 3 ^ ^ / +` → `3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3` and `1 2 + 3 4 + ^ 5 6 + ^` → `( ( 1 + 2 ) ^ ( 3 + 4 ) ) ^ ( 5 + 6 )`.

## Language Coverage
44 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative entries include C, C++, C#, Java, Python, Haskell, Common Lisp, Go, Ruby, Perl, Raku, and Tcl.

## Connections
- [[ReversePolishNotation]] — the postfix input form being converted.
- [[InfixNotation]] — the target output form.
- [[Stack]] — the central data structure holding partial subexpressions.
- [[OperatorPrecedence]] — governs when parentheses are required around subexpressions.
- [[ShuntingYardAlgorithm]] — the inverse direction (infix to RPN).

## Contradictions
- None — reference task page.
