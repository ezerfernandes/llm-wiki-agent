---
title: "Compiler/syntax analyzer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, parsing, compilers, recursive-descent]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Compiler/syntax_analyzer
---

## Summary
This task is part of Rosetta Code's multi-stage compiler series. The goal is to write a syntax analyzer (parser) that consumes the token stream produced by the companion Lexical Analyzer task and builds an Abstract Syntax Tree (AST) for a tiny C-like language, defined by a supplied EBNF grammar. The key insight is that statement parsing uses recursive descent while expression parsing uses precedence climbing, and the resulting AST is encoded as a binary tree and emitted in a depth-first flattened form (with ";" marking null/empty nodes) so it can be round-tripped by later stages.

## Task Requirements
- Read a token stream (line/column, token name, optional value) from a file and/or stdin.
- Parse it against the given EBNF grammar covering assignment, while, if/else, print, putc, blocks, and a precedence hierarchy of binary/unary operators.
- Construct a binary-tree AST using the fixed node-type vocabulary (Identifier, String, Integer, Sequence, If, Prtc, Prts, Prti, While, Assign, Negate, Not, and the arithmetic/relational/logical operators).
- Output the AST in flattened (pre-order) form: node type per line, value for leaf nodes, ";" for null nodes.
- Handle statement lists via left-leaning Sequence nodes; support the provided test programs (e.g. while.t, prime.t) plus the shared sample programs.
- If the language offers a parser library, optionally provide both a hand-written and a library-based solution.

## Language Coverage
27 languages implement this task, a moderate breadth reflecting that it is a substantial multi-step exercise rather than a one-liner. Representative implementations include C and Python (the reference versions), Go, Rust, Java, Scala, Common Lisp, Scheme, Perl, Forth, COBOL, and Wren.

## Connections
- [[AbstractSyntaxTree]] — the binary-tree output structure the parser builds.
- [[RecursiveDescentParser]] — the technique used for statement parsing.
- [[PrecedenceClimbing]] — the algorithm used for expression and operator-precedence parsing.
- [[Compiler]] — this stage sits between lexical analysis and code generation in the pipeline.
- [[LexicalAnalysis]] — the upstream stage whose token stream is the parser's input.

## Contradictions
- None — reference task page.
