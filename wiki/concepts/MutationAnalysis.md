---
title: "Mutation Analysis"
type: concept
tags: [testing, fuzzing, mutation-testing, test-adequacy, quality, software-engineering, security]
sources: [fuzzingbook-08-mutation-analysis]
last_updated: 2026-06-06
---

# Mutation Analysis

**Mutation analysis** (a.k.a. **mutation testing**) is a technique for assessing the quality of a *test suite* by seeding small artificial faults — [[Mutant|mutants]] — into the **program under test** and measuring what fraction the suite detects (the [[MutationScore|mutation score]]). The premise: if a suite cannot catch deliberately injected faults, it will also miss real bugs. A mutant the suite detects (a test fails on it) is said to be **killed**; one that goes undetected **survives**.

> **Direction matters.** Mutation analysis mutates the *program* to grade *tests*. This is the *opposite* of [[MutationBasedFuzzing|mutation-based fuzzing]] ([[fuzzingbook-05-mutation-fuzzer|Ch 5]]), which mutates the *input* to find bugs in a program. The shared word "mutation" is the only thing they have in common.

Mutation analysis is a [[TestAdequacy|test-adequacy criterion]] that strictly dominates [[Coverage|code coverage]]: it accounts for the strength of a suite's [[Assertion|assertions]]/[[TestOracle|oracle]], which coverage ignores entirely.

## From The Fuzzing Book — Mutation Analysis
[[fuzzingbook-08-mutation-analysis|Ch 8]] mints this concept. It first shows *why coverage is not enough*: a `triangle()` classifier tested by a `strong_oracle()` (asserts the exact category) and by a `weak_oracle()` (only asserts "not equilateral") obtains **identical** statement [[Coverage|coverage]], yet mutation analysis cleanly separates them — 100% vs 20% [[MutationScore|mutation score]]. The technique rests on two assumptions: the **Competent Programmer Hypothesis** / *Finite Neighborhood Hypothesis* (residual faults are tiny, single-token deviations from a correct program) and the **Coupling Effect** (tests that kill small faults in isolation tend to kill the complex faults composed from them), which together justify enumerating only *small* program variants. The chapter implements two frameworks over Python's [[AbstractSyntaxTree|`ast`]] module — `MuFunctionAnalyzer` for individual functions (each `Mutant` is a context manager that swaps the mutated function into `globals()`) and `MuProgramAnalyzer` for whole modules driven by [[UnitTesting|`unittest`]] suites via `MutantTestRunner` — both using a statement-deletion [[MutationOperator|mutation operator]]. It frames a test suite as "a program whose input is the program under test," so mutation analysis effectively *fuzzes the test suite*, and any surviving mutant is a bug in the suite. It is also a general tool to grade fuzzers and static/symbolic-execution frameworks, not just hand-written tests.

## Connections
- [[Mutant]] — the individual seeded fault; killed vs survived.
- [[MutationScore]] — the headline metric (killed / valid mutants).
- [[MutationOperator]] — the transformation rule that generates mutants.
- [[EquivalentMutant]] — the central limitation; undecidable to detect, depresses the score.
- [[TestAdequacy]] — the adequacy criterion this realizes; dominates coverage adequacy.
- [[FaultInjection]] — the manual precursor mutation analysis automates and de-biases.
- [[AbstractSyntaxTree]] — the program representation that is mutated.
- [[Coverage]] / [[fuzzingbook-04-coverage|Ch 4]] — the weaker adequacy measure this supersedes.
- [[MutationBasedFuzzing]] / [[fuzzingbook-05-mutation-fuzzer|Ch 5]] — contrast: mutates inputs, not programs.
- [[Testing]] / [[UnitTesting]] / [[TestOracle]] / [[Assertion]] — detection depends on oracle/assertion strength.
- [[DeltaDebugging]] / [[fuzzingbook-16-reducer|Ch 16]] — tightens the residual-defect upper bound (Exercise 4).
- [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] — Chao's estimator for immortal/equivalent mutants.

## Sources
- [[fuzzingbook-08-mutation-analysis]] — *The Fuzzing Book* Ch 8, "Mutation Analysis."
