---
title: "Binary Lambda Calculus (programming language)"
type: entity
tags: [programming-language, rosetta-code]
date: 2026-05-31
rc_category: "Category:Binary Lambda Calculus"
rc_task_entries: 51
rc_tasks_done_pct: "2.94%"
wiki_tasks_solved: 57
---

## Summary
Binary Lambda Calculus (BLC) is a purely functional, untyped language designed by John Tromp around 2004 as a concrete binary encoding of the pure lambda calculus, intended to define the smallest possible universal machine and a rigorous basis for measuring algorithmic information content (Kolmogorov complexity). Programs are bit strings: lambda abstraction and application are encoded with short prefix codes (00 and 01) while variables are written in unary De Bruijn index notation (1...10), so a complete self-interpreter fits in a few hundred bits. Evaluation follows the standard normal-order beta-reduction semantics of the lambda calculus, with input and output handled as lazy lists of bits, and there is no type system or primitive data—everything from booleans to numbers is Church/Scott encoded. It is used almost exclusively in theoretical computer science and code-golf contexts, as a minimalist demonstration of universal computation and for studying the information-theoretic size of programs rather than for practical software development.

## Rosetta Code Coverage
Solves **57** of the wiki's 1350 ingested Rosetta Code tasks. Rosetta Code's popularity ranking credits **Binary Lambda Calculus** with **51** task entries (2.94% of all tasks).

## Tasks Solved
- [[rc-100-doors]]
- [[rc-a-b]]
- [[rc-ackermann-function]]
- [[rc-apply-a-callback-to-an-array]]
- [[rc-array-concatenation]]
- [[rc-array-length]]
- [[rc-binary-digits]]
- [[rc-bitwise-io]]
- [[rc-boolean-values]]
- [[rc-call-a-function]]
- [[rc-catamorphism]]
- [[rc-church-numerals]]
- [[rc-comments]]
- [[rc-conditional-structures]]
- [[rc-copy-a-string]]
- [[rc-copy-stdin-to-stdout]]
- [[rc-currying]]
- [[rc-documentation]]
- [[rc-empty-program]]
- [[rc-empty-string]]
- [[rc-ethiopian-multiplication]]
- [[rc-even-or-odd]]
- [[rc-execute-brain]]
- [[rc-factorial]]
- [[rc-fibonacci-sequence]]
- [[rc-function-composition]]
- [[rc-function-definition]]
- [[rc-generic-swap]]
- [[rc-hailstone-sequence]]
- [[rc-halt-and-catch-fire]]
- [[rc-hello-world-newbie]]
- [[rc-hello-world-newline-omission]]
- [[rc-hello-world-text]]
- [[rc-higher-order-functions]]
- [[rc-hilbert-curve]]
- [[rc-logical-operations]]
- [[rc-loops-for]]
- [[rc-loops-infinite]]
- [[rc-mutual-recursion]]
- [[rc-quine]]
- [[rc-quoting-constructs]]
- [[rc-return-multiple-values]]
- [[rc-reverse-a-string]]
- [[rc-shell-one-liner]]
- [[rc-sieve-of-eratosthenes]]
- [[rc-sorting-algorithms-insertion-sort]]
- [[rc-sorting-algorithms-merge-sort]]
- [[rc-special-characters]]
- [[rc-string-append]]
- [[rc-string-prepend]]
- [[rc-terminal-control-ringing-the-terminal-bell]]
- [[rc-thue-morse]]
- [[rc-universal-lambda-machine]]
- [[rc-variadic-fixed-point-combinator]]
- [[rc-write-language-name-in-3d-ascii]]
- [[rc-y-combinator]]
- [[rc-zero-to-the-zero-power]]

## Connections
- [[RosettaCode]] — tasks sourced from the Rosetta Code project
