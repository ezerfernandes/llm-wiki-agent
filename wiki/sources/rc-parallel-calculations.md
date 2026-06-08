---
title: "Parallel calculations (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, parallel-computing, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Parallel_calculations
---

## Summary
Given a collection of numbers, the task is to find the one whose smallest prime factor is the largest — i.e. the number composed of relatively large factors. The factorizations are to be computed in parallel across separate threads or processes to exploit multi-core CPUs, then the results are scanned to return the winning number and its prime factors. The point is not concurrency for its own sake but distributing an embarrassingly parallel, CPU-bound workload.

## Task Requirements
- Take a collection of numbers and factor each into its prime factors.
- Perform the factorizations in parallel using multiple threads or processes.
- For each number compute its minimal (smallest) prime factor.
- Search the results for the largest minimal prime factor and return that number along with its full prime decomposition.

## Language Coverage
46 languages implement this task, spanning systems languages, functional languages, and scripting languages, reflecting how varied parallelism primitives are across ecosystems. Representative implementations include C, C++, Go, Rust, Java, Haskell, Erlang, Python, Julia, and Scala.

## Connections
- [[PrimeFactorization]] — each number must be decomposed into primes
- [[ParallelComputing]] — work is distributed across CPU cores
- [[Multithreading]] — threads or processes run factorizations concurrently
- [[EmbarrassinglyParallel]] — independent per-number factorizations need no coordination

## Contradictions
- None — reference task page.
