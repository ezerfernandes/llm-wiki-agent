---
title: "Fibonacci word (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, recursion, information-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fibonacci_word
---

## Summary
The Fibonacci word is a string built with the same recurrence as the Fibonacci sequence, but concatenating strings instead of adding numbers: starting from "1" and "0", each successive word is the previous word followed by the one before it. The task is to generate these words up to n = 37 and report, for each, its length and Shannon entropy. The key insight is that word lengths follow the Fibonacci numbers, while the entropy converges toward a fixed value as the ratio of 0s to 1s approaches the golden ratio.

## Task Requirements
- Define F_Word(1) = "1" and F_Word(2) = "0".
- Form F_Word(3) = F_Word(2) + F_Word(1) = "01", and in general F_Word(n) = F_Word(n-1) + F_Word(n-2).
- Perform these steps up to n = 37.
- Do not print the large words; show only the first few if any.
- Produce a table for words 1 through 37 listing the number of characters in each word and each word's entropy.

## Language Coverage
72 languages implement this task, giving very broad coverage across functional, imperative, and array-oriented styles. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Perl, Raku, J, and Wolfram Language.

## Connections
- [[FibonacciSequence]] — the word recurrence mirrors the numeric one; word lengths are Fibonacci numbers
- [[Entropy]] — Shannon entropy of each word is computed and tabulated
- [[GoldenRatio]] — the symbol-frequency ratio converges to phi, governing the limiting entropy
- [[StringConcatenation]] — words are built purely by concatenating prior words
- [[Recursion]] — natural recursive/iterative definition of the word generation

## Contradictions
- None — reference task page.
