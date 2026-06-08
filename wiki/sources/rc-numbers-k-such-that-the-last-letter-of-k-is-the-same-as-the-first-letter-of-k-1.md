---
title: "Numbers k such that the last letter of k is the same as the first letter of k+1 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numbers_k_such_that_the_last_letter_of_k_is_the_same_as_the_first_letter_of_k+1
---

## Summary
The task asks the programmer to find non-negative integers k whose English-language name ends in the same letter that the name of k+1 begins with. For example, 18 ("eighteen") qualifies because it ends in 'n' and 19 ("nineteen") starts with 'n'. The core work is a robust integer-to-English-words converter combined with a simple letter-comparison filter; this is OEIS sequence A363659, originating from a GCHQ puzzle.

## Task Requirements
- Find and show the first 50 qualifying numbers.
- Report the 1,000th and 10,000th qualifying numbers.
- Show the breakdown by final digit for the first 1,000 and 10,000 qualifying numbers (numeric and/or graphical).
- Use canonical English names: 'zero' (not 'nought'), 'one hundred'/'one thousand' (not 'a hundred'/'a thousand').
- Stretch: find the 100,000th and millionth qualifying numbers and their final-digit breakdowns.

## Language Coverage
14 languages implement this task, a moderate spread across systems, scripting, and array/functional languages. Representative implementations include ALGOL 68, C++, Java, Julia, Nim, Perl, Python, Raku, J, jq, Phix, and Wren.

## Connections
- [[NumberNames]] — depends on an integer-to-English-words converter
- [[StringProcessing]] — comparing the first and last characters of generated names
- [[NumberTheory]] — generates an integer sequence (OEIS A363659)
- [[SequenceGeneration]] — enumerating and indexing qualifying terms

## Contradictions
- None — reference task page.
