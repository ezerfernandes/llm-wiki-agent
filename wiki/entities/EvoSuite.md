---
title: "EvoSuite"
type: entity
tags: [tool, testing, test-generation, search-based-testing, genetic-algorithm, java]
sources: [fuzzingbook-07-search-based-fuzzer]
last_updated: 2026-06-06
---

# EvoSuite

**EvoSuite** is the canonical **search-based test-generation tool**: it automatically generates JUnit test suites for Java classes by treating test generation as an optimization problem. It uses a [[GeneticAlgorithm|genetic algorithm]] to evolve whole test suites, guided by a [[FitnessFunction|fitness function]] built from [[BranchDistance|branch distance]] (plus an "approach level" toward the target) computed via bytecode [[CodeInstrumentation|instrumentation]] — the same [[SearchBasedTesting|SBST]] principles developed in [[fuzzingbook-07-search-based-fuzzer|Ch 7]] of *The Fuzzing Book*. It was created by [[GordonFraser|Gordon Fraser]], a co-author of the book.

## Role in The Fuzzing Book
[[fuzzingbook-07-search-based-fuzzer|Ch 7]] is, in effect, a from-scratch reconstruction of EvoSuite's core ideas in Python: representing inputs as a search space, instrumenting comparisons to compute branch distances, and optimizing with [[HillClimbing|hill climbing]] and a [[GeneticAlgorithm|genetic algorithm]]. EvoSuite itself is the production-scale, whole-class embodiment of these techniques.

## Connections
- [[GordonFraser]] — its creator and a *Fuzzing Book* co-author.
- [[SearchBasedTesting]] — the discipline EvoSuite operationalizes.
- [[GeneticAlgorithm]] / [[FitnessFunction]] / [[BranchDistance]] / [[CodeInstrumentation]] — the SBST machinery it relies on.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — reconstructs EvoSuite's principles in Python.

## Sources
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
