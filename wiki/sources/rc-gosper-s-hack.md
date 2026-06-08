---
title: "Gosper's hack (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, bit-manipulation, combinatorics, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Gosper's_hack
---

## Summary
Gosper's hack is an efficient bit-twiddling technique, attributed to Bill Gosper, that computes the next higher integer having the same number of set bits (same Hamming weight) as a given positive integer. Because every integer with k set bits corresponds to a distinct k-element subset, repeatedly applying the hack enumerates all combinations in ascending numeric order. The key insight is that the next value can be derived from a handful of constant-time bitwise operations rather than searching, making it a staple primitive for combination enumeration.

## Task Requirements
- Write a function or procedure that, given a positive integer, returns the next higher integer with the same number of set bits, using Gosper's hack.
- Demonstrate it by applying the function ten times to each of the starting values 1, 3, 7, and 15, showing the resulting sequences.

## Language Coverage
38 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative entries include C++, C#, Java, JavaScript, Python, Haskell, Julia, Go, Perl, Raku, Fortran, and Wren.

## Connections
- [[BitManipulation]] — relies entirely on bitwise AND, OR, XOR, negation, and shifts
- [[HammingWeight]] — preserves the population count (number of set bits) between successive values
- [[Combinations]] — enumerates k-subsets by treating set bits as selected elements
- [[Combinatorics]] — used to iterate over all combinations in lexicographic/numeric order

## Contradictions
- None — reference task page.
