---
title: "The Fuzzing Book Ch 07 — Search-Based Fuzzing"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, sbst, search-based-testing, metaheuristic, hill-climbing, genetic-algorithm, fitness-function, branch-distance, instrumentation]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-07-search-based-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Search-Based Fuzzing

## Summary
Chapter 7 of *The Fuzzing Book* (Part II — Lexical Fuzzing) reframes test-input generation as an **optimization problem** and solves it with **[[MetaheuristicSearch|meta-heuristic search]]** — the field known as [[SearchBasedTesting|search-based software testing (SBST)]]. Where the [[fuzzingbook-06-greybox-fuzzer|Ch 6]] greybox fuzzer *maximizes coverage broadly*, this chapter searches for **specific** inputs that reach a chosen target branch. The recipe has three ingredients: a *representation* of the search space (e.g. integer tuples, or fixed-length strings with an edit-distance neighborhood), a *[[FitnessFunction|fitness function]]* that estimates how close an input is to the goal, and a *search algorithm* that follows the fitness gradient. It develops the fitness signal from a hand-written distance (`calculate_distance`) into a general **[[BranchDistance|branch distance]]** computed by automatic AST [[CodeInstrumentation|instrumentation]] (`BranchTransformer`, `create_instrumented_function`, `evaluate_condition`), then climbs the resulting landscape with [[HillClimbing|hill climbing]] (`hillclimber`, `steepest_ascent_hillclimber`, `restarting_hillclimber`) before scaling to large spaces with the global [[EvolutionaryTesting|evolutionary]] (1+1)EA and a full [[GeneticAlgorithm|genetic algorithm]] (`genetic_algorithm`). The central worked examples are the toy `test_me(x, y)` branch `x == 2*(y+1)` and the [[fuzzingbook-04-coverage|Ch 4]] `cgi_decode()` string decoder. Prerequisite: code coverage ([[fuzzingbook-04-coverage|Ch 4]]); it forwards to grammar-aware evolutionary fuzzing.

## Key Concepts
- **[[SearchBasedTesting|Search-based software testing (SBST)]]** — generating test data by *searching* the input space for inputs satisfying an objective (e.g. reach a statement/branch), rather than enumerating or randomly sampling. Exhaustive search (BFS/DFS) is infeasible over the input domain; domain knowledge encoded as a *heuristic* makes it tractable.
- **[[MetaheuristicSearch|Meta-heuristic search]]** — generic, problem-independent search frameworks (hill climbing, evolutionary algorithms, swarm/annealing methods) instantiated per problem via a representation and a fitness function; far more efficient than exhaustive search over vast spaces. Often nature-inspired (evolution, swarm intelligence, chemical reactions).
- **Representation & neighborhood** — the encoding of a candidate solution and which candidates are "adjacent." For `test_me` the representation is an integer tuple `(x, y)` with a Moore neighborhood (`neighbors(x, y)` returns the 8 adjacent points, bounded by `MIN`/`MAX`). For strings, `neighbor_strings(x)` builds the edit-distance-1 neighbors (each character ±1 in ASCII).
- **[[FitnessFunction|Fitness function]]** — maps each point of the [[SearchSpace|search space]] to a numeric "goodness," defining a *search landscape* whose optimum is the solution. To cover branch `x == 2*(y+1)`, fitness is the distance `abs(x - 2*(y+1))` (smaller = better, optimum = 0). Minimization and maximization are interchangeable.
- **[[BranchDistance|Branch distance]]** — a fitness measure of how close a condition is to flipping. Each condition has a *true distance* and a *false distance*, one of which is always 0. The chapter gives the standard table: `a==b` → true `abs(a-b)`, false `1`; `a<b` → true `b-a+1`, false `a-b`; etc. (the `+1` constant avoids a 0 distance on the boundary). Conjunctions sum the operand distances; disjunctions take the minimum. Membership (`x in S`) uses the distance to the nearest element (`distance_character`).
- **[[CodeInstrumentation|Instrumentation]]** — adding code to observe values at a branch so fitness reflects the *concrete execution*, since the compared values may be derived deep in the code. Naïve approaches use a global `distance` variable; the robust approach *transforms* the comparison into a call `evaluate_condition(num, op, lhs, rhs)` so operands evaluate exactly once (preserving side effects and short-circuiting). `evaluate_condition` records true/false distances into global maps `distances_true`/`distances_false` via `update_maps` (keeping the closest, `min`, across repeated executions).
- **Automatic AST instrumentation** — `BranchTransformer(ast.NodeTransformer)` overrides `visit_Compare` to rewrite each comparison into an `evaluate_condition(...)` call and `visit_FunctionDef` to suffix `_instrumented`; `create_instrumented_function(f)` parses, transforms, `compile`s, and `exec`s the instrumented function into the module so `cgi_decode_instrumented` becomes callable.
- **Fitness over multiple branches & normalization** — to drive a specific *path* (e.g. valid hex: condition 1 true, 2 false, 3/4/5 true), `get_fitness_cgi` sums the relevant branch distances. Distances are first put through `normalize(x) = x/(1+x)` (maps `[0,∞) → [0,1)`, order-preserving) so large-valued conditions don't dominate; an unexecuted branch contributes the maximum 1.0.
- **[[HillClimbing|Hill climbing]]** — the simplest meta-heuristic: from a random start, move to a better neighbor and repeat. `hillclimber` moves to the *first* improving neighbor; `steepest_ascent_hillclimber` evaluates all neighbors and takes the best (fewer iterations, more tests each); `restarting_hillclimber` adds **random restarts** to escape *local optima* / plateaus.
- **[[EvolutionaryTesting|Global search]] & the (1+1)EA** — replacing neighborhood enumeration with a *mutation* operator (`flip_random_character`, one character of 10) yields "randomized hillclimbing," equivalent to the **(1+1) Evolutionary Algorithm**: a population of 1 producing 1 offspring, accepting offspring of *equal-or-better* fitness (`<=`) to traverse plateaus.
- **[[GeneticAlgorithm|Genetic algorithm]]** — a population-based evolutionary algorithm. `create_population` builds random chromosomes; `evaluate_population` pairs each with its fitness; `selection` is **tournament selection** (the `tournament_size` controls selective pressure / premature convergence); `crossover` splits two parents at a random cut to produce two offspring (applied with prob. 0.7); `mutate` perturbs genes with probability `1/len` using a Gaussian (σ=100) around the current character. `genetic_algorithm()` evolves 100 individuals up to 1000 generations toward the `cgi_decode` Unicode target.

