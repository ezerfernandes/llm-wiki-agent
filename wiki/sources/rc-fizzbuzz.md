---
title: "FizzBuzz (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, iteration, conditional-logic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/FizzBuzz
---

## Summary
FizzBuzz asks the programmer to print the integers from 1 to 100, but substituting "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both. It is a famous interview screening exercise meant to verify that a candidate can translate simple branching logic into working code. The key insight is that the "both" case must be tested first (or built up by string concatenation) to avoid prematurely printing just "Fizz" or "Buzz".

## Task Requirements
- Print the integers from 1 to 100 inclusive.
- For multiples of three, print "Fizz" instead of the number.
- For multiples of five, print "Buzz" instead of the number.
- For multiples of both three and five (i.e., fifteen), print "FizzBuzz" instead of the number.

## Language Coverage
411 languages implement this task, making it one of the most broadly covered entries on the site, spanning everything from assembly to esoteric languages. Representative implementations include C, Python, Java, JavaScript, Haskell, Rust, Go, Ruby, Scheme, and Brainf***.

## Connections
- [[Iteration]] — the core loop over a fixed integer range
- [[ConditionalLogic]] — branching on divisibility conditions
- [[Modulo]] — divisibility tested via the modulo/remainder operator
- [[StringConcatenation]] — an alternative implementation that builds the output by appending "Fizz" and "Buzz"

## Contradictions
- None — reference task page.
