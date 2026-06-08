---
title: "MutationCoverageFuzzer"
type: concept
tags: [fuzzing, testing, mutation-fuzzing, coverage-guided, python, class-hierarchy]
sources: [fuzzingbook-05-mutation-fuzzer]
last_updated: 2026-06-06
---

# MutationCoverageFuzzer

**`MutationCoverageFuzzer`** is *The Fuzzing Book*'s concrete [[CoverageGuidedFuzzing|coverage-guided]] [[MutationBasedFuzzing|mutation fuzzer]] — a `MutationFuzzer` subclass that keeps only those mutated inputs which achieve *new* [[Coverage|coverage]], evolving its population into a corpus of inputs that are all valid yet each exercise a distinct execution. It is the chapter's miniature reconstruction of [[AFL|AFL]]'s core heuristic: retain an input whenever it finds a new path through the program.

## How it works
- `reset()` re-seeds: it clears `population` to `[]` and creates `coverages_seen: Set[frozenset]` (the seeds are added during the first `fuzz` runs, not held statically).
- `run(runner)` (where `runner` is a [[Runner|`FunctionCoverageRunner`]]) calls the superclass `run`, then computes `new_coverage = frozenset(runner.coverage())`. If the outcome is `Runner.PASS` *and* `new_coverage` is not in `coverages_seen`, the input (`self.inp`) is appended to `population` and the coverage recorded.
- Mutation candidates are drawn from this growing population, so productive inputs get further mutated while unproductive ones are discarded — a feedback loop driven by coverage rather than blind variety.

## From The Fuzzing Book — Mutation-Based Fuzzing
[[fuzzingbook-05-mutation-fuzzer|Ch 5]] mints this class as the chapter's payoff. Running `MutationCoverageFuzzer(seed=[seed_input]).runs(http_runner, trials=10000)` on the `http_program()` URL validator yields a population in which *every* input is valid and has *different* coverage — covering varied combinations of schemes, paths, queries, and fragments. `population_coverage()` then plots the cumulative coverage growth. The chapter stresses the generality: applied to larger programs the strategy "happily explore[s] one path after the other," needing only a means to capture coverage. It explicitly frames this as AFL's idea and forwards to [[fuzzingbook-06-greybox-fuzzer|Ch 6]], which replaces uniform population sampling with *power schedules* that bias toward seeds hitting unlikely paths. (Exercise 4 notes AFL actually keys on new *branches* rather than the full coverage set used here.)

## Connections
- [[MutationBasedFuzzing]] — the technique it specializes with coverage feedback.
- [[CoverageGuidedFuzzing]] — the feedback principle it implements.
- [[Coverage]] / [[Runner]] — coverage captured via `FunctionCoverageRunner` decides what to keep.
- [[SeedInput]] — its evolving population starts from seeds.
- [[Mutator]] — supplies the candidate inputs it filters by coverage.
- [[RandomFuzzer]] — shares the `Fuzzer` base via `MutationFuzzer`.
- [[AFL]] — the real-world fuzzer whose "keep inputs that find new paths" heuristic this reproduces.
- [[fuzzingbook-05-mutation-fuzzer|Ch 5]] — where it is defined.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — adds power schedules over the corpus (greybox).

## Sources
- [[fuzzingbook-05-mutation-fuzzer]] — *The Fuzzing Book* Ch 5, "Mutation-Based Fuzzing."
