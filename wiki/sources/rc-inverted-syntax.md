---
title: "Inverted syntax (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-syntax, conditionals]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Inverted_syntax
---

## Summary
This task asks the programmer to demonstrate "inverted syntax" — language constructs where the usual order of clauses is reversed. Two forms are illustrated: conditional expressions where the action precedes the condition (e.g. `do X if Y` instead of `if Y then do X`), and assignment where the expression precedes the target variable (e.g. `6 = a` instead of `a = 6`). The key insight is that the solution depends entirely on what each language's grammar permits, so support ranges from native statement modifiers to none at all.

## Task Requirements
- Show the traditional form of a conditional statement (condition before action) and its inverted form (action before condition).
- Show the traditional form of an assignment (variable before expression) and its inverted form (expression before variable).
- Demonstrate whichever inverted forms the language actually supports, alongside the traditional equivalents.

## Language Coverage
63 languages implement this task, spanning scripting languages, functional languages, and assembly. Languages like Perl, Raku, Ruby, and Sidef show off native statement-modifier conditionals, while Python, Java, C, C++, Go, and Haskell illustrate the more constrained traditional ordering.

## Connections
- [[StatementModifiers]] — postfix conditionals like Perl/Ruby's `action if cond`
- [[ConditionalExpression]] — the if/then construct being reordered
- [[AssignmentOperator]] — left-vs-right operand ordering in assignment
- [[SyntaxAndGrammar]] — language grammar determines which forms are legal

## Contradictions
- None — reference task page.
