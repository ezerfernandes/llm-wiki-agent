---
title: "Undulating numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digits, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Undulating_numbers
---

## Summary
An undulating number in a given base has the repeating digit pattern ABABAB... where A and B are digits. For this task a number must have at least 3 digits and the two alternating digits must differ (A != B), excluding trivial repdigits like 111. The key insight is that undulating numbers can be generated directly by choosing the leading digit A and alternating digit B rather than scanning every integer, and the property is base-dependent — a number undulating in base 7 generally is not undulating when written in base 10.

## Task Requirements
- For base 10: list all three-digit undulating numbers.
- List all four-digit undulating numbers.
- List all three-digit undulating numbers that are prime.
- Find the 600th undulating number.
- Count how many undulating numbers are below 2^53, and report the largest such number.
- Bonus: repeat the analysis for base 7, expressing results in base 10 except items 4 and 5, which should also be shown in base 7.

## Language Coverage
20 languages implement this task, spanning systems and array languages alongside scripting and BASIC dialects. Representative implementations include ALGOL 68, C++, Java, Julia, Nim, Perl, Python, Raku, Rust, and Wren.

## Connections
- [[NumberTheory]] — the task studies a digit-pattern property of integers.
- [[PositionalNotation]] — undulation is defined relative to a chosen base.
- [[PrimalityTesting]] — one subtask filters undulating numbers for primes.
- [[OEIS]] — corresponds to sequence A046075, non-trivial undulants.
- [[BaseConversion]] — the bonus requires representing values in base 7 and base 10.

## Contradictions
- None — reference task page.
