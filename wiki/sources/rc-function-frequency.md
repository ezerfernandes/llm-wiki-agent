---
title: "Function frequency (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, static-analysis, metaprogramming, text-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Function_frequency
---

## Summary
The task asks the programmer to display the top ten most frequently occurring functions (or identifiers/tokens) used in a program or runtime environment. The key constraint is that this is a static analysis of source code — counting how often a function appears in the program text as written, not how often it executes at runtime. Its real intent is to demonstrate self-inspection: how a language can examine its own code or environment.

## Task Requirements
- Display the ten most frequently occurring functions (or identifiers/tokens, if preferred).
- The analysis must be static: count usage in the source as written by the programmer, not runtime execution counts.
- The chosen subject should suit the language's style (a program's source, or the runtime environment).
- The exercise is meant to showcase self-inspection / introspection within the language.

## Language Coverage
30 languages implement this task. Coverage spans Lisp-family and functional languages (Common Lisp, Racket, PicoLisp, Haskell, Erlang, J), mainstream scripting languages (Python, Perl, Raku, Tcl, AWK, Julia, Nim), and lower-level or niche entries (C, Go, Forth, REXX, FreeBASIC). Approaches range from genuine reflection over the language environment to simple tokenizing-and-counting of a source file.

## Connections
- [[StaticAnalysis]] — counts function usage in source text rather than at runtime
- [[Reflection]] — languages use self-inspection to enumerate their own functions
- [[Tokenization]] — many solutions lex the source into identifiers/tokens before counting
- [[FrequencyCounting]] — tallying occurrences and selecting the top ten
- [[Metaprogramming]] — treating program text as data to be analyzed

## Contradictions
- None — reference task page.
