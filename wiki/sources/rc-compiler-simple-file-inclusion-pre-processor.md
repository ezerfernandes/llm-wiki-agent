---
title: "Compiler/Simple file inclusion pre processor (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, text-processing, compiler]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Compiler/Simple_file_inclusion_pre_processor
---

## Summary
The task asks the programmer to implement a minimal file-inclusion pre-processor for their own language, in that language. Given a source file, the program scans for inclusion directives (such as C's `#include`, PL/1's `%include`, or COBOL's `COPY`) and emits a new source file where each directive is replaced by the literal contents of the referenced file. The key insight is that this is purely a text-processing exercise: validity of the resulting source is the compiler's concern, not the pre-processor's.

## Task Requirements
- Read a source file (from a file or standard input) and write an output source file (to a file or standard output).
- Replace each file-inclusion directive with the verbatim contents of the named file.
- Use the inclusion syntax standard for your language; if none exists, adopt a popular compiler's convention or invent one (e.g. C-style `#include`, avoiding `#` where it begins a comment).
- State the accepted syntax and any limitations, including whether nested includes are supported and the maximum nesting depth.
- Nested inclusion (an included file containing further directives) is optional; macro expansion and conditional compilation are explicitly not required.

## Language Coverage
12 languages implement this task, spanning interpreted, compiled, and array/stack paradigms. Representative entries include ALGOL 68, AWK, C, FreeBASIC, J, Julia, Perl, Phix, Raku, REXX, and Wren.

## Connections
- [[TextProcessing]] — the core operation of scanning and rewriting source text
- [[FileInclusion]] — the language facility being reproduced
- [[Preprocessor]] — the compilation phase this task models
- [[Recursion]] — the mechanism used when nested includes are supported

## Contradictions
- None — reference task page.
