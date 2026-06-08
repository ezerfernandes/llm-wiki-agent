---
title: "Evolutionary Fuzzing"
type: concept
tags: [fuzzing, evolutionary-computation, coverage-guided, search-based-testing, compiler-testing]
sources: [fuzzingbook-26-python-fuzzer-testing-compilers]
last_updated: 2026-06-06
---

# Evolutionary Fuzzing

**Evolutionary fuzzing** applies an evolutionary algorithm to test-input generation: maintain a *population* of inputs, produce *offspring* by **mutation**, score each by a **[[FitnessFunction|fitness function]]** (most often [[Coverage|code coverage]]), and keep the fittest as the next generation ("survival of the fittest"). Over many generations the population drifts toward inputs that cover more code and thus stand a better chance of triggering bugs. It is the input-fuzzing realization of [[EvolutionaryTesting|evolutionary/search-based testing]] and is the conceptual core of modern [[CoverageGuidedFuzzing|coverage-guided fuzzers]] like [[AFL]].

## From The Fuzzing Book — Testing Compilers (Python Fuzzer)
[[fuzzingbook-26-python-fuzzer-testing-compilers|Ch 26]] builds a complete evolutionary fuzzer over **Python programs** to reach a planted compiler bug (`has_distributive_law()` — code of the form `<elem> * (<elem> + <elem>)`):
- **Population** of [[DerivationTree|derivation trees]] (parsed Python via [[ISLa|`ISLaSolver`]]), seeded from a single `sum()` function.
- **Mutation** via `ISLaSolver.mutate(candidate, min_mutations=1, max_mutations=1)` — re-expand a random subtree.
- **Fitness** = `tree_fitness()`, which measures lines of `has_distributive_law()` covered (using the [[Coverage]] context manager) plus a `1/len(code_str)` bonus to penalize bloat.
- **`evolve()`** adds `OFFSPRING` mutated children per member; **`select()`** sorts by fitness and truncates to `POPULATION_SIZE` (=100); the driver loops up to `GENERATIONS` (=100) per trial with random restarts.

The chapter shows mutation alone (without coverage guidance) is far weaker: mutating an input *syntactically close* to a bug-triggering one is much faster than from scratch (`how_many_mutations('2 + 2')` ≪ `how_many_mutations('2')`), and a grammar-count estimate puts blind discovery of the distributive-law bug at ~19,000 runs — concrete evidence that coverage-guided evolution wins for structured inputs. It suggests [[fuzzingbook-16-reducer|Delta Debugging]] to shrink the discovered bug-triggering program afterward.

## Connections
- [[EvolutionaryTesting]] — the general search-based-testing technique this specializes to fuzzing.
- [[GeneticAlgorithm]] / [[FitnessFunction]] — the underlying algorithm and the scoring signal.
- [[Coverage]] / [[CoverageGuidedFuzzing]] — coverage as the fitness used to guide evolution; the basis of AFL-style fuzzers.
- [[PythonFuzzer]] / [[ISLa]] — the generator/mutator backend (`mutate()` over derivation trees).
- [[DerivationTree]] — the structured representation the population members take.
- [[CompilerTesting]] — the domain in which Ch 26 deploys evolutionary fuzzing.
- [[MutationBasedFuzzing]] — mutation as the offspring operator.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — the search-based/evolutionary foundations reused here.

## Sources
- [[fuzzingbook-26-python-fuzzer-testing-compilers]] — *The Fuzzing Book* Ch 26, "Testing Compilers (Python Fuzzer)."
