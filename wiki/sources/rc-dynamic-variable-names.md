---
title: "Dynamic variable names (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, metaprogramming, reflection]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Dynamic_variable_names
---

## Summary
This task asks the programmer to create a variable whose name is supplied by the user at runtime rather than hard-coded in the program text. The key insight is that the binding between an identifier string and a storage cell must be established dynamically, which exposes how different languages treat their namespaces — some offer first-class reflection or symbol tables, while others require workarounds like hash maps, `eval`, or environment manipulation.

## Task Requirements
- Create a variable with a user-defined name.
- The variable's name must not appear literally in the program source; it is read dynamically from the user.

## Language Coverage
93 languages implement this task, spanning interpreted dynamic languages, Lisps, shells, and even some compiled and assembly-omitted environments. Representative implementations include Python, Perl, Ruby, JavaScript, Common Lisp, Tcl, Bash/UNIX Shell, PHP, R, and Racket.

## Connections
- [[Metaprogramming]] — generating program structure (variable bindings) at runtime
- [[Reflection]] — inspecting and modifying a program's own namespace
- [[SymbolTable]] — the runtime mapping of names to storage that this task manipulates
- [[Eval]] — a common mechanism for realizing dynamically named bindings
- [[EvalInEnvironment]] — the cited similar task

## Contradictions
- None — reference task page.
