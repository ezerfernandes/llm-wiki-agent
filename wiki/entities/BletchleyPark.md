---
title: "Bletchley Park"
type: entity
tags: [history, codebreaking, wwii, cryptography, organization]
sources: [fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Bletchley Park

**Bletchley Park** was the British WWII codebreaking centre where [[AlanTuring|Alan Turing]], his statistical assistant [[IJGood|I. J. Good]], and many others worked to break German ciphers — most famously the [[EnigmaMachine|Enigma]] machine. Turing took on the notoriously hard **Naval Enigma**, and the statistical methods developed there to estimate the likelihood of trigrams never previously seen became the [[GoodTuringEstimator|Good-Turing estimator]].

## Role in The Fuzzing Book
[[fuzzingbook-30-when-to-stop-fuzzing|Chapter 30]] dramatizes Bletchley Park (1938 onward) as the origin of the unseen-species statistics that the chapter applies to fuzzing. Its `BletchleyPark` Python class brute-forces Enigma trigrams with a `RandomFuzzer`, and the recurrence counts of cracked trigrams supply the singletons used to estimate [[DiscoveryProbability|discovery probability]] and [[ResidualRisk|residual risk]].

## Connections
- [[AlanTuring]] / [[IJGood]] — led and assisted the codebreaking here.
- [[EnigmaMachine]] — the cipher broken at Bletchley.
- [[GoodTuringEstimator]] — the estimator born from this work.
- [[SpeciesDiscovery]] — the modern framework descending from it.

## Sources
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing."
