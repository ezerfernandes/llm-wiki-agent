---
title: "Idiomatically determine all the lowercase and uppercase letters (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, character-encoding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Idiomatically_determine_all_the_lowercase_and_uppercase_letters
---

## Summary
This task asks the programmer to display the full set of lowercase (a–z) and uppercase (A–Z) Latin/English letters that the programming language considers valid, doing so idiomatically rather than by hardcoding a literal string. The key insight is that the solution should work regardless of the underlying character encoding (ASCII, EBCDIC, or other), so it must rely on the language's own character-classification facilities instead of assuming contiguous code points.

## Task Requirements
- Display the set of all lowercase letters and the set of all uppercase letters usable by the program.
- A letter is defined as a member of the Latin (English) alphabet: a → z and A → Z.
- The method must find the letters regardless of hardware architecture / character encoding (ASCII, EBCDIC, etc.).
- Optionally mention the hardware architecture and operating system in use.

## Language Coverage
59 languages implement this task, spanning systems and assembly languages, scripting languages, and functional languages — representative examples include C, Rust, Go, Java, Python, Haskell, Common Lisp, Ruby, Perl, COBOL, and 8080 Assembly.

## Connections
- [[CharacterEncoding]] — the task hinges on not assuming ASCII vs EBCDIC code-point layouts
- [[StringProcessing]] — building and displaying alphabet sets
- [[ASCII]] — the most common encoding the idiom must remain independent of
- [[CharacterClassification]] — using library predicates like isupper/islower instead of literals

## Contradictions
- None — reference task page.
