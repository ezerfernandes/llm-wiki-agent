---
title: "Pseudo-random numbers/Middle-square method (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, pseudo-random, number-theory, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pseudo-random_numbers/Middle-square_method
---

## Summary
The task asks the programmer to implement John von Neumann's middle-square method for generating pseudo-random numbers. Starting from an n-digit seed, the value is squared to produce a 2n-digit number (zero-padded on the left if needed), and the middle n digits become both the next output and the next seed. The key insight is that this historically important but weak generator can converge to zero or short cycles, which is why it is now mainly of pedagogical interest.

## Task Requirements
- Implement a class or set of functions that generate 6-digit pseudo-random numbers using the middle-square algorithm.
- Square the current seed, pad to 12 digits with leading zeroes, and extract the middle 6 digits as the next value and seed.
- Show the first five integers generated from the seed 675248.
- Display the output on the task page.

## Language Coverage
56 languages implement this task, spanning mainstream high-level languages, scripting tools, and several assembly and esoteric entries. Representative implementations include Python, C, C++, Java, JavaScript, Rust, Go, Haskell, Ruby, and Perl, alongside lower-level entries like AArch64 Assembly and historical EDSAC order code.

## Connections
- [[PseudoRandomNumberGeneration]] — the broader family of algorithms this method belongs to
- [[MiddleSquareMethod]] — the specific technique, attributed to von Neumann
- [[ModularArithmetic]] — digit extraction is effectively arithmetic on positional segments
- [[StringProcessing]] — many solutions implement the middle-digit extraction via string slicing and zero-padding

## Contradictions
- None — reference task page.
