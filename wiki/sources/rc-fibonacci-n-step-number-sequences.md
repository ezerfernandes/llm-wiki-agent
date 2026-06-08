---
title: "Fibonacci n-step number sequences (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recurrence-relations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fibonacci_n-step_number_sequences
---

## Summary
This task generalizes the Fibonacci sequence so that each term is the sum of the previous n terms rather than just the previous two. For n=2 it reproduces the ordinary Fibonacci sequence, n=3 gives the tribonacci, n=4 the tetranacci, and so on, with the count of supplied initial values implicitly determining the step size n. The key insight is that one parameterized function, driven by a window of seed values, can produce any of these named sequences (including the Lucas series, which uses the same n=2 rule but starts from [2, 1]).

## Task Requirements
- Write a function that generates a Fibonacci n-step sequence given a list of initial values, where the number of initial values determines how many preceding terms are summed to produce the next term.
- Use that function to print at least the first ten members of the fibonacci (n=2), tribonacci (n=3), tetranacci (n=4), and Lucas sequences.

## Language Coverage
92 languages implement this task, spanning systems and scripting languages, functional languages, and several assembly dialects. Representative implementations include C, C++, Rust, Go, Python, Haskell, Java, JavaScript, Common Lisp, Raku, and 360 Assembly.

## Connections
- [[FibonacciSequence]] — the n=2 special case this task generalizes
- [[RecurrenceRelation]] — each term is defined as a sum of fixed preceding terms
- [[LucasNumbers]] — same recurrence with alternate seed values [2, 1]
- [[NumberTheory]] — integer sequences and their generating rules
- [[SlidingWindow]] — efficient generation by maintaining a window of the last n terms

## Contradictions
- None — reference task page.
