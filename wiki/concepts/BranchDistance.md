---
title: "Branch Distance"
type: concept
tags: [testing, search-based-testing, fitness-function, instrumentation, coverage]
sources: [fuzzingbook-07-search-based-fuzzer]
last_updated: 2026-06-06
---

# BranchDistance

**Branch distance** is the standard [[FitnessFunction|fitness function]] used in [[SearchBasedTesting|search-based testing]] to measure how close a program execution is to flipping a particular branch condition. Each condition has **two** distances — a *true distance* (how far it is from evaluating to `True`) and a *false distance* (how far from `False`); by construction exactly one of them is 0 on any execution. Driving an input toward a target branch means minimizing the relevant distance toward 0.

## From The Fuzzing Book — Search-Based Fuzzing
[[fuzzingbook-07-search-based-fuzzer|Ch 7]] derives branch distance from the intuition that `abs(x - 2*(y+1))` quantifies "how false" an equality is, then gives the general distance table for comparison operators:

| Condition | Distance True | Distance False |
|---|---|---|
| `a == b` | `abs(a-b)` | `1` |
| `a != b` | `1` | `abs(a-b)` |
| `a < b` | `b-a+1` | `a-b` |
| `a <= b` | `b-a` | `a-b+1` |
| `a > b` | `a-b+1` | `b-a` |

The constant `+1` prevents a 0 distance on the boundary (e.g. `a < b` with `a == b` is not yet true). For **compound** predicates, the distance to make `A and B` true is the *sum* of the operand distances, and for `A or B` it is the *minimum*; in practice this is complicated by nested/negated conditions and **short-circuit evaluation** (evaluating `B` for distance when it should be skipped can trigger unwanted side effects). For **membership** (`x in S`), distance is the difference to the nearest element (`distance_character`). The chapter computes these via [[CodeInstrumentation|instrumentation]]: `evaluate_condition(num, op, lhs, rhs)` replaces each comparison, records true/false distances into the global `distances_true`/`distances_false` maps (keeping the closest via `update_maps`/`min` across repeated executions), and returns the boolean. To build a fitness over a whole *path*, distances for the chosen branches are `normalize`d and summed.

## Connections
- [[FitnessFunction]] — branch distance is the canonical fitness for reaching a branch.
- [[CodeInstrumentation]] — `evaluate_condition`/`BranchTransformer` compute and record the distances.
- [[BranchCoverage]] — the coverage criterion branch distance is designed to satisfy (take a branch in a given direction).
- [[SearchBasedTesting]] / [[MetaheuristicSearch]] — the search that minimizes branch distance.
- [[HillClimbing]] / [[GeneticAlgorithm]] — algorithms that consume this fitness.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — where branch distance is defined and instrumented.

## Sources
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
