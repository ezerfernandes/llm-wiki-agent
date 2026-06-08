---
title: "The Fuzzing Book Ch 05 — Mutation-Based Fuzzing"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, mutation-fuzzing, coverage-guided, seed-inputs, afl]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-05-mutation-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Mutation-Based Fuzzing

## Summary
The third chapter of Part II (Lexical Fuzzing) confronts the central weakness of the blackbox random [[RandomFuzzer|`RandomFuzzer`]] from [[fuzzingbook-03-fuzzer|Ch 3]]: random strings are almost always *syntactically invalid* and get rejected at the input-parsing boundary, never reaching deeper code. The chapter's fix is **mutation-based fuzzing** — start from a known-*valid* **seed input** and apply small string mutations (delete, insert, bit-flip a character) that are likely to keep it valid while exercising new behavior. It builds this up incrementally: standalone mutation functions, a `mutate()` dispatcher, the `MutationFuzzer` class (a [[RandomFuzzer|`Fuzzer`]] subclass) that applies *multiple* mutations to a population, and finally `MutationCoverageFuzzer`, which keeps only mutated inputs that achieve *new* [[Coverage|coverage]] — turning the population into an evolving corpus. The running example is `http_program()`, a tiny URL validator: random fuzzing would need ~years to stumble onto a valid `http://` prefix, whereas mutating a single seed URL produces valid inputs immediately. The chapter explicitly introduces the core ideas of the [[AFL|American Fuzzy Lop]] fuzzer and sets up [[fuzzingbook-06-greybox-fuzzer|Ch 6]]'s power-scheduled greybox extension.

## Key Concepts
- **[[MutationBasedFuzzing|Mutation-based fuzzing]]** — generate new inputs by perturbing existing valid ones rather than synthesizing from scratch (contrasted with *generational/generative* fuzzing). Mutations from valid seeds have a high chance of staying valid, so they reach functionality beyond input processing.
- **Mutation operators** (`delete_random_character`, `insert_random_character`, `flip_random_character`) — three primitive string mutations; `delete` removes a char at a random position, `insert` adds a random printable ASCII char (32–126), `flip` XORs a random bit (`1 << randint(0,6)`) of a random char. The free function `mutate(s)` (the [[Mutator|mutator]]) picks one operator uniformly via `random.choice`.
- **[[SeedInput|Seed input]]** — a valid starting input (here `"http://www.google.com/search?q=fuzzing"`) supplied to the fuzzer; the corpus is seeded with it before any mutation begins.
- **`MutationFuzzer`** — a [[RandomFuzzer|`Fuzzer`]] subclass taking `seed: List[str]`, `min_mutations=2`, `max_mutations=10`. It keeps a `population` (initialised to the seed), serves each seed once via `fuzz()`, then calls `create_candidate()` — `random.choice(self.population)` followed by `randint(min,max)` chained `mutate()` calls. The chapter demonstrates the "`class C(C): ...`" reopening hack to add methods incrementally.
- **`FunctionRunner` / `FunctionCoverageRunner`** — [[Runner|`Runner`]] subclasses that wrap a Python callable: `FunctionRunner.run()` returns `(result, PASS|FAIL)`, and `FunctionCoverageRunner` additionally records `Coverage()` of the call so `coverage()` yields the executed `Location` set after each run.
- **[[MutationCoverageFuzzer|`MutationCoverageFuzzer`]]** — a `MutationFuzzer` subclass implementing [[CoverageGuidedFuzzing|coverage-guided fuzzing]]. It tracks `coverages_seen: Set[frozenset]`; in `run()`, an input that *passes* and yields a `frozenset(coverage())` not yet seen is appended to `population` and its coverage recorded. The population thus *evolves* toward maximal coverage diversity — exactly [[AFL|AFL]]'s "keep inputs that find a new path" heuristic.
- **`is_valid_url()` / `http_program()`** — the worked target: `urlparse()`-based URL validation that raises `ValueError` for unsupported schemes or empty hosts; `population_coverage()` plots the cumulative coverage curve of the evolved population.

## Key Claims
- Random fuzzing of `http_program()` has only a ~`1/(96**7) + 1/(96**8)` chance per input of producing a valid scheme prefix; at measured per-run cost this is on the order of *months to years* to get a single valid URL — empirically motivating mutation over generation.
- Mutating a *valid* seed URL with a single `mutate()` yields a high proportion of still-valid inputs (a large fraction of 20 trials), because small perturbations usually preserve structure.
- Reaching a rarer prefix like `https://` from an `http://` seed needs roughly `3 * 96 * len(seed)` mutations on average (pick the insert mutator `1/3`, the right char `'s'` `1/96`, the right position `1/len`) — affordable, unlike from-scratch generation.
- Multiple chained mutations (e.g. 50) progressively destroy the seed's recognizability but increase input *variety*; the cost is a rising chance of invalidity, which is why guidance is needed.
- `MutationCoverageFuzzer.runs(http_runner, trials=10000)` evolves a population in which *every* member is valid and has *distinct* coverage, covering varied combinations of schemes, paths, queries, and fragments — guidance is what makes the variety productive.
- The strategy generalizes to any program for which coverage can be captured: it "happily explore[s] one path after the other," needing only a coverage signal — the same principle scaled up by [[AFL]] and the next chapter's greybox fuzzer.

## Key Quotes
> "Most randomly generated inputs are syntactically invalid and thus are quickly rejected by the processing program. To exercise functionality beyond input processing, we must increase chances to obtain valid inputs." — the chapter's framing of why mutation beats generation.

> "Just like our examples above, AFL evolves test cases that have been successful – but for AFL, 'success' means finding a new path through the program execution." — connecting `MutationCoverageFuzzer` to [[AFL]]'s core heuristic.

> "Mutations from existing valid inputs have much higher chances to be valid, and thus to exercise functionality beyond input processing." — the chapter's Lessons-Learned thesis.

## Connections
- [[MutationBasedFuzzing]] — the technique this chapter mints; the core idea (perturb valid seeds).
- [[Mutator]] — the `mutate()` dispatcher over the three string mutation operators.
- [[SeedInput]] — the valid starting input(s) the fuzzer mutates.
- [[MutationCoverageFuzzer]] — the coverage-guided mutation fuzzer that evolves a population.
- [[RandomFuzzer]] — `MutationFuzzer` subclasses the same `Fuzzer` base; this chapter improves on the blackbox baseline measured in [[fuzzingbook-04-coverage|Ch 4]].
- [[Runner]] — `FunctionRunner`/`FunctionCoverageRunner` are new `Runner` subclasses wrapping callables and capturing coverage.
- [[Coverage]] / [[CoverageGuidedFuzzing]] — coverage is the feedback signal that decides which mutants to keep.
- [[Fuzzing]] — mutation-based fuzzing is one of the discipline's two main input-generation families.
- [[AFL]] — the real-world fuzzer whose mutation + coverage-feedback ideas this chapter reproduces in miniature.
- [[AndreasZeller]] — lead author of *The Fuzzing Book*.
- [[fuzzingbook-03-fuzzer|Ch 3]] — supplies the `Fuzzer`/`Runner` architecture and the random baseline.
- [[fuzzingbook-04-coverage|Ch 4]] — supplies the `Coverage` class and the "guide, don't just measure" thesis this chapter operationalizes.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — the explicit Next Step: power schedules that spend more energy on seeds hitting unlikely paths or near a target (AFL-style greybox).

## Contradictions
- None identified.
