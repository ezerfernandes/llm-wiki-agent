---
title: "Dynamic Invariant"
type: concept
tags: [testing, fuzzing, verification, specification-mining, dynamic-analysis, contracts, software-engineering]
sources: [fuzzingbook-22-dynamic-invariants]
last_updated: 2026-06-06
---

# Dynamic Invariant

A **dynamic invariant** (a "likely invariant") is a property over a function's arguments, return value, or program state that is *inferred* by observing many executions and that held in *all* of them — making it a plausible [[Precondition|pre-]] or [[Postcondition|postcondition]] of the function. The qualifier *dynamic* (versus a statically proven invariant) signals that the property is only an empirical generalization from observed runs: it may be invalidated by a future run, so its reliability grows with the diversity of executions seen. Dynamic invariants are the central artifact of [[SpecificationMining|specification mining]] and the kind of property [[Daikon]] detects.

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] derives dynamic invariants with a two-step recipe: (1) check every observed variable value against a fixed catalog `INVARIANT_PROPERTIES` of candidate properties over metavariables `X, Y, Z` (e.g. `"X > 0"`, `"X == Y + Z"`, `"isinstance(X, int)"`, `"X == len(Y)"`, `"X < Y < Z"`, `"X.startswith(Y)"`); and (2) keep only the properties that hold across *all* calls — implemented as a set *intersection* in `InvariantTracker.invariants()`, with the special variable `return_value` standing for the result. Because the set can only shrink, a single observed call *overspecializes* (`sum2(2, 2)` mines the spurious invariants `a == b` and `return_value == a * b`), while diverse runs prune it to the true invariants (`return_value == a + b`). Mined invariants are emitted by `InvariantAnnotator` as `@precondition`/`@postcondition` decorators (splitting on whether the property mentions `return_value`) or, in Exercise 9, as inline `assert` statements — making the function self-checking. The chapter is explicit that this miner is a simplification of [[Daikon]], which additionally handles data/object invariants, eliminates implied invariants, and uses statistical confidence.

## Connections
- [[SpecificationMining]] — dynamic invariants are the artifact specification mining produces.
- [[InvariantInference]] — the inference procedure (candidate properties → intersection) that yields them.
- [[Precondition]] / [[Postcondition]] — the two kinds of invariant (split by whether they mention `return_value`).
- [[Daikon]] — the seminal detector of dynamic/likely invariants.
- [[Assertion]] / [[DesignByContract]] / [[RunTimeVerification]] — how mined invariants are checked at runtime.
- [[TestGeneration]] — diverse generated runs prune overspecialized invariants down to the true ones.
- [[InvarianceTesting]] — testing that a property holds invariantly; the dynamic counterpart of asserting a mined invariant.

## Sources
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications."
