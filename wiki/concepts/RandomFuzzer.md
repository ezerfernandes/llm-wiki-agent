---
title: "RandomFuzzer"
type: concept
tags: [fuzzing, testing, random-testing, python, class-hierarchy]
sources: [fuzzingbook-03-fuzzer, fuzzingbook-04-coverage, fuzzingbook-05-mutation-fuzzer, fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# RandomFuzzer

**`RandomFuzzer`** is the simplest concrete [[Fuzzing|fuzzer]] in *The Fuzzing Book* — a subclass of the abstract **`Fuzzer`** base class — that emits strings of random characters. It is the class-form of the chapter's one-function `fuzzer()` and the canonical starting point for the book's fuzzer [[Runner|class hierarchy]] that all later, smarter fuzzers extend.

## The `Fuzzer` base class
`Fuzzer` defines the interface every fuzzer in the book implements:

- `fuzz() -> str` — return one generated input (abstract; the base returns `""`).
- `run(runner) -> (result, outcome)` — generate one input and feed it to a [[Runner]].
- `runs(runner, trials=10) -> list` — call `run()` `trials` times, returning a list of `(result, outcome)` pairs.

Subclasses override **only `fuzz()`**; the `run`/`runs` plumbing is inherited. This makes `Fuzzer` the single extension point reused by `MutationFuzzer` ([[fuzzingbook-05-mutation-fuzzer|Ch 5]]), `GreyboxFuzzer` ([[fuzzingbook-06-greybox-fuzzer|Ch 6]]), `GrammarFuzzer` ([[fuzzingbook-10-grammar-fuzzer|Ch 10]]), and beyond.

## From The Fuzzing Book — Fuzzing: Breaking Things with Random Inputs
[[fuzzingbook-03-fuzzer|Ch 3]] introduces `RandomFuzzer(min_length=10, max_length=100, char_start=32, char_range=32)`. Its `fuzz()` picks a length with `random.randrange(min_length, max_length + 1)` and appends `chr(random.randrange(char_start, char_start + char_range))` characters. Unlike the bare `fuzzer()` function it adds a configurable **`min_length`** and stores all parameters once at construction, so a configured fuzzer can be reused across many `run`/`runs` calls (e.g. `RandomFuzzer(char_start=0, char_range=256)` to cover the full byte range when fuzzing `troff`). This is [[RandomTesting|random testing]] over raw strings — blackbox, unguided, and the baseline the book improves on with mutation, coverage feedback, and grammars.

## From The Fuzzing Book — Code Coverage
[[fuzzingbook-04-coverage|Ch 4]] uses the Ch 3 `fuzzer()`/`RandomFuzzer` as its measurement subject: running it under the `Coverage` class against `cgi_decode()` and accumulating `population_coverage` curves shows the random fuzzer reaches **full [[LineCoverage|statement coverage]] after ~40–60 inputs** on average (full [[BranchCoverage|branch coverage]] takes longer). The same run also exposes an `IndexError` in `cgi_decode()` that *no* statement- or branch-coverage criterion catches — concrete evidence that random fuzzing finds bugs coverage metrics alone cannot, and the empirical baseline that motivates [[CoverageGuidedFuzzing|coverage-guided]] successors.

## From The Fuzzing Book — Mutation-Based Fuzzing
[[fuzzingbook-05-mutation-fuzzer|Ch 5]] uses `RandomFuzzer`/`fuzzer()` as the *foil*: it quantifies that blackbox random generation has only a ~`1/96**7` chance per input of producing even a valid `http://` prefix for the `http_program()` URL validator — *months to years* of runs for one valid input. The `MutationFuzzer` introduced there subclasses the same `Fuzzer` base (overriding `fuzz()`), but instead of generating from scratch it mutates valid [[SeedInput|seeds]] — the direct improvement on this page's blackbox baseline, later guided by coverage in [[MutationCoverageFuzzer|`MutationCoverageFuzzer`]].

## From The Fuzzing Book — When To Stop Fuzzing
[[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] reuses `RandomFuzzer` twice: as the brute-force engine inside `BletchleyPark` — `RandomFuzzer(min_length=3, max_length=3, char_start=65, char_range=26)` cracks [[EnigmaMachine|Enigma]] trigrams against an `EnigmaMachine(Runner)` — and to generate large populations (e.g. 50,000–400,000 inputs) fed to Python's `HTMLParser` to study trace-coverage growth. The recurrence counts of `RandomFuzzer` outputs (singletons vs abundant trigrams/traces) are exactly the data the [[GoodTuringEstimator|Good-Turing estimator]] consumes to estimate [[DiscoveryProbability|discovery probability]] and [[ResidualRisk|residual risk]].

## Connections
- [[EnigmaMachine]] / [[SpeciesDiscovery]] — Ch 30 drives a `RandomFuzzer` to crack trigrams and generate trace-coverage populations for species-discovery statistics.
- [[Fuzzing]] — `RandomFuzzer` is the simplest instantiation of the general technique.
- [[MutationBasedFuzzing]] / [[MutationCoverageFuzzer]] — the Ch 5 mutation fuzzers that subclass the same `Fuzzer` base and improve on this random baseline.
- [[Coverage]] / [[CoverageGuidedFuzzing]] — Ch 4 measures this fuzzer's coverage and motivates guiding it.
- [[Runner]] — the program-under-test abstraction a `Fuzzer` feeds via `run()`/`runs()`.
- [[RandomTesting]] — `RandomFuzzer.fuzz()` is random input generation applied to strings.
- [[fuzzingbook-03-fuzzer|Ch 3]] — where `Fuzzer`/`RandomFuzzer` are defined.
- [[fuzzingbook-05-mutation-fuzzer|Ch 5]] / [[fuzzingbook-06-greybox-fuzzer|Ch 6]] / [[fuzzingbook-10-grammar-fuzzer|Ch 10]] — fuzzers that subclass `Fuzzer` and override `fuzz()`.

## Sources
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
- [[fuzzingbook-04-coverage]] — *The Fuzzing Book* Ch 4, "Code Coverage" (measures this fuzzer's coverage).
- [[fuzzingbook-05-mutation-fuzzer]] — *The Fuzzing Book* Ch 5, "Mutation-Based Fuzzing" (uses this fuzzer as the blackbox foil improved on by mutation).
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing" (drives the Enigma brute-forcer and the HTMLParser trace-coverage populations).
