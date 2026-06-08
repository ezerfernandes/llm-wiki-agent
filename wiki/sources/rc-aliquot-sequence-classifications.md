---
title: "Aliquot sequence classifications (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Aliquot_sequence_classifications
---

## Summary
The aliquot sequence of a positive integer K starts at K, and each subsequent term is the sum of the proper divisors of the previous term. The task asks the programmer to generate enough of this sequence to classify K into one of several categories based on whether and how the sequence terminates or repeats. The key insight is recognizing the different periodic patterns: termination at 0, immediate repetition of K (perfect/amicable/sociable), or eventual repetition of a different number (aspiring/cyclic).

## Task Requirements
- Generate the aliquot sequence of a positive integer K (first term K, each next term being the sum of K's proper divisors).
- Classify K into one of: terminating (reaches 0), perfect (period 1, repeats K), amicable (period 2, repeats K), sociable (period > 2, repeats K), aspiring (period 1 but a number other than K), cyclic (period >= 2 but a number other than K), or non-terminating.
- Treat K as non-terminating if unclassified after generating 16 terms, or if any term exceeds 2**47 (140,737,488,355,328).
- Display the classification and sequences for integers 1 to 10 inclusive.
- Display the classification and sequences for 11, 12, 28, 496, 220, 1184, 12496, 1264460, 790, 909, 562, 1064, 1488, and optionally 15355717786080.

## Language Coverage
58 languages implement this task, spanning systems languages, scripting languages, functional languages, and assembly. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, Common Lisp, and ARM Assembly.

## Connections
- [[ProperDivisors]] — each term is the sum of the proper divisors of the previous term
- [[PerfectNumbers]] — K is perfect when the sequence immediately repeats K with period 1
- [[AmicableNumbers]] — K is amicable when it repeats K with period 2
- [[SociableNumbers]] — K is sociable when it repeats K with period greater than 2
- [[NumberTheory]] — the task is rooted in divisor-based integer classification

## Solved in (Rosetta Code languages)
Solved in **54** of the wiki's catalogued languages (Rosetta Code shows 58 language sections for this task). (4 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[ALGOL 68]], [[AppleScript]], [[ARM Assembly]], [[AWK]], [[BASIC]], [[C]], [[C++]], [[CLU]], [[Common Lisp]], [[Crystal]], [[D]], [[EasyLang]], [[EchoLisp]], [[Elixir]], [[Factor]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[Kotlin]], [[Liberty BASIC]], [[Nim]], [[Oforth]], [[PARI-GP]], [[Perl]], [[Phix]], [[Picat]], [[Pluto]], [[PowerShell]], [[Prolog]], [[Python]], [[QBasic]], [[Racket]], [[Raku]], [[REXX]], [[Ring]], [[RPL]], [[Ruby]], [[Rust]], [[Scala]], [[Swift]], [[Tcl]], [[V (Vlang)]], [[VBA]], [[Wren]], [[Yabasic]], [[ZX Spectrum Basic]]

## Contradictions
- None — reference task page.
