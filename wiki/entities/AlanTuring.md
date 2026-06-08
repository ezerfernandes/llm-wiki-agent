---
title: "Alan Turing"
type: entity
tags: [foundational, mathematician, computer-science, history]
sources: [dis-5-1-history, fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Alan Turing (1912–1954)

British mathematician and logician; one of the foundational figures of theoretical computer science. His 1937 paper *On Computable Numbers, with an Application to the Entscheidungsproblem* introduced the **[[TuringMachine|"Logical Computing Machine"]]** — the abstract automaton that defines what is mechanically computable and underlies the [[ChurchTuringThesis|Church-Turing thesis]].

During WWII, led code-breaking work at [[BletchleyPark]] against the German Enigma cipher (the [[Colossus]] machine targeted the *separate* Lorenz cipher). In 1946 designed the **[[AutomaticComputingEngine|Automatic Computing Engine (ACE)]]** at the [[NationalPhysicalLaboratory|UK National Physical Laboratory]] — one of the earliest [[StoredProgram|stored-program]] computer designs, contemporaneous with [[JohnVonNeumann|von Neumann]]'s [[EDVAC]] paper.

Per [[dis-5-1-history|*Dive into Systems* Ch 5.1]], Turing is the **theoretical pole** of the 1930s–1940s convergence that produced modern computing — paired with the **engineering pole** of [[JohnMauchly|Mauchly]] / [[PresperEckert|Eckert]] / [[KonradZuse|Zuse]] / [[HowardAiken|Aiken]] / [[TommyFlowers|Flowers]] and synthesized by [[JohnVonNeumann|von Neumann]].

## From The Fuzzing Book — When To Stop Fuzzing
[[fuzzingbook-30-when-to-stop-fuzzing|Chapter 30]] of *The Fuzzing Book* uses Turing's [[BletchleyPark]] work on the Naval [[EnigmaMachine|Enigma]] as its central example. To break ciphers, Turing wanted to *estimate the likelihood that an unseen trigram would appear next* — leading him and his assistant [[IJGood|I. J. Good]] to invent the [[GoodTuringEstimator|Good-Turing estimator]] of the [[DiscoveryProbability|discovery probability]] of never-before-seen events. The chapter shows this same estimator, generalized by Good to "species," now estimates the probability a fuzzer discovers a new path and bounds the [[ResidualRisk|residual risk]] of a campaign — making Turing a (surprising) founder of the [[SpeciesDiscovery|statistical theory of fuzzing]] as well as of computation itself.
