---
title: "The Fuzzing Book Ch 30 — When To Stop Fuzzing"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, statistics, estimation, residual-risk, species-discovery, good-turing, history]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-30-when-to-stop-fuzzing.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# When To Stop Fuzzing

## Summary
Chapter 30 is the **final chapter** of *The Fuzzing Book*, closing **Part VI (Managing Fuzzing)** with a *statistical* answer to the question every fuzzing campaign eventually faces: when have we hit diminishing returns and should stop? Its central insight is that fuzzing is an instance of **[[SpeciesDiscovery|species discovery]]** — the ecological problem of estimating how likely you are to encounter a *new species* given a sample of individuals — and that the same estimators ecologists and statisticians use apply directly to estimating the probability of discovering a new program path or a new bug. The chapter's worked example is historical: it reconstructs how [[AlanTuring|Alan Turing]] and his assistant [[IJGood|I. J. Good]] cracked the Naval [[EnigmaMachine|Enigma]] cipher at [[BletchleyPark|Bletchley Park]] during WWII, and how the **[[GoodTuringEstimator|Good-Turing estimator]]** they invented (singletons ÷ total samples) estimates the [[DiscoveryProbability|discovery probability]]. It then maps this onto fuzzing via execution-trace "species," shows that the Good-Turing estimate is an upper bound on **[[ResidualRisk|residual risk]]** (per [[MarcelBohme|Böhme]]'s [[SpeciesDiscovery|STADS]] framework), and introduces Anne [[AnneChao|Chao]]'s estimators for the *total* number of species ([[Chao1Estimator|Chao1]]) and for *extrapolating* future discovery. Builds on [[fuzzingbook-04-coverage|Ch 4]] (coverage), [[fuzzingbook-03-fuzzer|Ch 3]] (`RandomFuzzer`), [[fuzzingbook-06-greybox-fuzzer|Ch 6]] (greybox path coverage), and [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] (managing campaigns); it uses [[BenfordsLaw|Benford's law]] from [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] to make the Enigma example realistic.

