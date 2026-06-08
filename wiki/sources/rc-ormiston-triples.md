---
title: "Ormiston triples (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ormiston_triples
---

## Summary
An Ormiston triple is a run of three consecutive prime numbers that are all anagrams of each other — they share the same multiset of decimal digits but in different orderings (for example 11117123, 11117213, 11117321). The task is to enumerate these triples. The key insight is that anagrams have identical digit sums, so every member of a triple shares the same digital root, and a sorted-digit signature gives a cheap anagram test.

## Task Requirements
- Find and show the smallest member of each of the first 25 Ormiston triples.
- Find and show the count of Ormiston triples up to one billion.
- Stretch goal: find and show the count of Ormiston triples up to ten billion.

## Language Coverage
23 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative solutions include C, C++, Go, Rust-adjacent Nim, Haskell, F#, Java, Julia, Python, Perl, Raku, Ruby, Phix, and Wren.

## Connections
- [[PrimeNumbers]] — the triple members must all be prime
- [[Anagram]] — the defining condition is a shared digit multiset
- [[SieveOfEratosthenes]] — a common way to generate the candidate prime stream efficiently
- [[OrmistonPairs]] — the two-member analogue and directly related task
- [[NumberTheory]] — the broader domain of the problem

## Contradictions
- None — reference task page.
