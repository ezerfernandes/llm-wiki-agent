---
title: "CUSIP (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, checksum, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/CUSIP
---

## Summary
A CUSIP is a nine-character alphanumeric code identifying a North American financial security. The task is to validate that the final character (the check digit) of a given CUSIP is correct. The check digit is derived from the first eight characters using a positional weighting and digit-summing scheme, similar to the Luhn algorithm.

## Task Requirements
- Implement a check-digit validation routine over the first 8 characters of a CUSIP.
- Map each character to a numeric value: digits keep their value, letters use ordinal position + 9 (A=10), `*`=36, `@`=37, `#`=38.
- Double the value of characters at even positions, then add the tens and units digits of each value to a running sum.
- Compute the check digit as `(10 - (sum mod 10)) mod 10` and compare it to the 9th character.
- Validate the six provided test cases (Apple, Cisco, Google, Microsoft, and two Oracle codes — one correct, one incorrect).

## Language Coverage
78 languages implement this task, spanning mainstream, functional, and legacy systems. Representative implementations include C, C++, Python, Java, JavaScript, Go, Rust, Haskell, Perl, and REXX.

## Connections
- [[Checksum]] — the task is categorized under checksum algorithms.
- [[LuhnAlgorithm]] — the doubling-and-digit-sum technique mirrors Luhn.
- [[CheckDigit]] — the core concept being validated.
- [[SEDOL]] — related security-identifier validation task.
- [[ISIN]] — related international securities identifier with its own check digit.

## Contradictions
- None — reference task page.
