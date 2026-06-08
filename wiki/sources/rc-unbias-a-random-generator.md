---
title: "Unbias a random generator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, randomness]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Unbias_a_random_generator
---

## Summary
Given a biased one-bit random generator where the probability of a 1 differs from the probability of a 0, the task is to build an unbiased fair-coin generator that uses only the biased source. The key insight is Von Neumann debiasing: draw bits in pairs and discard equal pairs, since "1 then 0" and "0 then 1" are equally likely under independence, regardless of the underlying bias.

## Task Requirements
- Implement `randN` that returns 1 or 0, with a 1 occurring on average 1 out of N times, for integer N from 3 to 6 inclusive.
- Implement `unbiased` that uses only `randN` as its randomness source to produce fair (equiprobable) ones and zeroes.
- For each N in the range, generate and display counts of the outputs of `randN` and of `unbiased(randN)`.
- The unbiasing must generate two `randN` values at a time, returning a bit only when the two differ (always taking the first, or always the second).

## Language Coverage
63 languages implement this task, showing broad coverage across functional, imperative, and scripting paradigms. Representative implementations include Python, C, C++, Java, Haskell, Rust, Go, Ruby, Perl, Raku, and Common Lisp.

## Connections
- [[VonNeumannExtractor]] — the debiasing algorithm this task implements
- [[ProbabilityTheory]] — independence of paired outcomes underpins the method
- [[RandomNumberGeneration]] — the source of randomness being corrected
- [[RandomnessExtractor]] — the broader class of bias-removal techniques

## Contradictions
- None — reference task page.
