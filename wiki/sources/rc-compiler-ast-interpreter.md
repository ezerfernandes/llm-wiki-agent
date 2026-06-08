---
title: "Compiler/AST interpreter (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, interpreters, compilers, tree-traversal]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Compiler/AST_interpreter
---

## Summary
This task asks the programmer to build an AST interpreter: a tree-walking
evaluator that consumes the flattened Abstract Syntax Tree produced by the
companion Syntax Analyzer task and executes it directly. The core insight is
that interpretation reduces to a single recursive `interp(node)` function that
dispatches on node type, recursing into children and returning their evaluated
values. It is one stage in a multi-part compiler pipeline (lexer to parser to
interpreter / code generator / virtual machine).

## Task Requirements
- Reconstruct the AST from the parser's serialized output: read line by line, where the first token is the node type, a terminal node is `;` (NULL), a two-token line is a leaf (Identifier, Integer, or String) with the second token as its value, and otherwise recursively read a left and right subtree.
- Implement a recursive `interp(x)` that dispatches on node type: Integer/String return their value, Ident returns the current variable value, Assign stores into a global, binary and unary operators evaluate their operands, and `If`, `While`, `Prtc`, `Prti`, `Prts`, and `Sequence` implement control flow and printing.
- Use C-like division and modulus semantics: results truncate toward zero (3/2 = 1, 3/-2 = -1).
- No semantic analysis is required given the tiny language; the interpreter must pass the bundled prime-number test program and the additional sample programs.

## Language Coverage
24 languages implement this task, a moderate spread reflecting that it is part of a specialized multi-stage compiler series rather than a casual one-off. Representative implementations include C and Python (the reference versions), Java, Go, Rust, Kotlin, Scala, Scheme, Perl, and Forth.

## Connections
- [[AbstractSyntaxTree]] — the input data structure being interpreted
- [[TreeWalkingInterpreter]] — the evaluation strategy this task embodies
- [[Recursion]] — the dispatch function recurses over child nodes
- [[CompilerPipeline]] — sits between the syntax analyzer and the code generator / virtual machine stages
- [[SyntaxAnalysis]] — the upstream task that produces the serialized AST

## Contradictions
- None — reference task page.
