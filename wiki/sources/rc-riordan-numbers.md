---
title: "Riordan numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-sequence, recurrence]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Riordan_numbers
---

## Summary
The Riordan numbers (OEIS A005043) are an integer sequence arising in set theory and closely related to the Motzkin numbers, from which they can be derived. The task is to generate the sequence using its recurrence relation: starting from a(0)=1 and a(1)=0, each later term is a(n) = (n-1)*(2*a(n-1) + 3*a(n-2))/(n+1). The key insight is that despite the division, every term comes out as an exact integer.

## Task Requirements
- Find and display the first 32 Riordan numbers.
- Stretch: find and display the digit count of the 1,000th Riordan number.
- Stretch: find and display the digit count of the 10,000th Riordan number.
- May use any convenient generating function for the language.

## Language Coverage
44 languages implement this task, spanning systems and scripting languages, BASIC dialects, and functional and array languages — representative entries include Python, C++, C#, Java, Haskell, Julia, Perl, Raku, J, Wren, and even EDSAC order code. The large-index stretch goals favor languages with arbitrary-precision integers.

## Connections
- [[MotzkinNumbers]] — Riordan numbers are closely related and derivable from them
- [[IntegerSequence]] — the task generates an OEIS-cataloged sequence (A005043)
- [[RecurrenceRelation]] — terms defined by a second-order recurrence over prior terms
- [[BigInteger]] — the 1,000th and 10,000th terms require arbitrary-precision arithmetic
- [[NumberTheory]] — the sequence and its combinatorial interpretation

## Contradictions
- None — reference task page.
