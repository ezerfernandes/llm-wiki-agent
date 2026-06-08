---
title: "Exponential digital sums (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, digit-manipulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Exponential_digital_sums
---

## Summary
The task is to find integers greater than 1 whose decimal digits, when summed after the integer is raised to some integer power greater than 1, reproduce the original integer (for example, 9² = 81 and 8 + 1 = 9). Some integers satisfy this for multiple exponents, such as 18 (via powers 3, 6, and 7). The core insight is to search candidate bases and a range of exponents, computing each power and summing its digits to test for a fixed point.

## Task Requirements
- Find and show the first twenty integers, together with the exponents, that satisfy the condition (digit sum of n^k equals n, for some integer exponent k > 1).
- Find and show at least the first ten integers, with their exponents, that satisfy the condition in three or more distinct ways.
- Exclude the trivial exponent of 1 (where every integer qualifies) as well as 0 and 1.

## Language Coverage
18 languages implement this task, spanning systems and BASIC dialects through scripting and array languages — including C++, Java, JavaScript, Python, Perl, Raku, Julia, Nim, jq, Phix, and Wren.

## Connections
- [[NumberTheory]] — the property is a digit-based numerical relationship.
- [[DigitSum]] — summing decimal digits is the central operation.
- [[Exponentiation]] — candidates are tested across integer powers.
- [[BigIntegerArithmetic]] — high powers can overflow native integer types.

## Contradictions
- None — reference task page.
