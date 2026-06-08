---
title: "Path Coverage"
type: concept
tags: [fuzzing, coverage, greybox, afl, path-coverage, hashing]
sources: [fuzzingbook-06-greybox-fuzzer, fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# PathCoverage

**Path coverage** treats the *whole set of statements/branches an input exercises* as a single unit — a program **path** — rather than counting individual lines or branches in isolation. Two inputs that touch exactly the same code take the same path. Greybox fuzzers use path identity to ask "how *often* has each path been exercised?", so they can prioritize **rare** paths. Because enumerating paths exactly is infeasible, a practical encoding is to **hash** the covered-statement set into a compact **path ID**.

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] implements path identity with `getPathID(coverage)`, which returns `hashlib.md5(pickle.dumps(sorted(coverage))).hexdigest()` — a unique 128-bit hash for a set of covered [[Coverage|`Location`]] tuples. The `CountingGreyboxFuzzer` records `path_frequency[path_id]`, counting how many generated inputs took each path. This frequency `f(p)` feeds the boosted [[AFLFast]] schedule's energy formula `1 / f(p(s)) ** a`, which assigns high [[SeedEnergy|energy]] to seeds on low-frequency (rare) paths so the fuzzer [[BoostedGreyboxFuzzing|explores them more]]. This per-path counting is the bridge from raw [[Coverage|coverage]] to the path-frequency optimization that AFLFast models as a [[MarkovChain|Markov chain]].

## From The Fuzzing Book — When To Stop Fuzzing
[[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] reuses the same hash-the-covered-set idea as a **trace** — `getTraceHash(cov) = md5(pickle.dumps(cov.coverage()))` — and explicitly calls it a *coarse abstraction of the execution path* that ignores the order and repetition of statements. Treating each trace as a [[SpeciesDiscovery|species]] lets the [[GoodTuringEstimator|Good-Turing estimator]] estimate the [[DiscoveryProbability|probability of discovering a new path]] and bound [[ResidualRisk|residual risk]]. The chapter notes [[AFL]] uses a similar branch-hash as its measure of progress — connecting path identity (used for *prioritization* in Ch 6) to path identity used for *stopping* in Ch 30.

## Connections
- [[SpeciesDiscovery]] / [[DiscoveryProbability]] — Ch 30 treats each path/trace as a species to estimate new-path discovery.
- [[Coverage]] — path coverage aggregates the covered-statement set into one path.
- [[AFLFast]] / [[BoostedGreyboxFuzzing]] — uses path frequency to assign energy to rare paths.
- [[SeedEnergy]] / [[PowerSchedule]] — the boosted energy formula divides by path frequency.
- [[GreyboxFuzzing]] — the fuzzing model that tracks per-path frequencies.
- [[MarkovChain]] — AFLFast's analysis of path transitions.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — where `getPathID`/path frequency are defined.

## Sources
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing."
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing" (trace = coarse path abstraction; hashed for species-based discovery estimation).
