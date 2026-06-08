---
title: "Daikon"
type: entity
tags: [tool, specification-mining, dynamic-analysis, invariants, verification, testing, software-engineering, open-source]
sources: [fuzzingbook-22-dynamic-invariants]
last_updated: 2026-06-06
---

# Daikon

**Daikon** is the seminal **dynamic invariant detector** — a tool that observes a program's executions and reports *likely invariants* (pre-/postconditions and data invariants that held across all observed runs). Created by **Michael D. Ernst** and collaborators, it has been continuously maintained and extended for more than 20 years and detects invariants for a variety of languages, including C, C++, C#, Eiffel, F#, Java, Perl, and Visual Basic. The corresponding paper (Ernst et al. 2001) is one of the most-cited works in Software Engineering and effectively founded the field of [[SpecificationMining|specification mining]].

## Role in The Fuzzing Book
[[fuzzingbook-22-dynamic-invariants|Ch 22]] calls Daikon "the mother of function specification miners" and reconstructs a miniature of it: the chapter's `InvariantAnnotator` checks a catalog of candidate properties against observed calls and keeps those that always hold — exactly Daikon's [[InvariantInference|inference]] strategy. The chapter is explicit that Daikon goes further than its teaching implementation: Daikon holds a rich catalog of likely-invariant patterns, supports *data* and *object* invariants (not just function pre-/postconditions), can **eliminate invariants implied by others**, and uses **statistical confidence** to discard unlikely invariants. The chapter also notes Daikon's tight relationship with test generation — the Eclat tool (Pacheco & Ernst 2005) pairs a unit-test generator with Daikon-style mining to produce [[TestOracle|oracles]] and guide generation toward fault-revealing inputs — which is the same mining↔generation loop the chapter argues for.

## Connections
- [[SpecificationMining]] — Daikon is the canonical, seminal specification miner.
- [[DynamicInvariant]] — the "likely invariant" artifact Daikon detects.
- [[InvariantInference]] — Daikon's check-candidates-keep-those-that-always-hold engine (with implication elimination + confidence on top).
- [[Precondition]] / [[Postcondition]] / [[DesignByContract]] — the contract clauses Daikon mines.
- [[TestOracle]] / [[TestGeneration]] — Daikon-mined invariants serve as oracles and guide test generators (Eclat).
- [[AndreasZeller]] — Ch 22 author; the chapter's miner reconstructs Daikon in miniature.
- [[fuzzingbook-22-dynamic-invariants]] — the chapter that reconstructs Daikon's approach.

## Sources
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications."
