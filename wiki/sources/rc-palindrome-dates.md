---
title: "Palindrome dates (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dates, palindrome, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Palindrome_dates
---

## Summary
The task asks for a program that finds and displays the next 15 palindromic dates expressed in `yyyy-mm-dd` format, where the date with hyphens removed reads the same forwards and backwards. The motivating example is 2020-02-02 (rendered "20200202"), which is unusually a palindrome in both the `yyyy-mm-dd` and `dd-mm-yyyy` orderings. The key insight is that an 8-digit `yyyymmdd` string is a palindrome only when its first four reversed digits form a valid month and day, sharply constraining valid candidates.

## Task Requirements
- Calculate the next 15 palindromic dates after the current date.
- Use the `yyyy-mm-dd` date ordering.
- Treat a date as a palindrome when the digit string with hyphens removed reads identically reversed.
- Display the resulting dates.

## Language Coverage
54 languages implement this task, giving broad coverage across mainstream, scripting, and BASIC-family languages. Representative implementations include C, C++, C#, Java, Python, JavaScript, Go, Rust, Haskell, Perl, Ruby, and Raku.

## Connections
- [[Palindrome]] — the core string property being tested
- [[StringProcessing]] — reversal and comparison of digit strings
- [[DateArithmetic]] — iterating and validating calendar dates
- [[CalendarSystems]] — handling month/day bounds and leap years

## Contradictions
- None — reference task page.
