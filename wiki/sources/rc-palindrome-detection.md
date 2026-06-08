---
title: "Palindrome detection (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Palindrome_detection
---

## Summary
The task asks for a function or program that determines whether a given sequence of characters (or bytes) reads the same backward as forward — that is, whether it is a palindrome. The core insight is that a string is a palindrome exactly when it equals its own reversal, so most solutions reduce to comparing the string against its reverse, with an alternative two-pointer approach scanning inward from both ends.

## Task Requirements
- Write a function or program that checks whether a given sequence of characters (or bytes) is a palindrome.
- For extra credit: support Unicode characters.
- For extra credit: write a second function (possibly wrapping the first) that detects *inexact* palindromes — phrases that are palindromes once whitespace and punctuation are ignored and comparison is case-insensitive.

## Language Coverage
197 languages implement this task, reflecting its status as a classic introductory string-manipulation and recursion exercise. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Go, Rust, Perl, and Lisp, alongside assembly variants (8080, x86) and niche languages like APL, BQN, and Uiua.

## Connections
- [[Palindrome]] — the core property being detected
- [[StringReversal]] — the most common implementation strategy
- [[Recursion]] — recursive comparison of first and last characters
- [[StringProcessing]] — broader domain of the task
- [[UnicodeHandling]] — required for the extra-credit case

## Contradictions
- None — reference task page.
