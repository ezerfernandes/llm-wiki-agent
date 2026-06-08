---
title: "Execute HQ9+ (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, esoteric-language, interpreter]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Execute_HQ9+
---

## Summary
The task is to implement an interpreter (or compiler) for HQ9+, a deliberately minimal esoteric programming language with only four instructions. Each character of the input program is a single operation: `H` prints "Hello, world!", `Q` prints the program's own source code (a quine operation), `9` prints the full "99 Bottles of Beer" lyrics, and `+` increments an internal accumulator whose value is never observable. All other characters are ignored. The interest lies in the `Q` instruction, which forces a quine-like self-reproduction, and in `9`, which bundles an entire well-known output program into one character.

## Task Requirements
- Parse an HQ9+ source program character by character.
- `H` — output the string "Hello, world!".
- `Q` — output the entire source program text verbatim.
- `9` — output the complete lyrics of the "99 Bottles of Beer" song.
- `+` — add one to an accumulator (a register with no defined way to read it back).
- Ignore any character that is not one of the four valid instructions.

## Language Coverage
80 languages implement this task, reflecting both mainstream and esoteric ecosystems. Representative examples include C, C++, Java, Python, Haskell, Rust, Go, Ruby, Perl, and Common Lisp, alongside assembly variants (8080 Assembly, x86 Assembly) and several BASIC dialects.

## Connections
- [[EsotericProgrammingLanguage]] — HQ9+ is a canonical joke/esoteric language.
- [[Quine]] — the `Q` instruction requires reproducing the program's own source.
- [[Interpreter]] — the task is fundamentally a tiny language interpreter.
- [[99BottlesOfBeer]] — the `9` instruction emits this song's lyrics.
- [[StringProcessing]] — execution reduces to scanning and dispatching on characters.

## Contradictions
- None — reference task page.