## Key Concepts
- **[[SpeciesDiscovery|Software Testing as Species Discovery (STADS)]]** — [[MarcelBohme|Marcel Böhme]]'s framework reframing fuzzing as ecological sampling: each input *belongs to a species* (e.g. its execution trace / covered statement set), and questions like "how many bugs remain?" become "how many unseen species remain?". I.J. Good's 1953 generalization of Turing's wartime work already used the word "species" — Good was publishing in the biostatistics journal *Biometrika*, not about ciphers.
- **[[GoodTuringEstimator|Good-Turing estimator]]** — the [[DiscoveryProbability|discovery probability]] `p₀ = f₁ / n`, where `f₁` is the number of **singletons** (species seen exactly once) and `n` is the number of samples. Intuition: rare-but-observed singletons upper-bound the still-rarer unobserved species. Computed cheaply *during* a campaign with no extra repetitions, and shown empirically to match a costly repeated-sampling estimate within ~0.03.
- **[[DiscoveryProbability|Discovery probability]] & sample coverage** — `p₀` is the probability the *next* input yields a previously unseen species; its complement `1 − p₀` is the **sample coverage** (Turing's quantity: the fraction of all messages already decryptable with known trigrams), and the **inverse** `1/p₀` is a maximum-likelihood estimate of how many more inputs you can expect before the next discovery.
- **[[ResidualRisk|Residual risk]]** — the probability the *next* input reveals a not-yet-found vulnerability. Böhme (STADS) proves the Good-Turing discovery-probability estimate is an *upper bound* on residual risk: split each trace-species into "vulnerable" and "non-vulnerable" sub-species; only non-vulnerable ones have been seen, so the chance of a new species bounds the chance of a vulnerable one. *"Testing is not verification."*
- **Trace coverage & trace hashing** — `getTraceHash(cov)` defines an input's *species* by `hashlib.md5(pickle.dumps(cov.coverage()))` over the *set* of statements it exercises (a coarse abstraction of [[PathCoverage|path]] that ignores order and repetition). Each input maps to exactly one trace hash, mirroring "each message → exactly one trigram." `population_trace_coverage()` tracks cumulative coverage, singletons, and doubletons over time. Trace coverage is shown to grow more steadily and finely than raw [[Coverage|statement coverage]] — the chapter notes this is why **[[AFL]]** uses a similar branch-hash measure of progress.
- **[[Chao1Estimator|Chao1 estimator]]** — Anne [[AnneChao|Chao]]'s 1984 nonparametric estimate of the *asymptotic total* number of species `Ŝ = S(n) + f₁²/(2f₂)` (using singletons `f₁` and doubletons `f₂`), letting you report fuzzing *progress as a percentage* `S(n)/Ŝ` even when the true total is unknown.
- **Extrapolating fuzzing success** — Chao, Shen & Lin's 2003 extrapolator predicts species discovered after `m*` further inputs: `Ŝ(n+m*) = S(n) + f̂₀[1 − (1 − f₁/(n·f̂₀ + f₁))^{m*}]`, where `f̂₀ = Ŝ − S(n)` estimates undiscovered species. Shown to predict 3× extrapolation accurately.
- **Enigma worked example** — the `EnigmaMachine` (a `Runner` subclass) checks whether a message was encoded with a guessed **trigram** drawn from the *Kenngruppenbuch* (`k_book`); `BletchleyPark` brute-forces with a `RandomFuzzer(min_length=3, max_length=3)`; `BoostedBletchleyPark` tries the most-frequently-observed ("abundant") trigrams first and cracks substantially more messages per attempt budget. Trigram probabilities follow [[BenfordsLaw|Benford's law]] over `26³ = 17,576` trigrams.

## Key Claims
- The Polish **Bomba** decryption machine, which simulated six Enigmas trying keys until the code broke, "might have been the very first fuzzer."
- The Good-Turing estimate `f₁/n` of discovery probability is highly accurate yet far cheaper than the empirical (repeated-sampling) estimate and, crucially, can be computed live during a campaign without redundant repetitions.
- The Good-Turing discovery probability is an *upper bound on residual risk* — the probability of finding a new bug when none has been found — regardless of how "species" is defined (Böhme, STADS, ACM TOSEM 2018).
- Three actionable quantities fall out of one estimate: discovery probability `p₀` (chance the next input is novel), its complement (progress toward completion — *abort when `p₀` is too low*), and its inverse (expected inputs until the next discovery).
- The **majority** of observed species are singletons even after large sampling effort; rare observed species are good predictors of unobserved ones — the empirical hypothesis underlying 80 years of species-estimation theory.
- Chao1 gives a defensible *denominator* for progress %; the Chao–Shen–Lin extrapolator predicts future discovery well even at 3× the current sample size.
- Stopping rules: stop when the estimated discovery probability / residual risk drops below threshold, or when the projected extra species per extra input no longer justify the cost.

## Key Quotes
> "Turing did not only develop the foundations of computer science... Together with his assistant I.J. Good, he also invented estimators of the probability of an event occurring that has never previously occurred." — framing the Good-Turing estimator.

> "Testing is not verification. Maybe the next test input that is generated reveals a vulnerability." — why a campaign always carries residual risk.

> "_make use of what you have learned and go and create great fuzzers and test generators!_" — the book's closing exhortation (this is the last chapter).

## Connections
- [[SpeciesDiscovery]] / [[GoodTuringEstimator]] / [[DiscoveryProbability]] / [[ResidualRisk]] / [[Chao1Estimator]] — the statistical machinery this chapter mints.
- [[AlanTuring]] / [[IJGood]] / [[EnigmaMachine]] / [[BletchleyPark]] — the historical worked example.
- [[AnneChao]] — bio-statistician whose estimators (Chao1, extrapolation) ground the "how complete?" and "what next?" questions.
- [[MarcelBohme]] — STADS author; his proof connects Good-Turing to residual risk; a co-author of the book.
- [[Coverage]] / [[PathCoverage]] — trace coverage is a path abstraction; species = trace hash over the covered-statement set.
- [[BenfordsLaw]] — used (from [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]]) to assign realistic trigram probabilities.
- [[RandomFuzzer]] / [[Fuzzing]] — the `RandomFuzzer` brute-forces Enigma trigrams and generates the HTMLParser populations.
- [[AFL]] — cited as using a branch-hash measure of progress analogous to trace coverage.
- [[fuzzingbook-03-fuzzer|Ch 3]] (`RandomFuzzer`, `Runner`), [[fuzzingbook-04-coverage|Ch 4]] (`Coverage`, `cgi_decode`), [[fuzzingbook-06-greybox-fuzzer|Ch 6]] (path coverage), [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] (managing large campaigns) — prerequisites and siblings.

## Contradictions
- None identified.
