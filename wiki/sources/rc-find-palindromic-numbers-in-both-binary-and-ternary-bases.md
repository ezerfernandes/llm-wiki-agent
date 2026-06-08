---
title: "Find palindromic numbers in both binary and ternary bases (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, palindromes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_palindromic_numbers_in_both_binary_and_ternary_bases
---

## Summary
The task asks the programmer to find and display, in decimal, the first six non-negative integers whose digit representations are palindromes in both base 2 (binary) and base 3 (ternary) simultaneously. The key insight is that such doubly-palindromic numbers are extremely sparse, so a naive scan is slow; efficient solutions generate base-2 palindromes and test only those for ternary palindromicity. This corresponds to OEIS sequence A060792.

## Task Requirements
- Find the first six non-negative integers that are palindromes in both base 2 and base 3.
- Include 0 (zero) as the first number found, even though some definitions exclude it.
- Optionally also show each found decimal number in its binary and ternary forms.
- Show all output.
- It is permissible to assume the first two numbers and simply list them.

## Language Coverage
47 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative implementations include C, C++, C#, Java, Python, Haskell, Go, Julia, Perl, Raku, Ruby, and REXX.

## Connections
- [[Palindrome]] — the core property being tested in two bases at once
- [[NumberBaseConversion]] — converting decimal integers to base 2 and base 3 digit strings
- [[NumberTheory]] — sparse integer sequences and base-dependent properties
- [[OEIS]] — sequence A060792 catalogs these numbers

## Contradictions
- None — reference task page.
