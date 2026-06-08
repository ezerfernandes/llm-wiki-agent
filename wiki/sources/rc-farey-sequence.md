---
title: "Farey sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, fractions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Farey_sequence
---

## Summary
The Farey sequence F_n is the ordered list of completely reduced fractions between 0 and 1 whose denominators do not exceed n. The task asks the programmer to generate these sequences and count their members. The key insight is that fractions must be kept in lowest terms (reduced via GCD), and the sequence length grows asymptotically like 3·n² ÷ π².

## Task Requirements
- Compute and show the Farey sequence for orders 1 through 11 inclusive.
- Each sequence starts with 0/1 and ends with 1/1, arranged in increasing order.
- Compute and display the number of fractions in the Farey sequence for orders 100 through 1000 inclusive, stepping by hundreds.
- Display fractions in n/d form, using a slash (solidus) to separate numerator from denominator.

## Language Coverage
75 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Python, Haskell, Java, Perl, Raku, J, and APL.

## Connections
- [[FareySequence]] — the number-theoretic object being generated
- [[GreatestCommonDivisor]] — used to reduce each fraction to lowest terms
- [[SternBrocotTree]] — the mediant construction underlying neighboring Farey fractions
- [[EulerTotientFunction]] — governs how many new fractions appear at each order
- [[NumberTheory]] — the broader field this task belongs to

## Contradictions
- None — reference task page.
