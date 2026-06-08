---
title: "Search-Based Software Testing (SBST)"
type: concept
tags: [testing, fuzzing, search-based-testing, optimization, metaheuristic, test-generation]
sources: [fuzzingbook-07-search-based-fuzzer]
last_updated: 2026-06-06
---

# SearchBasedTesting

**Search-based software testing (SBST)** treats test-data generation as an **optimization problem**: given a testing objective (e.g. reach a particular statement or branch, maximize coverage, expose a fault), define a numeric [[FitnessFunction|fitness function]] that scores how close a candidate input is to the objective, then use a [[MetaheuristicSearch|meta-heuristic search]] algorithm to find an input that optimizes it. It is the *directed* counterpart to broad coverage-driven [[Fuzzing|fuzzing]]: instead of generating many diverse inputs and hoping to hit a target, SBST actively *searches* for a specific input.

## From The Fuzzing Book — Search-Based Fuzzing
[[fuzzingbook-07-search-based-fuzzer|Ch 7]] mints this concept and builds it end-to-end. It identifies the three ingredients of any SBST problem — a **representation** of the [[SearchSpace|search space]] (with a neighborhood relation), a **fitness function** that defines a search *landscape*, and a **search algorithm** that follows the gradient. Exhaustive search (BFS/DFS) over the input domain is infeasible, so a *heuristic* (encoded as fitness) guides the search; meta-heuristics make this efficient over vast spaces. The chapter instantiates SBST first with [[HillClimbing|hill climbing]] on a toy integer branch, then with the global (1+1)EA and a full [[GeneticAlgorithm|genetic algorithm]] on the `cgi_decode` string-decoding problem, using automatically [[CodeInstrumentation|instrumented]] [[BranchDistance|branch distances]] as fitness. It closes by noting the same machinery scales to grammar-structured inputs. The real-world embodiment is [[EvoSuite]], the search-based unit-test generator co-created by book co-author [[GordonFraser|Gordon Fraser]].

## Connections
- [[MetaheuristicSearch]] — the generic search frameworks SBST instantiates.
- [[FitnessFunction]] — the objective function that turns a testing goal into a search target.
- [[BranchDistance]] — the standard fitness for reaching a specific branch.
- [[HillClimbing]] / [[EvolutionaryTesting]] / [[GeneticAlgorithm]] — the search algorithms applied.
- [[CodeInstrumentation]] — how the fitness signal is obtained from a concrete execution.
- [[SearchSpace]] — the representation + neighborhood SBST explores.
- [[Coverage]] / [[BranchCoverage]] — coverage goals are the typical SBST objective.
- [[Fuzzing]] — SBST is the objective-driven member of the fuzzing/test-generation family.
- [[EvoSuite]] / [[GordonFraser]] — the canonical SBST tool and its co-creator.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — the chapter that develops SBST.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — directed greybox fuzzing (AFLGo) already framed reachability as optimization.

## Sources
- [[fuzzingbook-07-search-based-fuzzer]] — *The Fuzzing Book* Ch 7, "Search-Based Fuzzing."
