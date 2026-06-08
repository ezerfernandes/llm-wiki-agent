---
title: "Summarize and say sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Summarize_and_say_sequence
---

## Summary
This task defines a self-referential integer sequence where each term summarizes the previous one: count the occurrences of each distinct digit, then concatenate count-and-digit pairs for the digits sorted largest to smallest. Unlike the related look-and-say sequence, this "summarize" variant always converges, either to a fixed point or a short cycle, because summarizing collapses information. The goal is to find which seed values converge slowest.

## Task Requirements
- For a given seed, generate the sequence by counting alike digits and concatenating each count followed by its digit, ordered by digit from largest to smallest, omitting digits that do not appear.
- Treat convergence as the point where a term matches any previously seen term.
- Search all positive integer seeds under 1,000,000 (leading zeros not permitted).
- Report the seed value(s) that require the largest number of iterations to converge, the iteration count, and the resulting sequence.
- Note that digit permutations of a seed produce the same sequence (the answer is seeds 9009, 9090, 9900 at 21 iterations).

## Language Coverage
49 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, Raku, Julia, J, and REXX.

## Connections
- [[LookAndSaySequence]] — closely related self-referential sequence; the first five terms coincide
- [[SelfReferentialSequence]] — the general family this task belongs to
- [[FixedPoint]] — sequences here converge to stable values or short cycles
- [[StringProcessing]] — terms are manipulated as digit strings
- [[OEIS]] — corresponds to sequence A036058

## Contradictions
- None — reference task page.
