---
title: "Representation Invariant (repOK)"
type: concept
tags: [testing, fuzzing, verification, data-structures, design-by-contract, software-engineering]
sources: [fuzzingbook-03-fuzzer]
last_updated: 2026-06-06
---

# Representation Invariant (repOK)

A **representation invariant** is a consistency condition that every valid state of a data structure must satisfy. The function or method that checks it is conventionally named **`repOK()`** ("the representation is ok"), returning `True` (or asserting) when the structure is internally consistent. It is the data-structure-level form of a [[DesignByContract|design-by-contract]] [[Postcondition|invariant]] and a powerful *program-specific* checker that extends what [[Fuzzing|fuzzing]] can detect beyond crashes and hangs.

## From The Fuzzing Book — Fuzzing: Breaking Things with Random Inputs
[[fuzzingbook-03-fuzzer|Ch 3]] introduces `repOK()` as the answer to *"how do we catch failures more subtle than a crash?"*. Generic runtime checkers like [[AddressSanitizer]] catch memory errors, but domain-level corruption needs domain-level checks. The chapter's examples:

- **Airport-code map** — `code_repOK(code)` asserts each code is exactly three uppercase letters; `airport_codes_repOK()` checks every entry. Mutating functions (`add_new_airport_2`) assert `repOK()` *before and after* every change, catching an inconsistency the moment it is introduced.
- **Red-black tree** — a `RedBlackTree.repOK()` bundles five structural [[Assertion|assertions]] (root has no parent, root is black, red nodes have black children, the tree is acyclic, parents are consistent), invoked on every `add_element`/`delete_element`.

The lesson: the more `repOK()` assertions you embed, the more errors a fuzzer surfaces — and the assertions double as executable documentation of your design assumptions. The chapter contrasts this dynamic checking with [[StaticAnalysis|static type checking]] ([[MyPy]]), noting that statically verifying rich properties (three uppercase letters, acyclicity) quickly exceeds what type checkers can express — so `repOK()` plus a good [[TestGeneration|test generator]] remains necessary.

## Connections
- [[Assertion]] — `repOK()` is implemented as a bundle of assertions.
- [[DesignByContract]] / [[Precondition]] / [[Postcondition]] — `repOK()` is the class invariant; checking it on entry/exit of mutators is contract programming.
- [[Fuzzing]] / [[Runner]] — a custom `Runner` calling `repOK()` turns subtle data corruption into observable `FAIL` outcomes.
- [[StaticAnalysis]] / [[MyPy]] — the static complement; handles simple type invariants, not rich structural ones.
- [[fuzzingbook-03-fuzzer|Ch 3]] — introduces `repOK()` as a program-specific checker.
- [[fuzzingbook-22-dynamic-invariants|Ch 22]] — mines such invariants automatically from executions.

## Sources
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
