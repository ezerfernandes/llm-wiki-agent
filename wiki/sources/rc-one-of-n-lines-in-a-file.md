---
title: "One of n lines in a file (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, algorithms, randomness]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/One_of_n_lines_in_a_file
---

## Summary
The task asks the programmer to choose a line uniformly at random from a file while reading it only once, without holding the whole file in memory, and without knowing the line count in advance. The trick is to keep the current line as the candidate and replace it with the Nth line with probability 1/N as each line is read; this yields a uniform distribution over all lines. It is a single-item special case of reservoir sampling.

## Task Requirements
- Implement a routine `one_of_n(n)` that, given the number of lines `n`, applies the 1/N replacement rule and returns the chosen line number.
- Run `one_of_n` in a simulation of a 10-line file repeated 1,000,000 times (fewer repetitions allowed if noted up-front).
- Print how many times each of the 10 lines was chosen, demonstrating the distribution is roughly uniform.

## Language Coverage
73 languages implement this task, spanning systems and scripting languages alike: C, C++, Rust, Go, Java, Python, Haskell, Ruby, Perl, and Common Lisp are representative, with many BASIC dialects and niche entries (J, Factor, DuckDB) also present.

## Connections
- [[ReservoirSampling]] — this task is the n=1 case of the reservoir sampling family
- [[ProbabilityDistribution]] — the algorithm produces a uniform distribution over lines
- [[RandomNumberGeneration]] — relies on uniform random values in [0,1) for each replacement decision
- [[StreamingAlgorithms]] — processes input in a single pass with constant memory

## Contradictions
- None — reference task page.
