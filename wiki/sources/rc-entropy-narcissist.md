---
title: "Entropy/Narcissist (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, information-theory, quine]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Entropy/Narcissist
---

## Summary
The task asks the programmer to write a program that reads its own source code and computes and prints the Shannon entropy of that source. It is a self-referential ("narcissist") variant of the plain Entropy task: the program must inspect itself, so the key insight is combining quine-like self-access (reading the program file or its own text) with the per-character frequency entropy calculation.

## Task Requirements
- Compute the Shannon entropy of the program's own source code.
- Treat the source as the input data, counting the frequency of each distinct character (or byte).
- Output the resulting entropy value, typically in bits per symbol.

## Language Coverage
45 languages implement this task, spanning systems languages, scripting languages, and functional and Lisp-family languages. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Ruby, Julia, and Racket.

## Connections
- [[ShannonEntropy]] — the information-theoretic measure being computed
- [[InformationTheory]] — the field defining entropy of a symbol source
- [[Quine]] — the self-reading / self-referential program technique this task requires
- [[FrequencyCounting]] — tallying per-character occurrences to build the probability distribution

## Contradictions
- None — reference task page.
