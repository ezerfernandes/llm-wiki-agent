---
title: "Balanced brackets (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, stack, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Balanced_brackets
---

## Summary
The task asks the programmer to generate a string containing N opening brackets `[` and N closing brackets `]` in arbitrary order, then determine whether that string is balanced. A string is balanced when every opening bracket has a properly nested matching closing bracket, with none mis-nested. The key insight is that this reduces to a single-pass counter (increment on `[`, decrement on `]`, fail if the count ever goes negative and require it to end at zero), the simplest case of stack-based bracket matching.

## Task Requirements
- Generate a string with exactly N opening brackets `[` and N closing brackets `]`, arranged in some arbitrary (e.g. shuffled) order.
- Determine whether the generated string is balanced — consisting entirely of correctly ordered, properly nested open/close pairs.
- Handle the edge cases shown: the empty string is OK, `[]`, `[][]`, and `[[][]]` are OK, while `][`, `][][`, and `[]][[]` are NOT OK.

## Language Coverage
158 languages implement this task, reflecting very broad coverage across paradigms — from low-level assembly to high-level functional and scripting languages. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, JavaScript, Ruby, and APL.

## Connections
- [[Stack]] — the canonical data structure for bracket matching (a depth counter suffices for a single bracket type)
- [[StringProcessing]] — the task operates by scanning a character sequence
- [[Parsing]] — balanced-bracket checking is a foundational parsing/grammar problem
- [[DyckLanguage]] — balanced bracket strings form the Dyck language, a classic context-free language

## Contradictions
- None — reference task page.
