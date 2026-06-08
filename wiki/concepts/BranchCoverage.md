---
title: "Branch Coverage"
type: concept
tags: [testing, coverage, fuzzing, dynamic-analysis, white-box-testing]
sources: [fuzzingbook-04-coverage, fuzzingbook-07-search-based-fuzzer, fuzzingbook-20-concolic-fuzzer]
last_updated: 2026-06-06
---

# BranchCoverage

**Branch coverage** is the white-box [[Coverage|coverage]] criterion that requires *each control decision in the program to be taken in both directions* — every `if`/`while`/`elif` condition must evaluate to `True` for at least one test and to `False` for at least one test. It is stricter than [[LineCoverage|statement coverage]]: the two coincide on an `if`/`else`, but diverge for a conditional with no `else` body, where statement coverage is satisfied by a single test taking the `True` path while branch coverage also demands a test where the body is skipped.

## From The Fuzzing Book — Code Coverage
[[fuzzingbook-04-coverage|Ch 4]] (Exercise 2) shows how to *simulate* branch coverage on top of the line-tracing `Coverage` class without new instrumentation: a branch is approximated by a **pair of subsequent lines executed**, so `branch_coverage(trace)` walks the ordered `trace()` and collects each consecutive `((prev_fn, prev_line), (curr_fn, curr_line))` pair. The chapter packages this as a subclass, `class BranchCoverage(Coverage)`, whose `coverage()` returns the set of executed line-pairs instead of the set of single lines. Repeating the chapter's experiments with `BranchCoverage` (via `population_branch_coverage`) shows that achieving branch coverage of `cgi_decode()` with random inputs **takes longer than statement coverage** — it is simply a harder criterion to satisfy. Some pairs only appear via an exception raised on illegal input (e.g. `%g`), and some are artifacts of running test cases back-to-back.

## From The Fuzzing Book — Search-Based Fuzzing
[[fuzzingbook-07-search-based-fuzzer|Ch 7]] turns *reaching* a specific branch (in a chosen direction) into a numeric optimization target via the [[BranchDistance|branch distance]] — a [[FitnessFunction|fitness]] measuring how close an execution is to flipping a condition. Each condition gets a *true distance* and a *false distance* (one always 0), computed by [[CodeInstrumentation|instrumenting]] comparisons with `evaluate_condition`; [[SearchBasedTesting|search-based]] algorithms ([[HillClimbing|hill climbing]], [[GeneticAlgorithm|genetic algorithms]]) then minimize that distance to cover the branch. This is the *directed* complement to Ch 4's measurement of branch coverage.

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] gives a *constraint-solving* route to covering a branch in a chosen direction, complementing Ch 7's numeric branch-distance search. [[ConcolicExecution|Concolic execution]] records the predicate of each branch on the executed path as part of the [[PathConstraint|path condition]]; *negating* that predicate and solving the result with an [[SMTSolver|SMT solver]] yields a concrete input guaranteed to flip the branch. Where Ch 7 *minimizes a distance* toward a branch, Ch 20 *solves for* it directly — exact when the constraints fall within Z3's theories, but defeated by the same implicit-control-flow blind spot.

## Connections
- [[Coverage]] — the umbrella concept.
- [[ConcolicExecution]] / [[PathConstraint]] — Ch 20 flips a branch by negating its predicate and SMT-solving the path condition.
- [[BranchDistance]] — Ch 7's fitness for *reaching* a branch (how close to flipping a condition).
- [[SearchBasedTesting]] — uses branch distance to search for branch-covering inputs.
- [[LineCoverage]] — the weaker sibling criterion; branch coverage subsumes it.
- [[TraceFunction]] — the ordered `trace()` (line pairs) is what makes the line-pair approximation possible.
- [[ControlFlow]] — branches/decisions (`if`/`while`) are exactly the control-flow constructs this criterion targets.
- [[CoverageGuidedFuzzing]] — branch/edge coverage is the feedback signal real greybox fuzzers (AFL) actually maximize.
- [[fuzzingbook-04-coverage|Ch 4]] — where the `BranchCoverage` subclass is defined.

## Sources
- [[fuzzingbook-04-coverage]] — *The Fuzzing Book* Ch 4, "Code Coverage."
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing" (branch distance as fitness for reaching a branch).
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing" (flip a branch by negating its path-condition predicate and SMT-solving).
