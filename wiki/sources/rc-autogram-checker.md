---
title: "Autogram checker (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Autogram_checker
---

## Summary
An autogram is a self-enumerating sentence that accurately inventories its own characters using spelled-out cardinal number names ("one", "two", ...). The task is to write a routine that verifies whether a given sentence is a valid autogram by parsing its claimed character counts and comparing them against the actual counts in the text. The core challenge is mapping number words back to integers and tallying characters case-insensitively while ignoring spaces and periods.

## Task Requirements
- Implement a checker that determines whether a sentence is an autogram and run it against 8 supplied test sentences.
- Ignore capitalization; never count spaces or full stops.
- Ignore punctuation in all cases except sentences 3 and 7, where commas, hyphens, apostrophes, and exclamation marks must be counted.
- For sentences 3 and 7, accept punctuation referenced by spelled-out English names ("comma", "apostrophe", "hyphen"), tolerate inconsistent apostrophe usage in count spellings, and treat "single" as a synonym for "one".
- May assume no more than 99 instances of any countable character.

## Language Coverage
15 languages implement this task, a modest set typical of niche string-puzzle tasks. Representative implementations include ALGOL 68, Crystal, Fortran, FreeBASIC, J, JavaScript, Julia, Python, Raku, Rust, and Wren.

## Connections
- [[StringProcessing]] — tallying and comparing character frequencies
- [[NumberWords]] — parsing spelled-out cardinal numbers back into integers
- [[SelfReference]] — the sentence describing its own composition
- [[FrequencyCounting]] — building a histogram of characters in the text

## Contradictions
- None — reference task page.
