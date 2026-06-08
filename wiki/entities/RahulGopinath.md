---
title: "Rahul Gopinath"
type: entity
tags: [person, author, researcher, software-engineering, testing, fuzzing, grammar-mining, security]
sources: [fuzzingbook-18-grammar-miner, fuzzingbook-19-information-flow, fuzzingbook-25-carver]
last_updated: 2026-06-06
---

# Rahul Gopinath

**Rahul Gopinath** is a software-engineering researcher and a co-author of *[[fuzzingbook-01-tours|The Fuzzing Book]]* (with [[AndreasZeller|Andreas Zeller]], [[MarcelBohme|Marcel Böhme]], [[GordonFraser|Gordon Fraser]], and [[ChristianHoller|Christian Holler]]). His research centers on **input-grammar mining** and program-guided grammar inference — automatically recovering the input language of a program from sample executions — including work in the **AUTOGRAM** / **Mimid** line of grammar miners. He has also worked on mutation analysis and the empirical foundations of test adequacy.

## Role in The Fuzzing Book
Co-author of the continuously updated online edition (CISPA, 2024). His grammar-mining research underpins the book's semantic-fuzzing material, most directly the [[GrammarMiner|`GrammarMiner`]] machinery.

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] is squarely in Gopinath's research area: program-guided [[GrammarInference|grammar inference]]. The chapter recovers an input [[Grammar|grammar]] by dynamically tracing how input substrings flow through a program's variables, building the [[GrammarMiner|`GrammarMiner`]] pipeline (`Tracer` → `DefineTracker` → `TreeMiner` → `GrammarMiner`, hardened with reassignment and scope handling). The approach is based on the **AUTOGRAM** work of Höschele & Zeller, the lineage from which Gopinath's later **Mimid** grammar miner descends.

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] builds the [[DynamicTaintTracking|dynamic taint-tracking]] mechanism ([[CharacterOrigin|`ostr`]] per-character origins) that his grammar miners can use in place of substring matching to decide whether a value came from the input — the precise alternative his [[GrammarMiner|`GrammarMiner`]] line ([[fuzzingbook-18-grammar-miner|Ch 18]]) is designed to drop into.

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]], which Gopinath co-authors, extends his [[GrammarMining|grammar-mining]] theme from *input* grammars to *call* grammars: the [[APIGrammarMining|`CallGrammarMiner`]] mines a [[Grammar|grammar]] from function calls recorded ([[TestCarving|carved]]) during a real execution, a tracer-driven sibling of the [[GrammarMiner|`GrammarMiner`]] of [[fuzzingbook-18-grammar-miner|Ch 18]] aimed at [[APIFuzzing|API-level fuzzing]].

## Connections
- [[APIGrammarMining]] / [[TestCarving]] — the Ch 25 call-grammar miner, sibling of his input-grammar work.
- [[GrammarInference]] / [[GrammarMiner]] / [[GrammarMining]] — his core research area, realized in Ch 18.
- [[InformationFlow]] / [[DynamicTaintAnalysis]] / [[CharacterOrigin]] — the Ch 19 taint mechanism his miners can build on.
- [[AndreasZeller]] — lead book author and frequent collaborator (AUTOGRAM lineage).
- [[MarcelBohme]] / [[GordonFraser]] / [[ChristianHoller]] — his *Fuzzing Book* co-authors.
- [[CISPA]] — the book's publisher and home of the grammar-mining research line.
- [[DynamicTaintTracking]] — the precise fragment-origin mechanism his miners can build on (Ch 19).
- [[fuzzingbook-18-grammar-miner]] — the chapter most aligned with his work.

## Sources
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars."
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests" (the call-grammar miner sibling of his work).
