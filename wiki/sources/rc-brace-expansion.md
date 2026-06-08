---
title: "Brace expansion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, parsing, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Brace_expansion
---

## Summary
The task asks the programmer to implement the brace-expansion feature popularized by Unix shells, where a string like `enable_{audio,video}` expands into the list `enable_audio`, `enable_video`. The key insight is to treat the input as a tree of nested alternations interspersed with literal text, where the output is the string-concatenating Cartesian product produced by walking the tree and descending into exactly one branch of each alternation. The hard part is parsing: handling backslash escapes and matching only "balanced" brace pairs that actually contain a comma, while leaving stray braces, commas, and comma-less brace pairs as literals.

## Task Requirements
- Write a function that performs brace expansion on any input string.
- An alternation multiplies the parent branch's alternatives n-fold, one copy per child branch alternative; sibling alternations in the same branch combine as a Cartesian product.
- Preserve all alternatives including duplicates and empty strings, ordered lexicographically with respect to the alternations.
- During parsing, an unescaped backslash escapes the next character (backslashes are passed to the output unchanged).
- Match each unescaped closing brace to the nearest unassociated unescaped opening brace; a comma binds to the innermost containing pair.
- Only brace pairs containing at least one comma form alternations; comma-less pairs, unmatched braces, and stray commas are literals.
- Demonstrate the function and pass the four given test cases.

## Language Coverage
48 languages implement this task, showing broad coverage across functional, imperative, and shell-adjacent languages. Representative implementations include Perl (the reference), Python, Haskell, Common Lisp, Rust, Go, JavaScript, C++, Raku, and Prolog.

## Connections
- [[StringProcessing]] — the task is fundamentally about parsing and transforming strings
- [[RecursiveDescentParsing]] — nested brace pairs naturally call for recursive parsing
- [[CartesianProduct]] — sibling alternations combine as a string-concatenating Cartesian product
- [[EscapeCharacter]] — backslash escaping governs which braces and commas are literal
- [[ShellExpansion]] — the feature originates in Unix shells like Bash

## Contradictions
- None — reference task page.
