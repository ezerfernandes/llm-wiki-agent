---
title: "Hex words (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hex_words
---

## Summary
A "hex word" is a word whose lowercase form uses only the letters a, b, c, d, e, and f — exactly the characters valid in hexadecimal notation. The task asks the programmer to scan a standard word list for such words of 4+ letters, reinterpret each as a hexadecimal number, convert to decimal, and compute its base-10 digital root. The key insight is that any all-hex-letter word is simultaneously a valid hexadecimal integer, so it can be parsed numerically.

## Task Requirements
- From unixdict.txt, find all hex words (letters only from a-f) of 4 letters or more.
- Convert each word to its decimal equivalent (interpreting it as a base-16 number) and compute its base-10 digital root.
- Display the word, its decimal value, and its digital root, sorted in increasing order of digital root, plus the total count.
- Then filter to only words containing at least 4 distinct letters, and display the same three statistics sorted in decreasing order of decimal equivalent, plus that total count.

## Language Coverage
41 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative examples include Python, Rust, Java, C++, Perl, Raku, Julia, J, Factor, AWK, and Fortran.

## Connections
- [[Hexadecimal]] — words are reinterpreted as base-16 integers
- [[DigitalRoot]] — the iterated digit-sum statistic computed for each word
- [[StringProcessing]] — filtering words by allowed character set and distinct-letter count
- [[Sorting]] — output ordered by digital root and by decimal value
- [[NumberBases]] — conversion between base-16 representation and decimal

## Contradictions
- None — reference task page.
