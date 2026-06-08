---
title: "Static Analysis"
type: concept
tags: [verification, tooling, software-engineering, type-checking, testing]
sources: [fuzzingbook-03-fuzzer]
last_updated: 2026-06-06
---

# Static Analysis

**Static analysis** inspects a program *without running it* to find defects — type errors, undefined behavior, unreachable code, contract violations — by reasoning over the source or an intermediate representation. It contrasts with the *dynamic* checking that [[Fuzzing|fuzzing]], [[Assertion|assertions]], and [[AddressSanitizer|runtime sanitizers]] perform, and the two are complementary: static analysis covers all paths but is limited to properties it can prove cheaply, while dynamic checking observes only executed paths but can verify arbitrarily rich conditions.

## From The Fuzzing Book — Fuzzing: Breaking Things with Random Inputs
[[fuzzingbook-03-fuzzer|Ch 3]] positions static type checking as a partial alternative to runtime [[RepresentationInvariant|`repOK()`]] checks. It shows the [[MyPy]] static type checker catching `typed_airport_codes[1] = "First"` — an `int` key into a `Dict[str, str]` — at analysis time rather than runtime. The chapter's honest limit: statically verifying *advanced* properties (an airport code being exactly three uppercase letters, a tree being acyclic) "quickly reach the limits of static checking," so `repOK()` assertions and a good [[TestGeneration|test generator]] are still required. The takeaway is layered defense — types caught statically, richer invariants caught dynamically during fuzzing.

## Connections
- [[MyPy]] — the static type checker the chapter demonstrates.
- [[RepresentationInvariant]] / [[Assertion]] — the dynamic checks static analysis complements but cannot fully replace.
- [[Fuzzing]] — the dynamic counterpart; layered with static checks for best defect coverage.
- [[AddressSanitizer]] — a runtime (dynamic) memory checker, contrasted with static analysis.
- [[DesignByContract]] — contracts can be checked statically (where tractable) or dynamically.
- [[fuzzingbook-03-fuzzer|Ch 3]] — introduces static type checking alongside `repOK()`.

## Sources
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