## Key Claims
- A meta-heuristic search problem is fully specified by three parts: an **algorithm**, a **representation**, and a **fitness function**.
- For test generation, fitness functions estimate how close an execution comes to a target location; obtaining that distance requires **instrumentation** to observe the compared values during execution.
- Local search (hill climbing) works well only when the neighborhood is well-defined and small; on the small ASCII `cgi_decode` space it reliably solves the problem, but on the UTF-16 space (65 536 characters/position) the neighborhood explodes and search becomes "unreasonably long."
- A single global `distance` variable is too clumsy and unsafe for real programs: branch conditions can have side effects and short-circuit, so the operands must be evaluated exactly once — achieved by *transforming* comparisons into `evaluate_condition` calls rather than *adding* tracing alongside the original comparison.
- Branch distances of different conditions must be **normalized** (`x/(1+x)`) before summing, otherwise a condition over large values biases the search; an unexecuted branch must contribute the maximum normalized value (1.0).
- The crucial difference between hill climbing and the (1+1)EA is `new_fitness <= fitness` vs `new_fitness < fitness`: accepting *equal* fitness lets the randomized search drift across fitness **plateaus** that would otherwise trap a strict hill climber (which instead relies on random restarts).
- Global search algorithms like genetic algorithms are far more flexible and scale to larger test-generation problems than local search.
- The same search machinery generalizes from simple integer/string inputs to **complex, grammar-structured** test inputs (the chapter's "Next Steps").

## Key Quotes
> "When we have an idea of what we are looking for, then we can *search* for it. ... if we can estimate which of several program inputs is closer to the one we are looking for, then this information can guide us to reach the target quicker – this information is known as a *heuristic*." — framing SBST.

> "A meta-heuristic search problem consists of an algorithm, a representation, and a fitness function." — Lessons Learned.

> "Local search algorithms like hillclimbing work well when the neighborhood is well-defined and not too large. Global search algorithms like genetic algorithms are very flexible and scale up well to larger test problems." — Lessons Learned.

## Connections
- [[SearchBasedTesting]] — the discipline this chapter mints (test generation as search/optimization).
- [[MetaheuristicSearch]] — the generic search frameworks (hill climbing, EA, GA) it instantiates.
- [[FitnessFunction]] — the heuristic that turns "reach a branch" into an optimization objective.
- [[BranchDistance]] — the concrete fitness for covering a target branch (true/false distance table, conjunction = sum, disjunction = min).
- [[CodeInstrumentation]] — AST rewriting (`BranchTransformer`, `evaluate_condition`) that observes branch operands without double-evaluating side effects.
- [[HillClimbing]] — first/steepest-ascent/restarting local search over the neighborhood.
- [[EvolutionaryTesting]] — the (1+1)EA bridge from local to global search; population-based evolution.
- [[GeneticAlgorithm]] — population, tournament selection, crossover, Gaussian mutation (`genetic_algorithm`).
- [[SearchSpace]] — the representation + neighborhood the search explores.
- [[BranchCoverage]] / [[Coverage]] — the search *target* (a specific branch) is a coverage goal; instrumentation extends Ch 4's coverage idea with distance.
- [[Fuzzing]] — search-based fuzzing as the *directed/objective-driven* member of the fuzzing family.
- [[GeneticPareto]] — GEPA's evolutionary prompt optimization is a modern instance of the GA template (population + mutation + Pareto selection) described here.
- [[GordonFraser]] — book co-author; co-creator of [[EvoSuite]], the canonical search-based unit-test generator built on exactly these ideas.
- [[EvoSuite]] — real-world SBST tool applying branch-distance fitness + GA to whole-class test generation.
- [[AndreasZeller]] — lead author of *The Fuzzing Book*.
- [[fuzzingbook-04-coverage|Ch 4]] — prerequisite; supplies coverage and the `cgi_decode` running example.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — sibling: greybox fuzzing already framed *directed* fuzzing (AFLGo) as optimization via call-graph distance; this chapter generalizes the optimization view.

## Contradictions
- None identified.
