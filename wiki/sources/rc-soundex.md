---
title: "Soundex (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, phonetic-algorithm]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Soundex
---

## Summary
Soundex is a phonetic indexing algorithm that encodes words by pronunciation so homophones map to the same code, letting names with minor spelling differences match. The task is to implement the encoder, which produces a code of the first letter followed by three digits derived from the remaining consonants. The key subtlety is correctly handling consonants that share a code when separated by vowels versus by "H" or "W".

## Task Requirements
- Encode a word so that homophones produce the same representation, following the official US National Archives soundex rules.
- Keep the first letter, then map subsequent consonants to digit codes, collapsing adjacent duplicates.
- If a vowel (A, E, I, O, U) separates two consonants with the same code, code the consonant to the right of the vowel (e.g., Tymczak -> T-522).
- If "H" or "W" separates two consonants with the same code, do not code the consonant to the right (e.g., Ashcraft -> A-261, not A-226).
- Validate against test cases such as Ashcraft -> A-261.

## Language Coverage
86 languages implement this task, spanning systems and scripting languages to functional and legacy/mainframe environments. Representative examples include C, C++, Java, Python, Perl, Haskell, Go, Rust, Ruby, and REXX.

## Connections
- [[StringProcessing]] — operates on characters and substitution mapping
- [[PhoneticAlgorithm]] — soundex is a foundational phonetic matching scheme
- [[HashingAndIndexing]] — produces a fixed-length index key for lookup/matching
- [[StringSimilarity]] — used to match approximately-equal homophones

## Contradictions
- None — reference task page.
