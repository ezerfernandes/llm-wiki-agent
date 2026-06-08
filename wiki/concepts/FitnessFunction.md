---
title: "Fitness Function"
type: concept
tags: [optimization, metaheuristic, search, testing, evolutionary-computation]
sources: [fuzzingbook-07-search-based-fuzzer]
last_updated: 2026-06-06
---

# FitnessFunction

A **fitness function** is the heuristic at the heart of every [[MetaheuristicSearch|meta-heuristic search]]: it maps each point of the [[SearchSpace|search space]] to a numeric **fitness value** estimating how good that candidate is relative to the objective. Plotting fitness as elevation over the search space yields a **fitness landscape** whose optimum is the solution (the highest peak, or — when minimizing distance — the lowest valley). Any maximization objective can be re-expressed as minimization and vice versa, so "better" may mean smaller. The fitness function encodes the *domain knowledge* that makes search tractable; its quality (gradient, absence of large plateaus) largely determines whether search succeeds.

## From The Fuzzing Book — Search-Based Fuzzing
[[fuzzingbook-07-search-based-fuzzer|Ch 7]] introduces fitness functions for [[SearchBasedTesting|search-based test generation]], where the objective is reaching a target branch. For the toy condition `x == 2*(y+1)`, fitness is the hand-written distance `calculate_distance(x, y) = abs(x - 2*(y+1))` (optimum 0). The chapter generalizes this to the [[BranchDistance|branch distance]] computed by [[CodeInstrumentation|instrumentation]], and shows two refinements needed for real fitness functions: (1) **normalization** — pass each branch distance through `normalize(x) = x/(1+x)` (order-preserving, maps to `[0,1)`) before summing across conditions, so a condition over large values doesn't dominate; and (2) an **unexecuted branch** must contribute the maximum (1.0), strictly worse than any executed branch. It also illustrates how a poor fitness landscape (the `bad_fitness`/`test_me2` example) creates **local optima** and **plateaus** that trap naive hill climbers.

## Connections
- [[MetaheuristicSearch]] — fitness is the heuristic these algorithms optimize.
- [[BranchDistance]] — the canonical fitness for reaching a branch.
- [[CodeInstrumentation]] — how the fitness value is observed from a concrete execution.
- [[SearchBasedTesting]] — fitness turns a testing goal into a search objective.
- [[HillClimbing]] / [[GeneticAlgorithm]] — algorithms driven by the fitness signal.
- [[SearchSpace]] — the domain the fitness function maps over.
- [[GeneticPareto]] — GEPA uses LLM-read fitness signals to direct mutation rather than blind perturbation.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — the chapter introducing fitness functions for testing.

## Sources
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
