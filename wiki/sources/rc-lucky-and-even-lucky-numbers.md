---
title: "Lucky and even lucky numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sieve, cli]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Lucky_and_even_lucky_numbers
---

## Summary
The task asks the programmer to generate "lucky numbers" and "even lucky numbers" using a sieve-like elimination process. Starting from all odd integers (lucky) or all even integers (even lucky), one repeatedly notes the n-th surviving value m and then discards every m-th element of the remaining list, advancing n each round. The key insight is that the survival rule depends on the dynamically shrinking list itself, much like the Sieve of Eratosthenes but using positional counts rather than divisibility.

## Task Requirements
- Write one or two functions to generate lucky numbers and even lucky numbers via the elimination sieve.
- Build a command-line interface selecting the kind of numbers and which one(s) to show.
- Validate common CLI errors: missing arguments, too many arguments, illegal (non-numeric) numbers, and misspelled kind argument (`lucky` / `evenLucky`).
- Support case-insensitive kind arguments; print a single number, a range by index (j..k), or a range by value (j..-k, where |k| is the upper bound).
- Print the resulting list on one line.
- Demonstrate: first 20 lucky and even lucky numbers; all lucky and even lucky numbers between 6000 and 6100; and (extra credit) the 10,000th lucky and even lucky numbers.

## Language Coverage
30 languages implement this task, spanning systems languages, functional languages, and scripting tongues. Representative entries include C, C++, D, Go, Haskell, Java, JavaScript, Julia, Python, Perl, Raku, Ruby, REXX, and Wren.

## Connections
- [[SieveOfEratosthenes]] — the elimination-by-position procedure is structurally analogous to a sieve.
- [[NumberTheory]] — lucky numbers are an integer sequence studied alongside primes.
- [[IntegerSequence]] — corresponds to OEIS A000959 (lucky) and A045954 (even lucky).
- [[CommandLineParsing]] — the task centers on robust CLI argument validation and range selection.

## Contradictions
- None — reference task page.
