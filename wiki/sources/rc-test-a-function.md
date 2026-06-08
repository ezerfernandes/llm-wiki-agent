---
title: "Test a function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, testing, software-engineering]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Test_a_function
---

## Summary
This task asks the programmer to use a well-known, language-idiomatic testing library, module, or suite to write tests for their language's solution to the [[Palindrome]] task. The point is not the palindrome logic itself but demonstrating each language's established unit-testing toolchain and conventions. If a language lacks a community-standard testing framework, the entry should say so or be omitted.

## Task Requirements
- Pick the testing framework that is well known and idiomatic to the language's community.
- Write some tests against the language's existing entry in the Palindrome task.
- Cover both positive cases (strings that are palindromes) and negative cases (strings that are not).
- If no well-known testing library exists for the language, state that explicitly or omit the language.

## Language Coverage
71 languages implement this task, spanning everything from functional and Lisp dialects to scripting and systems languages, each showcasing its native test harness. Representative examples include Python (unittest), Java (JUnit), Ruby (Test::Unit/MiniTest), Rust (built-in `#[test]`), Go (the `testing` package), Haskell (HUnit/QuickCheck), Tcl (tcltest), Perl, Clojure, and Scala (ScalaTest).

## Connections
- [[Palindrome]] — the function under test
- [[UnitTesting]] — the core software-engineering practice being demonstrated
- [[TestDrivenDevelopment]] — the broader methodology these frameworks support
- [[Assertion]] — the primitive used to express test expectations
- [[StringProcessing]] — domain of the palindrome check itself

## Contradictions
- None — reference task page.
