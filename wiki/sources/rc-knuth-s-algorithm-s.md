---
title: "Knuth's algorithm S (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, reservoir-sampling, probability, closures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Knuth's_algorithm_S
---

## Summary
The task asks the programmer to implement Knuth's algorithm S, a reservoir-sampling method that draws an equiprobable random sample of n items from a stream of M items whose total length is unknown until the stream ends. The key insight is that equal selection probability can be maintained online: each item past the first n is kept with probability n/i and, if kept, randomly displaces one existing sample member, so every seen item ends up with the same n/M chance.

## Task Requirements
- Implement a `s_of_n_creator` that takes the maximum sample size `n` and returns a closure/callable `s_of_n` taking a single `item` argument.
- `s_of_n` must return an equi-weighted random sample of up to n of the items seen so far on each call, using algorithm S: keep the first n outright; for the i-th item (i > n) keep it with probability n/i and, if kept, randomly (1/n) replace one current sample member.
- Verify correctness empirically: run n == 3 over digits 0-9 in order for 100,000 repetitions and report the selection-frequency of each digit (each should appear roughly equally often).

## Language Coverage
50 languages implement this task, spanning functional, object-oriented, and scripting paradigms, with most relying on closures or stateful objects to retain the running count and sample. Representative implementations include Python, Haskell, C, C++, Go, Rust, Java, Common Lisp, Ruby, and OCaml.

## Connections
- [[ReservoirSampling]] — algorithm S is the classic single-sample reservoir-sampling technique
- [[Closures]] — the creator returns a stateful function capturing n and the running sample
- [[ProbabilityTheory]] — correctness rests on maintaining uniform n/M selection probability
- [[RandomNumberGeneration]] — relies on uniform random draws for the keep/replace decisions

## Contradictions
- None — reference task page.
