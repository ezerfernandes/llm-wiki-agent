---
title: "Arithmetic evaluation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, parsing, recursion, interpreters]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Arithmetic_evaluation
---

## Summary
The task asks the programmer to write a program that parses and evaluates arithmetic expressions given as strings like "(1+3)*7". The key constraint is that parsing must produce an abstract syntax tree (AST), and evaluation must walk that tree rather than delegating to the host language's `eval`. This forces the implementer to confront tokenizing, operator precedence, and tree-walking evaluation directly.

## Task Requirements
- Parse the input expression into an abstract syntax tree (AST).
- Evaluate by traversing the AST, not via `eval` or equivalent language features.
- Accept the expression as a string or list of symbols (e.g. "(1+3)*7").
- Support the four binary operators `+ - * /` with conventional precedence.
- Honor precedence-control parentheses.
- Apply standard precedence: parentheses first, then multiplication/division (left to right), then addition/subtraction (left to right).

## Language Coverage
74 languages implement this task, spanning functional, object-oriented, logic, and BASIC-family languages. Representative implementations include C, C++, Java, Python, Haskell, OCaml, Common Lisp, Prolog, Rust, Go, Scheme, and Perl.

## Connections
- [[AbstractSyntaxTree]] — the parsed representation the task requires building and evaluating.
- [[RecursiveDescentParsing]] — common technique for handling precedence and parentheses.
- [[OperatorPrecedence]] — the precedence rules the parser must encode.
- [[TreeWalkingInterpreter]] — the evaluation strategy of traversing the AST.
- [[Tokenization]] — splitting the input string into operands, operators, and parentheses.

## Contradictions
- None — reference task page.
