---
title: "Fusc sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion, integer-sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fusc_sequence
---

## Summary
The fusc sequence (OEIS A2487, also called Stern's Diatomic Series or the Stern-Brocot sequence) is an integer sequence defined recursively: fusc(0)=0, fusc(1)=1, and for n>1, fusc(n)=fusc(n/2) when n is even, otherwise fusc((n-1)/2)+fusc((n+1)/2). A notable property is that fusc(A)=fusc(B) whenever B is the binary representation of A reversed. The task asks programmers to generate and display these numbers in a formatted way.

## Task Requirements
- Show the first 61 fusc numbers (starting at index 0) in a horizontal format.
- Show each fusc number (and its index) whose decimal length exceeds that of all previous fusc numbers (record-length values).
- Format numbers with commas where appropriate (thousands separators).
- Display all output on the task page.

## Language Coverage
69 languages implement this task, reflecting broad coverage across mainstream, functional, and BASIC-family languages. Representative implementations include C, C++, Java, Python, Go, Rust, Haskell, Julia, Perl, Raku, and REXX.

## Connections
- [[SternBrocotSequence]] — fusc is the same sequence shifted, indexing the Stern-Brocot tree
- [[Recursion]] — the definition is naturally recursive on even/odd cases
- [[NumberTheory]] — an integer sequence catalogued as OEIS A2487
- [[BinaryRepresentation]] — fusc(A) equals fusc of the bit-reversed value of A
- [[CalkinWilfSequence]] — a related enumeration of the rationals

## Contradictions
- None — reference task page.
