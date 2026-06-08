---
title: "Recaman's sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-sequence]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Recaman's_sequence
---

## Summary
The task asks the programmer to generate Recamán's sequence, an integer sequence (OEIS A005132) starting at a(0)=0. Each subsequent term a(n) jumps backward by n to a(n-1)-n only if that result is positive and has not already appeared; otherwise it jumps forward to a(n-1)+n. The key insight is tracking already-seen values (typically via a set) to enforce the "not previously generated" condition.

## Task Requirements
- Generate and display the first 15 members of the sequence.
- Find and display the first duplicated number in the sequence.
- Optionally, determine how many terms are needed until every integer from 0 to 1000 inclusive has been generated.

## Language Coverage
64 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative examples include C, C++, C#, Rust, Go, Java, Python, Haskell, Perl, and Ruby.

## Connections
- [[IntegerSequences]] — Recamán's sequence is a member (OEIS A005132)
- [[NumberTheory]] — concerns properties of natural-number sequences
- [[SetMembership]] — requires tracking previously generated values for the duplicate check
- [[GreedyConstruction]] — each term chosen by a local rule on the previous term

## Contradictions
- None — reference task page.
