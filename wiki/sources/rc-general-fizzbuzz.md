---
title: "General FizzBuzz (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, string-processing, iteration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/General_FizzBuzz
---

## Summary
A generalized version of the classic FizzBuzz exercise where the divisor/word pairs are supplied by the user rather than hardcoded. Given a maximum number and a list of (factor, word) pairs, the program prints each integer from 1 to the maximum, substituting the associated word(s) for any number divisible by a factor. The key insight is decoupling the matching rule from the data, turning a fixed puzzle into a parameterized table-driven loop.

## Task Requirements
- Read a maximum number and three (factor, word) pairs from the user.
- Print integers 1 through the maximum.
- For each number divisible by a factor, print that factor's word instead of the number.
- When a number is divisible by multiple factors, concatenate all matching words in ascending order of factor (e.g. 15 with factors 3=Fizz, 5=Buzz prints "FizzBuzz").
- Print the number itself only when no factor divides it.

## Language Coverage
87 languages implement this task, spanning systems languages, scripting languages, functional languages, and BASIC dialects. Representative examples include C, C++, Java, Python, Go, Rust, Haskell, Clojure, Perl, Ruby, and Lua.

## Connections
- [[FizzBuzz]] — the specialized base task this generalizes
- [[Divisibility]] — core test driving each substitution
- [[ModularArithmetic]] — the modulo operation determines factor membership
- [[Iteration]] — the loop over the integer range
- [[TableDrivenDesign]] — replacing hardcoded rules with user-supplied data

## Contradictions
- None — reference task page.
