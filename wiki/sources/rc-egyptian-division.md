---
title: "Egyptian division (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Egyptian_division
---

## Summary
Egyptian division computes integer quotient and remainder using only addition and doubling, mirroring ancient Egyptian arithmetic and closely related to Ethiopian (Russian peasant) multiplication. The key insight is that any quotient can be expressed in binary: build a table of powers of two alongside the divisor repeatedly doubled, then greedily sum rows from largest to smallest to reconstruct the dividend, accumulating the matching powers of two as the answer.

## Task Requirements
- Build two parallel lists: `powers_of_2` (1, 2, 4, ...) and `doublings` (divisor, 2·divisor, 4·divisor, ...), stopping while `2^i · divisor <= dividend`.
- Initialize `answer` and `accumulator` to zero.
- Iterate the table rows in reverse construction order; if adding a row's doubling to the accumulator stays `<= dividend`, add it and add that row's power of two to the answer.
- The quotient is `answer`; the remainder is `|accumulator - dividend|`.
- Implement as a clear function and demonstrate by dividing 580 by 34 (answer 17, remainder 2).

## Language Coverage
68 languages implement this task, spanning a broad mix from systems and functional languages to scripting and BASIC dialects. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, Ruby, Perl, Raku, Scheme, and REXX.

## Connections
- [[BinaryRepresentation]] — the quotient is effectively built from its binary digits via the powers-of-two table
- [[EthiopianMultiplication]] — sibling algorithm using the same doubling/halving technique
- [[IntegerDivision]] — produces quotient and remainder
- [[BitwiseOperations]] — doubling is a left shift; the method is shift-and-add division

## Contradictions
- None — reference task page.
