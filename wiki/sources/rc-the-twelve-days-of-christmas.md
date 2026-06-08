---
title: "The Twelve Days of Christmas (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, cumulative-song]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/The_Twelve_Days_of_Christmas
---

## Summary
This task asks the programmer to write a program that prints the full lyrics of the Christmas carol "The Twelve Days of Christmas". The carol is a cumulative song: each of its twelve verses adds one new gift and then repeats all the previously named gifts in descending order. The key insight is that the natural solution stores the twelve gift phrases in an ordered list and uses nested iteration so each verse reprints the accumulated gifts rather than hardcoding all the repetition.

## Task Requirements
- Output the complete lyrics of the carol "The Twelve Days of Christmas".
- Reproduce the words in the correct order across all twelve verses.
- Case, formatting, and punctuation are left to the programmer's discretion.

## Language Coverage
125 languages implement this task, giving very broad coverage across mainstream, scripting, functional, and assembly languages. Representative examples include Python, C, C++, Java, JavaScript, Haskell, Ruby, Rust, Go, Perl, and even low-level entries like 8086 Assembly and Z80 Assembly.

## Connections
- [[StringProcessing]] — building and concatenating verse text from phrase fragments
- [[CumulativeSong]] — the structural pattern where each verse accumulates prior content
- [[Iteration]] — nested loops generate the twelve verses and their descending gift lists
- [[OrdinalNumbers]] — verses reference "first" through "twelfth" day requiring ordinal mapping

## Contradictions
- None — reference task page.
