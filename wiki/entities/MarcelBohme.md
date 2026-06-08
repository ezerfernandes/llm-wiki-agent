---
title: "Marcel Böhme"
type: entity
tags: [person, author, researcher, fuzzing, security, software-engineering, greybox]
sources: [fuzzingbook-06-greybox-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer, fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Marcel Böhme

**Marcel Böhme** is a software-security researcher best known for foundational work on **greybox fuzzing**. He is the author (with collaborators) of the influential [[AFL]] variants **AFLFast** — *"Coverage-based Greybox Fuzzing as Markov Chain"* (CCS 2016) — and **AFLGo** — *"Directed Greybox Fuzzing"* (CCS 2017) — as well as the efficiency analysis *"A Probabilistic Analysis of the Efficiency of Automated Software Testing"* (IEEE TSE, 2016). He is a co-author of *[[fuzzingbook-01-tours|The Fuzzing Book]]* (CISPA, 2024) alongside [[AndreasZeller|Andreas Zeller]], Rahul Gopinath, Gordon Fraser, and Christian Holler.

## Role in The Fuzzing Book
Böhme's research is the direct source of *The Fuzzing Book*'s greybox chapter. [[fuzzingbook-06-greybox-fuzzer|Ch 6]] reconstructs his [[AFLFast]] exponential [[PowerSchedule|power schedule]] (boosting [[PathCoverage|low-frequency paths]], modeled as a [[MarkovChain|Markov chain]]) as the [[BoostedGreyboxFuzzing|boosted greybox fuzzer]], and his AFLGo function-level-distance schedule as the [[DirectedGreyboxFuzzing|directed greybox fuzzer]]. The chapter cites his CCS'16, CCS'17, and TSE'16 papers as further reading.

## Role in The Fuzzing Book — Greybox Fuzzing with Grammars
As a book co-author, Böhme's greybox-fuzzing research is also the backdrop for [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]], which extends the AFL-style greybox loop with grammar structure and reconstructs the [[AFLSmart]] "smart greybox" design ([[RegionMutation|region-based mutation]] + [[DegreeOfValidity|validity]]-based power schedules) alongside the [[LangFuzz]] fragment approach of fellow co-author [[ChristianHoller]].

## Role in The Fuzzing Book — When To Stop Fuzzing
Böhme's **[[SpeciesDiscovery|STADS — Software Testing as Species Discovery]]** framework (ACM TOSEM 2018) is the statistical backbone of [[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]], the book's final chapter. STADS recasts fuzzing as ecological sampling and lets the [[GoodTuringEstimator|Good-Turing estimator]] estimate the [[DiscoveryProbability|discovery probability]] of new program paths. Böhme's key result, reconstructed in the chapter, is that this estimate is an *upper bound on [[ResidualRisk|residual risk]]* — the probability of an undiscovered vulnerability — giving fuzzing a principled stopping criterion.

## Connections
- [[SpeciesDiscovery]] / [[ResidualRisk]] — his STADS framework and its residual-risk bound, central to Ch 30.
- [[AFLFast]] — his CCS'16 Markov-chain boosting of AFL.
- [[DirectedGreyboxFuzzing]] — his CCS'17 AFLGo directed-fuzzing work.
- [[BoostedGreyboxFuzzing]] / [[PowerSchedule]] / [[SeedEnergy]] — the energy-assignment ideas he pioneered.
- [[AFL]] — the base fuzzer his AFLFast/AFLGo variants extend.
- [[GreyboxFuzzing]] — the technique his research advanced.
- [[MarkovChain]] — the model underlying his AFLFast analysis.
- [[AndreasZeller]] / [[ChristianHoller]] — co-authors of *The Fuzzing Book*.
- [[AFLSmart]] — the smart-greybox fuzzer reconstructed in Ch 15, extending the AFL line of greybox research.
- [[GrammarAwareGreyboxFuzzing]] — Ch 15's fusion of greybox feedback with grammar structure.
- [[fuzzingbook-06-greybox-fuzzer|Ch 6]] — the chapter built on his work.
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — grammar-aware greybox fuzzing, co-authored.

## Sources
- [[fuzzingbook-06-greybox-fuzzer]] — *The Fuzzing Book* Ch 6, "Greybox Fuzzing."
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing" (built on his STADS framework).
