---
title: "1-Minimality"
type: concept
tags: [debugging, testing, input-reduction, software-engineering, algorithm]
sources: [fuzzingbook-16-reducer]
last_updated: 2026-06-06
---

# 1-Minimality

**1-minimality** is the correctness guarantee a reducer can provide: a failing input is *1-minimal* when **removing any single element (e.g. any single character) makes the test stop failing.** In other words, no part of the input is redundant with respect to the failure — every remaining piece is load-bearing. It is the practical stopping criterion for [[InputReduction|input reduction]]; a globally minimal input would require testing all subsets (exponential), whereas 1-minimality is achievable in (at worst) quadratic time.

## In The Fuzzing Book — Ch 16
[[fuzzingbook-16-reducer|Ch 16]] establishes that [[DeltaDebugging|delta debugging]] ([[DDMin|`ddmin`]]) *guarantees* a 1-minimal result, because its final stage always tries to delete characters one at a time — once it can delete none without losing the failure, the input is 1-minimal by definition. The chapter's `MysteryRunner` example reduces a ~4100-character input to `()`, where neither character can be removed without the test passing. Note that 1-minimal does **not** mean *globally* smallest: a different reduction path could in principle reach a different small input, and the [[GrammarReducer|grammar-based reducer]] often reaches a *smaller* and more meaningful minimum by reasoning over structure rather than characters.

## Connections
- [[DeltaDebugging]] / [[DDMin]] — the algorithm whose final character-deletion stage guarantees 1-minimality.
- [[InputReduction]] — 1-minimality is the standard stopping criterion for reducers.
- [[GrammarReducer]] / [[HierarchicalDeltaDebugging]] — often reach a smaller minimum by reducing the tree, not the string.
- [[Testing]] / [[TestOracle]] — 1-minimality is defined relative to the failing oracle.
- [[fuzzingbook-16-reducer]] — the chapter that defines and demonstrates the property.

## Sources
- [[fuzzingbook-16-reducer]] — *The Fuzzing Book* Ch 16, "Reducing Failure-Inducing Inputs."
