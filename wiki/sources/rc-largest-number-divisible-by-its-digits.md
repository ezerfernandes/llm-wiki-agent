---
title: "Largest number divisible by its digits (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisibility]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Largest_number_divisible_by_its_digits
---

## Summary
The task is to find the largest base-10 integer whose digits are all distinct and whose value is evenly divisible by each of its individual digits. Such numbers are known as Lynch-Bell numbers (OEIS A115569). The key insight is that a zero digit is forbidden (division by zero) and digits must be unique, so any candidate has at most 9 digits; the search space can be pruned with divisibility analytics rather than brute-forced naively.

## Task Requirements
- Find the single largest such integer in base 10.
- Digits must all be different and must not include zero.
- The number must be evenly divisible by each of its own digits.
- An actual search is required; hardcoding/verifying the known answer is disallowed.
- May use analytics and clever algorithms to shrink the search space.
- Stretch goal: do the same for hexadecimal (base 16).

## Language Coverage
57 languages implement this task, giving broad coverage across compiled, scripting, functional, and esoteric families. Representative implementations include C, C++, C#, Java, Go, Rust-adjacent Crystal, Python, Haskell, Julia, Perl, Raku, Ruby, J, and Wren.

## Connections
- [[Divisibility]] — the core test applied digit by digit.
- [[NumberTheory]] — Lynch-Bell numbers are a number-theoretic sequence.
- [[SearchSpacePruning]] — analytics to reduce candidates before checking.
- [[DigitManipulation]] — extracting and testing individual digits.

## Contradictions
- None — reference task page.
