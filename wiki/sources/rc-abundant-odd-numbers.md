---
title: "Abundant odd numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Abundant_odd_numbers
---

## Summary
An abundant number is an integer n whose sum of proper divisors (aliquot sum) exceeds n, equivalently whose divisor sum sigma(n) exceeds 2n. This task narrows the search to the rarer odd abundant numbers, asking the programmer to compute each candidate's divisor sum and test the abundance condition. The key practical challenge is efficiency: the third part requires scanning past one billion, so a fast sigma/aliquot routine matters.

## Task Requirements
- Find and display the first 25 abundant odd numbers, with either their proper divisor sum or sigma sum.
- Find and display the one thousandth abundant odd number, with its divisor sum.
- Find and display the first abundant odd number greater than one billion (10^9), with its divisor sum.

## Language Coverage
85 languages implement this task, giving very broad coverage across compiled, scripting, functional, and assembly families. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Julia, Raku, REXX, and several assembly dialects (360 Assembly, ARM, x86).

## Connections
- [[AbundantNumber]] — the central definition being tested
- [[SumOfDivisors]] — sigma(n), the function computed for each candidate
- [[AliquotSum]] — sum of proper divisors, equivalent abundance criterion
- [[NumberTheory]] — the mathematical domain of the task
- [[OEIS]] — sequence A005231 enumerates odd abundant numbers

## Solved in (Rosetta Code languages)
Solved in **79** of the wiki's catalogued languages (Rosetta Code shows 85 language sections for this task). (6 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[360 Assembly]], [[AArch64 Assembly]], [[Ada]], [[Agena]], [[ALGOL 60]], [[ALGOL 68]], [[ALGOL W]], [[AppleScript]], [[ARM Assembly]], [[Arturo]], [[AutoHotkey]], [[AWK]], [[Ballerina]], [[BASIC]], [[BQN]], [[C]], [[C++]], [[CLU]], [[COBOL]], [[Common Lisp]], [[Crystal]], [[D]], [[Delphi]], [[EasyLang]], [[Factor]], [[Fortran]], [[Frink]], [[FutureBasic]], [[Go]], [[Groovy]], [[Haskell]], [[J]], [[Java]], [[JavaScript]], [[Julia]], [[K]], [[Kotlin]], [[Lobster]], [[Loglan82]], [[Lua]], [[MAD]], [[Maple]], [[Maxima]], [[MiniScript]], [[Modula-2]], [[Nim]], [[Oberon-07]], [[PARI-GP]], [[Pascal]], [[Perl]], [[Phix]], [[PHP]], [[PicoLisp]], [[PL-I]], [[Pluto]], [[PowerShell]], [[Processing]], [[Python]], [[Quackery]], [[R]], [[Racket]], [[Raku]], [[Rebol]], [[REXX]], [[Ring]], [[RPL]], [[Ruby]], [[Rust]], [[Scala]], [[Sidef]], [[Smalltalk]], [[Swift]], [[Uiua]], [[V (Vlang)]], [[Visual Basic]], [[Wren]], [[X86 Assembly]], [[XPL0]]

## Contradictions
- None — reference task page.
