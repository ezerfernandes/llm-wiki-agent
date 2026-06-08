---
title: "Parsing/Shunting-yard algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, parsing, stack, expression-evaluation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Parsing/Shunting-yard_algorithm
---

## Summary
The task asks the programmer to implement Dijkstra's shunting-yard algorithm, which converts a space-separated infix expression into Reverse Polish Notation (RPN, postfix). The key insight is that an operator stack plus precedence and associativity rules are sufficient to reorder tokens into postfix in a single left-to-right pass, without building an explicit parse tree. Solutions must trace the state of the operator stack and RPN output after each token is consumed.

## Task Requirements
- Accept a correct, space-separated infix expression of tokens.
- Produce a space-separated RPN output string.
- Respect the given precedence and associativity table: `^` (4, right), `*` and `/` (3, left), `+` and `-` (2, left).
- Handle parentheses for grouping.
- Show the operator stack and RPN output as each token is processed.
- Test with `3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3` and print the result.
- Extra credit: annotate each token-processing step with an explanatory comment. Function/argument handling is not required.

## Language Coverage
57 languages implement this task, reflecting broad coverage of a classic parsing exercise across mainstream, functional, and esoteric languages. Representative implementations include C, C++, C#, Java, Python, Go, Rust, Haskell, OCaml, Common Lisp, Ruby, and JavaScript.

## Connections
- [[ShuntingYardAlgorithm]] — the named algorithm this task implements, due to Edsger Dijkstra.
- [[ReversePolishNotation]] — the postfix output format produced from infix input.
- [[StackDataStructure]] — the operator stack that drives the conversion.
- [[OperatorPrecedence]] — precedence and associativity rules that determine output ordering.
- [[ExpressionParsing]] — the broader problem class of turning textual expressions into evaluable form.

## Contradictions
- None — reference task page.
