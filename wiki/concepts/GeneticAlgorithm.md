---
title: "Genetic Algorithm"
type: concept
tags: [optimization, metaheuristic, evolutionary-computation, search-based-testing, genetic-algorithm]
sources: [fuzzingbook-07-search-based-fuzzer]
last_updated: 2026-06-06
---

# GeneticAlgorithm

A **genetic algorithm (GA)** is the best-known population-based evolutionary [[MetaheuristicSearch|meta-heuristic]]. Solutions are *genetically encoded*: a **chromosome** is a sequence of **genes**, the encoded form is the **genotype**, and the actual solution it represents is the **phenotype** — [[FitnessFunction|fitness]] is measured on the phenotype. The GA evolves a population through repeated **selection → crossover → mutation**: fitter individuals are more likely to reproduce, crossover recombines parental genes, and mutation introduces new genetic material, so the population's fitness improves generation over generation until an optimum or a budget limit is reached.

## From The Fuzzing Book — Search-Based Fuzzing
[[fuzzingbook-07-search-based-fuzzer|Ch 7]] builds a GA to generate `cgi_decode` inputs, treating each character of a fixed-length string as a gene. The components:
- **`create_population(size)`** — random chromosomes; **`evaluate_population`** pairs each with its fitness `(individual, fitness)`.
- **`selection(evaluated_population, tournament_size)`** — **tournament selection**: pick `tournament_size` random individuals and return the best. `tournament_size` controls *selective pressure* — too large causes premature convergence (loss of diversity), too small inhibits evolution (a small value like 5 is typical).
- **`crossover(parent1, parent2)`** — single-point crossover at a random cut, producing two offspring (applied with probability 0.7).
- **`mutate(chromosome)`** — each gene mutates with probability `P = 1/len`, and a mutated gene is perturbed by sampling a **Gaussian** (σ=100) around its current value, favoring small changes over random replacement.
- **`genetic_algorithm()`** — evolves 100 individuals for up to 1000 generations, each new generation fully replacing the old, halting when best fitness reaches 0.

The chapter positions the GA as the *global* alternative to [[HillClimbing|hill climbing]]: more flexible and scaling well to large test-generation problems (e.g. the UTF-16 space where local search stalls).

## Connections
- [[EvolutionaryTesting]] — the GA is the full population-based evolutionary algorithm (the (1+1)EA is its degenerate single-individual form).
- [[MetaheuristicSearch]] — a GA is a nature-inspired global meta-heuristic.
- [[FitnessFunction]] / [[BranchDistance]] — measured on the phenotype to drive selection.
- [[HillClimbing]] — the local-search alternative the GA scales past.
- [[SearchBasedTesting]] — the testing application.
- [[GeneticPareto]] — GEPA extends the GA template (population + mutation + crossover) with Pareto-frontier selection for prompt optimization.
- [[EvoSuite]] / [[GordonFraser]] — EvoSuite applies a GA with branch-distance fitness to unit-test generation.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — where this GA is built.

## Sources
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
