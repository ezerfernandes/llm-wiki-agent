---
title: "Gordon Fraser"
type: entity
tags: [person, author, researcher, software-engineering, testing, search-based-testing, fuzzing]
sources: [fuzzingbook-07-search-based-fuzzer]
last_updated: 2026-06-06
---

# Gordon Fraser

**Gordon Fraser** is a software-engineering researcher best known for **search-based software testing (SBST)** and automated test generation. He is the original creator of **[[EvoSuite]]**, the influential search-based unit-test generator for Java that uses [[GeneticAlgorithm|genetic-algorithm]] search with [[BranchDistance|branch-distance]] fitness to generate whole test suites. He is a co-author of *[[fuzzingbook-01-tours|The Fuzzing Book]]* (CISPA, 2024) alongside [[AndreasZeller|Andreas Zeller]], Rahul Gopinath, [[MarcelBohme|Marcel Böhme]], and Christian Holler.

## Role in The Fuzzing Book
Fraser's SBST research is the direct source of *The Fuzzing Book*'s search-based chapter. [[fuzzingbook-07-search-based-fuzzer|Ch 7]] develops exactly the machinery underlying [[EvoSuite]] — representing test generation as a search problem, computing [[FitnessFunction|fitness]] via automatic [[CodeInstrumentation|branch instrumentation]], and optimizing with [[HillClimbing|hill climbing]] and [[GeneticAlgorithm|genetic algorithms]] ([[SearchBasedTesting|SBST]]).

## Connections
- [[EvoSuite]] — the search-based test-generation tool he created.
- [[SearchBasedTesting]] — the field he is a leading contributor to.
- [[GeneticAlgorithm]] / [[FitnessFunction]] / [[BranchDistance]] — the SBST machinery his work and Ch 7 build on.
- [[AndreasZeller]] / [[MarcelBohme]] — co-authors of *The Fuzzing Book*.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — the chapter rooted in his SBST research.

## Sources
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
