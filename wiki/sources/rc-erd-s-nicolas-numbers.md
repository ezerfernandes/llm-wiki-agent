---
title: "Erdős-Nicolas numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Erdős-Nicolas_numbers
---

## Summary
An Erdős–Nicolas number is a positive integer that is not perfect but equals the sum of its first k divisors (in ascending order, including 1) for some k greater than one. The task is to find and display the first 8 such numbers along with the value of k needed for each. The key insight is that the number must match a running partial sum of its sorted divisors exactly, without being perfect (which would require summing all proper divisors).

## Task Requirements
- For each candidate, enumerate its divisors in ascending order (including 1).
- Check whether a prefix sum of those divisors (using k > 1 divisors) equals the number itself.
- Exclude perfect numbers (where the sum of all proper divisors equals the number).
- Find and show the first 8 Erdős–Nicolas numbers and the corresponding k for each.
- Stretch goal: continue finding further Erdős–Nicolas numbers as patience allows.
- Optimization note: all known such numbers are even, so the search may restrict to even integers.

## Language Coverage
27 languages implement this task, spanning systems languages, scripting languages, and array/functional languages. Representative implementations include C, C++, C#, Go, Java, JavaScript, Python, Perl, Raku, Julia, and J.

## Connections
- [[NumberTheory]] — the task is rooted in divisor-sum properties of integers.
- [[PerfectNumber]] — Erdős–Nicolas numbers are explicitly defined in contrast to perfect numbers.
- [[Divisors]] — computing and ordering divisors is the core operation.
- [[PrefixSum]] — detection relies on running partial sums of the sorted divisor list.

## Contradictions
- None — reference task page.
