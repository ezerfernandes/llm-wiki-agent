---
title: "Boustrophedon transform (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences, recurrence-relations]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Boustrophedon_transform
---

## Summary
The boustrophedon transform maps an input integer sequence to a new one via a series of additions, classically by building a triangle and reading off its alternating ("ox-plowing") boundary values. The task asks for a routine implementing the transform, either by constructing the boustrophedon triangle or by applying the recurrence T(k,0)=a_k and T(k,n)=T(k,n-1)+T(k-1,k-n), with the result read off the diagonal as b_n=T(n,n). The key insight is that summing along rows in alternating directions accumulates the prior row's values, linking these transforms to the Euler up/down numbers.

## Task Requirements
- Write a procedure that performs a boustrophedon transform on a given input sequence.
- Apply it to six demonstration sequences: (1,0,0,...), all-ones, (-1)^n alternating, primes (2,3,5,7,11,...), Fibonacci (1,1,2,3,5,...), and factorials (1,1,2,6,24,...).
- Show the first fifteen values of each transformed sequence.
- Stretch: if big integers are supported, report the first 20 digits, last 20 digits, and total digit count of the 1000th element of each transformed sequence.

## Language Coverage
27 languages implement this task, spanning systems languages, functional languages, array languages, and BASIC dialects. Representative entries include C++, Rust, Zig, Haskell, F#, Java, JavaScript, Python, Julia, Perl, Raku, J, and Wren.

## Connections
- [[BoustrophedonTransform]] — the named integer-sequence transform itself
- [[RecurrenceRelation]] — the T(k,n) recurrence defining the triangle
- [[EulerNumbers]] — the up/down numbers (OEIS A000111) produced from a unit input
- [[FibonacciSequence]] — one of the demonstration input sequences
- [[Factorial]] — another demonstration input sequence
- [[BigIntegerArithmetic]] — required for the 1000th-element stretch goal

## Contradictions
- None — reference task page.
