---
title: "The Fuzzing Book Ch 06 — Greybox Fuzzing"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, greybox, coverage-guided, power-schedule, afl, aflfast, aflgo, directed-fuzzing]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-06-greybox-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Greybox Fuzzing

## Summary
Chapter 6 of *The Fuzzing Book* (Part II — Lexical Fuzzing) reconstructs the algorithm behind [[AFL|American Fuzzy Lop]] and its [[MarcelBohme|Böhme]]-led variants **AFLFast** and **AFLGo**. Building directly on [[fuzzingbook-05-mutation-fuzzer|Ch 5]]'s mutation-based fuzzing, it adds the missing ingredient that makes a fuzzer *greybox*: a **[[PowerSchedule|power schedule]]** that distributes finite fuzzing time across a seed population by assigning each seed an **[[SeedEnergy|energy]]** (the probability it is chosen next). The chapter develops, in increasing sophistication, a blackbox `AdvancedMutationFuzzer`, a coverage-feedback `GreyboxFuzzer`, a *boosted* `CountingGreyboxFuzzer` with an exponential `AFLFastSchedule` that pours energy into rarely-exercised paths (framed as a Markov chain, [[MarkovChain]]), and finally a *directed* `AFLGoSchedule` that steers toward a target program location using pre-computed [[CallGraph|call-graph]] distances. The central worked examples are the toy `crashme` function (learning to produce the crashing input `bad!`), the Python `HTMLParser`, and a generated **maze** whose target tile the directed fuzzer learns to reach. It forwards to [[fuzzingbook-07-search-based-fuzzer|Ch 7]] (search-based fuzzing as optimization) and [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] (grammar-aware "smart" greybox fuzzing).

