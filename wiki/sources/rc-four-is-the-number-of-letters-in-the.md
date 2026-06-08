---
title: "Four is the number of letters in the ... (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, self-referential-sequence, number-spelling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Four_is_the_number_of_letters_in_the_...
---

## Summary
This task implements a self-referential, never-ending sentence that describes itself: "Four is the number of letters in the first word of this sentence, two in the second, three in the third, ...". Each term of the resulting integer sequence is the count of Latin letters in the corresponding word of the sentence, where the letter counts are themselves spelled out in English (e.g. "four", "two", "three") and woven back into the sentence. The key insight is that the sentence must be generated lazily, building only as many words as are needed, because spelling out a count word adds new words whose own letters must later be counted.

## Task Requirements
- Provide a function that returns the sequence of letter counts for the first N words of the never-ending sentence, plus a driver routine to invoke it.
- Spell numbers in English using the short scale (2,000,000,000 = two billion), with no "and" in number names.
- Count only upper- and lowercase Latin letters (A-Z, a-z); commas and hyphens are not counted; hyphenated forms like "twenty-three" (11 letters) count as one word.
- Construct only as much of the sentence as needed.
- Show the letter count and the word itself for the Nth word, and after each test case report the total character count (including blanks, commas, punctuation) of the constructed sentence.
- Test cases: display the first 201 sequence terms, then the count/word for the 1,000th, 10,000th, 100,000th, 1,000,000th, and optionally 10,000,000th words.

## Language Coverage
18 languages implement this task, spanning systems, scripting, and functional styles. Representative implementations include C, C++, Rust, Go, Java, Kotlin, Haskell, Python, Perl, Raku, Julia, and REXX.

## Connections
- [[SelfReferentialSequence]] — the sentence describes its own structure
- [[NumberToWords]] — spelling integers in English is the core subroutine
- [[LazyEvaluation]] — the sentence is built incrementally, only as far as needed
- [[StringProcessing]] — letter counting excludes commas and hyphens
- [[OEIS]] — corresponds to OEIS sequence A072425

## Contradictions
- None — reference task page.
