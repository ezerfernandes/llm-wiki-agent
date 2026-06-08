---
title: "ddmin (Delta Debugging Minimization)"
type: concept
tags: [debugging, testing, fuzzing, input-reduction, algorithm, software-engineering]
sources: [fuzzingbook-16-reducer]
last_updated: 2026-06-06
---

# ddmin (Delta Debugging Minimization)

**`ddmin`** is the concrete minimization procedure at the heart of [[DeltaDebugging|delta debugging]] (Zeller & Hildebrandt 2002). Given a failing input, it produces a [[OneMinimality|1-minimal]] sub-input that still fails — using only a `FAIL`/`PASS`/`UNRESOLVED` [[TestOracle|oracle]], with no knowledge of input structure. In [[fuzzingbook-16-reducer|Ch 16]] it is implemented as `DeltaDebuggingReducer.reduce()`.

## The algorithm
Granularity `n` controls the chunk size (`1/n` of the current input):

1. Start `n = 2`. Assert the input `FAIL`s (else raise `AssertionError`).
2. Split the input into `n` equal chunks. For each chunk, test the **complement** (input with that chunk removed):
   - If a complement still `FAIL`s → adopt it as the new input, *decrease* granularity (`n = max(n - 1, 2)`), and restart the pass. The failing region has shrunk.
   - If **no** complement fails → *increase* granularity (`n = min(n * 2, len(inp))`), cutting away smaller pieces next time.
3. Stop when `n == len(inp)` (down to single characters with nothing left to remove).

Because the final stage removes characters one at a time, the result is **1-minimal**: deleting any single remaining character makes the test stop failing.

## Properties
- **Best case** `O(log₂ n)` tests — when removing a half (or quarter, …) immediately reproduces the failure, this is exactly binary search.
- **Worst case** `O(n²)` tests — the pathological situation where only the *last* character matters, forcing the algorithm to attempt deleting every character at fine granularity.
- **Caching** — `DeltaDebuggingReducer` inherits `CachingReducer`, memoizing outcomes so repeated candidates are free.
- **Deterministic, fast tests required** — non-deterministic or slow oracles undermine the many experiments `ddmin` performs.
- **Lexical only** — `ddmin` treats the input as a flat string; on syntactically structured inputs its cuts produce invalid (`UNRESOLVED`) candidates and it stalls, motivating [[GrammarReducer|grammar-based reduction]].

## Connections
- [[DeltaDebugging]] — the algorithm `ddmin` instantiates; this is its operational core.
- [[InputReduction]] — `ddmin` is the canonical lexical reducer.
- [[OneMinimality]] — the guarantee `ddmin`'s final stage provides.
- [[GrammarReducer]] / [[HierarchicalDeltaDebugging]] — the structure-aware successor when `ddmin` stalls.
- [[AndreasZeller]] — co-author of the originating paper.
- [[Fuzzing]] / [[Testing]] — `ddmin`'s prerequisites (fast, deterministic tests) match fuzzing's.
- [[fuzzingbook-16-reducer]] — the chapter implementing `DeltaDebuggingReducer.reduce()`.

## Sources
- [[fuzzingbook-16-reducer]] — *The Fuzzing Book* Ch 16, "Reducing Failure-Inducing Inputs."
