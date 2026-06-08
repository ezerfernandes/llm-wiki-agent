---
title: "Operator precedence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-design, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Operator_precedence
---

## Summary
This task asks the programmer to document, rather than compute: produce the full table of the language's operators ordered from highest to lowest precedence, noting the associativity (left, right, or non-associative) of each level. Operators sharing a precedence level are grouped together, and the entry must also state whether function arguments are passed by value or by reference. The key insight is that precedence and associativity together determine how an unparenthesized expression is parsed into a syntax tree.

## Task Requirements
- List all operators and constructs the language uses, in descending order of precedence (higher rows bind tighter than lower rows).
- Group operators that share the same precedence level into the same cell, indicating the associativity direction for that level.
- Note that operators in the same cell are evaluated at the same precedence in the given direction (left-to-right or right-to-left).
- State whether arguments are passed by value or by reference.

## Language Coverage
99 languages implement this task, spanning C-family languages, functional and Lisp-family languages, BASIC dialects, and stack/array languages. Representative implementations include C, C++, Java, Python, Perl, Raku, Haskell, Common Lisp, Ada, and Forth (the latter being a notable case where prefix/postfix RPN evaluation makes traditional precedence largely moot).

## Connections
- [[OperatorPrecedence]] — the core ordering rule the task documents
- [[OperatorAssociativity]] — left/right binding direction within a precedence level
- [[ExpressionParsing]] — how precedence and associativity drive tree construction
- [[OrderOfOperations]] — the mathematical convention these tables encode
- [[EvaluationStrategy]] — pass-by-value vs pass-by-reference for arguments

## Contradictions
- None — reference task page.
