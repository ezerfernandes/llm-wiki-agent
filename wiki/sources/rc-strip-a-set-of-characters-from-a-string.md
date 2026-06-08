---
title: "Strip a set of characters from a string (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Strip_a_set_of_characters_from_a_string
---

## Summary
The task asks the programmer to write a `stripchars` function that removes every occurrence of any character in a given set from an input string. It takes two arguments — the source string and a string whose characters define the set to delete — and returns the source with all set members filtered out. The key insight is treating the second argument as a membership set rather than a substring to match.

## Task Requirements
- Define a function taking two arguments: the string to strip and a string of characters to remove.
- Return the first string with every character that appears in the second argument removed (regardless of position or count).
- Example: `stripchars("She was a soul stripper. She took my heart!", "aei")` yields `"Sh ws  soul strppr. Sh took my hrt!"`.

## Language Coverage
151 languages implement this task, reflecting very broad coverage as a fundamental string-manipulation exercise. Representative implementations include Python, C, C++, Java, JavaScript, Haskell, Ruby, Rust, Perl, Go, and Common Lisp.

## Connections
- [[StringProcessing]] — core domain of the task
- [[SetMembership]] — characters to remove form a lookup set
- [[CharacterFiltering]] — selectively dropping elements that satisfy a predicate
- [[HigherOrderFunctions]] — many solutions use filter/comprehension over a membership test

## Contradictions
- None — reference task page.
