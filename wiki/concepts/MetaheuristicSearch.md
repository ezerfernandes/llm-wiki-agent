---
title: "Meta-Heuristic Search"
type: concept
tags: [optimization, metaheuristic, search, testing, evolutionary-computation]
sources: [fuzzingbook-07-search-based-fuzzer]
last_updated: 2026-06-06
---

# MetaheuristicSearch

A **meta-heuristic** is a generic, problem-independent search framework that uses a *heuristic* (an estimate of how good a candidate is) to explore a [[SearchSpace|search space]] efficiently, without examining every point. The "meta" denotes that the framework is abstract and can be *instantiated* differently for different problems by supplying a representation and a [[FitnessFunction|fitness function]]. Meta-heuristics include local search (e.g. [[HillClimbing|hill climbing]], simulated annealing) and population-based / nature-inspired methods (e.g. [[GeneticAlgorithm|genetic algorithms]], swarm intelligence, chemical-reaction-inspired algorithms). They trade guaranteed optimality for the ability to handle vast search spaces where exhaustive search (BFS/DFS) is infeasible.

## From The Fuzzing Book — Search-Based Fuzzing
[[fuzzingbook-07-search-based-fuzzer|Ch 7]] uses meta-heuristic search as the engine of [[SearchBasedTesting|search-based software testing]]. It explains that classic search (breadth/depth-first) is unrealistic for test generation because it may have to examine all possible inputs, whereas a meta-heuristic guided by a fitness "landscape" can reach a target quickly. The chapter contrasts **local** meta-heuristics — [[HillClimbing|hill climbing]] variants that only inspect a candidate's immediate neighborhood — with **global** ones — the (1+1)EA and full [[GeneticAlgorithm|genetic algorithm]] that take larger steps via mutation/crossover and scale to large spaces (e.g. the UTF-16 `cgi_decode` problem where the local neighborhood explodes to 65 536 candidates per character).

## Connections
- [[SearchBasedTesting]] — applies meta-heuristics to test-data generation.
- [[HillClimbing]] — the simplest (local) meta-heuristic.
- [[EvolutionaryTesting]] / [[GeneticAlgorithm]] — global, population-based meta-heuristics.
- [[FitnessFunction]] — the heuristic estimate a meta-heuristic optimizes.
- [[SearchSpace]] — the representation + neighborhood being searched.
- [[GeneticPareto]] — GEPA is a modern evolutionary meta-heuristic (population + Pareto selection).
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — the chapter that introduces these algorithms.

## Sources
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
