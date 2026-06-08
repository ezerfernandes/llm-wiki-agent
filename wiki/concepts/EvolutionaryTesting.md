---
title: "Evolutionary Testing"
type: concept
tags: [optimization, metaheuristic, evolutionary-computation, search-based-testing, global-search]
sources: [fuzzingbook-07-search-based-fuzzer, fuzzingbook-26-python-fuzzer-testing-compilers]
last_updated: 2026-06-06
---

# EvolutionaryTesting

**Evolutionary testing** is the application of **evolutionary algorithms** — [[MetaheuristicSearch|meta-heuristics]] inspired by natural evolution — to test-data generation. Evolution maintains a *population* of candidate solutions under environmental pressure: fitter individuals survive and reproduce, so the population's overall [[FitnessFunction|fitness]] gradually improves. Unlike local [[HillClimbing|hill climbing]], evolutionary search is **global** — a *mutation* operator can take large steps anywhere in the [[SearchSpace|search space]], so it does not get trapped in a small neighborhood.

## From The Fuzzing Book — Search-Based Fuzzing
[[fuzzingbook-07-search-based-fuzzer|Ch 7]] introduces global/evolutionary search by replacing neighborhood enumeration with a mutation operator (`flip_random_character`, changing 1 of 10 characters). The resulting "randomized hillclimbing" — mutate the current individual, keep the offspring if it is *equal-or-better* — is exactly the **(1+1) Evolutionary Algorithm ((1+1)EA)**: a population of size 1 producing 1 offspring. The chapter stresses the crucial change from `<` to `<=` in the acceptance test: accepting *equal* fitness lets the search drift across **plateaus** that a strict hill climber cannot cross (it instead needs random restarts). A good mutation should be able, through repeated application, to reach any point in the space, while still preserving most of an individual's traits (not replacing it with a random one). The full population-based form is the [[GeneticAlgorithm|genetic algorithm]].

## From The Fuzzing Book — Testing Compilers (Python Fuzzer)
[[fuzzingbook-26-python-fuzzer-testing-compilers|Ch 26]] applies the full population-based form to *fuzzing program code* — see [[EvolutionaryFuzzing|evolutionary fuzzing]]. It evolves a population of [[DerivationTree|derivation trees]] (parsed Python) using `ISLaSolver.mutate()` as the mutation operator, a [[Coverage|coverage]]-based `tree_fitness()` (lines covered in a planted-bug checker, plus a `1/len` shortness bonus), an `evolve()`/`select()` (`POPULATION_SIZE`=100) loop, and random restarts after `GENERATIONS`. The chapter quantifies the payoff: coverage-guided evolution reaches a distributive-law compiler bug that blind mutation would need ~19,000 runs to hit — concrete evidence that a [[FitnessFunction|fitness]]-guided search beats undirected generation for structured inputs.

## Connections
- [[EvolutionaryFuzzing]] — the input-fuzzing specialization of this technique (Ch 26).
- [[GeneticAlgorithm]] — the full population-based evolutionary algorithm this chapter builds.
- [[HillClimbing]] — the (1+1)EA is "randomized hillclimbing" with `<=` acceptance.
- [[MetaheuristicSearch]] — evolutionary algorithms are nature-inspired meta-heuristics.
- [[FitnessFunction]] / [[BranchDistance]] — drives selection/survival.
- [[SearchBasedTesting]] — the testing application.
- [[GeneticPareto]] — GEPA is a modern evolutionary search over prompts (population + mutation + Pareto selection).
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — where the (1+1)EA and GA are introduced.

## Sources
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
- [[fuzzingbook-26-python-fuzzer-testing-compilers]] — *The Fuzzing Book* Ch 26, "Testing Compilers" (coverage-guided evolutionary fuzzing of Python programs).
