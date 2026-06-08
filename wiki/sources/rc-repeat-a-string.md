---
title: "Repeat a string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Repeat_a_string
---

## Summary
This task asks the programmer to take a string and concatenate it with itself a given number of times, e.g. `repeat("ha", 5)` yields `"hahahahaha"`. The key insight is that most languages expose this through a dedicated string-multiplication operator or library function, so the interesting variation lies in how each language spells it rather than in algorithmic difficulty.

## Task Requirements
- Implement a function that repeats an arbitrary string N times and returns the concatenated result.
- Demonstrate it with the example `repeat("ha", 5)` => `"hahahahaha"`.
- Optionally show a simpler/more efficient path for repeating a single character (fill a string with one character), e.g. `repeat-char("*", 5)` => `"*****"`.

## Language Coverage
208 languages implement this task, reflecting that string repetition is a near-universal primitive. Representative solutions include Python (`"ha" * 5`), Ruby, Perl, JavaScript, C, C++, Go, Rust, Haskell, Java, and even esoteric and assembly languages such as Brainf***, Befunge, and 8080 Assembly.

## Connections
- [[StringManipulation]] — the broader category this task belongs to.
- [[StringConcatenation]] — repetition is iterated concatenation.
- [[OperatorOverloading]] — many languages overload `*` to mean string repetition.

## Contradictions
- None — reference task page.
