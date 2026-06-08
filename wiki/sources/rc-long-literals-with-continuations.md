---
title: "Long literals, with continuations (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, source-formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Long_literals,_with_continuations
---

## Summary
The task asks the programmer to declare a single long string literal — the space-separated English names of all named chemical elements in atomic-number order — while keeping each source line under 81 bytes. The key challenge is spreading one logical literal across many physical source lines using whatever continuation, concatenation, or abutment mechanism the language idiomatically offers, and doing so in a way that is easy for a future maintainer to extend as new elements are discovered.

## Task Requirements
- Build a long literal list of the named chemical elements, in ascending atomic-number order, excluding placeholder/"unnamed" element names.
- Restrict each program statement width to less than 81 bytes (or tighter if the language demands it); note the starting column if statements cannot begin in column one.
- The declaration may use leading/embedded/trailing blanks for readability, but the final stored list must have exactly one blank between elements and no superfluous blanks.
- Use line continuation if available, and/or demonstrate alternatives such as concatenation; comment any non-obvious continuation character.
- Respect any clause-length limit on continued statements (only if under ~4000 bytes).
- Include a variable holding the last update/revision date, and write the list so others can easily add elements.
- When run, display the revision date unambiguously, the count of elements, and the name of the last (highest) element.

## Language Coverage
45 languages implement this task, spanning fixed-column legacy languages, modern scripting languages, and assembly. Representative examples include Fortran, REXX, Ada, C++, Java, Python, Perl, Raku, Haskell, and 6502 Assembly, each illustrating its own idiom for splitting one literal across multiple source lines.

## Connections
- [[StringConcatenation]] — building one logical string from multiple literal fragments
- [[LineContinuation]] — the core mechanism for spanning a statement across source lines
- [[StringProcessing]] — normalizing the final list to single-space delimiters
- [[Tokenization]] — treating the literal as a whitespace-separated list of words

## Contradictions
- None — reference task page.
