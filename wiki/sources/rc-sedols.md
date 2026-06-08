---
title: "SEDOLs (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, checksum, string-processing, finance]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/SEDOLs
---

## Summary
The task asks the programmer to compute and append the trailing check digit for a list of 6-character SEDOL codes (Stock Exchange Daily Official List identifiers used in the UK). Each of the first six characters is converted to a numeric value, multiplied by a fixed positional weight, summed, and the check digit is the amount needed to round the weighted sum up to the next multiple of 10. The key insight is the character-to-value mapping (digits map to themselves, letters A=10 through Z=35) combined with the weight vector [1, 3, 1, 7, 3, 9].

## Task Requirements
- Read a list of 6-digit/character SEDOL strings.
- For each one, calculate the checksum digit and append it to produce the full 7-character SEDOL.
- Produce output matching the expected results for the given sample input.
- Extra credit: validate that each input is well-formed, in particular rejecting invalid characters (vowels are not permitted in SEDOLs).

## Language Coverage
94 languages implement this task, reflecting broad coverage across mainstream and niche languages. Representative implementations include Python, C, C++, Java, Haskell, Rust, Go, Perl, Ruby, and COBOL.

## Connections
- [[Checksum]] — the core operation, a weighted modular check digit.
- [[ModularArithmetic]] — the check digit is derived via arithmetic modulo 10.
- [[LuhnTest]] — a related check-digit algorithm referenced by the task.
- [[ISIN]] — related securities-identifier task that embeds checksum validation.
- [[StringProcessing]] — character-by-character mapping and validation of fixed-width codes.

## Contradictions
- None — reference task page.
