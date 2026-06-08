---
title: "Multisplit (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, parsing, tokenization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Multisplit
---

## Summary
The task is to split an input string using an ordered collection of multiple, potentially multi-character separators, while still recording which separators were matched and where. The key subtlety is that separator order encodes matching priority: when one separator is a prefix of another (an ambiguity), the higher-priority separator wins. This is a building block for lightweight tokenizers and parsers.

## Task Requirements
- Write a function/method that takes an input string and an ordered list of separators.
- Treat earlier separators as higher priority; on ambiguity (e.g., one separator is a prefix of another) match the highest-priority one.
- Allow separators to be reused, and return an ordered sequence of the substrings between matches (including empty strings for adjacent separators).
- Demonstrate with input `a!===b=!=c` and separators `==`, `!=`, `=`, yielding `"a", "", "b", "", "c"`.
- Extra credit: also report which separator matched at each split point and the offset in the input where it matched.

## Language Coverage
65 languages implement this task, reflecting broad coverage across functional, scripting, systems, and BASIC-family languages. Representative implementations include C, C++, C#, Java, Python, Haskell, Go, Perl, Raku, Ruby, JavaScript, and Tcl.

## Connections
- [[StringProcessing]] — core operation of dividing a string on delimiters
- [[Tokenization]] — multisplit is a minimal tokenizer producing tokens plus delimiters
- [[Parsing]] — used as a primitive in small parsing tasks
- [[GreedyMatching]] — priority-ordered, longest/highest-priority delimiter selection
- [[StringMatching]] — locating multiple candidate separators within the input

## Contradictions
- None — reference task page.
