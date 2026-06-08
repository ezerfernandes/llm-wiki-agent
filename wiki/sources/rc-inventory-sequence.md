---
title: "Inventory sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, self-referential-sequence]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Inventory_sequence
---

## Summary
The task asks the programmer to generate the "inventory sequence" (OEIS A342585), a self-referential integer sequence built by repeatedly tallying its own contents. Starting an inventory from 0, you append the count of each successive integer (how many 0s, how many 1s, etc.); when you hit a number whose count is 0, you append that final 0 and restart the inventory from 0 again. The key insight is that the sequence describes itself, so each pass produces a new run of counts terminated by a zero.

## Task Requirements
- Generate and display the first 100 elements of the sequence.
- Find and display the position and value of the first element greater than or equal to 1000.
- Stretch: find the position and value of the first element >= 2000, 3000, ... up to 10,000.
- Stretch: plot a graph of the first 10,000 elements.

## Language Coverage
42 languages implement this task, spanning low-level assembly, classic and modern languages. Representative implementations include Python, Haskell, Java, JavaScript, Julia, Perl, Raku, Ruby, C++, and 8086 Assembly.

## Connections
- [[SelfReferentialSequence]] — the sequence is defined by counting its own elements
- [[IntegerSequences]] — catalogued as OEIS A342585
- [[Counting]] — each pass tallies occurrences of each value seen so far
- [[FrequencyTable]] — the inventory step is effectively a running histogram of values

## Contradictions
- None — reference task page.