## Key Concepts
- **[[GreyboxFuzzing|Greybox fuzzing]]** — between blackbox and whitebox: uses *lightweight* coverage instrumentation as feedback (which branches an input hits, and a coarse hit-count) without heavyweight program analysis or constraint solving. An input that increases coverage is added to the seed corpus. `GreyboxFuzzer(AdvancedMutationFuzzer)` overrides `run()` to append any input whose `frozenset(runner.coverage())` is new to `self.population`.
- **[[SeedInput|Seeds]] and the `Seed` class** — `Seed(data)` wraps an input string with extra attributes for advanced schedules: `coverage` (a set of [[Coverage|`Location`]] tuples), `distance` (to a target), and `energy`.
- **[[PowerSchedule|Power schedule]]** — `PowerSchedule` decides how fuzzing time is spent: `assignEnergy()` sets each seed's energy, `normalizedEnergy()` normalizes it to a probability distribution, and `choose()` uses `random.choices(population, weights=norm_energy)` to draw a seed. The base schedule assigns *uniform* energy (each seed equally likely).
- **[[SeedEnergy|Energy]]** — the likelihood a seed is chosen from the population for mutation; "spending energy" on a seed means fuzzing it. The whole greybox optimization is about not wasting energy on non-progressive seeds.
- **[[Mutator|Mutators]]** — the chapter's `Mutator` defines `delete_random_character`, `insert_random_character`, `flip_random_character`, dispatched by `mutate()`. `AdvancedMutationFuzzer.create_candidate()` *stacks* multiple mutations (`min(len(candidate), 1 << random.randint(1,5))`). `DictMutator` adds `insert_from_dictionary` (inject a keyword); `MazeMutator` adds `append_from_dictionary` and `delete_last_character`.
- **[[Runner|`FunctionCoverageRunner`]]** — reused from [[fuzzingbook-05-mutation-fuzzer|Ch 5]]; wraps a Python function, runs an input under [[Coverage|coverage]] tracing, and returns the executed `(function, line)` locations.
- **[[PathCoverage|Path coverage via path-ID hashing]]** — `getPathID(coverage)` returns `hashlib.md5(pickle.dumps(sorted(coverage))).hexdigest()`, a unique hash for a covered-statement set. This lets the fuzzer count how often each *path* is exercised (`path_frequency`).
- **[[BoostedGreyboxFuzzing|Boosted greybox fuzzing]] / [[AFLFast]]** — `CountingGreyboxFuzzer` tracks `path_frequency[path_id]`; `AFLFastSchedule(exponent)` assigns each seed an **exponential** energy `1 / f(p(s)) ** a`, inversely proportional to how often its path `p` has been hit. This shifts effort from a dominant high-frequency path onto rare ones, exploring more paths per unit time (Böhme et al.'s AFLFast).
- **[[DirectedGreyboxFuzzing|Directed greybox fuzzing]] (AFLGo)** — frames "reach a target location" as an optimization problem. `DirectedSchedule` assigns energy `(1 / seed.distance) ** exponent`, where `seed.distance` is the average function-level [[CallGraph|call-graph]] distance (`nx.shortest_path_length`) of the seed's covered functions to the target function (unreachable functions get distance `0xFFFF`). `AFLGoSchedule` improves this by *normalizing* distances between the population's min and max, dramatically boosting near-target seeds — it solves the maze hundreds of times where undirected schedules solve it ~never.

## Key Claims
- A greybox fuzzer leverages coverage feedback to "learn how to reach deeper into the program" while still generating thousands of inputs per second; it is neither blackbox (it uses *some* program analysis) nor whitebox (no heavyweight analysis / constraint solving).
- AFL instruments a program by injecting a trampoline after every conditional jump that assigns each branch a unique ID and increments a coarse hit-counter; instrumentation is usually compile-time but can be done on binaries via QEMU or Intel PinTool. For Python, coverage is collected without instrumentation.
- Coverage feedback alone (greybox vs blackbox) measurably increases statements covered for the same number of inputs — the new seeds act as "bread crumbs" guiding the fuzzer into deeper code (e.g. from `good` the fuzzer learns to emit the crashing `bad!`).
- Assigning *more energy to seeds exercising low-frequency paths* (the exponential `AFLFastSchedule`) explores program paths far more efficiently than the uniform schedule — the boosted fuzzer reaches the same coverage much faster. A too-large exponent can cause floating-point overflow/imprecision.
- Directed fuzzing with pre-computed, instrumentation-injected distance values makes the average-distance computation "extremely efficient" at runtime; the normalized `AFLGoSchedule` generates hundreds of maze solutions where `DirectedSchedule` and the plain greybox fuzzer generate essentially none.
- The mutator defines the fuzzer's search space; customizing it (dictionaries, later grammars) narrows the space to relevant inputs and raises the valid-input ratio — but pure greybox still misses important keywords like `<html>`, motivating grammar-based mutators in [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]].

## Key Quotes
> "A power schedule distributes the precious fuzzing time among the seeds in the population. Our objective is to maximize the time spent fuzzing those (most progressive) seeds which lead to higher coverage increase in shorter time." — defining the power schedule.

> "We call the likelihood with which a seed is chosen from the population as the seed's *energy*. ... We call the procedure that decides a seed's energy as the fuzzer's *power schedule*." — energy and power schedule.

> "By fuzzing seeds more often that exercise low-frequency paths, we can explore program paths in a much more efficient manner." — the AFLFast boosting insight.

## Connections
- [[GreyboxFuzzing]] — the technique this chapter mints and builds end-to-end.
- [[PowerSchedule]] / [[SeedEnergy]] — the core new machinery (energy distribution over seeds).
- [[BoostedGreyboxFuzzing]] / [[AFLFast]] — exponential energy for rare paths (`CountingGreyboxFuzzer` + `AFLFastSchedule`).
- [[DirectedGreyboxFuzzing]] — AFLGo-style steering toward a target via [[CallGraph|call-graph]] distance.
- [[PathCoverage]] — path-ID hashing (`getPathID`) underpinning the boosted schedule.
- [[CoverageGuidedFuzzing]] / [[Coverage]] — the feedback signal greybox fuzzing consumes.
- [[MutationBasedFuzzing]] / [[Mutator]] / [[SeedInput]] — the mutation substrate extended here (`Mutator`, `DictMutator`, `MazeMutator`).
- [[MarkovChain]] — AFLFast models greybox fuzzing as a Markov chain over paths (Böhme et al., CCS'16).
- [[CallGraph]] — static call graph used to pre-compute function-level distance for directed fuzzing.
- [[AFL]] — the real-world fuzzer this chapter reconstructs (incl. AFLFast/AFLGo variants).
- [[MarcelBohme]] — book co-author and author of AFLFast, AFLGo, and the directed-greybox / efficiency papers cited here.
- [[AndreasZeller]] — lead author of *The Fuzzing Book*.
- [[fuzzingbook-05-mutation-fuzzer|Ch 5]] — direct prerequisite; supplies `Mutator`/`FunctionCoverageRunner`/seed-corpus ideas.
- [[fuzzingbook-04-coverage|Ch 4]] — the coverage feedback signal.
- [[fuzzingbook-07-search-based-fuzzer|Ch 7]] — search-based fuzzing (population "evolved" via mutation as optimization).
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — smart, grammar-aware greybox fuzzing extending this chapter's `Mutator`.

## Contradictions
- None identified.
