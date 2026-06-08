---
title: "Digital root (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Digital_root
---

## Summary
The task asks the programmer to compute the digital root of a number by repeatedly summing its digits until a single digit remains, and to also report the additive persistence — the count of summation steps needed. The key insight is that the digital root is equivalent to the value of the number modulo (base minus one), making it computable directly via casting out nines, though the task emphasizes the iterative digit-summing definition.

## Task Requirements
- Compute the digital root: sum the digits of n, then repeatedly sum the digits of the result until only one digit remains.
- Compute the additive persistence: the number of summation iterations required to reach a single digit.
- Demonstrate on examples such as 627615 (persistence 2, root 9), 39390 (persistence 2, root 6), 588225 (persistence 2, root 3), and 393900588225 (persistence 2, root 9).
- Support calculation in bases other than base 10.

## Language Coverage
125 languages implement this task, giving very broad coverage across paradigms and eras — from assembly and esoteric languages to modern scripting and functional languages. Representative implementations include C, Python, Java, Haskell, Rust, Go, Ruby, Perl, REXX, and J.

## Connections
- [[NumberTheory]] — digital root is a number-theoretic property tied to modular arithmetic.
- [[CastingOutNines]] — the digital root equals n mod (base − 1), the basis of this verification trick.
- [[ModularArithmetic]] — digital root in base b is congruent to the value modulo b − 1.
- [[DigitManipulation]] — the core operation is decomposing a number into its digits and summing them.
- [[Recursion]] — the repeated digit-summing is naturally expressed iteratively or recursively.

## Contradictions
- None — reference task page.
