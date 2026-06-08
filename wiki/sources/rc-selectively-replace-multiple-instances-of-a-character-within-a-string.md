---
title: "Selectively replace multiple instances of a character within a string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Selectively_replace_multiple_instances_of_a_character_within_a_string
---

## Summary
This task asks the programmer to perform position-aware character replacement within a string: rather than replacing every occurrence of a character, only specific numbered occurrences are substituted. The key insight is that the replacement targets the *Nth* instance of a given character, so the solution must count occurrences as it scans rather than doing a blind global replace.

## Task Requirements
- Start with the string `"abracadabra"`.
- Replace the 1st 'a' with 'A', the 2nd 'a' with 'B', the 4th 'a' with 'C', the 5th 'a' with 'D'.
- Replace the 1st 'b' with 'E'.
- Replace the 2nd 'r' with 'F'.
- Leave the 3rd 'a', the 2nd 'b', and the 1st 'r' untouched.
- The result must be `"AErBcadCbFD"`.

## Language Coverage
40 languages implement this task, spanning systems languages, scripting languages, and stream editors. Representative implementations include C, C++, Java, JavaScript, Python, Haskell, Julia, Perl, Raku, Ruby, Go, and even the line editor `ed` and the stream editor `sed`.

## Connections
- [[StringManipulation]] — the task is a string-processing exercise
- [[StringIndexing]] — replacements are keyed to positional (Nth) occurrences
- [[CharacterMapping]] — each (char, occurrence) pair maps to a substitute character

## Contradictions
- None — reference task page.
