---
title: "Hill Climbing"
type: concept
tags: [optimization, metaheuristic, local-search, search-based-testing]
sources: [fuzzingbook-07-search-based-fuzzer]
last_updated: 2026-06-06
---

# HillClimbing

**Hill climbing** is the simplest [[MetaheuristicSearch|meta-heuristic]] — a **local search**: start from a random point, repeatedly examine the immediate neighborhood, and move to a neighbor with better [[FitnessFunction|fitness]] until none exists. Its great weakness is getting stuck at a **local optimum** or on a fitness **plateau**, since it only ever sees nearby candidates and never moves to something worse. (When fitness is a distance to be minimized, "climbing" is really descending into a valley.)

## From The Fuzzing Book — Search-Based Fuzzing
[[fuzzingbook-07-search-based-fuzzer|Ch 7]] applies hill climbing to [[SearchBasedTesting|search-based test generation]] and presents three variants:
- **`hillclimber`** — moves to the *first* neighbor (from `neighbors(x, y)`) with strictly better fitness (`new_fitness < fitness`).
- **`steepest_ascent_hillclimber`** — evaluates *all* neighbors and takes the best; needs fewer iterations but runs more tests per iteration.
- **`restarting_hillclimber`** — when no neighbor improves (a local optimum / plateau), it performs a **random restart** from a fresh random point, the standard escape hatch.

On the toy `test_me` branch the fitness landscape has a clean gradient and hill climbing always succeeds; on `test_me2`/`bad_fitness` the landscape has local optima, motivating restarts. Applied to strings, `hillclimb_cgi` reuses the identical algorithm over the `neighbor_strings` edit-distance-1 neighborhood and reliably finds valid hex inputs — but on the UTF-16 space the neighborhood (65 536 candidates per character) becomes too large, motivating the move to global [[EvolutionaryTesting|evolutionary]] search and the [[GeneticAlgorithm|genetic algorithm]].

## Connections
- [[MetaheuristicSearch]] — hill climbing is its simplest (local) instance.
- [[FitnessFunction]] / [[BranchDistance]] — the signal the climb follows.
- [[SearchSpace]] — the neighborhood relation hill climbing walks.
- [[EvolutionaryTesting]] — replacing neighborhood enumeration with mutation gives the global (1+1)EA ("randomized hillclimbing").
- [[GeneticAlgorithm]] — the population-based global alternative when the neighborhood is too large.
- [[SearchBasedTesting]] — the application here.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — where the hillclimber variants are built.

## Sources
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
