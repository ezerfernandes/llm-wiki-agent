---
title: "Quine (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, self-reference, metaprogramming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Quine
---

## Summary
A quine is a self-referential program that outputs its own complete source code without reading any external file. Named after logician Willard Van Orman Quine, the classic technique splits the program into two identical halves — one as live code and one quoted as a string or data literal — where the code prints the quoted part twice, once unquoted and once re-quoted. The central challenge is handling quoting and escaping (quotation marks, backslashes, newlines) so the reproduced output matches the original exactly.

## Task Requirements
- Write a program that outputs its own source code with no external file access.
- Achieve self-reference; trivial constant expressions printed by a top-level interpreter are disallowed, and empty programs producing no output are not allowed.
- Optionally add a variant that accesses the code directly if the language permits.
- Cope with quoting difficulties: escaping quote characters, embedding or escaping newlines, and reproducing the string literal faithfully (e.g. via a source-representation function, constructing the quote from its ASCII code 34 or 39, or writing the whole program on one line).

## Language Coverage
187 languages implement this task, an exceptionally broad spread that includes esoteric and minimalist languages where quines are a signature puzzle. Representative implementations include C, Python, Haskell, Lisp, JavaScript, Ruby, Brainf***, Befunge, Unlambda, and Whitespace.

## Connections
- [[SelfReference]] — the program embeds and reproduces its own description.
- [[Metaprogramming]] — code that treats its own source text as data.
- [[FixedPointCombinator]] — Kleene's recursion theorem guarantees quines exist for any sufficiently powerful language.
- [[StringEscaping]] — the core practical difficulty of quoting quotes and newlines.
- [[Homoiconicity]] — Lisp-family languages exploit code-as-data structure for trivial quines.

## Contradictions
- None — reference task page.
