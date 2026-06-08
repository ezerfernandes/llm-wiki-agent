---
title: "AFLFast"
type: concept
tags: [fuzzing, greybox, afl, power-schedule, markov-chain, optimization, security]
sources: [fuzzingbook-06-greybox-fuzzer]
last_updated: 2026-06-06
---

# AFLFast

**AFLFast** is a [[PowerSchedule|power-schedule]] enhancement to [[AFL]] introduced by [[MarcelBohme|Marcel Böhme]] et al. in *"Coverage-based Greybox Fuzzing as Markov Chain"* (CCS 2016). Its key insight: model the seed-selection process as a [[MarkovChain|Markov chain]] over program paths, then assign **more [[SeedEnergy|energy]] to seeds exercising low-frequency (rare) paths**. Because most generated inputs pile onto a few "hot" high-frequency paths, redirecting effort to rarely-taken paths discovers new program states — and new bugs — far faster, without changing the underlying mutation engine. AFLFast is one of the standard variants reconstructed in *The Fuzzing Book*'s greybox chapter.

## From The Fuzzing Book — Greybox Fuzzing
[[fuzzingbook-06-greybox-fuzzer|Ch 6]] implements AFLFast as `AFLFastSchedule(exponent)`, an *exponential power schedule* that assigns each seed `energy = 1 / f(p(s)) ** a`, where `p(s)` is the seed's [[PathCoverage|path ID]] (`getPathID`), `f(p)` is the number of times that path has been exercised, and `a` is a tunable exponent (the chapter uses `a = 5`). It is driven by the `CountingGreyboxFuzzer`, which maintains `path_frequency`. Compared to the uniform [[PowerSchedule|`PowerSchedule`]], AFLFast "shaves" executions off the dominant high-frequency path and redistributes them to lower-frequency paths, assigning the most energy to the seed on the lowest-frequency path — and it reaches the same [[Coverage|coverage]] much faster. The chapter warns that too large an exponent risks floating-point overflow/imprecision, and cites Böhme et al.'s CCS'16 paper and the [[BoostedGreyboxFuzzing|boosting]] implementation in AFL.

## Connections
- [[BoostedGreyboxFuzzing]] — AFLFast *is* the book's boosted greybox schedule.
- [[PowerSchedule]] / [[SeedEnergy]] — AFLFast is an exponential energy schedule.
- [[PathCoverage]] — energy is inversely proportional to a path's exercise frequency.
- [[MarkovChain]] — the paper models greybox fuzzing as a Markov chain over paths.
- [[GreyboxFuzzing]] — the fuzzing model AFLFast accelerates.
- [[AFL]] — the base fuzzer AFLFast extends.
- [[MarcelBohme]] — lead author of AFLFast.
- [[DirectedGreyboxFuzzing]] — the sibling AFLGo directed schedule from the same chapter.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — where AFLFast is reconstructed.

## Sources
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing."
