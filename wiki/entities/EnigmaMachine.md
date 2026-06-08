---
title: "Enigma Machine"
type: entity
tags: [history, cryptography, codebreaking, wwii, fuzzing-example]
sources: [fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Enigma Machine

The **Enigma machine** was an electromechanical rotor cipher device used by Nazi Germany to encrypt military and naval communications in WWII. The **Naval Enigma** was especially hard to break: part of its key was a three-letter **trigram** selected from the *Kenngruppenbuch* (K-book), a book listing all trigrams in random order. Breaking it was the work [[AlanTuring|Alan Turing]] led at [[BletchleyPark|Bletchley Park]], building on the Polish-built **Bomba** decryption machine — which, by simulating six Enigmas and trying keys until the code broke, *"might have been the very first fuzzer."*

## Role in The Fuzzing Book
[[fuzzingbook-30-when-to-stop-fuzzing|Chapter 30]] uses a simplified Naval Enigma as its central worked example. The Python `EnigmaMachine` class (a `Runner` subclass) checks whether a `message` was encoded with a guessed `key` (trigram); trigram probabilities follow [[BenfordsLaw|Benford's law]] over `26³ = 17,576` trigrams. A `BletchleyPark` class brute-forces messages with a `RandomFuzzer(min_length=3, max_length=3)`, and `BoostedBletchleyPark` tries the most-observed ("abundant") trigrams first — cracking far more messages per attempt budget. Counting how often each trigram recurs (and how many are singletons) is exactly the data the [[GoodTuringEstimator|Good-Turing estimator]] needs, motivating the chapter's statistics of [[DiscoveryProbability|discovery probability]] and [[ResidualRisk|residual risk]].

## Connections
- [[AlanTuring]] / [[IJGood]] — broke the Naval Enigma and invented the estimator from its statistics.
- [[BletchleyPark]] — where the codebreaking happened.
- [[GoodTuringEstimator]] — derived in the chapter from Enigma trigram counts.
- [[BenfordsLaw]] — used to assign realistic trigram probabilities.
- [[RandomFuzzer]] / [[Fuzzing]] — the brute-force "fuzzer" that cracks trigrams; the Bomba prefigured fuzzing.
- [[SpeciesDiscovery]] — trigrams are the chapter's first "species."

## Sources
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing."
