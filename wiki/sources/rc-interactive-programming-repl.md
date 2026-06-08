---
title: "Interactive programming (repl) (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, repl, interactive-mode, language-basics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Interactive_programming_(repl)
---

## Summary
This task asks the programmer to demonstrate a language's built-in interactive mode (a read-eval-print loop, command mode, or shell) rather than build one. The demonstration is to show how to launch that mode, then interactively define a function of two strings and a separator that returns the strings joined by two concatenated copies of the separator. The key point is that it exercises a language's REPL ergonomics for live definition and evaluation, not its parsing capabilities.

## Task Requirements
- Show how to start the language's interactive mode / REPL.
- Within that session, interactively create a function taking two strings and a separator argument.
- The function must return the two strings joined by two concatenated instances of the separator.
- Example: `f('Rosetta', 'Code', ':')` should return `'Rosetta::Code'`.
- Explicitly not about implementing one's own interactive mode — use the language's provided REPL.

## Language Coverage
107 languages implement this task, a very broad set reflecting how common interactive modes are across interpreted and even compiled ecosystems. Representative entries include Python, Ruby, Haskell, Common Lisp, Clojure, Scheme, Erlang, Julia, OCaml, Tcl, and the UNIX Shell.

## Connections
- [[ReadEvalPrintLoop]] — the core interactive evaluation cycle this task exercises
- [[StringConcatenation]] — building the result by joining strings with a doubled separator
- [[CommandLineInterpreter]] — the shell-style interface that hosts the session
- [[FunctionDefinition]] — defining a callable interactively at runtime

## Contradictions
- None — reference task page.
