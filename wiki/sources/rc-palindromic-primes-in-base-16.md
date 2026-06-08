---
title: "Palindromic primes in base 16 (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Palindromic_primes_in_base_16
---

## Summary
This task asks the programmer to find all numbers n less than 500 (decimal) that are simultaneously prime and palindromic when written in base 16 (hexadecimal). The key insight is combining a primality test with a base-16 string conversion whose digit sequence reads the same forwards and backwards.

## Task Requirements
- Iterate over numbers n where n < 500 (decimal).
- Keep only the values of n that are prime.
- Among those, keep only the ones whose hexadecimal (base 16) representation is a palindrome.
- Report the qualifying numbers.

## Language Coverage
35 languages implement this task, spanning systems, scripting, functional, and array families. Representative implementations include C++, Rust, Go, Java, Python, Haskell, F#, Julia, Perl, Raku, Ruby, AWK, J, and Wren.

## Connections
- [[PrimeNumbers]] — candidates must pass a primality test
- [[PalindromeDetection]] — the core property checked on the digit sequence
- [[NumberBases]] — conversion of n into base 16 before testing
- [[RadixConversion]] — turning an integer into its hexadecimal digits

## Contradictions
- None — reference task page.
