---
title: "Specification Mining"
type: concept
tags: [testing, fuzzing, verification, specification-mining, dynamic-analysis, software-engineering]
sources: [fuzzingbook-22-dynamic-invariants]
last_updated: 2026-06-06
---

# Specification Mining

**Specification mining** is the automatic recovery of a formal *specification* — a description of what a program expects and delivers — from observations of the program, rather than having a human write it. The mined artifact can be a set of [[DynamicInvariant|dynamic invariants]] (pre-/postconditions), a set of [[TypeInference|type signatures]], an [[FiniteStateMachine|API usage protocol]] (legal call sequences), or an input [[Grammar|grammar]]. It is motivated by the observation that most real code ships *without* explicit specifications — "without specifications, there are no bugs, only surprises" (Ken Thompson) — yet testing, verification, and symbolic analysis all need something to check against.

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] frames specification mining as *retrofitting* existing code with checkable descriptions of its behavior, learned from runs. It realizes two concrete miners — a `TypeAnnotator` for [[TypeInference|types]] and an `InvariantAnnotator` for value [[InvariantInference|invariants]] — both built on `sys.settrace` call tracing ([[DynamicAnalysis|dynamic analysis]]). The Background positions [[Daikon]] (Ernst et al.) as "the mother of function specification miners," and broadens the scope: protocol mining ("Mining Specifications," Ammons et al. 2002) learns legal call sequences, and the book's own [[fuzzingbook-18-grammar-miner|grammar mining (Ch 18)]] is itself a specification-mining approach that learns input-format specs. The chapter's key methodological point is the chicken-and-egg loop between mining and generation: mined specs are only as good as the executions observed, so pairing a miner with a comprehensive [[TestGeneration|test generator]] (or system-level [[Fuzzing|fuzzer]], an "infinite source of executions") is what makes the mined specs precise.

## Connections
- [[DynamicInvariant]] — the pre-/postcondition artifact this chapter mines.
- [[TypeInference]] / [[InvariantInference]] — the two concrete mining tasks (`TypeAnnotator`, `InvariantAnnotator`).
- [[Daikon]] — the seminal dynamic invariant detector; the canonical specification miner.
- [[DesignByContract]] — mined specs are the contract clauses (pre-/postconditions, types).
- [[TestOracle]] — mined specs serve as oracles for regression and generated-test checking.
- [[fuzzingbook-18-grammar-miner]] — grammar mining as input-format specification mining.
- [[TestGeneration]] / [[Fuzzing]] — diverse generated runs make mined specs precise (the mining↔generation loop).

## Sources
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications."
